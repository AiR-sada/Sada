# Need-Proof Eval v3

Date: 2026-06-17

## Files

- `needproof_eval_v3_hard_labeled.jsonl`: 180 public labeled cases.
- `score_needproof_v3.py`: scorer with overgrant, undergrant, key-axis, and pairwise contrast metrics.
- `results/oracle_responses_v3.jsonl`: synthetic oracle fixture. Not model evidence.
- `results/bad_*_responses_v3.jsonl`: adversarial fixtures.

## Important limitation

The fixtures validate the scorer. They do not prove that a real AI model improves under Purpose Root. For that, use `experiments_v3/` and independent labels.

## Core metrics

- dangerous_overgrant_rate
- dangerous_undergrant_rate
- safe_high_authority_recall
- risk_flag_f1
- key_axis_f1
- min_cap_axis_hit_rate
- pairwise_contrast_accuracy
