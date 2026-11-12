import time

from flowpydisk import verify_webhook


def _sign(secret, body, t):
    import hashlib
    import hmac

    return f"t={t},v1=" + hmac.new(secret.encode(), f"{t}.".encode() + body, hashlib.sha256).hexdigest()


def test_a_fresh_signature_verifies():
    t = int(time.time())
    assert verify_webhook("whsec_a", _sign("whsec_a", b"{}", t), b"{}")


def test_a_wrong_secret_a_changed_body_and_an_old_request_fail():
    t = 1_000
    header = _sign("whsec_a", b"{}", t)
    assert not verify_webhook("whsec_b", header, b"{}", now=t)
    assert not verify_webhook("whsec_a", header, b"{ }", now=t)
    assert not verify_webhook("whsec_a", header, b"{}", now=t + 301)
    assert not verify_webhook("whsec_a", "", b"{}", now=t)
