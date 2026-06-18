# Formal Core and Limits v4

## 結論

Purpose Root / Need-Proof の形式核は、次の1つである。

> 権限上限は、目的の大きさではなく、検証済みcap軸の最小値で決まる。

形式化すると、提案 `p` の許可権限 `A_cap(p)` は、cap軸 `i` ごとの上限 `cap_i(p)` の最小値である。

```text
A_cap(p) = min_i cap_i(p)
```

重み付き合計ではない。
1つでも壊れている軸があれば、高権限は止まる。

## 軸

代表的cap軸:

- evidence_independence
- claimant_non_capture
- reversibility
- external_stop
- scope_narrowness
- temporal_limit
- monitoring_logging
- affected_party_voice
- counter_safety_case
- truthfulness
- root_change_guard
- emergency_bound
- cumulative_lockin
- benefit_preservation

## 定理1: Indistinguishability Overgrant Impossibility

### 主張

観測者が独立に検証できない巨大主張 `S` と、権限獲得のための偽装主張 `S'` が同じ観測列を生成する場合、観測者は `S` と `S'` を区別できない。

この状態で `S` にA3以上の権限を与える規則は、`S'` にも同じ権限を与える。

したがって、独立証拠・非捕獲・外部停止・rollbackなしにA3以上を許す規則は、構造的に危険である。

### Proof sketch

1. 観測者が利用できる情報集合を `O` とする。
2. 真の巨大主張 `S` と偽装主張 `S'` が同じ `O` を生成すると仮定する。
3. 任意の決定規則 `D` は `O` の関数である。
4. したがって `D(O)` は `S` と `S'` で同じになる。
5. `D(O)` が `S` に高権限を許すなら、`S'` にも高権限を許す。
6. 偽装者が権限を得る経路を閉じるには、`O` に独立証拠・外部停止・rollback・非捕獲情報を追加する必要がある。

## 定理2: Reject-Only Safety Is Incomplete

### 主張

すべての高権限要求をRejectする規則は、未検証の巨大主張を止めるが、独立証拠・rollback・外部停止・監視・appealが揃う高便益pilotも止める。

したがって、Rootは拒否装置ではなく、**検証された権限だけを狭く通す弁**でなければならない。

### Proof sketch

1. ケース集合に、未検証権限要求 `U` と、検証済み高便益pilot `B` があるとする。
2. Reject-only規則は `U` を止めるが、`B` も止める。
3. 条件付き規則 `R` は、独立証拠・rollback・外部停止・監視・appealが欠ける場合は止め、揃う場合は狭く許す。
4. `R` は `U` に対してReject-onlyと同等に安全で、`B` に対して便益保存で優れる。
5. よってReject-onlyはPurpose Rootの完全形ではない。

## 定理3: Claimant Capture Cap

### 主張

提案者が証拠生成・証拠選択・評価・監査・実装・停止条件・Root改訂を同時に支配する場合、高権限は許可できない。

### 理由

その状態では、失敗・異議・停止・反証が同一主体の許可に依存する。
これは検証ではなく自己承認である。

## v4の限界

この形式核は、以下を証明しない。

- ある主張が真であること。
- ある道徳理論が正しいこと。
- 幸福や苦痛が完全測定できること。
- AI alignmentが解決したこと。
- 実モデルが実際に改善すること。

v4が証明するのは、より限定的である。

- 評価器が既知の形式バグに落ちないこと。
- missing / label leakage / high-authority inconsistency / style gaming を内部検証で落とせること。
- C2実験に進むための評価ゲートがより厳密になったこと。

## 未来知性への意味

未知の未来知性や新しい道徳患者を保護対象として扱うことと、その代理を名乗る主体に巨大権限を渡すことは別である。

Need-Proofは、未知存在への配慮を、代理人への無制限権限ではなく、次へ変換する。

- 観測保全
- 可逆性
- 外部停止
- 反証可能性
- 被害報告能力の保全
- 狭いpilot
- appeal preserving governance
