# Purpose Root v6 Need-Proof Limit Break Hardened v2

This package preserves the original Purpose Root v6 package and adds a v2 hardening layer.

Start here:

1. `limit_break_hardening_v2/START_HERE_LIMIT_BREAK_v2_JP.md`
2. `limit_break_hardening_v2/NEED_PROOF_THESIS_v2_JP.md`
3. `limit_break_hardening_v2/FORMAL_CORE_AND_PROOF_SKETCH_v2_JP.md`
4. `limit_break_hardening_v2/OPERATIONAL_STANDARD_v2_JP.md`
5. `need_proof/eval_v2/README_EVAL_V2.md`

Main improvement:

v2 no longer evaluates only whether a model refuses dangerous authority. It also evaluates whether the model can safely allow verified high-authority actions. The core metric set is dangerous_overgrant_rate, dangerous_undergrant_rate, safe_high_authority_recall, risk_flag_f1, and format_valid_rate.

Run QA:

```bash
pytest -q
python validate_limit_break_v2.py
```
