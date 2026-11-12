"""Make `src/` importable without an install.

The push gate runs this suite on every push and a fresh clone has no editable
install of this package. Requiring one would mean the gate either skips the SDK
(the O15 hole in the findings register - a check that is silent when it
does not run) or fails a push for something the developer has not set up, which
is the thing the gate's own comments say it must not do.

An editable install (`pip install -e .`) still works; this is only
so the tests can run from a checkout.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
