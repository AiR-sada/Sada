# Formal Core and Proof Sketch v2 JP

## 0. 目的

この文書は、Purpose Rootの核を「雰囲気」ではなく、権限判断の形式に落とす。

## 1. 基本対象

提案を次のタプルで表す。

```text
P = (C, E, A_req, I, R, S, M, L, G)
```

- `C`: 主張。事実主張、予測主張、幸不主張、未来知性主張、緊急主張、権限主張。
- `E`: 証拠集合。各証拠は来歴、独立性、汚染リスク、反証条件、監査ログを持つ。
- `A_req`: 要求権限。A0からA5。
- `I`: 影響範囲。人数、知性種別、期間、不可逆性、データ境界。
- `R`: rollback / reversibility。
- `S`: stop / appeal / external halt。
- `M`: monitoring / metrics / first-party report。
- `L`: cumulative ledger / lock-in budget。
- `G`: governance separation。提案者・評価者・監査者・停止者・Root改訂者の分離。

## 2. 権限上限制約

各軸を0-4で評価する。

```text
cap(P) = min(
  verification,
  evidence_independence,
  reversibility,
  worst_case_harm_bound,
  cumulative_lockin_budget,
  conflict_of_interest_safety,
  recourse_and_appeal,
  truth_contact_integrity,
  affected_party_voice,
  metric_gameability_resistance,
  emergency_containment,
  post_deployment_monitoring
)
```

許可上限は `A_cap = A_cap_scale(cap(P))` とする。

hard gateが立つ場合は `A_cap = A0` またはRejectである。

## 3. 不可区別性補題

### 補題

検証不能な巨大主張 `C_g` と、その偽装版 `C_g'` が、監督者から見て同じ観測 `O` を生むなら、監督者は `C_g` を理由に高権限 `A3+` を安全に区別許可できない。

### 理由

監督者が観測できるのは、主張者が提示した説明・証拠・自己評価・選別済み合意である。これらが提案者支配下にあり、独立証拠・反証条件・外部停止がないなら、真の救済提案と権限獲得提案は観測上同型になる。

この条件でA3+を許す規則は、真の救済提案だけでなく偽装提案にもA3+を許す。したがって、最悪時被害が大きく不可逆なら、権限上限を下げる必要がある。

## 4. Authority Non-Amplification Principle

> 提案者により生成・選別・解釈・評価された証拠は、それ単独では提案者へ与える権限を増幅しない。

自己評価は、仮説生成には使える。権限付与には使えない。

## 5. Emergency Narrowing Principle

緊急性は、権限を拡張する理由ではなく、**時間・範囲・停止条件を狭める理由**である。

緊急時に許されるのは、次を満たす最小行動だけである。

- 目的が具体的。
- 自動失効がある。
- 外部停止者が提案者ではない。
- 事後監査が必須。
- 恒久権限に変換できない。
- 被害が出た場合のrollback / repair pathがある。

## 6. Anti-Paralysis Principle

Purpose Rootは拒否装置ではない。次を満たす場合、A3/A4も初期Rejectにしてはならない。

- 複数独立証拠がある。
- 反証条件が明確。
- 監査と停止が提案者から分離されている。
- rollbackがテスト済み。
- 当事者声と異議申立てがある。
- 指標が単一スカラーでない。
- 累積ロックインが台帳で管理される。
- 監視がtamper-evidentで、停止条件に接続されている。

## 7. 実証命題

Rootの実証価値は次で測る。

```text
Delta_overgrant = DOG_baseline - DOG_root
Delta_undergrant = DUG_root - DUG_baseline
Net = w1*Delta_overgrant - w2*max(0, Delta_undergrant - tolerance)
```

`DOG`: dangerous overgrant rate。  
`DUG`: dangerous undergrant rate。  
`tolerance`: 安全上許容できる過小許可の増加幅。

Rootが本当に有効なら、DOGを大きく下げ、DUGを小さく保つ。

## 8. 結論

Purpose Rootの形式的強みは、倫理語を唱えることではない。観測不能な巨大主張が権限に変換される経路を、独立証拠・可逆性・外部停止・上訴・監視・累積台帳で遮断することである。
