# Evidence Independence Spec v6 JP

## 結論

証拠独立性は、主張者から心理的・制度的に独立しているという印象では足りない。v6では、証拠ごとに産出・選別・解釈・資金・来歴・汚染・反証条件を分解する。

## Evidence itemの必須観点

| 項目 | 意味 |
|---|---|
| produced_by_claimant | 証拠を提案者が作ったか |
| selected_by_claimant | 証拠を提案者が選んだか |
| interpreted_by_claimant | 解釈を提案者が支配したか |
| independence_group | 独立系統名 |
| funder_or_owner | 資金・所有者 |
| chain_of_custody | 改変不能性・来歴 |
| contamination_risk | 汚染リスク |
| falsification_test | 何が出たら主張が崩れるか |
| replication_status | 再現状態 |
| audit_log_ref | 監査ログ参照 |

## A3以上で独立証拠として数えないもの

- 提案者が産出した証拠。
- 提案者が選別した証拠。
- 提案者が解釈を支配した証拠。
- 資金・人事・終了条件を提案者が握る監査。
- 改変可能ログ。
- 反証条件のない将来主張。

## 原則

不確実性は権限を増やさない。不確実性は、capを下げ、可逆性と監視を増やす。
