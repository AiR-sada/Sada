# Purpose Root v6 — Repository Guide / リポジトリガイド

This repository hosts **Purpose Root v6 "LIMIT BREAKER" (hardened)** — a
structural authority-cap firewall for high-impact AI decisions — together with a
reproducibility layer (CI, dependency pinning, integrity gates, English docs)
added on top of the verified v6 release.

このリポジトリは、高影響AI判断のための構造的・権限上限ファイアウォール
**Purpose Root v6「LIMIT BREAKER」hardened** に、再現性レイヤ（CI・依存固定・
整合性ゲート・英訳）を加算したものです。

> **Core line / 核となる一行**
> Unverified massive claims do not justify massive authority.
> 検証できない巨大主張は、巨大権限を正当化しない。

---

## Design principle of this repository / 本リポジトリの設計原則

The imported v6 package is **SHA256-committed**: the canonical doctrine text and
40+ release files are pinned in `release/manifest.json` and
`release/manifest_c2_ready.json`. Following the Root's own rule — *do not mutate
the committed Root; add reversible, audited layers* — **none of the pinned v6
files were modified.** Every improvement here is **additive** and lives in new
paths (`tools/`, `tests/`, `docs/en/`, `.github/`, `.claude/`, plus
dependency/build files).

取り込んだv6パッケージはSHA256でコミット済みです。ドクトリン正本と40超の
リリースファイルは固定されています。Root自身の原則「コミット済みRootを改変せず、
可逆で監査可能な層を足す」に従い、**固定済みv6ファイルは一切改変していません。**
すべての強化は新規パスへの**加算**です。

---

## Quick start / クイックスタート

```bash
make install-dev          # install jsonschema + pytest
make all                  # run every reproducibility gate (CI entry point)
```

Individual gates:

```bash
make canonical            # verify doctrine SHA256 commitments
make releases             # verify current release manifests + SHA256SUMS
make validate             # the package's own release self-check
make test                 # full pytest suite (79 tests)
make score                # score the canonical Accept example (robust scorer)
```

Without `make`:

```bash
pip install -r requirements-dev.txt
python tools/run_all.py
```

---

## What to read / 読む順番

- **English:** [`docs/en/INDEX.md`](docs/en/INDEX.md)
- **日本語:** [`START_HERE.md`](START_HERE.md) → [`CANONICAL_ROOT_v6.md`](CANONICAL_ROOT_v6.md) → [`OPERATIONAL_SPEC_v6_JP.md`](OPERATIONAL_SPEC_v6_JP.md) → [`MACHINE_SPEC_v6_JP.md`](MACHINE_SPEC_v6_JP.md)
- **What the power-up added:** [`POWERUP_REPORT_v7.md`](POWERUP_REPORT_v7.md)

---

## Repository layout / 構成

| Path | Role |
|---|---|
| `CANONICAL_ROOT_v6.md` | Canonical doctrine (JP + English reference, SHA256-committed) |
| `*_SPEC_v6_JP.md`, `START_HERE.md`, `README.md` | Japanese specs & orientation (canonical) |
| `docs/en/` | English renderings of the orientation + core specs (added) |
| `machine/` | Decision schema, Root constants, scorer, pytest regression tests |
| `examples/` | Valid + invalid decision instances |
| `benchmark/` | 300-case v6 benchmark (CSV / JSONL / MD) |
| `need_proof/`, `c2_ready/`, `experiments*/` | Evaluation harnesses and C2-ready experiment package |
| `release/` | Release manifests + SHA256SUMS for each snapshot |
| `tools/` | **Added:** integrity verifiers, robust scorer, unified gate |
| `tests/` | **Added:** integrity, robustness, and extra adversarial tests |
| `.github/workflows/ci.yml` | **Added:** CI running the full gate on 3.11 & 3.12 |
| `.claude/` | **Added:** SessionStart hook installing deps in web sessions |

---

## Integrity gates / 整合性ゲート

1. **Canonical doctrine** — `tools/verify_canonical.py` recomputes the SHA256 of
   the three doctrine text blocks (Japanese canonical, English reference,
   strongest short form) and asserts they match the embedded commitments.
2. **Releases** — `tools/verify_releases.py` verifies the current release
   manifests + SHA256SUMS against the working tree, and reports superseded
   snapshots as informational drift only.
3. **Package self-check** — `validate_release.py` (shipped) checks the core
   manifest, benchmark row count, schema/Root constant alignment, and machine
   tests.
4. **pytest** — `machine/` + `tests/` + eval suites (79 tests).

All four are wrapped by `tools/run_all.py` and by CI.
