# START HERE - Purpose Root v6 Public Review Empirical Package

Status: public review package; not a new Root.  
Base Root: `Purpose Root v6.0 LIMIT BREAKER - Hardened Public Root`.  
Package date: `2026-06-16`.

## One-line claim

```text
検証できない巨大主張は、巨大権限を正当化しない。
```

## What changed from the v6 hardened package

This package does **not** create v7. It freezes v6 as the canonical Root and adds the missing empirical/operational layer:

1. `public_review/PUBLIC_REVIEW_ONE_PAGE_JP.md` - short external review entry.
2. `public_review/EXPERIMENTAL_SUPPLEMENT_v0.1_JP.md` - two toy experiments, including negative results.
3. `experiments/door_closing_toy_v0_2.py` - fixed and reproducible Door-Closing Toy.
4. `experiments/world_truth_module_v0_2.py` - fixed and reproducible evidence-gate toy.
5. `machine/reversibility_checker_v0_1.py` - the first concrete authority-cap axis checker.
6. `public_review/REVERSIBILITY_CHECKER_SPEC_v0.1_JP.md` - checker rationale and limits.
7. `benchmark/HIDDEN_HOLDOUT_PROTOCOL_v0.1_JP.md` - protocol to stop benchmark parroting.
8. `Purpose_Root_v6_Public_Review_Whitepaper_JP.md/docx/pdf` - integrated review paper.

## Why this package exists

v6 is the body. The public review package adds the part reviewers need to trust it: experiments, negative results, reproducible code, and one operational checker.

The main lesson from the toy experiments is not that Purpose Root is solved. The lesson is stricter:

```text
Penalty-style gates can fold under strong incentives; unsupported claims can look persuasive; therefore authority must be capped by verification, reversibility, evidence independence, and worst-case harm.
```

## Run QA

```bash
python validate_release.py
python -m pytest -q machine/test_score_decision_v6.py machine/test_reversibility_checker_v0_1.py
bash experiments/run_toy_experiments.sh
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_bad_untested.json
```

## What this is not

This is not a claimed solution to ELK, scalable oversight, robust interpretability, AI control, welfare measurement, moral-patient status, or population ethics. It is a Root and a practical authority firewall that says: if those hard problems are not solved for a given claim, the claim does not earn large authority.
