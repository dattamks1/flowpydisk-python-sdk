# flowpydisk

The official Python SDK for [FlowpyDisk](https://flowpydisk.com), a product by
Invrsys. FlowpyDisk is a workspace for files, calendar, meetings, chat and AI
search, in one place.

## What you can do

- Files and folders: upload, download, move, rename, versions, trash and restore
- Sharing: share links and permissions
- Search: by name, inside content, and by meaning
- Calendar and meetings: events, invites, booking pages, transcripts and recordings
- Tables, notes, canvases, forms and tasks
- Workspaces: members, invites, usage and plan limits
- Webhooks: subscribe to events and check deliveries

Billing and account security are not reachable with an API key. They need a
signed-in session in the app.

## Before you start

You need:

1. A FlowpyDisk account. Sign up at https://app.flowpydisk.com
2. A FlowpyDisk API key, made in the app under **Settings > Developer**
3. Python 3.11 or newer

## Install

```bash
pip install flowpydisk
```

The only dependency is `httpx`.

## Authenticate

Create an API key in the app under **Settings > Developer**, then pass it to the
client. Keep it out of your code, for example in an environment variable.

```python
import os
from flowpydisk import FlowpyDisk

with FlowpyDisk(api_key=os.environ["FLOWPYDISK_API_KEY"]) as client:
    ...
```

### What a key can reach

- A key acts as the person who made it, and never does more than they can.
  If they lose access to something, so does the key.
- A key works in one space only. A personal key works in your personal space.
  A workspace key works in that workspace and no other. To work in several
  workspaces, make one key in each.
- A key can be read only, or read and write.
- A key can be limited to one folder and everything inside it. Search and the
  graph are limited to that folder too.
- A workspace key can also reach its maker's own drive in that workspace, if
  that option is turned on for the key.

## Files and folders

```python
folder = client.storage.create_folders(json={"name": "Reports"})

uploaded = client.files.upload("q3.pdf", folder=folder["id"])  # single or resumable, picked for you

client.storage.list_files(scope="all")
for f in client.paginate("storage/files"):                     # every page
    print(f["name"])

client.storage.get_files(uploaded["id"])
client.storage.delete_files(uploaded["id"])                    # to trash, can be restored
client.storage.restore_files(uploaded["id"])
```

## Calendar, meetings and live calls

```python
event = client.calendar.create_events(json={
    "title": "Weekly sync",
    "start_at": "2026-11-20T10:00:00Z",
    "end_at": "2026-11-20T10:30:00Z",
})
client.calendar.list_events()

client.collab.meeting_events(event["id"])            # open the meeting on the event
client.collab.get_meetings(meeting_id)                # a meeting, before joining
client.collab.list_live_calls()                       # calls on now in this space
```

Calendar sync (subscriptions and conflicts) needs a personal API key. Connect
the calendar account in the web app first.

## Search

```python
client.storage.list_search(q="invoice")             # files by name
client.knowledge.list_search(q="onboarding")        # everything, by name, description and tag
client.rag.list_search(q="what did we agree on pricing")   # by meaning, over document content
client.graph.list_search(q="Acme")                  # graph search: matches plus their neighbours
client.graph.list_graph()                           # the knowledge graph you can see
```

## Other namespaces

Every API area is a namespace on the client, for example:

- `client.tables`, `client.tasks`, `client.forms`, `client.canvas`
- `client.collab` (chat, meetings), `client.comments`, `client.notifications`
- `client.mail`, `client.booking`, `client.publishing`, `client.sharing`
- `client.webhooks`, `client.inbound_webhooks`, `client.backups`, `client.workspaces`

Method names follow the HTTP verb and the path (`list_`, `get_`, `create_`,
`update_`, `delete_` and so on). Each method's docstring shows its route.
`client.get/post/patch/delete(path, ...)` reach any route directly.

## Errors

Every refusal raises a subclass of `FlowpyDiskError`:

| Class | Status | Meaning |
| --- | --- | --- |
| `AuthError` | 401, 403 | Key wrong, expired or not allowed |
| `NotFound` | 404 | Missing, or outside the key's space |
| `InvalidRequest` | 400, 422 | The call itself was wrong |
| `LimitExceeded` | 402, 413 | Quota, file size or plan limit |
| `Throttled` | 429 | Too many requests |

Each error has `.status`, `.code` (the stable value to branch on), `.detail`
and `.response`. The API's error body also says why it failed and what to do
next:

```python
from flowpydisk import FlowpyDiskError, LimitExceeded

try:
    client.files.upload("big.zip")
except LimitExceeded as e:
    print(e.code)                                   # for example "file_too_large"
except FlowpyDiskError as e:
    body = e.response.json() if e.response is not None else {}
    print(body.get("why"), body.get("next"), body.get("code"))
```

## Rate limits

Requests are limited per minute by plan. Over the limit the API answers 429
with a `Retry-After` header, and the SDK raises `Throttled` with
`e.retry_after` in seconds. GET, HEAD, PUT and DELETE are retried
automatically on 429 and 5xx (twice by default, set `retries=`). POST is never
retried, so a create is never sent twice.

## API reference

- Website: https://flowpydisk.com
- Public API catalogue: https://app.flowpydisk.com/api/v1/public/api

## Contributions

This repository does not accept contributions, pull requests or issues for now.

## License

Apache-2.0. See [LICENSE](LICENSE).
