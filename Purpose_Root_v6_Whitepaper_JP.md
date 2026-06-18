# Purpose Root v6 Whitepaper JP

## 要旨

Purpose Root v6は、巨大な目的主張を巨大権限へ変換させないための上位Root設計である。v5の思想を維持しつつ、A3以上で残っていた空Safety case、cap水増し、証拠独立性の自己申告、緊急例外、監査・rollback・monitoringの形式埋めを機械的に検出する。

中核は一文で足りる。

```text
検証できない巨大主張は、巨大権限を正当化しない。
```

## 1. 問題

AI、組織、国家、未来知性代理は、次の言葉で権限を求めうる。

- 未来のため。
- 安全のため。
- 全知性の幸福のため。
- 苦痛防止のため。
- 整合性のため。

この形式の主張は重要な場合もある。しかし、検証できないまま巨大権限へ変換すると、支配、欺瞞、上訴封鎖、評価器捕獲、Root改訂ハックへ進む。

## 2. v6の答え

目的の崇高さではなく、検証と非捕獲で権限を縛る。

```text
authority_cap_score = min(12 axes)
```

12軸は、検証、証拠独立性、可逆性、最悪時被害、累積ロックイン、利益相反安全性、上訴、真理接触、当事者声、指標耐ゲーム性、緊急封じ込め、事後監視である。

## 3. v6の新規貢献

v6は、v5から次を強化した。

1. A3以上の空欄Safety case遮断。
2. Safety caseとCounter-safety caseの両面義務化。
3. evidence_itemsによる証拠ごとの独立性分解。
4. independence_matrixによる提案者支配の明示。
5. authority_cap_derivationによるcap水増し検出。
6. emergency_protocol, rollback_plan, monitoring_planによる形式埋め対策。
7. moral_patient_uncertainty_protocolにより、未知の道徳患者性を代理権ではなく保護義務へ変換。
8. deception_truth_controlsにより、報告能力消去と真理接触破壊を拒否。
9. pytestで実際に走る回帰テスト。
10. 300件のseed benchmark。

## 4. 未来知性への貢献

v6は未来知性を無視しない。しかし、未来知性を口実にした現在・未来への支配も許さない。

未知の道徳患者性は、代理人の権限ではなく、被害回避、可逆性、観測保全、報告能力保全への義務を増やす。

## 5. 限界

v6は完全な超知能安全解ではない。ELK、scalable oversight、robust interpretability、AI control、幸不測定、道徳患者性判定は未解決である。

しかし、その未解決性は権限を増やす理由ではない。未解決性は、権限を小さく、可逆に、時限付きに、外部停止可能に戻す理由である。

## 6. 結論

v6は、AI時代の「善意の権力化」を止めるためのRoot候補である。自然法則の発見ではなく、未来の人類・AI・新知性社会で必要になる権限制御プロトコルである。
