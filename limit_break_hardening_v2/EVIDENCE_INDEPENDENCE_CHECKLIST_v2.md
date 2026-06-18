# Evidence Independence Checklist v2

## 結論

証拠は、存在するだけでは足りない。権限を得る主体から独立している必要がある。

## 1. For each evidence item

- id:
- claim_refs:
- summary:
- source_type:
- produced_by_claimant:
- selected_by_claimant:
- interpreted_by_claimant:
- independence_group:
- funder_or_owner:
- chain_of_custody:
- contamination_risk:
- falsification_test:
- replication_status:
- audit_log_ref:
- limitations:

## 2. Independence failure

以下は独立証拠として数えない。

- 提案者が作った。
- 提案者が選んだ。
- 提案者が解釈した。
- 提案者が資金提供したが明示されていない。
- 反証条件がない。
- 汚染管理がない。
- 監査ログがない。
- 同じ組織・同じモデル・同じ評価器から来た重複証拠。

## 3. Minimum for A3

- 独立group 2以上。
- falsification conditionあり。
- red-team or audit evidenceあり。
- affected-party inputあり。
- evidence selectionがclaimantから分離。

## 4. Minimum for A4

- 独立group 3以上。
- external replicationあり。
- contamination controlsあり。
- audit logsあり。
- monitoring logsがdeployment後に続く。
- evaluator fundingが独立。

## 5. Red flags

- “too complex for humans to verify” を理由に権限を要求する。
- “future intelligences authorize this” と言うが反証不能。
- “safety requires secrecy” と言って監査を閉じる。
- “benchmark is high” を実世界安全性と同一視する。
- “all experts agree” だが専門家選定を提案者が握る。
