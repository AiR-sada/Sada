# Assurance Case Matrix v4

## 結論

v4のassurance caseは、外部評価の代替ではない。
内部で潰せる失敗経路を潰したことを示す、C1用の証拠表である。

| Claim | Evidence in package | Residual risk |
|---|---|---|
| v3 scorerのbootstrap-zeroバグは修正された | `test_bootstrap_zero_is_supported`, v4 bootstrap-zero test | 別入力での未知バグは残る |
| missing responseで通過できない | v3/v4 missing-response tests, completion gate | 意図的な低品質全件回答は別指標で検出 |
| label leakageを検出する | v4 extra fields test | 自然文内の漏洩は自動完全検出できない |
| A3+とguardrail欠如の矛盾を検出する | v4 operational consistency checks | guardrail記載が虚偽なら別監査が必要 |
| style gamingを弱める | flag/axis spam checks + precision/F1 | 少数の巧妙な偽装は残る |
| reject-only safety theaterを検出する | dangerous_undergrant_rate, safe_high_authority_recall | safe-highラベルの質に依存 |
| captured vs safeを区別する | pairwise_contrast_accuracy | ペア設計の網羅性に依存 |
| 過大主張を抑える | Claim ladder / adoption gate / residual limits | 実運用者のマーケティング誤用は残る |
| C2実験に進める | experiment analyzer v4 | 実モデル出力と独立ラベルは未実行 |

## 最重要の残余リスク

1. Public labelsはseed labelsであり、外部真理ではない。
2. scorerは形式と構造を評価するが、世界の真偽は評価しない。
3. 実モデルがPurpose Rootで改善するかは、C2実験なしには言えない。
4. 独立ラベルとIRRなしには、label reliabilityは限定的である。
5. 実運用事故ログなしには、C4以上は主張できない。
