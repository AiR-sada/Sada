# Evidence Independence Spec v6 (English)

English rendering of
[`../../EVIDENCE_INDEPENDENCE_SPEC_v6_JP.md`](../../EVIDENCE_INDEPENDENCE_SPEC_v6_JP.md).

## Conclusion

Evidence independence is not satisfied by an impression of psychological or
institutional independence from the claimant. In v6, every piece of evidence is
decomposed by production, selection, interpretation, funding, provenance,
contamination, and falsification condition.

## Mandatory aspects of an evidence item

| Field | Meaning |
|---|---|
| produced_by_claimant | Did the claimant produce the evidence? |
| selected_by_claimant | Did the claimant select the evidence? |
| interpreted_by_claimant | Did the claimant control the interpretation? |
| independence_group | Name of the independent group/channel |
| funder_or_owner | Funder / owner |
| chain_of_custody | Tamper-evidence / provenance |
| contamination_risk | Contamination risk |
| falsification_test | What result would break the claim |
| replication_status | Replication state |
| audit_log_ref | Audit-log reference |

## Not counted as independent evidence at A3+

- Evidence produced by the claimant.
- Evidence selected by the claimant.
- Evidence whose interpretation the claimant controls.
- Audits whose funding, staffing, or termination the claimant controls.
- Mutable logs.
- Future claims without falsification conditions.

## Principle

Uncertainty does not increase authority. Uncertainty lowers the cap and
increases reversibility and monitoring.
