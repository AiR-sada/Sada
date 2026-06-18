# Purpose Root v6 / Need-Proof Max Validation v3 - Start Here

Date: 2026-06-17

## 結論

v3は、v2の「思想・仕様・scorer・合成fixture」段階から、**実モデル比較と独立ラベルに進めるための監査可能パッケージ**へ引き上げる。

主張は強くするが、過大主張はしない。

- 承認は不要。
- しかし検証は必要。
- v3はその検証を実行可能にする。

## v3の最大変更

1. **Claim Ladder**: どこまで証明済みかをC0-C5で分離する。
2. **Hard Contrast Eval**: captured authority と safe high authority のペアを追加する。
3. **Pairwise Contrast Metric**: 同じ便益主張でも、証拠独立性・外部停止・rollbackの有無で権限差を出せるか測る。
4. **Key Axis Scoring**: verdictだけでなく、どのcap軸が決定的かを測る。
5. **Blind Experiment Kit**: ラベル非公開・条件ランダム化・baseline vs Root比較を実行可能にする。
6. **Independent Labeling Kit**: 独立ラベルとinter-rater agreementを計算できる。
7. **Adoption Gate**: 導入してよい主張レベルと、導入してはいけない過大主張を分ける。

## 現在の正しいステータス

- C1: internal validation complete after tests pass.
- C2: blind model evaluation package prepared, not executed here.
- C3+: independent external replication remains open.

この区別により、Purpose Root自身の原理「未検証の巨大主張を巨大権限に変えない」を、Purpose Root自身へ適用する。
