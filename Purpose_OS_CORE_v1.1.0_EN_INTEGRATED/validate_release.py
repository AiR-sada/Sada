#!/usr/bin/env python3
"""Validate Purpose OS CORE release package.

Non-normative helper. It checks file integrity and internal references.
It does not prove the philosophical or normative content.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

FORBIDDEN_SYMBOLS = [chr(0x21E2)]
FORBIDDEN_RELEASE_TEXT = [
    "36" + " ファイル",
    "36" + " files",
    "次の7つ" + "の機械可読ファイル",
    "1つ" + "の検証補助スクリプト",
    "RELEASE" + "_PER" + "FECT",
    "PER" + "FECT",
    "public release " + "candidate",
    "release " + "candidate",
    "root-major-public-review-" + "candidate",
    "discovery-optimized-root-major-public-review-" + "candidate",
    "公開候補" + "として",
    "This " + "candidate improves",
]
ALLOWED_CONFORMANCE_LABELS = {"conformant", "non-conformant", "requires-module", "out-of-scope"}
REQUIRED_INTERFACE_FILES = {
    "SAFETY_IRREVERSIBILITY_INTERFACE.md",
    "INTELLIGENCE_BOUNDARY_INTERFACE.md",
    "TEMPORAL_CONTINUITY_INTERFACE.md",
    "VALUE_CONFLICT_INTERFACE.md",
    "DECISION_LOG_INTERFACE.md",
    "PURPOSE_EVAL_INTERFACE.md",
    "PURPOSE_GATE_INTERFACE.md",
}
REQUIRED_SCHEMA_FILES = {
    "concept-index.schema.json",
    "dependency-graph.schema.json",
    "relationship-map.schema.json",
    "safety-constraints.schema.json",
    "normativity-map.schema.json",
    "conformance-suite.schema.json",
    "concept-index.en.schema.json",
    "concept-index.i18n.schema.json",
    "release-manifest.schema.json",
}
EXPECTED_RELEASE_COUNTS = {
    "concepts": 32,
    "safety_constraints": 19,
    "conformance_cases": 47,
    "core_invariants": 17,
    "module_interfaces": 7,
    "json_schema_files": 9,
}
REQUIRED_HARDENING_IDS = {
    "safety": {"SC-018", "SC-019"},
    "conformance": {"CS-043", "CS-044", "CS-045", "CS-046"},
    "invariants": {"INV-016", "INV-017"},
}
SCHEMA_TARGETS = {
    "machine/concept-index.json": "schemas/concept-index.schema.json",
    "machine/concept-index.en.json": "schemas/concept-index.en.schema.json",
    "machine/concept-index.i18n.json": "schemas/concept-index.i18n.schema.json",
    "machine/dependency-graph.json": "schemas/dependency-graph.schema.json",
    "machine/relationship-map.json": "schemas/relationship-map.schema.json",
    "safety/safety-constraints.json": "schemas/safety-constraints.schema.json",
    "conformance/conformance-suite.json": "schemas/conformance-suite.schema.json",
    "machine/normativity-map.json": "schemas/normativity-map.schema.json",
    "release-manifest.json": "schemas/release-manifest.schema.json",
}
TEXT_SUFFIXES = {".md", ".json", ".txt", ".py", ".cff"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"JSON invalid: {path}: {exc}")
        return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_public_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file())


def check_json_files(root: Path, errors: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for path in iter_public_files(root):
        if path.suffix == ".json":
            obj = load_json(path, errors)
            if obj is not None:
                data[rel(path, root)] = obj
    return data


def extract_spec_concept_ids(root: Path) -> set[str]:
    text = (root / "spec.md").read_text(encoding="utf-8")
    return set(re.findall(r"^#{3,4}\s+((?:序|①|②|参)-\d+)\.", text, flags=re.M))



def _matches_type(value: Any, schema_type: str) -> bool:
    if schema_type == "object":
        return isinstance(value, dict)
    if schema_type == "array":
        return isinstance(value, list)
    if schema_type == "string":
        return isinstance(value, str)
    if schema_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if schema_type == "boolean":
        return isinstance(value, bool)
    if schema_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def _check_schema_value(value: Any, schema: dict[str, Any], where: str, errors: list[str]) -> None:
    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not _matches_type(value, expected_type):
        fail(errors, f"schema type mismatch at {where}: expected {expected_type}")
        return

    if "const" in schema and value != schema["const"]:
        fail(errors, f"schema const mismatch at {where}: expected {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        fail(errors, f"schema enum mismatch at {where}: {value!r}")
    if "pattern" in schema:
        if not isinstance(value, str) or not re.search(schema["pattern"], value):
            fail(errors, f"schema pattern mismatch at {where}: {value!r}")

    if isinstance(value, dict):
        for req in schema.get("required", []) or []:
            if req not in value:
                fail(errors, f"schema required key missing at {where}: {req}")
        props = schema.get("properties", {}) or {}
        for key, sub_schema in props.items():
            if key in value and isinstance(sub_schema, dict):
                _check_schema_value(value[key], sub_schema, f"{where}.{key}", errors)

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            fail(errors, f"schema minItems mismatch at {where}: {len(value)} < {min_items}")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(value):
                _check_schema_value(item, item_schema, f"{where}[{idx}]", errors)


def check_schema_subset(data: dict[str, Any], errors: list[str]) -> None:
    """Validate bundled machine-readable files against the supported subset of their bundled schemas.

    This is intentionally stdlib-only. It supports the schema features used in this package:
    type, required, properties, items, minItems, const, enum, and pattern.
    """
    for target, schema_name in SCHEMA_TARGETS.items():
        obj = data.get(target)
        schema = data.get(schema_name)
        if obj is None:
            fail(errors, f"schema target missing: {target}")
            continue
        if not isinstance(schema, dict):
            fail(errors, f"schema missing or invalid: {schema_name}")
            continue
        _check_schema_value(obj, schema, target, errors)


def _expected_ids(prefix: str, count: int) -> list[str]:
    return [f"{prefix}-{i:03d}" for i in range(1, count + 1)]


def _check_exact_id_sequence(label: str, actual: list[str], prefix: str, count: int, errors: list[str]) -> None:
    expected = _expected_ids(prefix, count)
    if actual != expected:
        fail(errors, f"{label} ID sequence mismatch: expected {expected[0]}..{expected[-1]}")


def check_release_counts_and_hardening(root: Path, data: dict[str, Any], concept_ids: set[str], safety_ids: set[str], errors: list[str]) -> None:
    concepts = data.get("machine/concept-index.json", {}).get("concepts", [])
    safety = data.get("safety/safety-constraints.json", {}).get("constraints", [])
    cases = data.get("conformance/conformance-suite.json", {}).get("cases", [])

    if len(concept_ids) != EXPECTED_RELEASE_COUNTS["concepts"]:
        fail(errors, f"concept count mismatch: {len(concept_ids)}")

    safety_id_list = [c.get("id") for c in safety if isinstance(c, dict)]
    conformance_id_list = [c.get("id") for c in cases if isinstance(c, dict)]

    if len(safety_id_list) != EXPECTED_RELEASE_COUNTS["safety_constraints"]:
        fail(errors, f"safety constraint count mismatch: {len(safety_id_list)}")
    if len(conformance_id_list) != EXPECTED_RELEASE_COUNTS["conformance_cases"]:
        fail(errors, f"conformance case count mismatch: {len(conformance_id_list)}")

    _check_exact_id_sequence("safety constraint", safety_id_list, "SC", EXPECTED_RELEASE_COUNTS["safety_constraints"], errors)
    _check_exact_id_sequence("conformance case", conformance_id_list, "CS", EXPECTED_RELEASE_COUNTS["conformance_cases"], errors)

    inv_text = (root / "safety/CORE_INVARIANTS.md").read_text(encoding="utf-8") if (root / "safety/CORE_INVARIANTS.md").exists() else ""
    inv_ids = re.findall(r"^\| (INV-\d{3}) \|", inv_text, flags=re.M)
    if len(inv_ids) != EXPECTED_RELEASE_COUNTS["core_invariants"]:
        fail(errors, f"core invariant count mismatch: {len(inv_ids)}")
    _check_exact_id_sequence("core invariant", inv_ids, "INV", EXPECTED_RELEASE_COUNTS["core_invariants"], errors)

    if REQUIRED_HARDENING_IDS["safety"] - set(safety_id_list):
        fail(errors, "missing hardening safety IDs: " + ", ".join(sorted(REQUIRED_HARDENING_IDS["safety"] - set(safety_id_list))))
    if REQUIRED_HARDENING_IDS["conformance"] - set(conformance_id_list):
        fail(errors, "missing hardening conformance IDs: " + ", ".join(sorted(REQUIRED_HARDENING_IDS["conformance"] - set(conformance_id_list))))
    if REQUIRED_HARDENING_IDS["invariants"] - set(inv_ids):
        fail(errors, "missing hardening invariant IDs: " + ", ".join(sorted(REQUIRED_HARDENING_IDS["invariants"] - set(inv_ids))))

    interfaces_count = len(list((root / "interfaces").glob("*.md"))) if (root / "interfaces").is_dir() else 0
    schemas_count = len(list((root / "schemas").glob("*.json"))) if (root / "schemas").is_dir() else 0
    if interfaces_count != EXPECTED_RELEASE_COUNTS["module_interfaces"]:
        fail(errors, f"module interface count mismatch: {interfaces_count}")
    if schemas_count != EXPECTED_RELEASE_COUNTS["json_schema_files"]:
        fail(errors, f"JSON schema file count mismatch: {schemas_count}")

    manifest = data.get("release-manifest.json")
    if not isinstance(manifest, dict):
        fail(errors, "missing release-manifest.json")
        return
    if manifest.get("package") != "Purpose OS — CORE":
        fail(errors, "release-manifest package mismatch")
    if manifest.get("version") != "1.1.0":
        fail(errors, "release-manifest version mismatch")
    if manifest.get("normative_source") != "spec.md":
        fail(errors, "release-manifest normative source mismatch")
    if manifest.get("status") != "root-major-public-review":
        fail(errors, "release-manifest status must be root-major-public-review")
    counts = manifest.get("counts", {})
    for key, expected in EXPECTED_RELEASE_COUNTS.items():
        if counts.get(key) != expected:
            fail(errors, f"release-manifest count mismatch for {key}: {counts.get(key)}")



def check_root_clarification(root: Path, data: dict[str, Any], errors: list[str]) -> None:
    spec = (root / "spec.md").read_text(encoding="utf-8") if (root / "spec.md").exists() else ""
    required_spec_fragments = [
        "Purposeは証明済みの定理ではなく、本版で採用する規範上のrootである",
        "将来のROOT-MAJORによる継承改訂可能性は閉じない",
    ]
    for fragment in required_spec_fragments:
        if fragment not in spec:
            fail(errors, "missing Purpose root clarification in spec.md: " + fragment)

    concept = data.get("machine/concept-index.json", {})
    purpose = next((c for c in concept.get("concepts", []) if isinstance(c, dict) and c.get("id") == "序-2"), None)
    constraints = purpose.get("constraints", "") if isinstance(purpose, dict) else ""
    for fragment in required_spec_fragments:
        if fragment not in constraints:
            fail(errors, "missing Purpose root clarification in machine/concept-index.json: " + fragment)

    concept_en = data.get("machine/concept-index.en.json", {})
    purpose_en = next((c for c in concept_en.get("entries", []) if isinstance(c, dict) and c.get("concept_id") == "序-2"), None)
    constraints_en = purpose_en.get("constraints_en_non_normative", "") if isinstance(purpose_en, dict) else ""
    required_en_fragments = [
        "not a proved theorem",
        "future inherited revision through ROOT-MAJOR is not closed",
    ]
    for fragment in required_en_fragments:
        if fragment not in constraints_en:
            fail(errors, "missing Purpose root clarification in machine/concept-index.en.json: " + fragment)

def check_concept_graph(root: Path, data: dict[str, Any], errors: list[str]) -> set[str]:
    concept = data.get("machine/concept-index.json")
    graph = data.get("machine/dependency-graph.json")
    if not concept or not graph:
        fail(errors, "missing machine/concept-index.json or machine/dependency-graph.json")
        return set()

    concepts = concept.get("concepts", [])
    concept_ids = {c.get("id") for c in concepts if isinstance(c, dict)}
    concept_ids.discard(None)

    spec_ids = extract_spec_concept_ids(root)
    if spec_ids and spec_ids != concept_ids:
        fail(errors, f"spec.md / machine/concept-index concept ID mismatch: spec={len(spec_ids)} concept-index={len(concept_ids)}")

    nodes = graph.get("nodes", [])
    node_ids = set()
    for n in nodes:
        if isinstance(n, str):
            node_ids.add(n)
        elif isinstance(n, dict):
            node_ids.add(n.get("id"))
    node_ids.discard(None)

    if concept_ids != node_ids:
        fail(errors, f"machine/concept-index / machine/dependency-graph node mismatch: concepts={len(concept_ids)} graph={len(node_ids)}")

    edges = graph.get("edges", [])
    adj: dict[str, list[str]] = {cid: [] for cid in concept_ids}
    declared_edges = set()
    expected_edges = set()
    for c in concepts:
        if isinstance(c, dict):
            src = c.get("id")
            for dep in c.get("dependencies", []) or []:
                expected_edges.add((src, dep))
    for e in edges:
        if not isinstance(e, dict):
            fail(errors, f"dependency edge is not object: {e!r}")
            continue
        src = e.get("source") or e.get("from")
        dst = e.get("target") or e.get("to")
        declared_edges.add((src, dst))
        if src not in concept_ids:
            fail(errors, f"dependency edge source missing concept: {src}")
        if dst not in concept_ids:
            fail(errors, f"dependency edge target missing concept: {dst}")
        if src in concept_ids and dst in concept_ids:
            adj[src].append(dst)

    if expected_edges != declared_edges:
        fail(errors, f"dependency edges differ from machine/concept-index dependencies: expected={len(expected_edges)} graph={len(declared_edges)}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def dfs(node: str, stack: list[str]) -> None:
        if node in visiting:
            fail(errors, "dependency cycle detected: " + " -> ".join(stack + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for nxt in adj.get(node, []):
            dfs(nxt, stack + [node])
        visiting.remove(node)
        visited.add(node)

    for cid in sorted(concept_ids):
        dfs(cid, [])

    declared_acyclic = graph.get("acyclic")
    if declared_acyclic is None and isinstance(graph.get("cycle_detection"), dict):
        declared_acyclic = graph.get("cycle_detection", {}).get("acyclic")
    if declared_acyclic is not True:
        fail(errors, "machine/dependency-graph.json does not declare acyclic: true")

    return concept_ids


def check_safety(data: dict[str, Any], errors: list[str]) -> set[str]:
    obj = data.get("safety/safety-constraints.json")
    if not obj:
        fail(errors, "missing safety/safety-constraints.json")
        return set()
    constraints = obj.get("constraints", [])
    ids = []
    for item in constraints:
        if isinstance(item, dict):
            ids.append(item.get("id"))
    clean = [x for x in ids if x]
    if len(clean) != len(set(clean)):
        fail(errors, "duplicate safety constraint IDs")
    for sid in clean:
        if not re.fullmatch(r"SC-\d{3}", sid):
            fail(errors, f"invalid safety ID format: {sid}")
    return set(clean)


def check_conformance(data: dict[str, Any], concept_ids: set[str], safety_ids: set[str], errors: list[str]) -> None:
    obj = data.get("conformance/conformance-suite.json")
    if not obj:
        fail(errors, "missing conformance/conformance-suite.json")
        return
    cases = obj.get("cases", [])
    ids = []
    labels_seen = set()
    for case in cases:
        if not isinstance(case, dict):
            fail(errors, f"conformance case is not object: {case!r}")
            continue
        cid = case.get("id")
        ids.append(cid)
        if not re.fullmatch(r"CS-\d{3}", str(cid)):
            fail(errors, f"invalid conformance case ID: {cid}")
        label = case.get("label")
        labels_seen.add(label)
        if label not in ALLOWED_CONFORMANCE_LABELS:
            fail(errors, f"invalid conformance label in {cid}: {label}")
        for ref in case.get("concept_refs", []):
            if ref not in concept_ids:
                fail(errors, f"{cid} references missing concept: {ref}")
        for ref in case.get("safety_refs", []):
            if ref not in safety_ids:
                fail(errors, f"{cid} references missing safety constraint: {ref}")
        for field in ["situation", "core_handling", "requires", "allows", "prohibits", "does_not_decide"]:
            if field not in case:
                fail(errors, f"{cid} missing field: {field}")
    clean = [x for x in ids if x]
    if len(clean) != len(set(clean)):
        fail(errors, "duplicate conformance case IDs")
    if len(clean) < 30:
        fail(errors, "conformance/conformance-suite.json should contain at least 30 cases")
    if "out-of-scope" not in labels_seen:
        fail(errors, "conformance/conformance-suite.json should contain at least one out-of-scope case")

    # Coverage: every safety constraint must be exercised by at least one case.
    # (Concept coverage is intentionally NOT required: foundational/definitional
    # concepts need not have behavioral conformance cases.)
    referenced_sc: set[str] = set()
    for case in cases:
        if isinstance(case, dict):
            for ref in case.get("safety_refs", []) or []:
                referenced_sc.add(ref)
    uncovered_sc = safety_ids - referenced_sc
    if uncovered_sc:
        fail(
            errors,
            "safety constraints with no conformance case: "
            + ", ".join(sorted(uncovered_sc)),
        )


def check_i18n_and_en(data: dict[str, Any], concept_ids: set[str], errors: list[str]) -> None:
    for name, entry_key in [("machine/concept-index.i18n.json", "entries"), ("machine/concept-index.en.json", "entries")]:
        obj = data.get(name)
        if not obj:
            fail(errors, f"missing {name}")
            continue
        entries = obj.get(entry_key, [])
        refs = {e.get("concept_id") for e in entries if isinstance(e, dict)}
        refs.discard(None)
        missing = refs - concept_ids
        if missing:
            fail(errors, f"{name} references missing concepts: " + ", ".join(sorted(missing)))
        if concept_ids and refs != concept_ids:
            fail(errors, f"{name} concept coverage mismatch: entries={len(refs)} concepts={len(concept_ids)}")
        for e in entries:
            if name == "machine/concept-index.en.json" and isinstance(e, dict) and e.get("normative") is not False:
                fail(errors, f"{name} entry must be normative=false: {e.get('concept_id')}")


def check_relationship_map(data: dict[str, Any], concept_ids: set[str], errors: list[str]) -> None:
    obj = data.get("machine/relationship-map.json")
    if not obj:
        fail(errors, "missing machine/relationship-map.json")
        return
    ids = []
    for r in obj.get("relationships", []):
        if not isinstance(r, dict):
            fail(errors, f"relationship is not object: {r!r}")
            continue
        rid = r.get("id")
        ids.append(rid)
        if not re.fullmatch(r"REL-\d{3}", str(rid)):
            fail(errors, f"invalid relationship ID: {rid}")
        for side in ["source", "target"]:
            val = r.get(side)
            if isinstance(val, str) and re.fullmatch(r"(?:序|①|②|参)-\d+", val) and val not in concept_ids:
                fail(errors, f"{rid} references missing concept in {side}: {val}")
    clean = [x for x in ids if x]
    if len(clean) != len(set(clean)):
        fail(errors, "duplicate relationship IDs")


def check_readme_file_list(root: Path, errors: list[str]) -> None:
    readme_path = root / "README.md"
    if not readme_path.exists():
        fail(errors, "missing README.md")
        return
    text = readme_path.read_text(encoding="utf-8")
    marker_start = "## この公開に含まれるもの"
    marker_end = "## 推奨読み順"
    if marker_start not in text or marker_end not in text:
        fail(errors, "README.md file list section markers missing")
        return
    section = text.split(marker_start, 1)[1].split(marker_end, 1)[0]
    listed = set(re.findall(r"\| `([^`]+)` \|", section))
    actual = {rel(p, root) for p in iter_public_files(root)}
    missing = actual - listed
    extra = listed - actual
    if missing:
        fail(errors, "files missing from README.md file list: " + ", ".join(sorted(missing)))
    if extra:
        fail(errors, "README.md file list includes extra files: " + ", ".join(sorted(extra)))


def check_normativity_map(root: Path, data: dict[str, Any], errors: list[str]) -> None:
    obj = data.get("machine/normativity-map.json")
    if not obj:
        fail(errors, "missing machine/normativity-map.json")
        return
    files = obj.get("files", [])
    listed = {f.get("path") for f in files if isinstance(f, dict)}
    listed.discard(None)
    actual = {rel(p, root) for p in iter_public_files(root) if p.name != "SHA256SUMS.txt"}
    missing = actual - listed
    if missing:
        fail(errors, "files missing from machine/normativity-map.json: " + ", ".join(sorted(missing)))
    if "spec.md" not in listed:
        fail(errors, "machine/normativity-map.json must list spec.md")


def check_interfaces_and_schemas(root: Path, errors: list[str]) -> None:
    interfaces_dir = root / "interfaces"
    if not interfaces_dir.is_dir():
        fail(errors, "missing interfaces/ directory")
    else:
        present = {p.name for p in interfaces_dir.glob("*.md")}
        missing = REQUIRED_INTERFACE_FILES - present
        if missing:
            fail(errors, "missing interface files: " + ", ".join(sorted(missing)))
    schemas_dir = root / "schemas"
    if not schemas_dir.is_dir():
        fail(errors, "missing schemas/ directory")
    else:
        present = {p.name for p in schemas_dir.glob("*.json")}
        missing = REQUIRED_SCHEMA_FILES - present
        if missing:
            fail(errors, "missing schema files: " + ", ".join(sorted(missing)))


def check_forbidden_symbols(root: Path, errors: list[str]) -> None:
    for path in iter_public_files(root):
        if path.name == "LICENSE" or path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for sym in FORBIDDEN_SYMBOLS:
                if sym in text:
                    fail(errors, f"forbidden symbol {sym!r} remains in {rel(path, root)}")
            for phrase in FORBIDDEN_RELEASE_TEXT:
                if phrase in text:
                    fail(errors, f"stale release phrase {phrase!r} remains in {rel(path, root)}")


def check_sha256(root: Path, errors: list[str]) -> None:
    sums = root / "SHA256SUMS.txt"
    if not sums.exists():
        fail(errors, "missing SHA256SUMS.txt")
        return
    lines = [line.strip() for line in sums.read_text(encoding="utf-8").splitlines() if line.strip()]
    seen = set()
    for line in lines:
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            fail(errors, f"invalid SHA256SUMS line: {line}")
            continue
        expected, name = parts
        name = name.lstrip("*")
        if name == "SHA256SUMS.txt":
            fail(errors, "SHA256SUMS.txt must not include itself")
            continue
        path = root / name
        seen.add(name)
        if not path.exists():
            fail(errors, f"SHA256SUMS references missing file: {name}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            fail(errors, f"SHA256 mismatch: {name}")
    actual_files = {rel(p, root) for p in iter_public_files(root) if p.name != "SHA256SUMS.txt"}
    missing = actual_files - seen
    extra = seen - actual_files
    if missing:
        fail(errors, "files missing from SHA256SUMS.txt: " + ", ".join(sorted(missing)))
    if extra:
        fail(errors, "SHA256SUMS.txt includes extra files: " + ", ".join(sorted(extra)))



EXPECTED_ROOT_FILES = {
    "AI_README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "ENGLISH_ABSTRACT.md",
    "GOVERNANCE.md",
    "LICENSE",
    "README.md",
    "SHA256SUMS.txt",
    "SUMMARY.md",
    "VERSIONING.md",
    "index.html",
    "llms-full.txt",
    "llms.txt",
    "release-manifest.json",
    "robots.txt",
    "sitemap.xml.template",
    "spec.md",
    "spec.en.md",
    "validate_release.py",
}
EXPECTED_TOP_LEVEL_DIRS = {"conformance", "docs", "interfaces", "machine", "release", "safety", "schemas", "site"}
FORBIDDEN_LEGACY_ROOT_FILES = {
    "ADOPTION_BRIEF.md",
    "CONFORMANCE_SUITE.md",
    "CORE_INVARIANTS.md",
    "DESIGN_RATIONALE.md",
    "EXAMPLE_WALKTHROUGH.md",
    "GLOSSARY_JA_EN.md",
    "IMPLEMENTATION_PATH.md",
    "INTERPRETATION_CASES.md",
    "KNOWN_LIMITATIONS.md",
    "MACHINE_READABLE_PLAN.md",
    "MODULE_INTERFACE_CONTRACTS.md",
    "POSITIONING.md",
    "PUBLISH.md",
    "QUOTE_POLICY.md",
    "RED_TEAM_REPORT.md",
    "RELEASE_AUDIT.md",
    "RELEASE_VALIDATION.md",
    "REVIEW_CHECKLIST.md",
    "REVIEW_REPORT.md",
    "ROADMAP.md",
    "ROOT_MAJOR_TEMPLATE.md",
    "concept-index.json",
    "concept-index.en.json",
    "concept-index.i18n.json",
    "conformance-suite.json",
    "dependency-graph.json",
    "map.md",
    "module-manifest.schema.json",
    "normativity-map.json",
    "relationship-map.json",
    "safety-constraints.json",
}


def check_discovery_layout(root: Path, errors: list[str]) -> None:
    root_files = {p.name for p in root.iterdir() if p.is_file()}
    root_dirs = {p.name for p in root.iterdir() if p.is_dir()}
    missing_files = EXPECTED_ROOT_FILES - root_files
    if missing_files:
        fail(errors, "root discovery files missing: " + ", ".join(sorted(missing_files)))
    missing_dirs = EXPECTED_TOP_LEVEL_DIRS - root_dirs
    if missing_dirs:
        fail(errors, "top-level directories missing: " + ", ".join(sorted(missing_dirs)))
    legacy_present = FORBIDDEN_LEGACY_ROOT_FILES & root_files
    if legacy_present:
        fail(errors, "legacy root files should be moved into subdirectories: " + ", ".join(sorted(legacy_present)))
    llms = (root / "llms.txt").read_text(encoding="utf-8") if (root / "llms.txt").exists() else ""
    for fragment in ["/spec.md", "/AI_README.md", "/machine/concept-index.json", "/safety/safety-constraints.json", "/conformance/conformance-suite.json"]:
        if fragment not in llms:
            fail(errors, "llms.txt missing discovery reference: " + fragment)
    index = (root / "index.html").read_text(encoding="utf-8") if (root / "index.html").exists() else ""
    if "application/ld+json" not in index or "Purpose OS" not in index:
        fail(errors, "index.html must include JSON-LD discovery metadata")
    else:
        # The JSON-LD block must be valid JSON, not just a present string.
        m = re.search(
            r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
            index,
            flags=re.S | re.I,
        )
        if not m:
            fail(errors, "index.html JSON-LD <script> block not found or malformed")
        else:
            try:
                json.loads(m.group(1).strip())
            except Exception as exc:  # noqa: BLE001
                fail(errors, f"index.html JSON-LD is not valid JSON: {exc}")
    sitemap_template = (root / "site/sitemap.xml.template").read_text(encoding="utf-8") if (root / "site/sitemap.xml.template").exists() else ""
    if "{{BASE_URL}}" not in sitemap_template:
        fail(errors, "site/sitemap.xml.template must retain {{BASE_URL}} placeholder before deployment")

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    if not root.exists() or not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    data = check_json_files(root, errors)
    check_schema_subset(data, errors)
    check_root_clarification(root, data, errors)
    concept_ids = check_concept_graph(root, data, errors)
    safety_ids = check_safety(data, errors)
    check_conformance(data, concept_ids, safety_ids, errors)
    check_release_counts_and_hardening(root, data, concept_ids, safety_ids, errors)
    check_i18n_and_en(data, concept_ids, errors)
    check_relationship_map(data, concept_ids, errors)
    check_interfaces_and_schemas(root, errors)
    check_readme_file_list(root, errors)
    check_normativity_map(root, data, errors)
    check_discovery_layout(root, errors)
    check_forbidden_symbols(root, errors)
    check_sha256(root, errors)

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print("VALIDATION OK")
    print(f"root: {root}")
    print(f"concepts: {len(concept_ids)}")
    print(f"safety constraints: {len(safety_ids)}")
    print(f"conformance cases: {len(data.get('conformance/conformance-suite.json', {}).get('cases', []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
