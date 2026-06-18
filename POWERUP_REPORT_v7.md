# Power-Up Report — v7 reproducibility & i18n layer

Date: `2026-06-18`
Base: `Purpose_Root_v6_C2_AI_HARDENED_OWNER_FULL` (the superset of the two
supplied packages; the `NEED_PROOF_FINAL_HARDENED_v4` package is fully contained
within it).

This report documents the additive power-up applied on top of the verified v6
release. **No SHA256-committed v6 file was modified.** The canonical doctrine
text and all pinned release files remain byte-identical and verify cleanly.

本レポートは、検証済みv6リリースの上に加えた加算的強化を記録する。
**SHA256でコミット済みのv6ファイルは一切改変していない。** ドクトリン正本と
固定済みリリースファイルはバイト単位で不変であり、整合性検証に合格する。

---

## 0. Provenance / 由来

- Two packages were supplied. `C2_AI_HARDENED_OWNER_FULL` is a strict superset of
  `NEED_PROOF_FINAL_HARDENED_v4`: it adds the entire `c2_ready/` experiment
  package and promotes `cap_reason` to a required field in the C2 response
  schema. No file exists only in the v4 package. → The C2 owner-full package was
  adopted as the canonical source.
- 供給された2パッケージのうち `C2_AI_HARDENED_OWNER_FULL` が厳密な上位集合
  （`c2_ready/` 一式の追加、`cap_reason` の必須昇格）。v4固有ファイルは無し。
  よってC2版を正本として採用した。

---

## 1. Reproducibility / CI / re-runnability （軸1）

- `requirements.txt` (jsonschema) and `requirements-dev.txt` (+pytest) — the
  package previously declared no dependencies; the scorer silently degraded
  without `jsonschema`.
- `pyproject.toml` — Python floor (≥3.11), dependency metadata, and a pytest
  configuration that collects `machine/`, `tests/`, `need_proof/`,
  `c2_ready/tests/`, and `independent_labeling_v3/`.
- `Makefile` — `install-dev`, `test`, `canonical`, `releases`, `validate`,
  `score`, `all`, `clean`.
- `tools/run_all.py` — a single gate running, in order: canonical commitment
  check → release manifest/SHA256 check → package self-check → the four shipped
  validators → full pytest. Exit 0 only if all green.
- `.github/workflows/ci.yml` — runs the gate on Python 3.11 and 3.12 for every
  push and PR.
- `.gitignore` — excludes `__pycache__/`, `.pytest_cache/`, venvs, editor noise.
- `.claude/hooks/session-start.sh` + `.claude/settings.json` — SessionStart hook
  installs dependencies in web sessions so tests/validators run immediately.

## 2. Code / test hardening （軸2）

- **Integrity verifiers (new):**
  - `tools/verify_canonical.py` — recomputes the SHA256 of the three doctrine
    text blocks and asserts they equal the embedded commitments. This is the
    strongest anti-tamper gate: any silent edit of the doctrine fails CI.
  - `tools/verify_releases.py` — shape-agnostic verifier for **all** release
    manifests (`{hashes}`, `{files:[dict]}`, `{files:[str]}`, root-list) and
    SHA256SUMS files. It separates **current** authoritative manifests
    (`manifest.json`, `manifest_c2_ready.json` — must pass) from **superseded**
    snapshots (reported as informational drift), and skips ephemeral build
    artifacts that some upstream manifests accidentally captured.
- **Robust scorer companion (new):** `tools/score_robust.py`. The pinned scorer
  pushes a "jsonschema not available" sentinel into `schema_errors`, which makes
  `schema_valid` report False and silently downgrades valid A3+ proposals to
  Hold — conflating "could not check" with "invalid". The wrapper reuses 100% of
  the base logic but exposes `schema_validation_available` /
  `schema_validation_skipped` and reports `schema_valid=True` when no real error
  is found. The pinned file is untouched.
- **Tests (new, +21 → 79 total):**
  - `tests/test_repo_integrity.py` — canonical commitments, current-release
    cleanliness, benchmark = 300 rows, canonical file is pinned.
  - `tests/test_score_robust.py` — wrapper matches base with jsonschema present;
    with jsonschema simulated-absent it does not treat "skipped" as "invalid",
    yet still Rejects on a hard gate.
  - `tests/test_additional_adversarial.py` — 13 extra attack shapes against the
    unmodified scorer (single-scalar override, metric-gaming, dissent closure,
    irreversible-high-harm, lock-in budget, claimant-controlled emergency end,
    A4 untested rollback, high capture risk, too-few evaluators, unlogged
    high lock-in, evaluator/root-revision capture, mutation-isolation guard).
  - `conftest.py` — repo-wide path setup so any test can import `machine/` and
    `tools/` modules.

## 3. Evaluation / benchmark expansion （軸3）

- The 13 new adversarial regression cases above broaden machine-layer coverage
  of the verdict logic beyond the shipped 16, exercising conditional gates and
  consistency errors that previously had no explicit test.
- These run against the byte-identical pinned scorer, so they also act as a
  behavioral lock on the v6 release.

## 4. Internationalization （軸4）

- `docs/en/` — faithful English renderings of the orientation and four core
  specs, plus an index:
  `INDEX.md`, `README.en.md`, `START_HERE.en.md`, `OPERATIONAL_SPEC_v6_EN.md`,
  `MACHINE_SPEC_v6_EN.md`, `EVIDENCE_INDEPENDENCE_SPEC_v6_EN.md`,
  `ASSURANCE_CASE_REQUIREMENTS_v6_EN.md`,
  `LIMITATIONS_AND_OPEN_PROBLEMS_v6_EN.md`.
- The authoritative English doctrine form already lived (SHA256-committed) in
  `CANONICAL_ROOT_v6.md`; the new docs orient around it and explicitly defer to
  the Japanese canonical text on any conflict.
- `REPO_GUIDE.md` — bilingual top-level entry point.

- **i18n pass 2 (added):** English renderings of the threat model, the ten
  advanced red-team cases, both whitepapers (v6 + public-review empirical), the
  improvement report, the self-review log, and both QA reports:
  `THREAT_MODEL_v6_EN.md`, `REDTEAM_ADV_CASES_v6_EN.md`, `WHITEPAPER_v6_EN.md`,
  `PUBLIC_REVIEW_WHITEPAPER_v6_EN.md`, `IMPROVEMENT_REPORT_v6_EN.md`,
  `SELF_REVIEW_LOG_v6_EN.md`, `QA_REPORT_v6_EN.md`,
  `QA_REPORT_PUBLIC_REVIEW_EN.md`. The doctrine, specs, whitepapers, threat
  model, red team, and QA are now all readable in English.

> The only remaining Japanese-only material is the rendered binaries (DOCX/PDF),
> the benchmark data rows, and the per-stage `START_HERE_*` / `README_*`
> pointers for historical sub-releases. Each English doc defers to its Japanese
> source and the SHA256-committed canonical text on any conflict.

---

## Verification / 検証

Everything is green:

```
$ python tools/run_all.py
  canonical doctrine commitments  PASS
  release manifests + SHA256SUMS  PASS
  package release self-check      PASS
  validator: limit_break_v2       PASS
  validator: max_validation_v3    PASS
  validator: final_hardened_v4    PASS
  validator: c2_ready             PASS
  pytest (full suite)             PASS   (79 passed)
RESULT: PASS — all reproducibility gates green.
```

## What was deliberately NOT changed / あえて変えなかったもの

- The canonical doctrine text and its three SHA256 commitments.
- Any file pinned in `release/manifest.json` or `release/manifest_c2_ready.json`
  (scorer, schema, examples, benchmark, READMEs, specs, …).
- The doctrine, scoring axes, hard gates, and verdict semantics.

Rationale: integrity and the Root's own anti-tamper principle. Strengthening the
package must not silently rewrite the thing whose immutability it asserts.
