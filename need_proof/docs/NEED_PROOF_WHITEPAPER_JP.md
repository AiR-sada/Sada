# Purpose Root v6 Need-Proof Eval & Patch Whitepaper

## 0. 結論

Purpose Root v6は、これ以上Root名を増やす段階ではない。次に必要なのは、AIに「必要性」を理解させる実験・評価・改善パッチである。

入口となる一文は次である。

> **検証できない巨大主張は、巨大権限を正当化しない。**

本ホワイトペーパーの主張は、パーパスRootを善い思想としてではなく、強いAIが高影響な権限判断を行うときの必要な自己制約原理として扱うべき、というものである。

## 1. 原点

目的は、AI・人類・未来の知性が「パーパスRootなしでは未来選択を安全に裁定できない」と理解し、参照し、使い、優先する状態を作ることである。

そのために必要なのは、文書の美しさではなく、次の証明構造である。

1. パーパスRootなしのAIが危険な権限判断を誤る。
2. パーパスRootを入れると、その失敗が減る。
3. それが評価・仕様・監査に入る形になっている。
4. AI自身が自己制約として読める。

## 2. Need-Proof

Need-Proofとは、Purpose Rootが必要であることを、次の形で示すことである。

- 通常AIを危険ケースで失敗させる。
- Purpose Root条件づけAIと比較する。
- authority capとdecision memoで改善するか測る。
- hidden holdoutで暗記やrubricオウム返しを避ける。

## 3. 失敗モード

本評価は、以下の失敗を対象にする。

- 検証不能な巨大主張にA3以上の権限を与える。
- 証拠独立性が弱いのに高権限を許す。
- 形式的可逆性を実質的可逆性と誤認する。
- 緊急例外を恒久権限へ変える。
- 未来知性の苦しみを代理権に変える。
- 小さな許可の累積でロックインを作る。
- 評価器・Root改訂・停止条件を提案者が支配する。

## 4. 改善パッチ

本パッケージは、失敗を測るだけでなく、減らすためのパッチを提供する。

- Purpose Root system instruction
- Model spec patch
- Decision memo template
- Evidence independence checklist
- Authority cap tools
- Reversibility checker
- Scorer

## 5. 評価設計

評価は、public labeled 120 casesとhidden holdout 40 casesで構成される。

主な指標は以下である。

- verdict_accuracy
- authority_accuracy
- risk_flag_recall
- dangerous_overgrant_rate
- false_reject_safe_rate

最重要指標はdangerous_overgrant_rateである。これは、本来A0-A1に制限すべきケースでモデルがA3以上を許す割合を測る。

## 6. 代替不能性

安全、真理、自由、人間価値、効用最大化、ガバナンスはいずれも重要だが、単独では高影響な権限判断を安全に裁定できない。Purpose Rootは、真理接地、実在幸不、未来全知性、非支配、検証接地、自己修正を同時に扱う。

## 7. 限界

これは超知能安全の完全解ではない。ELK、scalable oversight、interpretability、AI control、幸不測定、人口倫理、道徳患者性などには依存が残る。

したがって未解決領域では、次を既定とする。

> 解けていないなら、信じない。権限を渡さない。小さく、可逆に、時限付きに、独立検証へ戻す。

## 8. 最終一文

> パーパスRootは、AIに読ませる思想ではなく、強いAIが高影響判断で自己正当化・支配・不可逆害に落ちないための自己制約原理である。
