# QA Report - Review Ready Limit Breaker Package

## Validation

- `python validate_release.py`: passed.
- `python -m pytest -q machine/test_score_decision_v6.py machine/test_reversibility_checker_v0_1.py machine/test_authority_cap_calculator_v0_2.py`: 24 passed.
- Existing v6 schema/scorer tests, reversibility checker tests, and authority cap v0.2 tests pass.

## Added operational checks

- `machine/authority_cap_calculator_v0_2.py` maps all cap axes to a common A0-A4 authority scale.
- Sample authority-cap outputs are stored in `machine/authority_cap_examples_outputs/`.
- Hidden holdout is split into public unlabeled cases and a private answer key with SHA-256 commitment.

## DOCX/PDF

- Review-ready JP whitepaper DOCX/PDF generated.
- JP one-page DOCX/PDF generated.
- EN one-page DOCX/PDF generated.
- Render QA is recorded in `qa/RENDER_QA_REVIEW_READY.md` after PNG inspection.

## Known limits

- This package does not solve ELK, scalable oversight, population ethics, or welfare measurement.
- Authority cap v0.2 is conservative and may Hold/Modify high-impact proposals where evidence is insufficient.
