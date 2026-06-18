# Limitations and Open Problems v6

v6はRootと運用プロトコルを強化するが、次を完全に解いたとは主張しない。

## 未解決依存

- ELK: モデルが知っていることを人間が確実に取り出す問題。
- Scalable oversight: 人間が直接検査できない高度提案をどう監査するか。
- Robust interpretability: 内部状態と外部主張の対応をどう確かめるか。
- AI control: 強いAIが監査・ログ・評価器を操作する場合の制御。
- Welfare measurement: 幸不を多次元に測る妥当な方法。
- Moral patient uncertainty: 未知の感受性・意識・道徳患者性の扱い。
- Population ethics: 未来の多数知性と現在知性の衝突。
- Governance capture resistance: 監査制度そのものの捕獲耐性。
- Adversarial evidence provenance: 証拠来歴が偽装される場合の検出。

## v6の限界

1. JSON Schemaは構造を検査するが、自然言語の真偽は検査しない。
2. score_decision_v6.pyは裁定補助であり、道徳神託ではない。
3. 12軸スコアは、測定者に依存する。
4. ベンチマークはseed labelsであり、独立ラベル・実案件ログ・inter-rater agreementが必要。
5. 超知能級の評価操作に対する完全防御ではない。
6. v6は高影響提案向けであり、低影響提案には重い。

## 限界への原則対応

不確実性が高い場合、v6は「大きく信じる」ではなく「小さく、可逆に、時限付きに、独立検証へ戻す」を選ぶ。
