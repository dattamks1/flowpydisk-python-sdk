"""The transport: auth, errors, retries, pagination.

[SDK_PLAN §3–§4](../../../../docs/SDK_PLAN.md). Everything a generated
operation needs and cannot have. The generated layer (C3) will call
``client.request(...)``; nothing below it knows about any particular endpoint,
which is why this file can be finished before the generator is chosen.
"""

from __future__ import annotations

import time
from collections.abc import Iterator
from typing import Any
from urllib.parse import urljoin

import httpx

from ._errors import BY_STATUS, FlowpyDiskError, Throttled
from ._generated.operations import ALIASES, NAMESPACES
from .files import Files
from .index import Index

DEFAULT_BASE_URL = "https://app.flowpydisk.com"

#: Verbs that may be retried. A retried POST is a duplicate row: this product
#: has no idempotency keys, so "the connection dropped" and "it was created and
#: the response was lost" are indistinguishable from here. DELETE is in because
#: deleting twice is the same state as deleting once; POST never is.
RETRYABLE_METHODS = frozenset({"GET", "HEAD", "PUT", "DELETE"})

#: 5xx and 429 only. A 4xx will be refused identically however many times it is
#: sent, and retrying it just makes the caller wait to see their own mistake.
RETRYABLE_STATUS = frozenset({429, 500, 502, 503, 504})

DEFAULT_RETRIES = 2
DEFAULT_TIMEOUT = 30.0


class FlowpyDisk:
    """A client for the one space its API key was made in.

        client = FlowpyDisk(api_key="fd_…")

    A key acts in its own space and nowhere else: a key made in your personal
    space acts there, a key made in a workspace acts in that workspace. To act
    in a workspace, mint a key in that workspace (Settings > API Keys).

    There is no ``workspace`` argument (removed 2026-11-10, M3762). It sent a
    ``Workspace-Id`` header, and the server ignores that header for every API
    key, so a caller who passed it was told they acted in a workspace while
    acting in the key's own space.

    **There is no session-cookie mode**, and the absence is a decision rather
    than an omission - see SDK_PLAN §3. A program authenticates with an API key
    minted in Settings.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required. Mint one in Settings > API Keys.")
        self.base_url = base_url.rstrip("/") + "/"
        self.retries = retries
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "flowpydisk-python/0.0.1",
        }
        self._http = httpx.Client(headers=headers, timeout=timeout, transport=transport)
        # One attribute per tag in the spec: client.storage, client.tables, …
        # Built from the generated map rather than written out, so a new tag
        # arrives with the regeneration and no edit here - which is the whole
        # point of the layer being generated.
        for attr, cls in NAMESPACES.items():
            setattr(self, attr, cls(self))
        # A renamed tag keeps its older name as the same object, so
        # `client.ai_units is client.credits` (M4030). No warning: the older
        # name is promised, and the README says which one is current.
        for older, now in ALIASES.items():
            setattr(self, older, getattr(self, now))
        # The hand-written layer, over the top. `files` deliberately SHADOWS
        # nothing: the generated storage namespace keeps every endpoint, and
        # this adds the one call that is several endpoints (SDK_PLAN §4).
        self.files = Files(self)
        # "Index this file" for held files, one selector at a time (P7).
        self.index = Index(self)

    # -- lifecycle ---------------------------------------------------------

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> FlowpyDisk:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- the one call everything else is built on --------------------------

    def request(self, method: str, path: str, **kw: Any) -> Any:
        """Send one request, raise on refusal, return the decoded body.

        ``path`` is relative to the API root (``storage/files``), so a
        generated operation never has to know the deployment's hostname.
        """
        url = urljoin(self.base_url, f"api/v1/{path.lstrip('/')}")
        method = method.upper()
        attempts = self.retries + 1 if method in RETRYABLE_METHODS else 1

        last: httpx.Response | None = None
        for attempt in range(attempts):
            response = self._http.request(method, url, **kw)
            last = response
            if response.status_code not in RETRYABLE_STATUS or attempt == attempts - 1:
                break
            time.sleep(_backoff(response, attempt))

        assert last is not None  # noqa: S101 - the loop runs at least once
        if last.status_code >= 400:
            self._raise(last)
        if last.status_code == 204 or not last.content:
            return None
        # A picture the API streams (the marketplace preview's pages, reduced
        # images and posters, M1008) is its bytes, not JSON.
        if last.headers.get("content-type", "").startswith("image/"):
            return last.content
        return last.json()

    def get(self, path: str, **kw: Any) -> Any:
        return self.request("GET", path, **kw)

    def post(self, path: str, **kw: Any) -> Any:
        return self.request("POST", path, **kw)

    def patch(self, path: str, **kw: Any) -> Any:
        return self.request("PATCH", path, **kw)

    def delete(self, path: str, **kw: Any) -> Any:
        return self.request("DELETE", path, **kw)

    def blob_put(self, path: str, **kw: Any) -> httpx.Response:
        """PUT to a same-origin blob path, with this client's headers.

        For the RELATIVE presigned URLs a dev backend hands back
        (`/api/v1/storage/_dev/blob/…`). They are paths on our own origin and
        need the Bearer header; an absolute R2 link must not get it, and
        `files._blob_put` is where that fork lives. Raw response, not decoded:
        the caller wants the ETag header, and a blob PUT has no JSON body.
        """
        return self._http.put(urljoin(self.base_url, path.lstrip("/")), **kw)

    # -- pagination --------------------------------------------------------

    def paginate(self, path: str, *, limit: int = 200, **kw: Any) -> Iterator[dict]:
        """Every row of a paged listing, one at a time.

        Safe to offer only since the ordering tiebreak landed on 2026-09-14,
        and it is worth knowing why. These listings ordered by ``-created_at``
        with no tiebreak, so two rows sharing a timestamp had no defined order
        between pages: walking the list could return one of them twice and the
        other never, and the "never" half was invisible to every client.
        ``-id`` breaks the tie on all six paged listings now, so a walk is a
        walk.

        The entry is **M17 of docs/MOBILE_APP_REQUIREMENTS.md**, not of the
        findings register - which has its own unrelated M17 about rows only
        appending. Two documents number their own items, and citing the wrong
        one sends a reader somewhere confidently irrelevant.
        """
        offset = 0
        params = dict(kw.pop("params", {}) or {})
        while True:
            page = self.request("GET", path, params={**params, "limit": limit, "offset": offset}, **kw)
            rows = page if isinstance(page, list) else page.get("results", [])
            yield from rows
            if len(rows) < limit:
                return
            offset += limit

    # -- errors ------------------------------------------------------------

    def _raise(self, response: httpx.Response) -> None:
        code: str | None = None
        detail: Any = None
        try:
            body = response.json()
        except ValueError:
            # A proxy's HTML 502, a gateway timeout page. There is no envelope
            # to read, and inventing a code for it would make `.code` a value
            # the backend never sent.
            body = None
        if isinstance(body, dict):
            code = body.get("code")
            detail = body.get("detail", body.get("error", body))

        message = _readable(detail) or response.reason_phrase or f"HTTP {response.status_code}"
        cls = BY_STATUS.get(response.status_code, FlowpyDiskError)

        kw: dict[str, Any] = {
            "status": response.status_code,
            "code": code,
            "detail": detail,
            "response": response,
        }
        if cls is Throttled:
            raise Throttled(message, retry_after=_retry_after(response), **kw)
        raise cls(message, **kw)


def _readable(detail: Any) -> str:
    """A sentence, from whichever shape the backend used.

    Three shapes reach here and only one of them reads well on its own:

        {"detail": "File exceeds the 20 GB per-file limit."}   -> the string
        {"name": ["Ensure this field has no more than 255…"]}  -> DRF's field errors
        {}                                                      -> nothing at all

    The middle one is a serializer refusal, and it is common - the quickstart
    hit it on its first real run against a live server. Left alone it reaches
    the caller as `{'name': ['Ensure this field has…']}`, a dict repr in an
    exception message, which is the kind of thing that makes an SDK feel like
    a thin wrapper over `requests`. Flattened it is "name: Ensure this field
    has no more than 255 characters." and needs no explanation.
    """
    if not detail:
        return ""
    if isinstance(detail, str):
        return detail
    if isinstance(detail, list):
        return "; ".join(_readable(d) for d in detail if d)
    if isinstance(detail, dict):
        return "; ".join(f"{field}: {_readable(problem)}" for field, problem in detail.items() if problem)
    return str(detail)


def _retry_after(response: httpx.Response) -> float | None:
    raw = response.headers.get("Retry-After")
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        # The header also allows an HTTP-date. Rare here, and a wrong number is
        # worse than none: a caller who sleeps on a misparsed date sleeps for
        # the wrong length and blames the SDK.
        return None


def _backoff(response: httpx.Response, attempt: int) -> float:
    """The server's number if it gave one, otherwise 0.5s, 1s, 2s.

    `Retry-After` wins over the schedule, always. The server knows when its
    window reopens and the client is guessing; ignoring it is how a client
    retries into the same 429 three times and calls the API flaky.
    """
    told = _retry_after(response)
    if told is not None:
        return told
    return 0.5 * (2**attempt)
