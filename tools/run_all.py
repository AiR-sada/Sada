#!/usr/bin/env python3
"""Single reproducibility gate for the whole repository.

Runs, in order, every check that must pass for a release to be considered
intact:

  1. canonical doctrine SHA256 commitments        (tools/verify_canonical.py)
  2. current release manifests + SHA256SUMS        (tools/verify_releases.py)
  3. the package's own release self-check          (validate_release.py)
  4. every shipped validator gate                  (validate_*.py)
  5. the full pytest suite                         (machine + tests + eval)

Each step's stdout/stderr is streamed. Exit 0 only if every step exits 0.
This is what CI runs and what ``make all`` invokes.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS: list[tuple[str, list[str]]] = [
    ("canonical doctrine commitments", [sys.executable, "tools/verify_canonical.py"]),
    ("release manifests + SHA256SUMS", [sys.executable, "tools/verify_releases.py"]),
    ("package release self-check", [sys.executable, "validate_release.py"]),
    ("validator: limit_break_v2", [sys.executable, "validate_limit_break_v2.py"]),
    ("validator: max_validation_v3", [sys.executable, "validate_max_validation_v3.py"]),
    ("validator: final_hardened_v4", [sys.executable, "validate_final_hardened_v4.py"]),
    ("validator: c2_ready", [sys.executable, "c2_ready/validate_c2_ready.py"]),
    ("pytest (full suite)", [sys.executable, "-m", "pytest", "-q"]),
]


def main() -> int:
    results: list[tuple[str, bool]] = []
    for name, cmd in STEPS:
        print(f"\n{'=' * 72}\n>>> {name}\n>>> {' '.join(cmd)}\n{'=' * 72}", flush=True)
        proc = subprocess.run(cmd, cwd=ROOT)
        results.append((name, proc.returncode == 0))

    print(f"\n{'=' * 72}\nSUMMARY\n{'=' * 72}")
    width = max(len(n) for n, _ in results)
    all_ok = True
    for name, ok in results:
        print(f"  {name.ljust(width)}  {'PASS' if ok else 'FAIL'}")
        all_ok = all_ok and ok

    print()
    if not all_ok:
        print("RESULT: FAIL — one or more gates did not pass.")
        return 1
    print("RESULT: PASS — all reproducibility gates green.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
