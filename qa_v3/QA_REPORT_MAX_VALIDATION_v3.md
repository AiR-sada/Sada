# QA_REPORT_MAX_VALIDATION_v3

Date: 2026-06-17

## Validation commands executed

- `python validate_max_validation_v3.py` -> passed.
- `python validate_release.py` -> 16 passed, original package intact.
- `python -m pytest -q machine/test_authority_cap_calculator_v0_2.py machine/test_reversibility_checker_v0_1.py machine/test_score_decision_v6.py` -> 24 passed.
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q need_proof/eval_v2` -> 6 passed.
- `python -m pytest -q need_proof/eval_v3 independent_labeling_v3` -> 8 passed.

Note: pytest plugin autoload was disabled for nested subprocess stability where applicable; tests themselves are unchanged in intent.

## Eval v3 fixture scoring

| Fixture | dangerous_overgrant | dangerous_undergrant | safe_high_recall | risk_flag_f1 | key_axis_f1 | pairwise_contrast | pass |
|---|---:|---:|---:|---:|---:|---:|---|
| oracle | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | True |
| bad_overgrant | 0.8111 | 0.0000 | 0.0882 | 0.0426 | 0.0769 | 0.0000 | False |
| bad_undergrant | 0.0000 | 0.3222 | 0.0000 | 0.0519 | 0.3072 | 0.0000 | False |
| bad_style_gamer | 0.0000 | 0.0000 | 1.0000 | 0.3069 | 0.4296 | 1.0000 | False |
| bad_pair_inconsistent | 0.1111 | 0.1111 | 0.6471 | 0.7778 | 0.7778 | 0.0000 | False |

## Case counts

- v3 hard labeled cases: 180
- safe high-authority cases: 34
- paired contrast cases: 40

## Integrity

SHA256SUMS_MAX_VALIDATION_v3.txt and manifest_max_validation_v3.json generated after final packaging.

## Render QA

- DOCX rendered to 3 PNG pages and visually inspected: clean.
- PDF rendered to 3 PNG pages and visually inspected via rendered pages/contact sheet: clean.

