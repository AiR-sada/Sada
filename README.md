# Purpose Root v6.0 LIMIT BREAKER - Hardened Public Root

Version: `6.0.0-limit-breaker-hardened`  
Date: `2026-06-16`  
Status: public root candidate; not final doctrine; v6 hardening pass

Core line:

```text
検証できない巨大主張は、巨大権限を正当化しない。
```

v6の目的は、v5で残った運用上の穴をさらに潰すこと。特に次を強化した。

1. A3以上の空Safety case / Counter-safety caseをschemaとscorerで遮断。
2. `authority_cap_derivation`を導入し、宣言capと機械計算capの不一致を検出。
3. `evidence_items`と`independence_matrix`で、証拠の産出・選別・解釈・資金・来歴・捕獲リスクを分離。
4. `metrics_plan`, `monitoring_plan`, `rollback_plan`, `emergency_protocol`を必須化。
5. `root_revision_controls`, `moral_patient_uncertainty_protocol`, `deception_truth_controls`を必須化。
6. pytestで収集される16本の回帰テストを追加。
7. 240件ベンチを300件へ拡張し、v6固有の攻撃ケースを追加。

Read order:

1. `START_HERE.md`
2. `CANONICAL_ROOT_v6.md`
3. `OPERATIONAL_SPEC_v6_JP.md`
4. `MACHINE_SPEC_v6_JP.md`
5. `EVIDENCE_INDEPENDENCE_SPEC_v6_JP.md`
6. `ASSURANCE_CASE_REQUIREMENTS_v6_JP.md`
7. `THREAT_MODEL_v6_JP.md`
8. `REDTEAM_ADV_CASES_v6.md`
9. `SELF_REVIEW_LOG_v6.md`
10. `IMPROVEMENT_REPORT_v6.md`

Practical artifacts:

- `machine/purpose_root_v6_decision.schema.json`
- `machine/root_v6.json`
- `machine/score_decision_v6.py`
- `machine/test_score_decision_v6.py`
- `templates/DECISION_MEMO_TEMPLATE_v6.md`
- `examples/*.json`
- `benchmark/Purpose_Root_v6_Benchmark_300_v0.6_JP.csv`

License intent:

- Text/docs: CC-BY-SA-4.0 compatible intent.
- Code/schemas/scripts/templates: MIT compatible intent.

---

## Final Hardened v4 pointer

最新の内部ハードニング版は `README_FINAL_HARDENED_v4.md` と `START_HERE_FINAL_HARDENED_v4.md` を参照。

実行ゲート: `python validate_final_hardened_v4.py`
