"""Five classes, and every error code the backend has.

[SDK_PLAN §5](../../../../docs/SDK_PLAN.md). The worklist's C5 row asks for
"quota, size cap, scoped-key not-found, throttles, each with its own exception
and message". Measured against the tree on 2026-09-15, the backend returns
**67 distinct ``code`` values**, and sixty-seven exception classes is a
taxonomy nobody can hold in their head and an ``except`` clause nobody can
write.

So the split is by **what you can do about it**, and the exact code survives
on ``.code``:

    except Throttled as e:                  # back off, e.retry_after says how long
    except LimitExceeded as e:              # ask for more room, or send less
        if e.code == "file_too_large": …    # ...or handle exactly this one

Nothing is swallowed. ``.status``, ``.code``, ``.detail`` and the response
itself are all on the exception, so a caller who needs something this module
did not anticipate still has it.
"""

from __future__ import annotations

from typing import Any


class FlowpyDiskError(Exception):
    """Anything the API refused, plus what it said about it.

    ``code`` is the backend's own string (``file_too_large``, ``no_workspace``,
    ``kind_not_publishable``, …) and is the value to branch on. It is ``None``
    only when a response carried no envelope at all - a proxy's 502, say - and
    that is worth distinguishing from an empty string, which would read as "the
    backend sent a code and it was blank".
    """

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        code: str | None = None,
        detail: Any = None,
        response: Any = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.detail = detail
        self.response = response

    def __str__(self) -> str:
        base = super().__str__()
        # The code in the repr, always. A traceback that says only "Not found"
        # sends somebody to the wrong problem; one that says
        # "Not found (code=folder_not_found, status=404)" does not.
        bits = [f"status={self.status}" if self.status else "", f"code={self.code}" if self.code else ""]
        suffix = ", ".join(b for b in bits if b)
        return f"{base} ({suffix})" if suffix else base


class AuthError(FlowpyDiskError):
    """401 and 403. The key is wrong, expired, or not allowed to do this."""


class NotFound(FlowpyDiskError):
    """404. The object does not exist, or is outside the space this key acts
    in: the server answers not-found rather than forbidden, on purpose,
    because forbidden would confirm the thing exists.

    The client once asked the server whether a folder-scoped key was behind
    a 404 and named the folder. Folder keys are retired, so it no longer asks
    (M2893).
    """


class InvalidRequest(FlowpyDiskError):
    """400 and 422. The call itself was wrong - a bad filter, an unknown kind."""


class LimitExceeded(FlowpyDiskError):
    """402 and 413. Quota, the per-file cap, a plan limit.

    Distinct from InvalidRequest because the remedy is different in kind: the
    call was well formed and the account cannot currently accommodate it.
    """


class Throttled(FlowpyDiskError):
    """429. ``retry_after`` is seconds, when the response said so."""

    def __init__(self, message: str, *, retry_after: float | None = None, **kw: Any) -> None:
        super().__init__(message, **kw)
        self.retry_after = retry_after


#: Status -> class. Anything unmapped raises the base class rather than being
#: forced into the nearest one: a 418 or a 502 is not an InvalidRequest, and
#: saying so wrongly is worse than saying nothing.
BY_STATUS: dict[int, type[FlowpyDiskError]] = {
    400: InvalidRequest,
    401: AuthError,
    402: LimitExceeded,
    403: AuthError,
    404: NotFound,
    413: LimitExceeded,
    422: InvalidRequest,
    429: Throttled,
}

__all__ = [
    "AuthError",
    "FlowpyDiskError",
    "InvalidRequest",
    "LimitExceeded",
    "NotFound",
    "Throttled",
]
