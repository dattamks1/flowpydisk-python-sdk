"""Sign one exact-byte request for a FlowpyDisk incoming webhook endpoint."""

import hashlib
import hmac
from uuid import UUID


def sign_inbound_webhook(
    secret: str, endpoint_id: UUID | str, timestamp: int, nonce: str, body: bytes
) -> dict[str, str]:
    """Return v1 signing headers; send ``body`` unchanged as JSON bytes.

    Use a fresh printable nonce (16–128 characters) and current Unix timestamp
    for each request. The server accepts a timestamp within five minutes and
    claims each nonce once per endpoint.
    """
    if not isinstance(secret, str) or not secret:
        raise ValueError("secret must be a nonempty string")
    endpoint = UUID(str(endpoint_id))
    if not isinstance(timestamp, int) or isinstance(timestamp, bool) or timestamp <= 0:
        raise ValueError("timestamp must be a positive Unix second")
    if not isinstance(nonce, str) or not 16 <= len(nonce) <= 128 or any(ord(c) < 33 or ord(c) > 126 for c in nonce):
        raise ValueError("nonce must be 16–128 printable ASCII characters")
    if not isinstance(body, bytes):
        raise TypeError("body must be exact bytes")
    if len(body) > 1024 * 1024:
        raise ValueError("body exceeds 1 MiB")
    canonical = f"v1\n{endpoint}\n{timestamp}\n{nonce}\n".encode() + body
    digest = hmac.new(secret.encode("utf-8"), canonical, hashlib.sha256).hexdigest()
    return {
        "FlowpyDisk-Webhook-Timestamp": str(timestamp),
        "FlowpyDisk-Webhook-Nonce": nonce,
        "FlowpyDisk-Webhook-Signature": f"v1={digest}",
    }
