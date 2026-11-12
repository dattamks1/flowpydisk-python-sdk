"""`client.index.release(...)`: "Index this file" for held files (INGESTION_PLAN P7).

One call over `POST /knowledge/index/release` with exactly one selector. The
generated `client.knowledge.create_release(json=...)` stays; this is the shape
a person writes.
"""

from __future__ import annotations

import pytest
from flowpydisk import FlowpyDisk

FILE = "11111111-1111-4111-8111-111111111111"
FOLDER = "22222222-2222-4222-8222-222222222222"


@pytest.fixture
def sent(monkeypatch):
    calls = []
    client = FlowpyDisk(api_key="fd_test", base_url="http://127.0.0.1:9")

    def request(method, path, **kw):
        calls.append((method, path, kw.get("json")))
        return {"released": 1, "queued": 1, "waiting": 0, "skipped": 0}

    monkeypatch.setattr(client, "request", request)
    yield client, calls
    client.close()


def test_files_by_id(sent):
    client, calls = sent
    assert client.index.release(file_ids=[FILE])["released"] == 1
    assert calls == [("POST", "knowledge/index/release", {"items": [{"entity_type": "file", "entity_id": FILE}]})]


def test_a_folder_and_all_held(sent):
    client, calls = sent
    client.index.release(folder_id=FOLDER)
    client.index.release(all_held=True)
    assert [c[2] for c in calls] == [{"folder_id": FOLDER}, {"all_held": True}]


def test_exactly_one_selector(sent):
    client, calls = sent
    with pytest.raises(ValueError):
        client.index.release()
    with pytest.raises(ValueError):
        client.index.release(file_ids=[FILE], all_held=True)
    assert calls == []


def test_the_index_listing_sends_its_fact_filters(monkeypatch):
    # M1281: the listing filters by language, rows, size and days, as Ask AI does.
    calls = []
    client = FlowpyDisk(api_key="fd_test", base_url="http://127.0.0.1:9")

    def request(method, path, **kw):
        calls.append((method, path, kw.get("params")))

    monkeypatch.setattr(client, "request", request)
    client.knowledge.list_index(language="ja", min_rows=10, updated_after="2026-10-01", folder_id=FOLDER)
    client.close()
    sent = {"language": "ja", "min_rows": 10, "updated_after": "2026-10-01", "folder_id": FOLDER}
    assert calls == [("GET", "knowledge/index", sent)]
