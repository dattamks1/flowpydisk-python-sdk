"""The owner-key calendar sync calls generated from the public contract."""

import json

import httpx
from flowpydisk import FlowpyDisk


def test_calendar_sync_management_uses_owner_key_and_expected_routes():
    seen = []

    def respond(request):
        seen.append(request)
        return httpx.Response(200, json={"ok": True})

    with FlowpyDisk(api_key="fd_owner", transport=httpx.MockTransport(respond)) as client:
        assert client.calendar.list_calendars(connection_id="connection-1") == {"ok": True}
        assert client.calendar.list_subscriptions() == {"ok": True}
        assert client.calendar.create_subscriptions(
            json={
                "connection_id": "connection-1",
                "remote_calendar_id": "primary",
                "import_start": "2026-01-01T00:00:00Z",
                "import_end": "2026-02-01T00:00:00Z",
                "destination": False,
            }
        ) == {"ok": True}
        assert client.calendar.update_subscriptions("subscription-1", json={"destination": True}) == {"ok": True}
        assert client.calendar.sync_subscriptions("subscription-1") == {"ok": True}
        assert client.calendar.list_conflicts() == {"ok": True}
        assert client.calendar.resolve_conflicts("conflict-1", json={"choice": "keep_local"}) == {"ok": True}

    assert [(r.method, r.url.path, r.url.query.decode()) for r in seen] == [
        ("GET", "/api/v1/calendar/sync/calendars", "connection_id=connection-1"),
        ("GET", "/api/v1/calendar/sync/subscriptions", ""),
        ("POST", "/api/v1/calendar/sync/subscriptions", ""),
        ("PATCH", "/api/v1/calendar/sync/subscriptions/subscription-1", ""),
        ("POST", "/api/v1/calendar/sync/subscriptions/subscription-1/sync", ""),
        ("GET", "/api/v1/calendar/sync/conflicts", ""),
        ("POST", "/api/v1/calendar/sync/conflicts/conflict-1/resolve", ""),
    ]
    assert all(r.headers["Authorization"] == "Bearer fd_owner" for r in seen)
    assert all("Workspace-Id" not in r.headers for r in seen)
    assert json.loads(seen[2].content)["destination"] is False
    assert json.loads(seen[3].content) == {"destination": True}
    assert json.loads(seen[6].content) == {"choice": "keep_local"}

