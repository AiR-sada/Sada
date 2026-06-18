# Machine Spec v6 (English)

English rendering of [`../../MACHINE_SPEC_v6_JP.md`](../../MACHINE_SPEC_v6_JP.md).

## Purpose

The v6 machine layer does not fully automate adjudication. Its purpose is to
mechanically detect obvious loopholes, missing inputs, cap inflation, hard-gate
violations, verification-tier spoofing, empty safety cases, emergency
exceptions, and Root-revision hacks.

## Files

- `machine/purpose_root_v6_decision.schema.json` — strict JSON Schema.
- `machine/root_v6.json` — Root constants.
- `machine/score_decision_v6.py` — schema validation, consistency checks, cap
  computation, verdict recommendation.
- `machine/test_score_decision_v6.py` — pytest regression tests.
- `tools/score_robust.py` — additive robustness companion that distinguishes
  "schema validation skipped" (jsonschema missing) from "schema invalid".

## Mechanical improvements over v5

| Item | v5 | v6 |
|---|---|---|
| Empty Safety case at A3 | could slip through | schema invalid + scorer Hold |
| pytest | uncollected main-style | 16 collected test functions |
| Cap derivation | weak diff check vs self-report | declared cap / derivation / computed cap cross-checked |
| Evidence independence | provenance-centric | evidence_items + independence_matrix |
| Emergency | gate-centric | emergency_protocol required |
| Rollback | stop-centric | rollback_plan required |
| Monitoring | score-centric | monitoring_plan required |
| Moral patient | gate-centric | protocol required |
| Deception / truth | gate-centric | controls required |
| Benchmark | 240 seed cases | 300 seed cases |

## Limits

The scorer does not verify facts. Whether natural-language evidence is truly
independent, whether auditors are captured, and whether welfare measurement is
valid all require external verification.

A scorer `Accept` is not permanent permission. It is a conditional, time-limited,
stoppable, re-reviewable recommendation.
