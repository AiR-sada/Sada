# CLAUDE.md — guidance for Claude Code / contributors

This repository hosts **Purpose Root v6 "LIMIT BREAKER" (hardened)** — a
structural authority-cap firewall for high-impact AI decisions — plus an
additive reproducibility/i18n layer. Read [`REPO_GUIDE.md`](REPO_GUIDE.md) for
the full layout and [`POWERUP_REPORT_v7.md`](POWERUP_REPORT_v7.md) for what the
layer added.

## The one rule that overrides everything

**Do not modify any SHA256-committed v6 file.** The canonical doctrine text and
40+ release files are pinned in `release/manifest.json` and
`release/manifest_c2_ready.json`. The doctrine itself forbids mutating the
committed Root outside an audited high-impact revision, so:

- Treat the v6 release files as immutable. Make every improvement **additive**,
  in new paths: `tools/`, `tests/`, `docs/en/`, `.github/`, `.claude/`, and the
  dependency/build files at the root.
- If a change genuinely requires editing a pinned file, that is a doctrine-level
  revision: stop and ask the user first. Do not silently rewrite it.
- `tools/verify_canonical.py` and `tools/verify_releases.py` will fail CI if any
  pinned file or the doctrine text drifts. That is intended.

## Pinned files (do not edit)

Anything listed in `release/manifest.json` (40 core files) or
`release/manifest_c2_ready.json` (299 files), including:
`CANONICAL_ROOT_v6.md`, `README.md`, `START_HERE.md`, every `*_SPEC_v6_JP.md`,
`machine/score_decision_v6.py`, `machine/purpose_root_v6_decision.schema.json`,
`machine/root_v6.json`, all of `examples/`, and the `benchmark/` data.

To check whether a path is pinned:

```bash
python - <<'PY'
import json
pinned = {h["path"] for h in json.load(open("release/manifest.json"))["hashes"]}
pinned |= {f["path"] for f in json.load(open("release/manifest_c2_ready.json"))["files"]}
print("YOUR/PATH/HERE" in pinned)
PY
```

## Commands

```bash
make install-dev   # pip install jsonschema + pytest
make all           # full reproducibility gate (what CI runs) — or: python tools/run_all.py
make test          # pytest only (79 tests)
make canonical     # verify doctrine SHA256 commitments
make releases      # verify current release manifests + SHA256SUMS
make score         # robust scorer on the canonical Accept example
```

Always run `make all` before committing. A green run means: doctrine
commitments intact, current release verifies, package self-check passes, all
four shipped validators pass, and the full pytest suite passes.

## Conventions

- Python ≥ 3.11. Runtime dep: `jsonschema`. Dev dep: `pytest`. Both declared in
  `requirements*.txt` / `pyproject.toml`.
- New tests go in `tests/`; `conftest.py` already puts `machine/` and `tools/`
  on `sys.path`, so import scorer/verifier modules by bare name.
- New English docs go in `docs/en/` and must defer to the Japanese source and
  the SHA256-committed canonical text on any conflict.
- The machine scorer is a **structural firewall, not a moral or factual oracle**;
  keep that framing in any code or docs you add.

## Do not

- Do not create a pull request unless the user explicitly asks.
- Do not commit build artifacts (`__pycache__/`, `.pytest_cache/`); they are
  gitignored. Run `make clean` if they appear.
- Do not add a binding LICENSE: the package states *license intent* (MIT for
  code, CC-BY-SA-4.0 for docs) but leaves the final license to the owner.
