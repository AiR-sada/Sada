#!/bin/bash
# SessionStart hook: install Python deps so tests, validators, and the
# reproducibility gate (tools/run_all.py) work immediately in web sessions.
set -euo pipefail

# Web (remote) sessions only; local sessions manage their own environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"
python3 -m pip install -q -r requirements-dev.txt
