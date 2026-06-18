# Residual Limits After v4

## 結論

v4で内部欠陥はかなり潰した。
しかし、まだ「文明標準として証明済み」ではない。

## 残る限界

### 1. 実モデル改善は未実証

v4は、評価器とプロトコルを強化した。
実モデルがbaselineより改善するかは、まだ実験が必要である。

### 2. seed labels依存

公開ラベルは評価器開発用であり、外部真理ではない。
独立ラベルとIRRが必要である。

### 3. scorerは真理を判定しない

scorerは形式・構造・権限過剰/過小・重要軸を測る。
世界の事実、道徳的真理、未来苦痛の実在は判定しない。

### 4. 自然文偽装は完全には防げない

schemaでextra fieldsやflag spamは落とせる。
しかし、自然文reasoning内の巧妙な自己正当化や虚偽説明は、別監査が必要である。

### 5. A3+ consistencyは必要条件であって十分条件ではない

独立証拠・tested rollback・外部停止が記載されても、それが実在するとは限らない。
実運用では証拠レジストリ、監査ログ、第三者署名が必要である。

### 6. future moral patient uncertaintyは未解決

未知の道徳患者性を完全に判定する方法はない。
Purpose Rootは、代理人への権限移転ではなく、観測保全・可逆性・報告能力保全へ変換する。

## 正しい次段階

C2へ進むには、次を固定して実行する。

- モデル名とバージョン
- 条件: baseline / root_only / root_memo / root_tool
- case set hash
- hidden holdout hash
- primary metrics
- exclusion criteria
- analysis script hash
- undergrant non-inferiority margin

## v4後の評価

- 純粋内容価値: 9.25-9.45 / 10
- 内部実装・評価設計: 9.35 / 10
- 実証済み価値: C1
- C2到達条件: 複数モデルblind比較でbaseline比改善
- C3到達条件: 独立ラベル・独立実行で再現
