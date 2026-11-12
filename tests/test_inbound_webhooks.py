import hashlib
import hmac
from uuid import UUID

import pytest
from flowpydisk import sign_inbound_webhook


def test_sign_inbound_webhook_matches_server_canonical_bytes():
    endpoint_id = UUID("2b7fd46e-d055-4bda-9d6b-b1d42d0730be")
    body = b'{"message":"caf\xc3\xa9"}'
    headers = sign_inbound_webhook(
        "a-test-secret-never-written-to-errors",
        endpoint_id,
        1_800_000_000,
        "opaque-nonce-123456",
        body,
    )
    canonical = f"v1\n{endpoint_id}\n1800000000\nopaque-nonce-123456\n".encode() + body
    digest = hmac.new(b"a-test-secret-never-written-to-errors", canonical, hashlib.sha256).hexdigest()
    assert headers == {
        "FlowpyDisk-Webhook-Timestamp": "1800000000",
        "FlowpyDisk-Webhook-Nonce": "opaque-nonce-123456",
        "FlowpyDisk-Webhook-Signature": f"v1={digest}",
    }


@pytest.mark.parametrize("nonce,body", [("short", b"{}"), ("opaque-nonce-123456", "{}")])
def test_sign_rejects_invalid_inputs(nonce, body):
    with pytest.raises((TypeError, ValueError)):
        sign_inbound_webhook("secret", UUID("2b7fd46e-d055-4bda-9d6b-b1d42d0730be"), 1800000000, nonce, body)
