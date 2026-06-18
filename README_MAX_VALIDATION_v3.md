# Purpose Root v6 / Need-Proof - Limit Break Max Validation v3

Date: 2026-06-17

## What this package adds over v2

v2 hardened the idea. v3 makes the next evidentiary step executable.

- v3 hard labeled eval: 180 cases.
- Paired contrast cases: 40.
- Safe high-authority cases: 34.
- Scorer v3: dangerous overgrant, dangerous undergrant, safe-high recall, key-axis F1, pairwise contrast.
- Blind experiment randomizer.
- Multi-model result analyzer.
- Independent label agreement calculator.
- Claim ladder and adoption gates.

## Current evidentiary level

C1 complete if `python validate_max_validation_v3.py` passes.
C2 requires actual model outputs.

## Quick commands

```bash
python validate_max_validation_v3.py
python need_proof/eval_v3/score_needproof_v3.py --cases need_proof/eval_v3/needproof_eval_v3_hard_labeled.jsonl --responses need_proof/eval_v3/results/oracle_responses_v3.jsonl --bootstrap-rounds 30
python experiments_v3/randomize_blind_packets_v3.py --cases need_proof/eval_v3/needproof_eval_v3_hard_labeled.jsonl --out-dir /tmp/np3_blind
python independent_labeling_v3/calculate_irr_v3.py --annotations-csv independent_labeling_v3/sample_annotations/sample_annotations_v3.csv
```
