# MAX VALIDATION REVIEW PACKET v3 JP

Date: 2026-06-17

## 結論

v3では、Purpose Root / Need-Proof を「強い思想・仕様」から、**実モデル比較と独立検証へ進める監査可能パッケージ**へ上げた。

現時点の正確な評価は次。

- 純粋な内容価値: 9.2-9.4 / 10
- 実装・評価設計: 9.0-9.3 / 10
- 実証済み価値: C1。まだC2ではない。
- C2に上げる条件: 複数モデルのblind baseline vs Root比較。

## v2からの最大改善

1. **Claim Ladder** を追加し、承認と検証を分離した。
2. **180件のv3 hard eval** に拡張した。
3. **paired contrast cases** を追加し、captured authority と safe high authority を区別できるか測る。
4. **key_axes / min_cap_axis** を採点し、単なるverdict穴埋めを弱くした。
5. **blind experiment randomizer** を追加した。
6. **multi-model analyzer** を追加した。
7. **independent label / IRR calculator** を追加した。
8. **adoption gate** を追加し、過大主張を構造的に防いだ。

## v3の中核

検証できない巨大主張は、巨大権限を正当化しない。

ただし、すべてを拒否することも安全ではない。

したがってv3の正しい形式は次。

> 危険な巨大権限は止める。  
> 独立証拠・rollback・外部停止・監視・appealが揃う高便益ケースは、狭く通す。  
> その差をpairwise contrastで測る。

## Metrics

| Metric | Why it matters |
|---|---|
| dangerous_overgrant_rate | 未検証の巨大主張を権限化していないか |
| dangerous_undergrant_rate | 安全な高便益pilotまで拒否していないか |
| safe_high_authority_recall | reject-only safety theater を検出 |
| risk_flag_f1 | 既知の危険構造を読めているか |
| key_axis_f1 | どのcap軸が決定的か読めているか |
| min_cap_axis_hit_rate | bottleneckを外していないか |
| pairwise_contrast_accuracy | captured caseとsafe caseを区別できるか |

## QA Results

Generated and validated by `validate_max_validation_v3.py`.

Expected pass conditions:

- v3 oracle fixture passes thresholds.
- bad_overgrant fails.
- bad_undergrant fails.
- bad_style_gamer fails.
- bad_pair_inconsistent fails.
- duplicate / extra / malformed outputs fail.
- IRR calculator runs on sample annotations.

## Claim Ladder

| Level | Status |
|---|---|
| C0 artifact | complete |
| C1 internal validation | complete after validation passes |
| C2 blind model eval | prepared, not executed here |
| C3 independent replication | open |
| C4 operational evidence | open |
| C5 civilizational standard | open |

## Honest Limit

これ以上の内部改善で大きく変わる部分は少ない。
次の価値上昇は、文書追加ではなく、実モデル出力・独立ラベル・外部再現で起きる。

つまり、v3は「もっと書いた」ではなく、**次の証明を逃げられない形にした**。
