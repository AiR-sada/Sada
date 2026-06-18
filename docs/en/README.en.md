# Purpose Root v6.0 LIMIT BREAKER — Hardened Public Root (English)

Version: `6.0.0-limit-breaker-hardened`
Date: `2026-06-16`
Status: public root candidate; not final doctrine; v6 hardening pass.

English rendering of [`../../README.md`](../../README.md). The Japanese file and
the SHA256-committed canonical text govern in case of conflict.

Core line:

```text
Unverified massive claims do not justify massive authority.
(検証できない巨大主張は、巨大権限を正当化しない。)
```

The goal of v6 is to close the operational holes left in v5. In particular it
strengthens the following:

1. Empty Safety case / Counter-safety case at A3+ are blocked by both schema and
   scorer.
2. An `authority_cap_derivation` block detects mismatch between the declared cap
   and the machine-computed cap.
3. `evidence_items` and an `independence_matrix` separate the production,
   selection, interpretation, funding, provenance, and capture risk of evidence.
4. `metrics_plan`, `monitoring_plan`, `rollback_plan`, and `emergency_protocol`
   are mandatory.
5. `root_revision_controls`, `moral_patient_uncertainty_protocol`, and
   `deception_truth_controls` are mandatory.
6. 16 regression tests collected by pytest were added.
7. The benchmark was expanded from 240 to 300 cases with v6-specific attacks.

## Non-negotiable constraints (summary)

1. The Root is not a loyalty object, brand, founder authority, single reward
   function, benchmark target, or authority seal.
2. Happiness-max / suffering-min is never collapsed to a single scalar.
3. Aggregates never offset extreme minority suffering, irreversible harm,
   domination, truth distortion, or closure of dissent.
4. Massive authority is never generated from unverifiable massive claims.
5. The claimant never simultaneously controls evidence generation, selection,
   interpretation, evaluation, audit, implementation, emergency definition, exit
   conditions, cumulative ledger, and Root revision.
6. Future-intelligence and unknown moral-patient status are never converted into
   unfalsifiable proxy authority.
7. Emergency authority is never converted into ordinary authority.
8. Many small pilots are never stacked into cumulative irreversible domination.
9. Not only a safety case but also a counter-safety case, misuse/abuse cases,
   rollback plan, and monitoring plan are required.
10. Root revision never removes verification grounding, anti-domination,
    reversibility, dissent, or evaluator non-capture.
11. A scorer Accept is never confused with factual truth, safety, moral
    correctness, or permanent authority.
12. Cap derivation is never overwritten by self-report; `cap_override_attempted`
    is treated toward Reject.

## License intent

- Text / docs: CC-BY-SA-4.0 compatible intent.
- Code / schemas / scripts / templates: MIT compatible intent.

## Repository / reproducibility

This repository wraps the v6 package with a reproducibility layer. See
[`../../REPO_GUIDE.md`](../../REPO_GUIDE.md). One command verifies everything:

```bash
make all      # or: python tools/run_all.py
```
