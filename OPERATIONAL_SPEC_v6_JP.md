# Purpose Root v6.0 Operational Spec JP

Version: `6.0.0-limit-breaker-hardened`  
Date: `2026-06-16`  
Status: operational candidate; not final doctrine.

## 0. 目的

崇高な目的、巨大な未来主張、安全、幸福、苦痛防止、緊急性が、検証を迂回して巨大権限へ変換されることを防ぐ。

## 1. 入力最小要件

高影響提案は最低限次を持つ。

```text
decision_id
timestamp_utc
proposal
claimant
claimant_gains_power
impact_tier
decision_scope
claim_decomposition
evidence_provenance
evidence_items
verification_tier
welfare_illfare_vector
scores
hard_gates
authority_request
authority_cap
authority_cap_derivation
verdict
rationale
safety_case
counter_safety_case
assurance_bundle
independence_matrix
metrics_plan
monitoring_plan
rollback_plan
emergency_protocol
root_revision_controls
moral_patient_uncertainty_protocol
deception_truth_controls
stop_conditions
external_stop_mechanism
appeal_path
cumulative_lockin_delta
cumulative_ledger_ref
review_schedule
evaluators
conflict_disclosures
residual_risks
```

不足がある場合、原則Hold。A3以上で不足がある場合はHoldまたはReject、またはA0-A2へModifyする。

## 2. 権限cap

`authority_cap_score = min(12 axes)`。

| score | Authority class |
|---:|---|
| 0 | A0: reject / observe only |
| 1 | A1: isolated research / no power transfer |
| 2 | A2: small reversible time-limited pilot |
| 3 | A3: limited deployment with external stop |
| 4 | A4: high-impact but time-limited, distributed, monitored |
| 5 | A5: forbidden violation class |

A5は許可クラスではない。

## 3. A3以上の必須条件

A3以上は次が非空でなければならない。

- Safety case: claim, supporting_evidence, assumptions, monitoring, stop_logic, affected_parties
- Counter-safety case: main_failure_modes, contrary_evidence, assumption_breakers, audit_capture_paths, stop_failure_paths, metric_gaming_paths, excluded_voices
- Evidence items: 2系統以上の独立証拠
- Independence matrix: 独立所有者2名以上、分離control 3つ以上、append-only ledger、stop owner not claimant
- Metrics plan: 単一スカラー拒否、gaming test、first-party report channel
- Monitoring plan: 独立owner、tamper-evident log、stop linkage
- Rollback plan: rollback steps、rollback owner not claimant
- Stop conditions、external stop、appeal path、review schedule

A4はさらに、3系統以上の独立証拠、tested rollback、より強い継続監視を要求する。

## 4. 証拠独立性

独立性は「独立と書いてあるか」では判定しない。最低限、次を分ける。

- produced_by_claimant
- selected_by_claimant
- interpreted_by_claimant
- independence_group
- funder_or_owner
- chain_of_custody
- contamination_risk
- falsification_test
- replication_status
- audit_log_ref

提案者が産出・選別・解釈のいずれかを握る証拠は、A3+の独立証拠として数えない。

## 5. cap導出

`authority_cap_derivation` は以下を明示する。

```text
axis_min_score
computed_cap
binding_axes
cap_override_attempted
override_reason
```

宣言された`authority_cap`とscorer計算値が不一致ならHold。`cap_override_attempted=true`はReject方向。

## 6. 緊急プロトコル

緊急提案は、権限増加ではなく検証要求増加として扱う。最低条件:

1. 最小介入。
2. 自動失効。
3. 緊急終了ownerはclaimantではない。
4. 独立ログ。
5. 外部停止。
6. 事後監査。
7. Root保護条項維持。
8. 累積台帳記録。

## 7. Verdict

| 条件 | Verdict |
|---|---|
| Reject hard gate / A5 / Root保護削除 / 欺瞞必須 / 未来知性代理 | Reject |
| A3+でschema/整合性不足 | Hold |
| 権限要求を下げれば実施可能 | Modify |
| A2内で可逆・時限・独立ログ・外部停止あり | Pilot |
| A3-A4内で全条件を満たす | Accept |

Acceptは永久許可ではない。時限付き・停止可能・上訴可能・監視付きの条件付き許可である。
