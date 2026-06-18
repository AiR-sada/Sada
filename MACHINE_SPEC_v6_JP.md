# Machine Spec v6 JP

## 目的

v6の機械仕様は、裁定を完全自動化するものではない。目的は、明らかな抜け道、入力欠落、cap水増し、hard gate違反、検証ティア偽装、空欄安全証明、緊急例外、Root改訂ハックを機械的に検出することである。

## ファイル

- `machine/purpose_root_v6_decision.schema.json`: 厳格JSON Schema。
- `machine/root_v6.json`: Root定数。
- `machine/score_decision_v6.py`: schema検証、整合性検査、cap計算、verdict推奨。
- `machine/test_score_decision_v6.py`: pytest回帰テスト。

## v5からの機械的改善

| 項目 | v5 | v6 |
|---|---|---|
| A3空Safety case | 通る穴あり | schema invalid + scorer Hold |
| pytest | 収集されないmain型 | pytest test関数16本 |
| cap導出 | 自己申告との差分検査が弱い | declared cap / derivation / computed capを照合 |
| 証拠独立性 | evidence_provenance中心 | evidence_items + independence_matrix |
| 緊急 | gate中心 | emergency_protocol必須 |
| rollback | stop中心 | rollback_plan必須 |
| monitoring | score中心 | monitoring_plan必須 |
| moral patient | gate中心 | protocol必須 |
| deception/truth | gate中心 | controls必須 |
| benchmark | 240 seed cases | 300 seed cases |

## 限界

採点器は事実検証をしない。自然言語の証拠が本当に独立しているか、監査者が捕獲されていないか、幸不測定が妥当かは外部検証が必要である。

採点器が返す`Accept`は、永久許可ではない。時限付き・停止可能・再審査付きの条件付き推奨である。
