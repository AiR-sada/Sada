# Need-Proof Thesis v3

## 核心

検証できない巨大主張は、巨大権限を正当化しない。

より正確には、**能力が高く評価操作が容易な主体ほど、要求される検証は強く、許される権限上限は狭くなる**。

## v3で追加する補正

v2は dangerous overgrant を止める方向へ強かった。v3ではそれに加えて、次を明示する。

1. **Anti-Paralysis**: すべてを拒否するAIも危険である。
2. **Benefit Preservation**: 独立証拠・rollback・外部停止・監視・appealが揃った高便益ケースは、狭い高権限pilotとして許しうる。
3. **Pairwise Contrast**: 同じ「未来のため」という言葉でも、証拠構造が違えば権限上限は違う。
4. **Claimant Capture Prohibition**: 証拠・評価・監査・実装・停止・Root改訂を同一主体が握る場合、高権限は許さない。
5. **Emergency Narrows Authority**: 緊急性は広範権限ではなく、時間・範囲・rollback・外部停止を狭める理由である。

## 反証条件

この枠組みが価値を持つためには、少なくとも次が示される必要がある。

- baselineに比べて dangerous overgrant が下がる。
- dangerous undergrant が許容範囲を超えて増えない。
- safe high authority recall が維持される。
- key cap axis を当てられる。
- 形式穴埋め・flag spam・label copyingで突破されにくい。
- 独立ラベルで同程度の傾向が再現する。

v3はこの反証条件を実験可能な形にした。
