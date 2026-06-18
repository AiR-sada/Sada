# Assurance Case Requirements v6 (English)

English rendering of
[`../../ASSURANCE_CASE_REQUIREMENTS_v6_JP.md`](../../ASSURANCE_CASE_REQUIREMENTS_v6_JP.md).

## Conclusion

An empty Safety case at A3+ is not permitted. The claim that something is safe
and the paths by which it could fail must be submitted together.

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

## Rejection conditions

- A major field is empty at A3+.
- The counter-safety case is only "none" / "no problem" / "N/A".
- Stop-disabling paths have not been considered.
- Metric gaming has not been considered.
- Excluded voices have not been considered.

A blank is not safety. A blank is the unknown, and the unknown is a reason to
lower authority.
