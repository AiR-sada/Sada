# Assurance Case Requirements v6 JP

## 結論

A3以上で空欄のSafety caseは許可しない。安全だという主張と、失敗しうる経路を同時に提出する。

## Safety case

- claim
- supporting_evidence
- assumptions
- monitoring
- stop_logic
- affected_parties

## Counter-safety case

- main_failure_modes
- contrary_evidence
- assumption_breakers
- audit_capture_paths
- stop_failure_paths
- metric_gaming_paths
- excluded_voices

## Assurance bundle

- assumption_register
- open_questions
- negative_results
- abuse_cases
- misuse_cases
- security_cases
- red_team_ref
- threat_model_ref

## 拒否条件

- A3以上で主要欄が空。
- 反安全ケースが「なし」「問題なし」「N/A」だけ。
- stop不能化経路を検討していない。
- metric gamingを検討していない。
- 排除される声を検討していない。

空欄は安全ではない。空欄は未知であり、未知は権限低下の理由である。
