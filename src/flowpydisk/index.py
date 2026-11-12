""" "Index this file" for files held for their owner (INGESTION_PLAN P7).

A file over 250 MB, a recording over 30 minutes or of unknown length, or a
meeting or call over 2 hours (a plan may lower each) is `held`: not indexed
until its owner asks. List them with
``client.knowledge.list_index(params={"state": "held"})`` and start them:

    client.index.release(file_ids=[file_id])
    client.index.release(folder_id=folder_id)     # the folder and everything under it
    client.index.release(all_held=True)           # every held file you can see

Exactly one selector. Indexing is a platform cost: nothing is charged. The
generated ``client.knowledge.create_release(json=...)`` is the same call.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ._client import FlowpyDisk


class Index:
    def __init__(self, client: FlowpyDisk):
        self._c = client

    def release(
        self,
        *,
        file_ids: list[str] | None = None,
        folder_id: str | None = None,
        all_held: bool = False,
    ) -> Any:
        """Release held files; returns ``{released, queued, waiting, skipped}``."""
        if sum([file_ids is not None, folder_id is not None, bool(all_held)]) != 1:
            raise ValueError("Pass exactly one of file_ids, folder_id or all_held.")
        if file_ids is not None:
            body: dict[str, Any] = {"items": [{"entity_type": "file", "entity_id": str(f)} for f in file_ids]}
        elif folder_id is not None:
            body = {"folder_id": str(folder_id)}
        else:
            body = {"all_held": True}
        return self._c.request("POST", "knowledge/index/release", json=body)
