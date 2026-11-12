"""One call for something the API deliberately keeps as three or more.

SDK design plan, section 4. C4, and the row has grown since it
was written: the worklist calls this "the three-step dance", and since the
uploads programme shipped on 2026-09-07 it is a threshold decision, a quota
reservation, N presigned part PUTs with per-part retry, and a completion that
refuses a gap.

    client.files.upload("report.pdf")                  # picks its own transport
    client.files.upload(path, folder=folder_id)

**The transport is chosen from the server's advertised threshold, never from a
number in here.** `GET /storage/upload-limits` returns `max_file_bytes`,
`multipart_threshold_bytes` and `part_size_bytes`, and this asks. A client with
its own copy of the threshold is a client that is wrong the day the setting
changes - which is the whole reason step 1 of that programme made the cap a
setting and advertised it.

**What this does NOT do: resume across a process.** The web client resumes
after a reload because a browser can hand back a file handle (`resumeStore.js`,
`handleStore.js`); a script that died has no equivalent, and inventing one
means a state file whose staleness the caller has to reason about. So v1
retries a PART, and on a failure that outlives the retries it aborts cleanly
and raises. The upload id and the arrived parts are both readable from the API,
so a caller who wants resume can build it on `list_upload_parts` - and that is
a deliberate v2 line rather than an oversight.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, BinaryIO

import httpx

from ._errors import FlowpyDiskError, LimitExceeded

#: How many times one part is re-sent before the upload gives up. Parts are the
#: one place a retry is unambiguously safe: a part is addressed by number and
#: re-sending it replaces it, so unlike a POST there is no way to end up with
#: two of anything.
PART_ATTEMPTS = 3

#: How long one transfer may take before it is treated as hung.
#:
#: Explicit numbers rather than `timeout=None`, and ruff's S113 is right to
#: insist: `None` means a half-open socket never returns, so an upload that has
#: silently died holds the process until somebody kills it. These are budgets
#: for ONE part and ONE single-PUT body, not for the whole file - a 20 GB
#: upload is thousands of parts, each with its own 5 minutes.
#:
#: 8 MiB (the server's default part size) needs 300 s at ~27 KB/s, and the
#: single-PUT ceiling is 100 MB by default, which needs 900 s at ~110 KB/s.
#: Both are slower than any link this is worth serving, so a timeout here means
#: something is wrong rather than slow.
PART_TIMEOUT = 300.0
SINGLE_PUT_TIMEOUT = 900.0

#: A part PUT that comes back with one of these is not retried. 400 and 404 mean
#: the presigned URL is wrong or expired and re-sending sends it again; 413 means
#: the part is too big and will be too big next time. Matches the web client's
#: `FINAL_PART_STATUSES`, and the two should stay matched.
FINAL_PART_STATUSES = frozenset({400, 404, 413})


class Files:
    """Uploads and downloads, with the multi-call shapes hidden."""

    def __init__(self, client: Any) -> None:
        self._c = client
        self._limits: dict[str, Any] | None = None

    def limits(self, *, refresh: bool = False) -> dict[str, Any]:
        """The server's upload limits, fetched once per client.

        Cached because every upload needs them and they change about as often
        as a deploy; `refresh=True` for a long-lived process that wants to
        notice a settings change without restarting.
        """
        if self._limits is None or refresh:
            self._limits = self._c.get("storage/upload-limits")
        return self._limits

    def upload(
        self,
        path: str | os.PathLike[str],
        *,
        name: str | None = None,
        folder: str | None = None,
        kind: str = "file",
        **extra: Any,
    ) -> dict[str, Any]:
        """Upload a local file and return the File the server created.

        Picks single-PUT or resumable from the advertised threshold, refuses a
        file over the advertised cap before any request leaves (the server's
        own number, in the server's own words), and cleans up after itself if
        the transfer fails partway.
        """
        src = Path(path)
        size = src.stat().st_size
        self._refuse_over_cap(src, size)

        started = self._c.post(
            "storage/uploads",
            json={"name": name or src.name, "size_bytes": size, "folder": folder, "kind": kind, **extra},
        )
        file_id = started["file"]["id"]

        with src.open("rb") as fh:
            try:
                if started.get("upload_id"):
                    parts = self._send_parts(file_id, fh, started)
                    return self._c.post(f"storage/uploads/{file_id}/complete", json={"parts": parts})
                self._single_put(started["upload"], fh, size)
                return self._c.post(f"storage/uploads/{file_id}/complete", json={})
            except Exception:
                # Abort rather than leave the reservation and the staged parts
                # behind. The sweep would eventually collect them (steps 2 and
                # 3 of the uploads programme), but "eventually" is up to 24
                # hours of somebody's quota held by an upload that failed in
                # front of them.
                self._abort_quietly(file_id)
                raise

    def replace_content(self, file_id: str, path: str | os.PathLike[str], **extra: Any) -> dict[str, Any]:
        """Replace an existing file's bytes, keeping its id and its history.

        The same three-or-more-call shape as `upload`, against a different set
        of endpoints (`/content/upload`, `/content/parts`, `/content/complete`),
        and the same rules apply to all of it: the transport comes from the
        advertised threshold, parts retry individually, and a failure aborts
        rather than leaving the reservation held.

        Kept as a second method rather than folded into `upload` with a
        `file_id=` argument. They read as one operation and they are not: one
        creates a file and the other creates a VERSION of a file that already
        exists, which is the difference between an accident and an edit.
        """
        src = Path(path)
        size = src.stat().st_size
        self._refuse_over_cap(src, size)

        started = self._c.post(f"storage/files/{file_id}/content/upload", json={"size_bytes": size, **extra})
        # No try/abort here, unlike `upload`, and the asymmetry is the API's
        # rather than an oversight: there is no `/content/abort`. An abandoned
        # replacement is collected by the same inactivity sweep that collects
        # an abandoned upload (uploads step 3). Calling `/uploads/{id}/abort`
        # would address a different reservation entirely.
        with src.open("rb") as fh:
            if started.get("upload_id"):
                parts = self._send_parts(file_id, fh, started, endpoint="files/{id}/content/parts")
                return self._c.post(f"storage/files/{file_id}/content/complete", json={"parts": parts})
            self._single_put(started["upload"], fh, size)
            return self._c.post(f"storage/files/{file_id}/content/complete", json={})

    def _refuse_over_cap(self, src: Path, size: int) -> None:
        cap = self.limits().get("max_file_bytes")
        if cap and size > cap:
            # Locally, before the reservation. The server would refuse it too,
            # but only after the caller has waited for a round trip - and the
            # message would have to be guessed at from a 413.
            raise LimitExceeded(
                f"{src.name} is {size} bytes and this deployment's per-file cap is {cap}.",
                status=None,
                code="file_too_large",
            )

    def _blob_put(self, url: str, content: bytes, timeout: float, **kw: Any) -> httpx.Response:
        """PUT to a presigned URL, which may be absolute (R2) or relative (dev).

        **The rule is not "never send the key", and getting that wrong is the
        reason this method exists.** `mcp/flowpy_mcp/client.py` has carried it
        since it was written:

            Relative URLs are same-origin and need our Bearer header; absolute
            R2 URLs are self-authenticating and must not receive it.

        An absolute link is R2's, signed into the URL itself, and sending our
        `Authorization` with it hands a third party an API key. A relative one
        is a path on OUR origin - the dev backend's `/api/v1/storage/_dev/blob/…`
        - which needs the header like any other call and cannot be requested at
        all without a host.

        The first version of this sent everything bare, which is correct for
        R2 and fails outright against a dev server: httpx refuses a URL with no
        scheme. Both halves of the rule are asserted in `tests/test_files.py`.
        """
        if url.startswith("/"):
            return self._c.blob_put(url, content=content, timeout=timeout, **kw)
        # Absolute: R2's own signed link. No client, so no headers of ours.
        return httpx.put(url, content=content, timeout=timeout, **kw)

    def _single_put(self, upload: dict[str, Any], fh: BinaryIO, size: int) -> None:
        """One PUT of the whole body to the presigned target."""
        response = self._blob_put(
            upload["url"],
            fh.read(),
            SINGLE_PUT_TIMEOUT,
            headers={"Content-Length": str(size)},
        )
        if response.status_code >= 400:
            raise FlowpyDiskError(
                f"The storage service refused the upload ({response.status_code}).",
                status=response.status_code,
                response=response,
            )

    def _send_parts(
        self,
        file_id: str,
        fh: BinaryIO,
        started: dict[str, Any],
        *,
        endpoint: str = "uploads/{id}/parts",
    ) -> list[dict[str, Any]]:
        """Every part, in order, each retried on its own.

        Returns the `{part_number, etag}` list `complete` wants. A gap in that
        list is refused by the server rather than assembled, on purpose: the
        alternative is a TRUNCATED object that looks like a successful upload.
        """
        part_size = started.get("part_size") or self.limits().get("part_size_bytes")
        if not part_size:
            raise FlowpyDiskError("The server started a resumable upload without a part size.")

        parts: list[dict[str, Any]] = []
        number = 1
        while True:
            chunk = fh.read(part_size)
            if not chunk:
                break
            where = f"storage/{endpoint.replace('{id}', file_id)}"
            target = self._c.post(where, json={"part_number": number})
            parts.append({"part_number": number, "etag": self._put_part(target["url"], chunk, number)})
            number += 1
        return parts

    def _put_part(self, url: str, chunk: bytes, number: int) -> str:
        last: Exception | None = None
        for _attempt in range(PART_ATTEMPTS):
            try:
                response = self._blob_put(url, chunk, PART_TIMEOUT)
            except httpx.HTTPError as err:  # a dropped connection mid-part
                last = err
                continue
            if response.status_code < 400:
                etag = response.headers.get("ETag", "").strip('"')
                if not etag:
                    # The client cannot complete without it, and a blank etag
                    # in the completion list is refused by storage with a
                    # message about signatures that says nothing about this.
                    raise FlowpyDiskError(f"Part {number} was stored but returned no ETag.")
                return etag
            if response.status_code in FINAL_PART_STATUSES:
                raise FlowpyDiskError(
                    f"Part {number} was refused ({response.status_code}) and retrying will not help.",
                    status=response.status_code,
                    response=response,
                )
            last = FlowpyDiskError(f"Part {number} failed with {response.status_code}.")
        raise FlowpyDiskError(f"Part {number} failed {PART_ATTEMPTS} times: {last}")

    def _abort_quietly(self, file_id: str) -> None:
        try:
            self._c.post(f"storage/uploads/{file_id}/abort", json={})
        except FlowpyDiskError:
            # Best effort, and it must not replace the original exception: the
            # caller needs to know why the UPLOAD failed, not why the tidy-up
            # afterwards also failed. The server's sweep collects it either way.
            pass
