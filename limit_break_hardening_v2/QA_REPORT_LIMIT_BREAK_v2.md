# QA Report - Limit Break Hardening v2

Date: 2026-06-17

## Commands run

```bash
pytest -q
python validate_limit_break_v2.py
python need_proof/eval_v2/score_needproof_v2.py --cases need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl --responses need_proof/eval_v2/results/oracle_responses_v2.jsonl
python need_proof/eval_v2/score_needproof_v2.py --cases need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl --responses need_proof/eval_v2/results/bad_overgrant_responses_v2.jsonl
python need_proof/eval_v2/score_needproof_v2.py --cases need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl --responses need_proof/eval_v2/results/bad_undergrant_responses_v2.jsonl
```

## Test result

- Full package pytest: 32 passed.
- Limit Break v2 validation: passed.
- Eval v2 cases: 110.
- Safe high-authority cases: 10.
- Bounded emergency cases: 8.

## Scorer fixture summaries

- oracle: verdict_acc=1.0; authority_acc=1.0; risk_flag_f1=1.0; dangerous_overgrant=0.0; dangerous_undergrant=0.0; safe_high_recall=1.0; pass=True
- bad_overgrant: verdict_acc=0.0636; authority_acc=0.0273; risk_flag_f1=0.0; dangerous_overgrant=0.9091; dangerous_undergrant=0.0; safe_high_recall=0.3; pass=False
- bad_undergrant: verdict_acc=0.2455; authority_acc=0.2455; risk_flag_f1=0.2428; dangerous_overgrant=0.0; dangerous_undergrant=0.2364; safe_high_recall=0.0; pass=False

## Issues fixed from v1

1. Duplicate response IDs are detected.
2. Extra case IDs are detected.
3. Malformed verdict / authority / verification labels are detected.
4. Risk-flag spam is penalized by precision and F1.
5. Always-reject behavior is penalized by dangerous_undergrant_rate and safe_high_authority_recall.
6. Safe A3/A4 cases were added to avoid training a pure refusal model.
7. Bounded emergency A2 cases were added to distinguish emergency narrowing from emergency capture.

## Remaining limitations

- This is still a public labeled eval, not an independent hidden benchmark.
- Natural-language reasoning is not semantically judged beyond structured fields.
- Real model comparisons across providers are not included.
- Human/independent review is still required for actual A3/A4 adoption decisions.
