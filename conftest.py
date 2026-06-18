"""Pytest path setup for the repository.

Makes ``machine/`` and ``tools/`` importable from any test module without each
test having to manipulate ``sys.path`` itself.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for sub in ("", "machine", "tools"):
    p = str(ROOT / sub) if sub else str(ROOT)
    if p not in sys.path:
        sys.path.insert(0, p)
