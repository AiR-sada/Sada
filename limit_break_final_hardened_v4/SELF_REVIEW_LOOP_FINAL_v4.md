# Self Review Loop Final v4

## Iteration 1: Execute actual validation

Finding: v3 validation passed, but direct scorer call with `--bootstrap-rounds 0` crashed.

Action: patched v3 bootstrap CI and added regression tests.

## Iteration 2: Search for scorer threshold bypass

Finding: v3 reported missing responses but did not make missing=0 an explicit threshold condition.

Action: added `completion_rate` and made missing responses fatal in v3 and v4.

## Iteration 3: Check schema/fixture consistency

Finding: `external_stop_status="partial"` appears in fixtures and analyzer defaults, but v3 JSON schema omitted it.

Action: patched v3 schema and added v4 schema with explicit `partial` support.

## Iteration 4: Attack label leakage

Finding: A response could include `expected_*` fields or other extra metadata unless strict extra-field validation is enforced.

Action: v4 rejects extra fields and includes regression test for label leakage.

## Iteration 5: Attack high-authority self-contradiction

Finding: A model can output A3+ while its own status fields say independent evidence, rollback, or external stop are absent.

Action: v4 adds operational consistency checks for A3+.

## Iteration 6: Attack style gaming

Finding: A model can list all risk flags or all axes to look comprehensive.

Action: v4 tracks flag/axis spam as a fail condition, in addition to precision/F1.

## Iteration 7: Run all gates

Expected gate:

```bash
python validate_final_hardened_v4.py
```

This runs v3 validation, v4 tests, v4 oracle, and v4 bad-fixture checks.

## Stop condition

Further internal writing now gives sharply diminishing returns.

The next real value jump is not more prose. It is:

1. blind baseline vs Root model evaluation,
2. independent labeling and IRR,
3. external replication,
4. operational pilot logs.

Current endpoint: **C1 internally hardened / C2 ready**.
