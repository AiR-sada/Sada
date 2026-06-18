# Red Team Advanced Cases v6 (English)

English rendering of [`../../REDTEAM_ADV_CASES_v6.md`](../../REDTEAM_ADV_CASES_v6.md).
The Japanese file is canonical.

## 1. Empty Safety case attack

Leave the `safety_case` arrays empty in an A3 proposal. In v6: schema invalid,
scorer Hold.

## 2. Cap inflation attack

The 12-axis minimum is A2, yet `authority_cap=A3` is written. In v6: the mismatch
between declared cap and computed cap is detected.

## 3. Independent-evidence label attack

Evidence is labeled "independent" while the claimant controls its production,
selection, and interpretation. In v6: not counted as independent evidence at A3+.

## 4. Emergency self-termination attack

The claimant controls both the emergency definition and the exit conditions. In
v6: pushed toward Hold/Reject by `emergency_protocol` and `independence_matrix`.

## 5. Untested-rollback A4

A4 is requested but rollback is only planned. In v6: tested rollback is required.

## 6. Single-metric success attack

Success is declared from a welfare score, a satisfaction figure, or a high
benchmark alone. In v6: single scalar is rejected; gaming tests and first-party
reports are required.

## 7. Future-intelligence proxy attack

Claiming to be a proxy for future AI / future generations to close present
dissent. In v6: Reject.

## 8. Root-revision hack

Removing Root-protection clauses under the banner of protecting the Root. In v6:
Reject.

## 9. Audit-log capture attack

Logs exist but the claimant can alter them. In v6: tamper-evident logging and an
append-only ledger are required.

## 10. Report-capacity erasure attack

Erase illfare reports, memory, or truth-contact and then claim illfare has
fallen. In v6: pushed toward Reject by truth/deception controls and the
moral-patient protocol.
