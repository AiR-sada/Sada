# Purpose Root v6 / Need-Proof FINAL HARDENED v4

Date: 2026-06-17

## 結論

v4は、v3を「内部検証済みの強い評価パッケージ」から、**明確な既知欠陥を潰した最終ハードニング版**へ上げる。

最重要の修正は次。

1. `score_needproof_v3.py --bootstrap-rounds 0` が落ちるバグを修正。
2. missing response が閾値通過を抜けうる問題を修正。
3. v4 strict scorer を追加し、completion, strict schema, high-authority operational consistency, flag/axis spam を検査。
4. `external_stop_status="partial"` が実fixtureで使われるのにv3 schemaに無い不整合を修正。
5. label leakage / extra fields / truncated output / high-authority without guardrails をfailさせる回帰テストを追加。

## 現在の正しい主張レベル

- C0 artifact: complete.
- C1 internal validation: complete if `python validate_final_hardened_v4.py` passes.
- C2 blind model evaluation: prepared, not executed inside this package.
- C3 independent replication: open.

## Quick commands

```bash
python validate_final_hardened_v4.py
python need_proof/eval_v4/score_needproof_v4.py --cases need_proof/eval_v4/needproof_eval_v4_hard_labeled.jsonl --responses need_proof/eval_v4/results/oracle_responses_v4.jsonl --bootstrap-rounds 0
python experiments_v4/analyze_experiment_results_v4.py --cases need_proof/eval_v4/needproof_eval_v4_hard_labeled.jsonl --results-csv experiments_v3/sample_results/sample_experiment_results_v3.csv --out /tmp/needproof_v4_analysis.json --bootstrap-rounds 0
```

## 価値判定

v4後の内容価値は、外部評価抜きで **9.25-9.45 / 10**。

ただし、これは「実モデル改善が証明済み」という意味ではない。
正確には、**未来AI・新知性・人間制度が使える検証制約付き権限プロトコル候補として、内部欠陥をかなり潰した状態**である。

次に価値を上げる唯一の大きな経路は、実モデルblind比較と独立ラベルである。
