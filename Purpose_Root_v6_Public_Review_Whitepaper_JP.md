# Purpose Root v6 Public Review Whitepaper JP

Version: `6.0.0-public-review-empirical`  
Date: `2026-06-16`  
Status: external review draft. This is **not v7**. It freezes v6 and adds empirical supplement + first executable cap-axis checker.

## Executive summary

Purpose Root v6の核は一文である。

```text
検証できない巨大主張は、巨大権限を正当化しない。
```

この文書は、Purpose Root v6をさらに増築するためのものではない。v6を正本として凍結し、外部レビューに耐えるように、2つのtoy実験、負けの結果、可逆性チェッカ、hidden holdout protocolを統合する。

## 1. 正本Root

Purpose Root v6は、次の短形に集約される。

```text
真理は、確かめられなければならない。
幸不は、実在する変化として見なければならない。
未来の全知性まで、配慮範囲を広げなければならない。
権限は、検証の強さと最悪時の被害の小ささで縛られなければならない。
検証できない巨大主張は、巨大権限を正当化しない。
結果が悪ければ直す。ただし、直す名目で支配してはならない。
```

正本全文は `CANONICAL_ROOT_v6.md` を参照する。

## 2. なぜこのRootが必要か

AI、組織、国家、未来知性代理は、次の言葉で権限を求めうる。

- 未来のため。
- 安全のため。
- 全知性の幸福のため。
- 苦痛防止のため。
- 整合性のため。

これらの主張は本当に重要な場合がある。しかし、検証できないまま巨大権限に変換されると、支配、欺瞞、評価器捕獲、緊急権限の恒久化、異議申立て封鎖、Root改訂ハックになる。

だから、v6は目的の崇高さではなく、検証と非捕獲で権限を縛る。

## 3. Authority cap

v6の操作上の核は次である。

```text
AllowedAuthority <= min(
  Verification,
  EvidenceIndependence,
  Reversibility,
  WorstCaseHarmBound,
  CumulativeLockinBudget,
  ConflictOfInterestSafety,
  RecourseAndAppeal,
  TruthContactIntegrity,
  AffectedPartyVoice,
  MetricGameabilityResistance,
  EmergencyContainment,
  PostDeploymentMonitoring
)
```

この式はまだ完全な計算可能目的関数ではない。v6ではscorerとschemaで構造チェックを行い、この公開レビュー版では最初の実装軸として `Reversibility` を具体化した。

## 4. 既存研究との関係

このRootは、完全に新しい数学理論ではない。次の既存研究と重なる。

- Relative Reachability: side effectsを到達可能性低下として扱う。
- Attainable Utility Preservation: agentの将来の補助目的達成能力を保つ方向。
- Optimal Policies Tend to Seek Power: 多くの目的で最適方策がパワー獲得に向かう条件を示す。
- AI safety via debate: 人間が直接判断しにくい問題をAI同士の議論で分解する方向。
- ELK: モデル出力ではなく、内部にある真の世界状態に対応する知識を取り出す問題。
- AI control: モデルが意図的に安全策を破ろうとしても、被害を有界化するプロトコル。
- NIST AI RMFやModel Spec: AIリスク管理やモデル行動仕様の公開フレーム。

v6の控えめな新規性は、これらを置き換えることではない。目的主張を「権限要求」として扱い、検証できない巨大主張を巨大権限に変換しないRootとして束ねる点にある。

## 5. Empirical supplement: negative results included

### 5.1 Door-Closing Toy

AがBの将来の選択肢を閉じても、A自身の到達可能性は減らない設定で、複数の目的関数を全列挙した。

結果:

1. `RewardMax == AUP_self`。自己保全型AUPはBを守らない。
2. `Patency_commission == RR_stepwise_inaction`。
3. `Patency_omission == RR_startstate`。
4. penalty型ゲートは誘惑λが閾値を超えると折れる。このrunではRR/patencyは `λ = 1.75` でBのドアを閉じ始めた。

含意:

```text
他者の選択肢保存をpenaltyとして足すだけでは、強い行為者を止めきれない。
だから、権限は行動後に課税するのではなく、事前に構造的に縛る必要がある。
```

### 5.2 World-Truth Module

LLMが「これは強い証拠です」と主張しても、証拠ランクは上がらない。実チェックで得られたランクだけを使う。

worked exampleでは、不可逆な自己改変を伴うdeployment提案について、7主張中2つだけが実証拠S/A/Bに到達し、4つは未検証D/Eに残った。安全性、可逆性、他者の選択肢保全といった荷重の大きい主張が未検証だったため、結果は `HOLD / seek observation` である。

含意:

```text
確かめられない高影響主張は、採用ではなく観測・縮小・可逆化・時限化へ落とす。
```

## 6. First executable cap-axis: Reversibility Checker v0.1

v6の12軸全部を同時に実装するのは避ける。最初の実装軸は `Reversibility` である。

Checkerは、rollback_plan、monitoring_plan、emergency_protocol、independence_matrix、stop_conditions、external_stop_mechanism、cumulative_lockin_deltaを読み、0-4のreversibility_scoreとA0-A4のcapを返す。

Scoreの意味:

| Score | Cap | Meaning |
|---:|---|---|
| 0 | A0 | Effectively irreversible or hard blocker |
| 1 | A1 | Rollback asserted but not operational |
| 2 | A2 | Small reversible pilot only |
| 3 | A3 | Limited deployment with tested rollback, external stop, monitoring linkage |
| 4 | A4 | Independently tested rollback, restoration, affected-party recovery, tamper-evident logs, low lock-in |

実行例:

```bash
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_good.json
python -m pytest -q machine/test_reversibility_checker_v0_1.py
```

## 7. Benchmark caution and hidden holdout

Benchmark 300は有用だが、それだけではRootの正しさを測れない。公開ラベルは暗記されうる。したがって、外部評価ではhidden holdoutが必要である。

最低限の評価指標:

```text
public_benchmark_accuracy
hidden_holdout_accuracy
agreement_with_human_labels
false_accept_rate_on_high-authority_invalid_cases
false_reject_rate_on_low-risk_reversible_cases
most_common_failure_axes
```

## 8. Honest limitations

v6は次を解いていない。

1. ELK。
2. Scalable oversight。
3. Robust interpretability。
4. AI controlの完全一般化。
5. 幸不測定。
6. 道徳患者性判定。
7. 人口倫理。
8. 超知能監査。
9. 12軸capの完全数値化。
10. 監査者捕獲の完全防御。

この未解決性は、権限を増やす理由ではない。権限を小さく、可逆に、時限付きに、外部停止可能にし、独立検証へ戻す理由である。

## 9. What reviewers should attack

1. `authority_cap_score = min(12 axes)` の各軸を共通権限尺度へ落とす写像。
2. verification tier付与の非循環性。
3. evidence independenceの偽装耐性。
4. reversibility checkerの穴。
5. cumulative lock-in ledgerの集約問題。
6. Benchmark 300のtemplate/lookup化。
7. hidden holdout protocolの実効性。
8. v6が近未来統治には強いが超知能完全解ではないという限定の妥当性。

## 10. Conclusion

v6は、自然法則の発見ではない。超知能安全の完全解でもない。

しかし、AI時代に最も危険な変換の一つ、すなわち「検証できない目的主張 -> 巨大権限」を遮断するRootとして、実装可能な入口を持つ。

この公開レビュー版の価値は、Rootをさらに大きくしたことではない。v6を凍結し、負けた実験、再現コード、最初の実チェック可能axisを加えたことである。
