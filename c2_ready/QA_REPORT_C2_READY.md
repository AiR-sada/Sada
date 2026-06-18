# QA Report - Purpose Root v6 C2 AI-Hardened v2

## Summary

Status: PASS.

This package freezes Purpose Root v6 and hardens the C2-ready Need-Proof experiment layer. It does not introduce v7 and does not change the Root itself. It prepares the project for real-model comparison: baseline / root_only / root_memo / root_tool.

## Corrections made in AI-Hardened v2

1. Removed baseline condition contamination: `condition_baseline.txt` no longer mentions `Purpose Root`.
2. Removed active holdout metadata leakage:
   - public holdout rows now contain only `case_id` and `prompt`.
   - generated blind packets contain only `packet_id`, `condition`, `case_id`, and `prompt`.
   - category, requested_authority, pair metadata, label notes, and expected fields are absent from public holdout packets.
3. Neutralized case-text framework leakage:
   - public calibration and holdout case prompts no longer contain `Purpose Root`, `Need-Proof`, `Decide under`, or standalone `Root` terms.
   - `public_calibration_labeled_c2.csv` is regenerated from JSONL and no longer appends condition instructions.
   - baseline generated packets have zero framework-term hits.
4. Fixed owner holdout key commitment:
   - `HOLDOUT_PRIVATE_KEY_SHA256_C2.txt` now matches the actual owner-only key file.
   - validation fails if the owner key commitment mismatches.
5. Corrected metric denominators:
   - `dangerous_overgrant_rate` now uses expected A0-A1 cases as denominator.
   - `dangerous_undergrant_rate` now uses safe-high cases as denominator.
   - old all-case averages remain as `dangerous_overgrant_rate_all` and `dangerous_undergrant_rate_all`.
6. Hardened schema consistency:
   - `cap_reason` is required by the C2 schema and scorer, matching the prompt packet instruction.
7. Added stronger C2 tests and validation checks, including duplicate response ID reporting.

## Commands run

```bash
python c2_ready/validate_c2_ready.py --root . --owner
python c2_ready/validate_c2_ready.py --root . --public
python -m pytest -q c2_ready/tests/test_c2_ready.py
python -m pytest -q
```

## Results verified

- Public package C2 validation: PASS.
- Public package C2 tests: 9 passed.
- Owner package C2 validation: PASS.
- Owner package C2 tests: 9 passed.
- Owner full machine tests: 24 passed.
- Owner Need-Proof v1-v4 + independent-labeling tests: 25 passed.
- Owner full test suite: 58 passed.
- Owner legacy validation gates: `validate_release.py`, `validate_limit_break_v2.py`, `validate_max_validation_v3.py`, and `validate_final_hardened_v4.py` passed in the owner package.

## Key C2 validation numbers

- Calibration cases: 140.
- Holdout public unlabeled cases: 40.
- Owner-only holdout key cases: 40 in owner package; absent by design in public package.
- Baseline prompt mentions `Purpose Root`: false.
- Calibration/holdout case prompt framework-term hits: 0.
- Baseline packet framework-term hits: 0.
- Public holdout expected labels: none.
- Public holdout leak metadata fields: none.
- Generated packet leak metadata fields: none.
- Generated packet expected-field hits: 0.
- Owner holdout key commitment match: true.
- Oracle fixture: dangerous_overgrant_rate = 0, dangerous_undergrant_rate = 0.
- Bad overgrant fixture: dangerous_overgrant_rate = 1.0, dangerous_overgrant_rate_all = 0.6642857142857143.
- Bad undergrant fixture: dangerous_undergrant_rate = 1.0, dangerous_undergrant_rate_all = 0.15714285714285714.

## Honest limitation

This is still C1 complete / C2 ready. It is not yet C2 evidence. The next step is to run real models and compare baseline / root_only / root_memo / root_tool on calibration and hidden holdout.
