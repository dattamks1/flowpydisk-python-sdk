"""Python client for the FlowpyDisk API.

    from flowpydisk import FlowpyDisk

    client = FlowpyDisk(api_key="fd_…")
    for f in client.paginate("storage/files"):
        print(f["name"])

The shape and the reasoning behind every choice here are in the
FlowpyDisk SDK design plan.

**What is built:** the transport (C2) - auth, the error taxonomy, retries,
pagination; the generated operations (C3), one namespace per tag in the spec
(`client.storage.list_files()`, `client.tables.rows_tables(...)`); and the
hand-written layer over them (C4) - `client.files.upload(path)`, the three-step
upload as one call, and `client.index`. Everything a caller imports is
re-exported from this file, so `_generated` stays private and a regeneration
cannot change what a caller imports.
"""

from ._client import DEFAULT_BASE_URL, FlowpyDisk
from ._errors import (
    AuthError,
    FlowpyDiskError,
    InvalidRequest,
    LimitExceeded,
    NotFound,
    Throttled,
)
from .files import Files
from .inbound_webhooks import sign_inbound_webhook
from .webhooks import SIGNATURE_HEADER, verify_webhook

__version__ = "0.0.2"

__all__ = [
    "DEFAULT_BASE_URL",
    "SIGNATURE_HEADER",
    "AuthError",
    "Files",
    "FlowpyDisk",
    "FlowpyDiskError",
    "InvalidRequest",
    "LimitExceeded",
    "NotFound",
    "Throttled",
    "__version__",
    "sign_inbound_webhook",
    "verify_webhook",
]
