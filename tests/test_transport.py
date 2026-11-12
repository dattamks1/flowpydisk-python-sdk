"""The transport, against a real socket.

**Not a mock, deliberately.** Every assertion here goes over TCP to an HTTP
server running in a thread: real headers, real status codes, real bodies, real
retries. A mocked `httpx` client would prove that this module calls the
functions it calls, which is the assertion that stays green when the header
name is wrong.

It is also not the live instance. C2's row says "one end-to-end call against
the local instance", and `test_live.py` beside this is that - opt-in, and
**loud** when asked to run and unable to. This file is what the push gate runs
on every push, so it has to be hermetic and fast, and it is both: no Django, no
database, no network beyond loopback.
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from flowpydisk import (
    AuthError,
    FlowpyDisk,
    FlowpyDiskError,
    InvalidRequest,
    LimitExceeded,
    NotFound,
    Throttled,
)

#: What the next request gets, set per test. A list so a test can queue several
#: and assert on a retry: the server pops one per request and repeats the last.
RESPONSES: list[tuple[int, object, dict]] = []
#: Every request the server saw, so a test can assert on headers and paths
#: rather than only on what came back.
SEEN: list[dict] = []


class Handler(BaseHTTPRequestHandler):
    def _respond(self) -> None:
        SEEN.append(
            {
                "path": self.path,
                "method": self.command,
                "headers": dict(self.headers),
            }
        )
        status, body, headers = RESPONSES[0] if len(RESPONSES) == 1 else RESPONSES.pop(0)
        # Bytes go out as they are, under the Content-Type the test queued;
        # anything else is JSON.
        binary = isinstance(body, bytes)
        payload = b"" if body is None else body if binary else json.dumps(body).encode()
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k.replace("_", "-"), v)
        if payload:
            if not binary:
                self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if payload:
            self.wfile.write(payload)

    do_GET = do_POST = do_PATCH = do_DELETE = _respond

    def log_message(self, *a: object) -> None:
        """Silence. The default writes every request to stderr, which turns a
        quiet `pytest -q` into forty lines of access log."""


@pytest.fixture
def server():
    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    RESPONSES.clear()
    SEEN.clear()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()
    httpd.server_close()


@pytest.fixture
def client(server):
    with FlowpyDisk(api_key="fd_test", base_url=server, retries=1) as c:
        yield c


def queue(status: int, body: object = None, **headers: str) -> None:
    RESPONSES.append((status, body, headers))


# -- the request that works ------------------------------------------------


def test_a_key_becomes_a_bearer_header_and_the_path_is_versioned(client):
    queue(200, {"results": []})
    client.get("storage/files")

    assert SEEN[0]["path"] == "/api/v1/storage/files"
    assert SEEN[0]["headers"]["Authorization"] == "Bearer fd_test"
    # The key names the space, so the client never sends Workspace-Id: the
    # server ignores it for every API key (M3762).
    assert "Workspace-Id" not in SEEN[0]["headers"]


def test_there_is_no_workspace_argument(server):
    """M3762: `workspace=` sent a header the server ignores for every API key,
    so a caller believed they acted in a workspace and acted in the key's own
    space. It is gone, and passing it is refused loudly rather than accepted
    and dropped."""
    with pytest.raises(TypeError, match="workspace"):
        FlowpyDisk(api_key="fd_test", base_url=server, workspace="ws-1")


def test_no_content_is_none_not_a_crash(client):
    queue(204)
    assert client.delete("storage/files/abc") is None


def test_a_picture_comes_back_as_its_bytes(client):
    """M1008: the marketplace preview's pictures are JPEGs we stream. Decoding
    one as JSON raised, so every generated operation for an image route was a
    method that could only fail."""
    jpeg = b"\xff\xd8\xff\xe0" + b"0" * 32
    queue(200, jpeg, Content_Type="image/jpeg")
    assert client.get("market/files/abc/preview/image") == jpeg


def test_an_api_key_is_required():
    with pytest.raises(ValueError, match="api_key"):
        FlowpyDisk(api_key="")


# -- the errors ------------------------------------------------------------


@pytest.mark.parametrize(
    ("status", "cls"),
    [
        (400, InvalidRequest),
        (401, AuthError),
        (402, LimitExceeded),
        (403, AuthError),
        (404, NotFound),
        (413, LimitExceeded),
        (422, InvalidRequest),
        (429, Throttled),
    ],
)
def test_each_status_raises_the_class_a_caller_can_act_on(client, status, cls):
    queue(status, {"code": "whatever", "detail": "no"})
    with pytest.raises(cls):
        client.get("storage/files")


def test_an_unmapped_status_stays_the_base_class(client):
    """A 418 is not an InvalidRequest, and saying so wrongly is worse than
    saying nothing. The base class carries the status either way."""
    queue(418, {"detail": "teapot"})
    with pytest.raises(FlowpyDiskError) as caught:
        client.get("storage/files")
    assert type(caught.value) is FlowpyDiskError
    assert caught.value.status == 418


def test_the_backend_code_survives_onto_the_exception(client):
    """The whole point of five classes over sixty-seven: the class says what
    you can do, `.code` says exactly what happened."""
    queue(413, {"code": "file_too_large", "detail": "File exceeds the 20 GB per-file limit."})
    with pytest.raises(LimitExceeded) as caught:
        client.post("storage/files")
    assert caught.value.code == "file_too_large"
    assert caught.value.status == 413
    assert "20 GB" in str(caught.value)
    # And the code is IN the repr, so a traceback in somebody's log is
    # actionable without the debugger they no longer have attached.
    assert "file_too_large" in str(caught.value)


def test_a_body_with_no_envelope_does_not_invent_a_code(client):
    """A proxy's HTML 502. `.code` must stay None rather than becoming a string
    the backend never sent."""
    RESPONSES.append((502, None, {}))
    with pytest.raises(FlowpyDiskError) as caught:
        client.post("storage/files")
    assert caught.value.code is None
    assert caught.value.status == 502


def test_a_not_found_is_raised_as_it_came_without_a_second_request(client):
    """M2893: folder keys are retired, so a 404 no longer sends a follow-up
    `GET /auth/api-keys` to ask whether the key is confined to a folder."""
    queue(404, {"code": "folder_not_found", "detail": "Not found."})
    with pytest.raises(NotFound) as caught:
        client.get("storage/folders/abc")
    assert caught.value.code == "folder_not_found"
    assert "confined" not in str(caught.value)
    assert [s["path"] for s in SEEN] == ["/api/v1/storage/folders/abc"]


def test_throttled_carries_the_servers_own_number(client):
    queue(429, {"code": "throttled"}, **{"Retry-After": "7"})
    queue(429, {"code": "throttled"}, **{"Retry-After": "7"})
    with pytest.raises(Throttled) as caught:
        client.post("storage/files")  # POST: not retried, so this raises at once
    assert caught.value.retry_after == 7.0


def test_a_retry_after_that_is_a_date_is_not_guessed_at(client):
    """The header also permits an HTTP-date. A misparsed one makes a caller
    sleep for the wrong length and blame the SDK, so None is the honest
    answer."""
    queue(429, {"code": "throttled"}, **{"Retry-After": "Wed, 21 Oct 2026 07:28:00 GMT"})
    with pytest.raises(Throttled) as caught:
        client.post("storage/files")
    assert caught.value.retry_after is None


# -- retries ---------------------------------------------------------------


def test_a_get_retries_a_500_and_then_succeeds(client):
    queue(500, {"detail": "boom"})
    queue(200, {"results": [{"id": "1"}]})
    assert client.get("storage/files") == {"results": [{"id": "1"}]}
    assert len(SEEN) == 2


def test_a_post_is_never_retried(client):
    """A retried create is a duplicate row. This product has no idempotency
    keys, so "the connection dropped" and "it was created and the response was
    lost" are indistinguishable from the client - and one of those two answers
    charges somebody twice."""
    queue(500, {"detail": "boom"})
    queue(200, {"id": "1"})
    with pytest.raises(FlowpyDiskError):
        client.post("storage/files")
    assert len(SEEN) == 1


def test_a_400_is_not_retried(client):
    """It will be refused identically however many times it is sent. Retrying
    just makes the caller wait to see their own mistake."""
    queue(400, {"code": "bad_filter"})
    with pytest.raises(InvalidRequest):
        client.get("storage/files")
    assert len(SEEN) == 1


# -- pagination ------------------------------------------------------------


def test_paginate_walks_every_page_and_stops_on_a_short_one(client):
    queue(200, {"results": [{"id": str(i)} for i in range(3)]})
    queue(200, {"results": [{"id": "3"}]})
    rows = list(client.paginate("storage/files", limit=3))

    assert [r["id"] for r in rows] == ["0", "1", "2", "3"]
    assert len(SEEN) == 2
    assert "offset=0" in SEEN[0]["path"]
    assert "offset=3" in SEEN[1]["path"]


def test_paginate_handles_a_bare_list(client):
    """Not every listing in this API is enveloped, and a generator that only
    understood one shape would silently yield nothing for the other."""
    queue(200, [{"id": "a"}])
    assert [r["id"] for r in client.paginate("storage/folders", limit=50)] == ["a"]


def test_paginate_keeps_the_callers_own_params(client):
    queue(200, {"results": []})
    list(client.paginate("storage/files", params={"ordering": "-created_at"}))
    assert "ordering=-created_at" in SEEN[0]["path"]


# -- error messages a person can read --------------------------------------


def test_a_field_error_reads_as_a_sentence_not_a_dict_repr(client):
    """DRF's serializer refusals are `{field: [messages]}`, and the quickstart
    hit one on its first run against a live server: a 300-character file name.

    Left alone it reaches the caller as `{'name': ['Ensure this field has…']}`
    - a dict repr inside an exception message, which is what makes an SDK feel
    like a thin wrapper over `requests`."""
    queue(400, {"name": ["Ensure this field has no more than 255 characters."]})
    with pytest.raises(InvalidRequest) as caught:
        client.post("storage/uploads")
    assert "name: Ensure this field has no more than 255 characters." in str(caught.value)


def test_several_field_errors_all_survive(client):
    queue(400, {"name": ["Too long."], "size_bytes": ["Must be positive."]})
    with pytest.raises(InvalidRequest) as caught:
        client.post("storage/uploads")
    message = str(caught.value)
    assert "name: Too long." in message
    assert "size_bytes: Must be positive." in message


def test_an_empty_body_falls_back_to_the_status(client):
    """A bare 404 with Content-Length: 0 is what `GET /storage/files/{id}`
    actually returns for a missing file - confirmed against a running server,
    not assumed. There is no code and no detail to report, and inventing
    either would be worse than the reason phrase."""
    RESPONSES.append((404, None, {}))
    with pytest.raises(NotFound) as caught:
        client.get("storage/files/does-not-exist")
    assert caught.value.code is None
    assert "Not Found" in str(caught.value)
