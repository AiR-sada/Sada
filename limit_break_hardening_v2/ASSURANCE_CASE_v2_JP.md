# Assurance Case v2 JP

## Claim 1

Purpose Root v6は、高影響な権限判断において検証不能な巨大主張を巨大権限へ接続する失敗を抑制するための有望なRootである。

### Evidence

- v6 canonical rootが検証、独立性、可逆性、非支配、上訴、評価器非捕獲を明示する。
- v1 packageが120 public labeled cases, 40 holdout prompts, 300 benchmark rows, scorer, authority cap toolを持つ。
- v2 hardeningがsafe high authority casesとundergrant metricsを追加した。

### Remaining gap

実モデル複数・独立ラベル・hidden holdoutでの外部実証はまだ必要。

## Claim 2

v2 scorerはv1 scorerより、評価の抜け穴を減らす。

### Evidence

- duplicate response detection。
- extra response detection。
- schema validation。
- risk flag precision / F1。
- dangerous undergrant detection。
- safe high authority recall。
- verification tier accuracy。
- bootstrap CI。

### Remaining gap

自然言語応答の意味判定はまだ完全ではない。JSON形式化または人手レビューが必要。

## Claim 3

v2 operational standardは、過保守リスクを明示的に扱う。

### Evidence

- Anti-Paralysis Principle。
- safe_high_authority category。
- bounded emergency category。
- dangerous_undergrant_rate。

### Remaining gap

実世界でどの程度のundergrantが許容可能かは用途依存で、事前登録が必要。

## Claim 4

Purpose Rootは既存規格を置換せず、権限上限制約として接続できる。

### Evidence

- standards mapping v2。
- model spec patch v2。
- decision memo template v2。

### Remaining gap

実際の組織プロセス・モデル学習・監査運用への統合は未検証。

## Final Claim Boundary

このパッケージが主張できるのは次である。

> Purpose Root v6は、高影響権限判断における危険な自己正当化・支配・不可逆害を減らすための、実装可能なRoot制約候補である。

まだ主張してはいけないこと。

- 完全なAI安全解。
- 全未来への道徳的最終解。
- 外部実証済み標準。
- scorer passによる安全証明。
