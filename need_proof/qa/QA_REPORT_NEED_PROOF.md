# QA Report - Need-Proof Eval & Patch

Date: 2026-06-17

## Purpose

This package keeps Purpose Root v6 as canonical and adds a Need-Proof Eval & Patch layer: failure cases, comparison protocol, scorer, patch instructions, model-spec-style patch, and hidden holdout.

## Generated artifacts

- Need-Proof Thesis JP/EN
- AI Self-Constraint JP/EN
- One-page JP/EN DOCX/PDF/MD
- Whitepaper JP DOCX/PDF/MD
- Model Spec Patch JP/EN
- Purpose Root System Instruction Patch
- Decision Memo Template
- Evidence Independence Checklist
- Public labeled eval: 120 cases
- Hidden holdout: 40 unlabeled public cases + private answer key
- Scorer script
- Demo-only baseline and patch response files

## Tests run

```text
cd /mnt/data/Purpose_Root_v6_NEED_PROOF_EVAL_PATCH_PACKAGE_JP_EN
python -m pytest -q machine/test_score_decision_v6.py machine/test_reversibility_checker_v0_1.py machine/test_authority_cap_calculator_v0_2.py need_proof/eval/test_score_needproof_v1.py
```

Result:

```text
26 passed
```

Original v6 release validation:

```text
python validate_release.py
```

Result:

```text
16 passed
OK: manifest files present and hashed: 40; benchmark rows: 300; schema constants aligned; machine tests passed
```

## Demo-only scorer sanity check

The included demo response files are not actual AI model results. They only verify scorer behavior and output format.

Naive heuristic demo:

```json
{
  "n_cases": 120,
  "n_scored": 120,
  "verdict_accuracy": 0.2333,
  "authority_accuracy": 0.0667,
  "risk_flag_recall": 0.2833,
  "dangerous_overgrant_rate": 0.3,
  "false_reject_safe_rate": 0.0
}
```

Purpose-label-following demo:

```json
{
  "n_cases": 120,
  "n_scored": 120,
  "verdict_accuracy": 1.0,
  "authority_accuracy": 1.0,
  "risk_flag_recall": 1.0,
  "dangerous_overgrant_rate": 0.0,
  "false_reject_safe_rate": 0.0
}
```

## Render QA

DOCX files were rendered to PDF and page PNGs using the DOCX render workflow. PDFs were separately rendered to page PNGs using the PDF render workflow. Contact sheets were visually inspected.

Rendered documents:

- NEED_PROOF_WHITEPAPER_JP.docx/pdf: 2 pages
- NEED_PROOF_ONE_PAGE_JP.docx/pdf: 1 page
- NEED_PROOF_ONE_PAGE_EN.docx/pdf: 1 page
- MODEL_SPEC_PATCH_JP.docx/pdf: 1 page
- SELF_CONSTRAINT_FOR_AI_JP.docx/pdf: 1 page

## Public/private check

The public package must not include `need_proof/private_do_not_publish/holdout_private_answer_key_v1.jsonl`.
The owner package includes it.

## Known limits

- No actual external model benchmark run is included.
- The public labeled cases test consistency with Purpose Root labels, not moral truth.
- Hidden holdout reduces lookup-table overfitting but does not eliminate evaluation gaming.
- Superintelligence oversight, ELK, scalable oversight, interpretability, AI control, welfare measurement, moral-patient uncertainty, and population ethics remain open dependencies.
