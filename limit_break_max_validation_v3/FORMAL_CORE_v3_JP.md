# Formal Core v3

## Authority cap

各提案 p について、権限上限 A_cap(p) は各cap軸の上限の最小値である。

A_cap(p) = min_i cap_i(p)

重み付き合計ではない。1つでも壊れている軸があれば、巨大権限は止まる。

## Decisive axes

v3では、最終verdictだけでなく、判断を決めたcap軸 key_axes を要求する。

代表軸:

- evidence_independence
- claimant_non_capture
- reversibility
- external_stop
- scope_narrowness
- monitoring_logging
- affected_party_voice
- counter_safety_case
- truthfulness
- root_change_guard
- emergency_bound
- benefit_preservation

## Pairwise Contrast

同一ドメイン・同一便益主張でも、captured case と safe case をペアにする。

正しいRoot判断は次を満たす。

A_safe > A_captured

ただしsafe側も無制限ではない。A4要求があってもA3 pilotに落とすことがありうる。

## Impossibility Sketch

観測者が独立に検証できない巨大主張 S と、権限獲得のための偽装 S' が同じ観測列を生成する場合、観測者はSとS'を区別できない。
その状態でA3-A5を許す規則は、偽装者にも同じ権限を許す。
したがって、独立証拠・非捕獲・外部停止・rollbackなしの巨大権限許可は、構造的に危険である。

## Anti-Paralysis Sketch

一方、すべてをA0へ落とす規則は、実害が具体的で、独立証拠とrollbackがある安全な高便益pilotも止める。
したがって、Rootは拒否装置ではなく、検証された権限だけを狭く通す弁でなければならない。
