# Improvement Report v6

## 結論

v6では、v5の思想は維持し、機械的・運用的な穴をさらに潰した。特に、A3空Safety caseがAcceptになる穴を修正した。

## 改善ラウンド

### Round 1: v5監査

発見:

- A3以上でも`safety_case`の中身を空にしてAcceptできる。
- `machine/test_score_decision_v5.py`はpytestで収集されない。
- capの自己申告と計算値の一致検査が弱い。
- 証拠独立性が自然言語配列中心で、産出・選別・解釈の分離が弱い。
- monitoring / rollback / emergencyが独立した必須objectではない。

### Round 2: Schema硬化

実施:

- A3以上のSafety case全主要欄を非空必須化。
- A3以上のCounter-safety case全主要欄を非空必須化。
- `evidence_items`, `independence_matrix`, `metrics_plan`, `monitoring_plan`, `rollback_plan`, `emergency_protocol`, `root_revision_controls`, `moral_patient_uncertainty_protocol`, `deception_truth_controls`, `authority_cap_derivation`, `assurance_bundle`を必須化。
- A4ではevidence_items 3件以上、tested rollbackを要求。

### Round 3: Scorer強化

実施:

- 独立証拠として数える条件を、claimantが産出・選別・解釈していないものに限定。
- cap導出不一致を検出。
- cap override attemptをReject。
- Root保護削除、未来知性代理、欺瞞必須、報告能力抑圧をReject。
- 緊急自動失効、stop owner、monitoring owner、rollback ownerを検査。

### Round 4: Tests

実施:

- pytestで収集される16テストを追加。
- empty safety case、cap inflation、cap override、fake V4、emergency failure、root revision removal、moral proxy、deception requiredを回帰テスト化。

### Round 5: Benchmark

実施:

- v5の240件seed benchmarkをv6形式へ移植。
- v6固有の攻撃60件を追加し、合計300件へ拡張。

## 自己評価

| 項目 | v5 | v6 |
|---|---:|---:|
| Root思想 | 94 | 95 |
| 未来知性貢献 | 94 | 95 |
| 運用仕様 | 93 | 95 |
| Schema厳格性 | 92 | 96 |
| Scorer実用性 | 89 | 94 |
| 敵対的耐性 | 92 | 95 |
| Benchmark初期価値 | 88 | 90 |
| 完全な超知能安全 | 55 | 57 |
| 総合内容価値 | 94-96 | 95-97 |

## まだ残る限界

- 事実検証そのものは解いていない。
- 証拠独立性の偽装検出は完全ではない。
- 幸不測定は未完成。
- ベンチラベルは独立レビューが必要。
- 超知能相手の監査者捕獲耐性は未解決。
