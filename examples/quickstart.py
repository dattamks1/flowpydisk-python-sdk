#!/usr/bin/env python
"""A first script against FlowpyDisk, start to finish.

    pip install -e sdk/python
    export FLOWPYDISK_API_KEY=fd_…                 # Settings > API Keys
    export FLOWPYDISK_BASE_URL=https://app.flowpydisk.com   # or your own
    python sdk/python/examples/quickstart.py

Everything below runs against a real instance. Nothing here is pseudocode:
C6's bar is that somebody can follow this without reading the spec, so it was
written BY running it, and three things in this file changed because the run
disagreed with the draft.

It tidies up after itself as far as the API allows: the file it uploads is
TRASHED on the way out, which is the reversible delete. Trashed is not gone -
the bytes still count until the trash is emptied - so a second run starts with
a non-zero usage and uploads "quickstart (2).txt". That is the product working
as intended, and the script says so where it happens rather than claiming to
leave no trace.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

from flowpydisk import FlowpyDisk, FlowpyDiskError, LimitExceeded, NotFound

BASE_URL = os.environ.get("FLOWPYDISK_BASE_URL", "https://app.flowpydisk.com")
API_KEY = os.environ.get("FLOWPYDISK_API_KEY")


def main() -> int:
    if not API_KEY:
        print("Set FLOWPYDISK_API_KEY. Mint one in Settings > API Keys.", file=sys.stderr)  # noqa: T201
        return 2

    # 1. A client. It acts in the space the key was made in: a workspace key
    #    acts in its workspace, a personal key in your personal space.
    #    Everything below is identical either way.
    with FlowpyDisk(api_key=API_KEY, base_url=BASE_URL) as client:
        # 2. What the account is using. Every endpoint is a method on a
        #    namespace named after its area of the API.
        usage = client.storage.list_usage()
        print(f"storage in use: {usage.get('used_bytes')} bytes")  # noqa: T201

        # 3. What this deployment will accept, before choosing a file. These
        #    are settings rather than constants, so ASK rather than assume.
        limits = client.files.limits()
        print(  # noqa: T201
            f"per-file cap {limits['max_file_bytes']} bytes; "
            f"anything over {limits['multipart_threshold_bytes']} uploads in parts"
        )

        # 4. Upload. One call, whichever transport the size calls for - the
        #    single PUT and the multipart part-by-part dance are both in here.
        with tempfile.TemporaryDirectory() as tmp:
            sample = Path(tmp) / "quickstart.txt"
            sample.write_text("Written by the FlowpyDisk quickstart.\n")
            uploaded = client.files.upload(sample)
            file_id = uploaded["id"]
            print(f"uploaded {uploaded['name']} as {file_id}")  # noqa: T201

            # 5. Read it back, and rename it. `get_files` takes one id;
            #    `update_files` PATCHes it.
            fetched = client.storage.get_files(file_id)
            print(f"server says it is {fetched['size_bytes']} bytes")  # noqa: T201
            client.storage.update_files(file_id, json={"name": "renamed-by-quickstart.txt"})

            # 6. Walk every file, one page at a time. Safe since every paged
            #    listing got a total order on 2026-09-14 (MOBILE_APP_
            #    REQUIREMENTS M17) - before that a walk could return a row
            #    twice and another never.
            names = [f["name"] for f in client.paginate("storage/files", limit=50)]
            print(f"{len(names)} file(s) at the root; ours is {'renamed-by-quickstart.txt' in names}")  # noqa: T201

            # 7. Errors say what you can do about them, and `.code` says
            #    exactly what happened.
            try:
                client.storage.get_files("00000000-0000-0000-0000-000000000000")
            except NotFound as err:
                print(f"a missing file raises NotFound (code={err.code})")  # noqa: T201

            try:
                huge = Path(tmp) / "too-big.bin"
                huge.write_bytes(b"x" * 16)
                client.files.upload(huge, name="x" * 300)
            except LimitExceeded as err:
                print(f"over a limit ({err.code}): {err}")  # noqa: T201
            except FlowpyDiskError as err:
                # A serializer refusal carries no `code` - it is a field error,
                # `{"name": ["…"]}`, which the SDK flattens into a sentence.
                print(f"refused: {err}")  # noqa: T201

            # 8. Tidy up. TRASH, not purge: `delete_files` is the reversible
            #    one and purging is deliberately a separate call. So the file
            #    is out of the listing but its bytes still count against the
            #    quota until the trash is emptied - which is why a second run
            #    of this script starts with a non-zero usage and uploads
            #    "quickstart (2).txt". Both are the product working as
            #    intended, and worth seeing once here rather than wondering
            #    about later.
            client.storage.delete_files(file_id)
            print("trashed it; empty the trash to reclaim the bytes")  # noqa: T201

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
