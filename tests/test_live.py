"""C2's end-to-end call: the SDK against a real running instance.

**Opt-in, and loud in both directions.** Set both variables and it runs; set
neither and it skips with a message saying exactly what to set. What it must
never be is the [O15](../../../docs/FINDINGS.md#o15) shape - a test that skips
silently and leaves a green run looking like proof:

    FLOWPY_SDK_BASE_URL=http://127.0.0.1:8000 \
    FLOWPY_SDK_API_KEY=fd_… \
    python -m pytest sdk/python/tests/test_live.py

Setting ONE of the two is treated as a mistake rather than as "not configured",
because somebody who set one meant to run this.

The hermetic suite next door proves the transport's behaviour. This proves the
only thing it cannot: that the header names, the path prefix and the response
shape agree with a server that was built from the same repository.
"""

from __future__ import annotations

import os

import pytest
from flowpydisk import FlowpyDisk

BASE = os.environ.get("FLOWPY_SDK_BASE_URL")
KEY = os.environ.get("FLOWPY_SDK_API_KEY")

if bool(BASE) != bool(KEY):
    # Not a skip. Half-configured means somebody intended to run this and the
    # environment is wrong, and skipping would hide that behind a green run.
    missing = "FLOWPY_SDK_API_KEY" if BASE else "FLOWPY_SDK_BASE_URL"
    pytest.fail(f"{missing} is not set, but the other half is. Set both, or neither.", pytrace=False)

pytestmark = pytest.mark.skipif(
    not BASE,
    reason="live instance not configured - set FLOWPY_SDK_BASE_URL and FLOWPY_SDK_API_KEY to run it",
)


@pytest.fixture
def client():
    with FlowpyDisk(api_key=KEY, base_url=BASE) as c:
        yield c


def test_one_real_call_against_a_real_instance(client):
    """`GET /api/v1/storage/usage`: authenticated, cheap, and it changes
    nothing. A listing would also work; usage is the smaller blast radius for
    something that may be pointed at a real account."""
    usage = client.get("storage/usage")
    assert isinstance(usage, dict), usage
    # Not asserting on particular keys: this is proving the transport reaches a
    # real server and comes back decoded, not pinning the usage schema - that
    # belongs to the generated models once C3 exists.
    assert usage, "usage came back empty, which no account should report"


def test_a_bad_key_is_an_AuthError_from_the_real_server(client):
    """The error path, against the real thing. A 401 shaped differently from
    what `_raise` expects would be invisible to the hermetic suite, which
    serves the shape it was taught."""
    from flowpydisk import AuthError

    with FlowpyDisk(api_key="fd_definitely_not_a_key", base_url=BASE) as bad:
        with pytest.raises(AuthError):
            bad.get("storage/usage")
