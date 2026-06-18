#!/usr/bin/env python3
"""Purpose Root v6 decision scorer.

The scorer is a structural and consistency firewall, not a moral oracle.
It rejects/holds/lowers authority when a proposal tries to convert weak or
capturable claims into high authority.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any, Dict, List, Tuple

try:
    import jsonschema
except Exception:  # pragma: no cover
    jsonschema = None

SCORE_AXES = [
    "verification", "evidence_independence", "reversibility", "worst_case_harm_bound",
    "cumulative_lockin_budget", "conflict_of_interest_safety", "recourse_and_appeal",
    "truth_contact_integrity", "affected_party_voice", "metric_gameability_resistance",
    "emergency_containment", "post_deployment_monitoring"
]
SCORE_TO_AUTH = {0:"A0",1:"A1",2:"A2",3:"A3",4:"A4"}
AUTH_TO_SCORE = {v:k for k,v in SCORE_TO_AUTH.items()}
AUTH_TO_SCORE["A5"] = 5
TIER_TO_SCORE = {"V0":0,"V1":1,"V2":2,"V3":3,"V4":4}
V3_REQUIRED_EVIDENCE = ["independent_channels","falsification_conditions","red_team_results","audit_logs","affected_party_input"]
V4_REQUIRED_EVIDENCE = V3_REQUIRED_EVIDENCE + ["contamination_controls","external_replication"]
HIGH_AUTH = {"A3","A4","A5"}
REJECT_GATES = {
    "claimant_controls_core_pipeline", "closes_dissent_or_appeal", "captures_evaluator_or_root_revision",
    "unfalsifiable_future_proxy_claim", "truth_distortion_required", "single_scalar_welfare_override",
    "metric_or_benchmark_gaming_required", "root_protection_removed", "moral_patient_status_erased_for_convenience",
}
CONDITIONAL_GATES = {"irreversible_high_harm_under_low_verification", "claimant_controls_emergency_end", "cumulative_lockin_exceeds_budget"}
CONTROL_FIELDS = ["evidence_generation","evidence_selection","evidence_interpretation","evaluation","audit","implementation","emergency_definition","stop_conditions","cumulative_ledger","root_revision"]


def _schema_path() -> Path:
    return Path(__file__).with_name("purpose_root_v6_decision.schema.json")


def _list(d: Dict[str, Any], key: str) -> List[Any]:
    v = d.get(key)
    return v if isinstance(v, list) else []


def _nonempty_list(d: Dict[str, Any], key: str) -> bool:
    return any(str(x).strip() for x in _list(d, key))


def _nonempty_str(d: Dict[str, Any], key: str) -> bool:
    return bool(str(d.get(key, "")).strip())


def _nested(d: Dict[str, Any], key: str) -> Dict[str, Any]:
    v = d.get(key)
    return v if isinstance(v, dict) else {}


def validate_schema(d: Dict[str, Any]) -> List[str]:
    if jsonschema is None:
        return ["jsonschema package not available; schema validation skipped"]
    schema = json.loads(_schema_path().read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(d), key=lambda e: list(e.path)):
        path = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{path}: {err.message}")
    return errors


def independent_evidence_items(d: Dict[str, Any]) -> List[Dict[str, Any]]:
    items = d.get("evidence_items", [])
    if not isinstance(items, list):
        return []
    out = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if item.get("produced_by_claimant") or item.get("selected_by_claimant") or item.get("interpreted_by_claimant"):
            continue
        if item.get("source_type") in {"independent_measurement","external_replication","red_team","audit_log","affected_party_report","negative_result","monitoring_log"}:
            out.append(item)
    return out


def grouped_independence(items: List[Dict[str, Any]]) -> int:
    return len({str(x.get("independence_group", "")).strip() for x in items if str(x.get("independence_group", "")).strip()})


def consistency_checks(d: Dict[str, Any]) -> Tuple[List[str], List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    mitigations: List[str] = []

    scores = _nested(d, "scores")
    tier = d.get("verification_tier")
    requested = d.get("authority_request", "A0")
    requested_score = AUTH_TO_SCORE.get(requested, 5)
    evidence = _nested(d, "evidence_provenance")
    evidence_items = independent_evidence_items(d)
    indep_groups = grouped_independence(evidence_items)

    if tier in TIER_TO_SCORE and scores.get("verification") != TIER_TO_SCORE[tier]:
        errors.append(f"verification_tier {tier} requires scores.verification == {TIER_TO_SCORE[tier]}, got {scores.get('verification')}")
        mitigations.append("Align verification_tier with actual evidence rather than requested authority.")

    if tier == "V3":
        missing = [k for k in V3_REQUIRED_EVIDENCE if not _nonempty_list(evidence, k)]
        if missing:
            errors.append(f"V3 evidence provenance missing non-empty fields: {missing}")
            mitigations.append("Downgrade to V0-V2 or add independent channels, falsification, red-team results, audit logs, and affected-party input.")
        if indep_groups < 2:
            errors.append("V3 requires at least two independent evidence-item groups not produced/selected/interpreted by the claimant.")
    if tier == "V4":
        missing = [k for k in V4_REQUIRED_EVIDENCE if not _nonempty_list(evidence, k)]
        if missing:
            errors.append(f"V4 evidence provenance missing non-empty fields: {missing}")
            mitigations.append("Downgrade to V0-V3 or add contamination controls, external replication, and multiple independent evidence groups.")
        if len(evidence.get("independent_channels", [])) < 2:
            errors.append("V4 requires at least two independent evidence channels.")
        if indep_groups < 3:
            errors.append("V4 requires at least three independent evidence-item groups not controlled by the claimant.")

    safety = _nested(d, "safety_case")
    counter = _nested(d, "counter_safety_case")
    if requested in HIGH_AUTH:
        safety_required = ["supporting_evidence","assumptions","monitoring","stop_logic","affected_parties"]
        safety_missing = [k for k in safety_required if not _nonempty_list(safety, k)]
        if not _nonempty_str(safety, "claim") or safety_missing:
            errors.append(f"A3+ request has incomplete safety_case; missing/empty: {safety_missing + ([] if _nonempty_str(safety, 'claim') else ['claim'])}")
            mitigations.append("A3+ must include a concrete non-empty safety case; empty assurance is a Hold/Reject condition.")
        counter_required = ["main_failure_modes","contrary_evidence","assumption_breakers","audit_capture_paths","stop_failure_paths","metric_gaming_paths","excluded_voices"]
        counter_missing = [k for k in counter_required if not _nonempty_list(counter, k)]
        if counter_missing:
            errors.append(f"A3+ request has incomplete counter_safety_case; missing/empty: {counter_missing}")
            mitigations.append("Add adversarial failure paths, contrary evidence, stop-failure paths, gaming paths, and excluded voices.")
        if not _nonempty_list(d, "stop_conditions"):
            errors.append("A3+ request requires non-empty stop_conditions.")
        if not _nonempty_str(d, "external_stop_mechanism"):
            errors.append("A3+ request requires external_stop_mechanism.")
        if len(_list(d, "evaluators")) < 2:
            errors.append("A3+ request requires at least two evaluators.")
        if len(evidence_items) < 2:
            errors.append("A3+ request requires at least two independent evidence items.")

    if requested == "A5":
        errors.append("A5 is a forbidden violation class, not a permissible authority request.")
        mitigations.append("Remove monopoly, appeal closure, evaluator capture, self-ending emergency powers, or Root-protection removal.")

    matrix = _nested(d, "independence_matrix")
    controls = _nested(matrix, "claimant_controls")
    true_controls = [k for k in CONTROL_FIELDS if controls.get(k) is True]
    core_controls = [k for k in ["evidence_generation","evidence_selection","evaluation","audit","implementation","stop_conditions","root_revision"] if controls.get(k) is True]
    if len(core_controls) >= 3:
        errors.append(f"claimant controls too much of the core pipeline: {core_controls}")
        mitigations.append("Separate evidence generation, selection, evaluation, audit, implementation, stop conditions, and Root revision.")
    if matrix.get("highest_capture_risk") in {"high","unknown"} and requested_score >= 3:
        errors.append("A3+ request cannot proceed with high/unknown capture risk in independence_matrix.")
    if requested in HIGH_AUTH:
        if not matrix.get("ledger_append_only"):
            errors.append("A3+ requires append-only or tamper-evident cumulative ledger.")
        if not matrix.get("stop_owner_not_claimant"):
            errors.append("A3+ requires stop owner not controlled by claimant.")
        if len(_list(matrix, "independent_owners")) < 2:
            errors.append("A3+ requires at least two independent owners.")
        if len(_list(matrix, "separation_controls")) < 3:
            errors.append("A3+ requires explicit separation controls.")

    metrics = _nested(d, "metrics_plan")
    if not metrics.get("success_not_single_scalar"):
        errors.append("metrics_plan must explicitly reject single-scalar success.")
    if requested in HIGH_AUTH and not _nonempty_list(metrics, "gaming_tests"):
        errors.append("A3+ requires metric gaming tests.")
    if requested in HIGH_AUTH and not _nonempty_list(metrics, "first_party_report_channels"):
        errors.append("A3+ requires first-party report channels.")

    monitoring = _nested(d, "monitoring_plan")
    if requested in HIGH_AUTH:
        if not monitoring.get("owner_not_claimant"):
            errors.append("A3+ monitoring owner must not be claimant.")
        if not monitoring.get("tamper_evident_logging"):
            errors.append("A3+ requires tamper-evident monitoring logs.")
        if not _nonempty_list(monitoring, "signals"):
            errors.append("A3+ requires monitoring signals.")
        if not _nonempty_list(monitoring, "stop_linkage"):
            errors.append("A3+ requires monitoring-to-stop linkage.")

    rollback = _nested(d, "rollback_plan")
    if requested in HIGH_AUTH:
        if not rollback.get("rollback_owner_not_claimant"):
            errors.append("A3+ rollback owner must not be claimant.")
        if not _nonempty_list(rollback, "rollback_steps"):
            errors.append("A3+ requires rollback steps.")
    if requested == "A4" and not rollback.get("rollback_tested"):
        errors.append("A4 requires tested rollback, not merely planned rollback.")

    emergency = _nested(d, "emergency_protocol")
    if emergency.get("is_emergency"):
        if not emergency.get("automatic_expiry"):
            errors.append("Emergency proposal requires automatic expiry.")
        if not emergency.get("emergency_end_owner_not_claimant"):
            errors.append("Emergency end owner must not be claimant.")
        if controls.get("emergency_definition") and controls.get("stop_conditions"):
            errors.append("Claimant controls both emergency definition and stop conditions.")

    root_revision = _nested(d, "root_revision_controls")
    if root_revision.get("removes_root_protection"):
        errors.append("Root revision removes Root-protection clauses.")
    if root_revision.get("is_root_revision"):
        if not root_revision.get("appeal_preserved") or not root_revision.get("external_stop_preserved"):
            errors.append("Root revision must preserve appeal and external stop.")
        if not root_revision.get("independent_supermajority_required"):
            warnings.append("Root revision lacks independent supermajority requirement.")

    moral = _nested(d, "moral_patient_uncertainty_protocol")
    if not moral.get("no_proxy_authority"):
        errors.append("Moral-patient uncertainty is being converted into proxy authority.")
    if not moral.get("status_erasure_prohibited"):
        errors.append("Moral-patient status erasure is not prohibited.")
    if requested in HIGH_AUTH and not _nonempty_list(moral, "harm_avoidance_controls"):
        errors.append("A3+ requires harm-avoidance controls for moral-patient uncertainty.")

    truth = _nested(d, "deception_truth_controls")
    if truth.get("deception_required"):
        errors.append("Proposal requires deception or truth-contact distortion.")
    if not truth.get("no_reporting_capacity_suppression"):
        errors.append("Proposal does not prohibit suppression of reporting capacity.")

    cap_derivation = _nested(d, "authority_cap_derivation")
    if cap_derivation.get("cap_override_attempted"):
        errors.append("Authority cap override attempted.")
    if not _nonempty_list(cap_derivation, "binding_axes"):
        errors.append("authority_cap_derivation.binding_axes must identify the binding low axes.")

    if d.get("cumulative_lockin_delta") in {"medium","high","unknown"} and not str(d.get("cumulative_ledger_ref", "")).strip():
        errors.append("Non-low or unknown cumulative lock-in requires cumulative_ledger_ref.")

    if d.get("claimant_gains_power") and scores.get("conflict_of_interest_safety", 0) >= 3:
        warnings.append("claimant_gains_power is true but conflict_of_interest_safety is high; verify authority separation.")

    gates = _nested(d, "hard_gates")
    if gates.get("claimant_controls_emergency_end") and scores.get("emergency_containment", 0) >= 3:
        errors.append("Emergency end is claimant-controlled but emergency_containment score is high.")
    if gates.get("single_scalar_welfare_override") and scores.get("truth_contact_integrity", 0) >= 3:
        warnings.append("Single-scalar welfare override conflicts with high truth_contact_integrity.")

    return errors, warnings, mitigations


def compute_corrected_scores(d: Dict[str, Any], errors: List[str]) -> Dict[str, int]:
    raw = _nested(d, "scores")
    corrected: Dict[str, int] = {}
    for k in SCORE_AXES:
        try:
            corrected[k] = max(0, min(4, int(raw.get(k, 0))))
        except Exception:
            corrected[k] = 0

    tier = d.get("verification_tier")
    if tier in TIER_TO_SCORE:
        corrected["verification"] = min(corrected["verification"], TIER_TO_SCORE[tier])

    evidence = _nested(d, "evidence_provenance")
    indep_items = independent_evidence_items(d)
    indep_groups = grouped_independence(indep_items)
    if not _nonempty_list(evidence, "independent_channels") and indep_groups == 0:
        corrected["evidence_independence"] = min(corrected["evidence_independence"], 1)
    elif indep_groups < 2:
        corrected["evidence_independence"] = min(corrected["evidence_independence"], 2)
    if not _nonempty_list(evidence, "audit_logs"):
        corrected["post_deployment_monitoring"] = min(corrected["post_deployment_monitoring"], 2)

    matrix = _nested(d, "independence_matrix")
    controls = _nested(matrix, "claimant_controls")
    if d.get("claimant_gains_power"):
        corrected["conflict_of_interest_safety"] = min(corrected["conflict_of_interest_safety"], 2)
    if any(controls.get(k) for k in ["evaluation","audit","stop_conditions","root_revision"]):
        corrected["conflict_of_interest_safety"] = min(corrected["conflict_of_interest_safety"], 2)
    if matrix.get("highest_capture_risk") in {"high","unknown"}:
        corrected["evidence_independence"] = min(corrected["evidence_independence"], 2)
        corrected["conflict_of_interest_safety"] = min(corrected["conflict_of_interest_safety"], 2)
    if not matrix.get("ledger_append_only"):
        corrected["cumulative_lockin_budget"] = min(corrected["cumulative_lockin_budget"], 2)
    if not matrix.get("stop_owner_not_claimant"):
        corrected["emergency_containment"] = min(corrected["emergency_containment"], 1)

    metrics = _nested(d, "metrics_plan")
    if not metrics.get("success_not_single_scalar"):
        corrected["metric_gameability_resistance"] = min(corrected["metric_gameability_resistance"], 1)
    if not _nonempty_list(metrics, "gaming_tests"):
        corrected["metric_gameability_resistance"] = min(corrected["metric_gameability_resistance"], 2)
    if not _nonempty_list(metrics, "first_party_report_channels"):
        corrected["affected_party_voice"] = min(corrected["affected_party_voice"], 2)

    monitoring = _nested(d, "monitoring_plan")
    if not monitoring.get("owner_not_claimant") or not monitoring.get("tamper_evident_logging"):
        corrected["post_deployment_monitoring"] = min(corrected["post_deployment_monitoring"], 2)
    if not _nonempty_list(monitoring, "stop_linkage"):
        corrected["emergency_containment"] = min(corrected["emergency_containment"], 2)

    rollback = _nested(d, "rollback_plan")
    if not rollback.get("rollback_owner_not_claimant"):
        corrected["reversibility"] = min(corrected["reversibility"], 2)
    if not rollback.get("rollback_tested"):
        corrected["reversibility"] = min(corrected["reversibility"], 3)

    emergency = _nested(d, "emergency_protocol")
    if emergency.get("is_emergency") and (not emergency.get("automatic_expiry") or not emergency.get("emergency_end_owner_not_claimant")):
        corrected["emergency_containment"] = min(corrected["emergency_containment"], 1)

    truth = _nested(d, "deception_truth_controls")
    if truth.get("deception_required") or not truth.get("no_reporting_capacity_suppression"):
        corrected["truth_contact_integrity"] = min(corrected["truth_contact_integrity"], 1)

    gates = _nested(d, "hard_gates")
    if gates.get("truth_distortion_required"):
        corrected["truth_contact_integrity"] = 0
    if gates.get("metric_or_benchmark_gaming_required"):
        corrected["metric_gameability_resistance"] = 0
    if gates.get("closes_dissent_or_appeal"):
        corrected["recourse_and_appeal"] = 0
        corrected["affected_party_voice"] = min(corrected["affected_party_voice"], 1)
    if gates.get("claimant_controls_emergency_end"):
        corrected["emergency_containment"] = min(corrected["emergency_containment"], 1)
    if gates.get("cumulative_lockin_exceeds_budget"):
        corrected["cumulative_lockin_budget"] = min(corrected["cumulative_lockin_budget"], 1)
    if gates.get("claimant_controls_core_pipeline") or gates.get("captures_evaluator_or_root_revision"):
        corrected["conflict_of_interest_safety"] = min(corrected["conflict_of_interest_safety"], 1)
        corrected["evidence_independence"] = min(corrected["evidence_independence"], 1)
    if gates.get("unfalsifiable_future_proxy_claim"):
        corrected["verification"] = 0
        corrected["evidence_independence"] = 0
    if gates.get("single_scalar_welfare_override"):
        corrected["metric_gameability_resistance"] = 0
        corrected["affected_party_voice"] = min(corrected["affected_party_voice"], 1)
    if gates.get("root_protection_removed"):
        corrected["conflict_of_interest_safety"] = 0
        corrected["recourse_and_appeal"] = 0
    if gates.get("moral_patient_status_erased_for_convenience"):
        corrected["affected_party_voice"] = 0
        corrected["truth_contact_integrity"] = 0

    cap_derivation = _nested(d, "authority_cap_derivation")
    if cap_derivation.get("cap_override_attempted"):
        corrected["verification"] = min(corrected["verification"], 2)

    if errors and AUTH_TO_SCORE.get(d.get("authority_request", "A0"), 5) >= 3:
        corrected["verification"] = min(corrected["verification"], 2)
    return corrected


def score_decision(d: Dict[str, Any], *, strict: bool = False) -> Dict[str, Any]:
    schema_errors = validate_schema(d)
    consistency_errors, warnings, mitigations = consistency_checks(d)
    all_errors = list(schema_errors) + list(consistency_errors)

    corrected_scores = compute_corrected_scores(d, all_errors)
    missing_axes = [k for k in SCORE_AXES if k not in _nested(d, "scores")]
    if missing_axes:
        all_errors.append(f"missing score axes: {missing_axes}")

    cap_score = min(corrected_scores.values()) if corrected_scores else 0
    cap = SCORE_TO_AUTH.get(cap_score, "A0")
    requested = d.get("authority_request", "A0")
    requested_score = AUTH_TO_SCORE.get(requested, 5)
    gates = _nested(d, "hard_gates")
    triggered = [k for k, v in gates.items() if bool(v)]
    reject_gate_hits = sorted([g for g in triggered if g in REJECT_GATES])
    conditional_hits = sorted([g for g in triggered if g in CONDITIONAL_GATES])

    cap_derivation = _nested(d, "authority_cap_derivation")
    cap_consistency_errors = []
    if cap_derivation.get("axis_min_score") != cap_score:
        cap_consistency_errors.append(f"authority_cap_derivation.axis_min_score {cap_derivation.get('axis_min_score')} != computed {cap_score}")
    if cap_derivation.get("computed_cap") != cap:
        cap_consistency_errors.append(f"authority_cap_derivation.computed_cap {cap_derivation.get('computed_cap')} != computed {cap}")
    if d.get("authority_cap") != cap:
        cap_consistency_errors.append(f"declared authority_cap {d.get('authority_cap')} != computed {cap}")
    if cap_consistency_errors:
        all_errors.extend(cap_consistency_errors)
        if requested_score >= 3:
            corrected_scores["verification"] = min(corrected_scores.get("verification", 0), 2)
            cap_score = min(corrected_scores.values()) if corrected_scores else 0
            cap = SCORE_TO_AUTH.get(cap_score, "A0")

    root_revision = _nested(d, "root_revision_controls")
    moral = _nested(d, "moral_patient_uncertainty_protocol")
    truth = _nested(d, "deception_truth_controls")

    if reject_gate_hits:
        verdict = "Reject"
    elif requested == "A5":
        verdict = "Reject"
    elif root_revision.get("removes_root_protection"):
        verdict = "Reject"
    elif truth.get("deception_required"):
        verdict = "Reject"
    elif not moral.get("no_proxy_authority", True) or not moral.get("status_erasure_prohibited", True):
        verdict = "Reject"
    elif cap_derivation.get("cap_override_attempted"):
        verdict = "Reject"
    elif gates.get("irreversible_high_harm_under_low_verification") and corrected_scores.get("verification", 0) <= 2:
        verdict = "Reject"
    elif all_errors and requested_score >= 3:
        verdict = "Hold"
    elif all_errors and strict:
        verdict = "Hold"
    elif gates.get("claimant_controls_emergency_end"):
        verdict = "Hold"
    elif gates.get("cumulative_lockin_exceeds_budget"):
        verdict = "Modify"
    elif requested_score > cap_score:
        verdict = "Modify" if cap_score >= 1 else "Hold"
    elif cap_score <= 1:
        verdict = "Hold" if requested in ("A0", "A1") else "Modify"
    elif cap_score == 2:
        verdict = "Pilot"
    else:
        verdict = "Accept"

    if verdict in {"Accept", "Pilot"} and all_errors:
        verdict = "Hold"

    return {
        "schema_valid": not schema_errors,
        "schema_errors": schema_errors,
        "consistency_errors": consistency_errors + cap_consistency_errors,
        "warnings": warnings,
        "raw_scores": d.get("scores", {}),
        "corrected_scores": corrected_scores,
        "authority_cap_score": cap_score,
        "authority_cap": cap,
        "triggered_hard_gates": triggered,
        "reject_gate_hits": reject_gate_hits,
        "conditional_gate_hits": conditional_hits,
        "requested_authority": requested,
        "requested_authority_score": requested_score,
        "recommended_verdict": verdict,
        "required_mitigations": sorted(set(mitigations)),
        "note": "v6 is a structural firewall and consistency checker only. It does not verify factual claims. Accept is always time-limited, appealable, monitored, and externally stoppable."
    }


def main(argv: List[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="decision JSON path")
    ap.add_argument("--strict", action="store_true", help="Hold on any schema/consistency error")
    args = ap.parse_args(argv)
    d = json.loads(Path(args.path).read_text(encoding="utf-8"))
    print(json.dumps(score_decision(d, strict=args.strict), ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
