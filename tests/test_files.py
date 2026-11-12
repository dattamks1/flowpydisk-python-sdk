"""`files.upload()`, over a real socket, on both transports.

The API keeps this as three or more calls and each of them can go wrong in a
way the next one cannot see. So these assert on the CONVERSATION, not on the
return value: which requests were made, in which order, with which bodies. A
test that only checked "a File came back" would pass against an implementation
that uploaded the wrong bytes.

Same server-in-a-thread as `test_transport.py`, extended to speak the upload
endpoints and to stand in for the storage host the presigned URLs point at -
which is itself part of the point: the presigned PUT must NOT carry our
`Authorization` header, and only a real request can show that.
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from flowpydisk import FlowpyDisk, FlowpyDiskError, LimitExceeded

LIMITS = {
    "max_file_bytes": 1000,
    "multipart_threshold_bytes": 100,
    "part_size_bytes": 20,
    "max_parts": 10000,
    "single_put_max_bytes": 100,
    "resume_window_hours": 24,
}

SEEN: list[dict] = []
#: Status to answer each part PUT with, popped in order; 200 once empty. Lets a
#: test make part 2 fail without touching the rest of the flow.
PART_STATUS: list[int] = []
#: Non-empty to make the stub answer with a RELATIVE presigned path, the way a
#: dev backend does, instead of an absolute URL the way R2 does.
RELATIVE: list[bool] = []
STATE: dict = {}


class Handler(BaseHTTPRequestHandler):
    def _read(self) -> bytes:
        length = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(length) if length else b""

    def _send(self, status: int, body: object = None, **headers: str) -> None:
        payload = b"" if body is None else json.dumps(body).encode()
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        if payload:
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if payload:
            self.wfile.write(payload)

    def do_GET(self) -> None:
        SEEN.append({"method": "GET", "path": self.path, "headers": dict(self.headers)})
        if self.path.endswith("/upload-limits"):
            return self._send(200, LIMITS)
        return self._send(404, {"code": "not_found"})

    def do_PUT(self) -> None:
        """The storage host. Presigned URLs land here."""
        body = self._read()
        SEEN.append({"method": "PUT", "path": self.path, "body": body, "headers": dict(self.headers)})
        STATE.setdefault("bytes", bytearray()).extend(body)
        status = PART_STATUS.pop(0) if PART_STATUS else 200
        if status >= 400:
            return self._send(status, {"detail": "no"})
        # A real part PUT answers with an ETag, and the client cannot complete
        # without one.
        return self._send(200, None, ETag=f'"etag-{len(SEEN)}"')

    def do_POST(self) -> None:
        body = json.loads(self._read() or b"{}")
        SEEN.append({"method": "POST", "path": self.path, "body": body})
        base = f"http://127.0.0.1:{self.server.server_address[1]}"

        if self.path.endswith("/storage/uploads"):
            size = body["size_bytes"]
            started = {"file": {"id": "file-1", "name": body["name"]}, "reservation_id": "r1"}
            if size > LIMITS["multipart_threshold_bytes"]:
                started |= {"upload_id": "u1", "part_size": LIMITS["part_size_bytes"]}
            else:
                where = "/api/v1/storage/_dev/blob/abc" if RELATIVE else f"{base}/blob/single"
                started |= {"upload": {"url": where, "object_key": "k"}}
            return self._send(201, started)
        if self.path.endswith("/content/upload"):
            size = body["size_bytes"]
            started = {"file": {"id": "file-9"}, "reservation_id": "r2"}
            if size > LIMITS["multipart_threshold_bytes"]:
                started |= {"upload_id": "u2", "part_size": LIMITS["part_size_bytes"]}
            else:
                started |= {"upload": {"url": f"{base}/blob/replace", "object_key": "k"}}
            return self._send(201, started)
        if self.path.endswith("/parts"):
            n = body["part_number"]
            return self._send(200, {"url": f"{base}/blob/part-{n}", "part_number": n})
        if self.path.endswith("/complete"):
            STATE["completed_with"] = body
            return self._send(200, {"id": "file-1", "name": "done"})
        if self.path.endswith("/abort"):
            STATE["aborted"] = True
            return self._send(200, {})
        return self._send(404, {"code": "not_found"})

    def log_message(self, *a: object) -> None:
        """Quiet; the default writes an access log to stderr."""


@pytest.fixture
def client():
    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    SEEN.clear()
    PART_STATUS.clear()
    RELATIVE.clear()
    STATE.clear()
    with FlowpyDisk(api_key="fd_test", base_url=f"http://127.0.0.1:{httpd.server_address[1]}") as c:
        yield c
    httpd.shutdown()
    httpd.server_close()


def a_file(tmp_path, size: int, name: str = "f.bin"):
    path = tmp_path / name
    path.write_bytes(bytes(range(256)) * (size // 256) + b"x" * (size % 256))
    return path


def posts(suffix: str) -> list[dict]:
    return [s for s in SEEN if s["method"] == "POST" and s["path"].endswith(suffix)]


# -- the small file: one PUT ----------------------------------------------


def test_a_small_file_goes_in_one_put(client, tmp_path):
    src = a_file(tmp_path, 50)  # under the advertised 100-byte threshold
    client.files.upload(src)

    assert len(posts("/storage/uploads")) == 1
    puts = [s for s in SEEN if s["method"] == "PUT"]
    assert len(puts) == 1
    assert puts[0]["body"] == src.read_bytes(), "the bytes on the wire are the file"
    assert STATE["completed_with"] == {}, "a single-PUT completion carries no parts"


def test_an_absolute_presigned_put_does_not_carry_the_api_key(client, tmp_path):
    """An absolute URL is R2's, signed into the URL itself.

    Sending `Authorization: Bearer fd_…` with it hands a third party an API
    key. Only a real request can show this - a mocked transport would assert
    about whatever the mock was told.
    """
    client.files.upload(a_file(tmp_path, 50))
    put = next(s for s in SEEN if s["method"] == "PUT")
    assert "Authorization" not in put["headers"]


def test_a_RELATIVE_presigned_put_is_resolved_and_DOES_carry_the_key(client, tmp_path):
    """The other half of the rule, and the half the first version got wrong.

    A dev backend answers with a PATH - `/api/v1/storage/_dev/blob/…` - which
    is same-origin and needs the Bearer header like any other call, and cannot
    be requested at all without a host. Sent bare, httpx refuses it outright:
    *"Request URL is missing an 'http://' or 'https://' protocol."*

    `mcp/flowpy_mcp/client.py` has carried this rule since it was written. The
    SDK shipped the "never send the key" half only, every test passed, and it
    was the QUICKSTART - run against a real server for the first time - that
    found it. Findings register M230.
    """
    RELATIVE.append(True)
    client.files.upload(a_file(tmp_path, 50))

    put = next(s for s in SEEN if s["method"] == "PUT")
    assert put["path"].startswith("/api/v1/storage/_dev/blob/"), put["path"]
    assert put["headers"]["Authorization"] == "Bearer fd_test"


# -- the large file: parts -------------------------------------------------


def test_a_large_file_is_split_into_parts_and_completed_with_their_etags(client, tmp_path):
    src = a_file(tmp_path, 110)  # over the threshold; 20-byte parts -> 6 parts
    client.files.upload(src)

    puts = [s for s in SEEN if s["method"] == "PUT"]
    assert len(puts) == 6
    assert b"".join(p["body"] for p in puts) == src.read_bytes(), "reassembled, the parts are the file"

    parts = STATE["completed_with"]["parts"]
    assert [p["part_number"] for p in parts] == [1, 2, 3, 4, 5, 6], "numbered from 1, contiguous"
    assert all(p["etag"] for p in parts), "every part carries the etag its PUT returned"


def test_the_transport_comes_from_the_servers_threshold_not_a_local_constant(client, tmp_path):
    """101 bytes against an advertised 100-byte threshold is multipart.

    The number is the server's, fetched at upload time. A client with its own
    copy is wrong the day the setting changes - which is the whole reason the
    uploads programme made it a setting and advertised it.
    """
    client.files.upload(a_file(tmp_path, 101))
    assert posts("/parts"), "just over the advertised threshold must be resumable"

    SEEN.clear()
    STATE.clear()
    client.files.upload(a_file(tmp_path, 99, "small.bin"))
    assert not posts("/parts"), "just under it must be a single PUT"


def test_a_part_that_fails_is_retried_and_the_upload_survives(client, tmp_path):
    PART_STATUS.extend([500])  # part 1 fails once, then everything succeeds
    client.files.upload(a_file(tmp_path, 110))

    puts = [s for s in SEEN if s["method"] == "PUT"]
    assert len(puts) == 7, "six parts plus one retry"
    assert not STATE.get("aborted")


def test_a_part_refused_for_good_is_not_retried(client, tmp_path):
    """400/404/413 on a part mean the presigned URL is wrong or the part is too
    big. Re-sending sends the same thing to the same place."""
    PART_STATUS.extend([413])
    with pytest.raises(FlowpyDiskError, match="retrying will not help"):
        client.files.upload(a_file(tmp_path, 110))
    assert len([s for s in SEEN if s["method"] == "PUT"]) == 1


# -- failure leaves nothing behind ----------------------------------------


def test_a_failed_upload_aborts_its_reservation(client, tmp_path):
    """Otherwise the sweep collects it eventually - and "eventually" is up to
    24 hours of somebody's quota held by an upload that failed in front of
    them."""
    PART_STATUS.extend([413])
    with pytest.raises(FlowpyDiskError):
        client.files.upload(a_file(tmp_path, 110))
    assert STATE.get("aborted") is True


def test_an_over_cap_file_is_refused_before_anything_is_reserved(client, tmp_path):
    """The server would refuse it too, but only after a round trip - and the
    caller would have to guess the reason from a 413."""
    with pytest.raises(LimitExceeded) as caught:
        client.files.upload(a_file(tmp_path, 1001))  # cap is 1000
    assert caught.value.code == "file_too_large"
    assert not posts("/storage/uploads"), "nothing was reserved"


# -- limits ----------------------------------------------------------------


def test_limits_are_fetched_once_per_client(client, tmp_path):
    client.files.upload(a_file(tmp_path, 10, "a.bin"))
    client.files.upload(a_file(tmp_path, 10, "b.bin"))
    fetches = [s for s in SEEN if s["method"] == "GET" and s["path"].endswith("/upload-limits")]
    assert len(fetches) == 1


def test_limits_can_be_refreshed_on_purpose(client):
    client.files.limits()
    client.files.limits(refresh=True)
    fetches = [s for s in SEEN if s["method"] == "GET" and s["path"].endswith("/upload-limits")]
    assert len(fetches) == 2


# -- replacing an existing file's content ----------------------------------


def test_replace_content_uses_the_content_endpoints_not_the_upload_ones(client, tmp_path):
    """A different set of endpoints for a different operation.

    `upload` creates a file; `replace_content` creates a VERSION of one that
    already exists. Folding them together behind a `file_id=` argument would
    make the difference between an accident and an edit a keyword argument.
    """
    src = a_file(tmp_path, 110)  # over the threshold, so it exercises parts too
    client.files.replace_content("file-9", src)

    assert posts("/content/upload"), "step 1 is the content endpoint"
    assert not posts("/storage/uploads"), "it must not start a NEW upload"
    assert [p["path"] for p in posts("/parts")] == ["/api/v1/storage/files/file-9/content/parts"] * 6, (
        "the parts go to the content parts endpoint, addressed by file id"
    )
    assert STATE["completed_with"]["parts"], "completed with the etags it collected"
    puts = [s for s in SEEN if s["method"] == "PUT"]
    assert b"".join(p["body"] for p in puts) == src.read_bytes()


def test_replace_content_refuses_an_over_cap_file_before_reserving(client, tmp_path):
    with pytest.raises(LimitExceeded):
        client.files.replace_content("file-9", a_file(tmp_path, 1001))
    assert not posts("/content/upload")
