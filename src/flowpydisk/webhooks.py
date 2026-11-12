"""Verifying a FlowpyDisk webhook request, for a receiver written in Python.

    from flowpydisk import verify_webhook

    ok = verify_webhook(secret, request.headers["FlowpyDisk-Signature"], request.body)

`FlowpyDisk-Signature` is `t=<unix seconds>,v1=<hex>`: HMAC-SHA256, keyed by
the webhook's secret, over `"<t>.<raw body>"`. Pass the body exactly as it
arrived, before any JSON parsing, because re-serialising changes the bytes.
A `t` more than `tolerance` seconds from now is refused, which is what stops a
captured request being replayed.

A copy of `backend/apps/webhooks/signing.verify`, kept here so a receiver need
not import the backend; a guard in the backend tests the two against each
other.
"""

from __future__ import annotations

import hashlib
import hmac
import time

SIGNATURE_HEADER = "FlowpyDisk-Signature"


def verify_webhook(secret: str, header: str, body: bytes, *, tolerance: int = 300, now: int | None = None) -> bool:
    parts: dict[str, list[str]] = {}
    for item in (header or "").split(","):
        key, _, value = item.strip().partition("=")
        parts.setdefault(key, []).append(value)
    try:
        t = int(parts["t"][0])
    except (KeyError, ValueError):
        return False
    current = int(time.time()) if now is None else now
    if abs(current - t) > tolerance:
        return False
    if isinstance(body, str):
        body = body.encode()
    expected = hmac.new(secret.encode(), f"{t}.".encode() + body, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, v) for v in parts.get("v1", []))
