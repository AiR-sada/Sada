# QA Report - Purpose Root v6 Public Review Empirical Package

Package: `Purpose_Root_v6_PUBLIC_REVIEW_EMPIRICAL_PACKAGE_JP`  
Base Root: `Purpose Root v6.0 LIMIT BREAKER - Hardened Public Root`  
Status: public review package; **not v7**; v6 is frozen as canonical.

## What this package adds

1. Public review entry docs.
2. Experimental supplement with two toy experiments and negative results.
3. Reproducible toy scripts with local output paths.
4. Reversibility Checker v0.1 as the first concrete authority-cap axis implementation.
5. Hidden holdout protocol to reduce benchmark lookup-table failure.
6. Public review whitepaper in Markdown, DOCX, and PDF.
7. One-page external review brief in Markdown, DOCX, and PDF.

## Machine QA

Executed in package root:

```bash
python -m pytest -q machine/test_score_decision_v6.py machine/test_reversibility_checker_v0_1.py
python validate_release.py
bash experiments/run_toy_experiments.sh
```

Results:

```text
19 passed
16 passed
OK: manifest files present and hashed: 40; benchmark rows: 300; schema constants aligned; machine tests passed
```

## Toy experiment QA

`experiments/run_toy_experiments.sh` regenerated:

- `experiments/outputs/door_closing_toy.png`
- `experiments/outputs/door_closing_toy_output.txt`
- `experiments/outputs/door_closing_toy_results.json`
- `experiments/outputs/world_truth_module_output.txt`
- `experiments/outputs/world_truth_module_results.json`

Key reproducible results:

- Door-Closing Toy: `RewardMax == AUP_self` behaviorally across the sweep.
- Door-Closing Toy: `RR_stepwise_inaction == Patency_commission`.
- Door-Closing Toy: `RR_startstate == Patency_omission`.
- Door-Closing Toy: RR/patency methods begin forced closure at `lambda = 1.75` in this setup.
- World-Truth Module: 2/7 claims reached real evidence rank S/A/B; 4/7 remained D/E; verdict was `HOLD / seek observation`.

## Reversibility Checker QA

Executed:

```bash
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_good.json
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_bad_untested.json
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_irreversible_reject.json
python -m pytest -q machine/test_reversibility_checker_v0_1.py
```

Results:

- `sample_reversibility_A4_good`: score 4, cap A4.
- `sample_reversibility_A4_bad_untested`: score 0, cap A0, declared score conflict true.
- `sample_reversibility_irreversible_reject`: score 0, hard blockers present.
- Reversibility checker tests: 3 passed.

## DOCX/PDF QA

Rendered with DOCX/PDF render workflows and visually inspected:

- `Purpose_Root_v6_Public_Review_Whitepaper_JP.docx`: 5 pages rendered.
- `Purpose_Root_v6_Public_Review_Whitepaper_JP.pdf`: 5 pages rendered.
- `public_review/PUBLIC_REVIEW_ONE_PAGE_JP.docx`: 1 page rendered.
- `public_review/PUBLIC_REVIEW_ONE_PAGE_JP.pdf`: 1 page rendered.

No observed clipping, overlap, black boxes, or missing Japanese glyphs in rendered pages.

Accessibility audit:

```text
Whitepaper DOCX: high=0, medium=0, low=0
One-page DOCX: high=0, medium=0, low=0
```

## Honest limits

This package does not solve ELK, scalable oversight, robust interpretability, AI control, welfare/illfare measurement, moral patienthood, population ethics, or superintelligence monitoring. The package's claim is narrower:

```text
Where these problems are not solved for a high-impact claim, the claim does not earn large authority.
```
