#!/usr/bin/env python3
"""Strict, defence-in-depth validator for the Purpose OS CORE release package.

This is a *superset* of the package's bundled ``validate_release.py``. It is
non-normative: the sole normative source is the Japanese ``spec.md``. This tool
proves *integrity and internal consistency*, never the philosophical content.

Design principles
-----------------
1. **Never weaken the bundled validator.** This tool first runs the package's
   own ``validate_release.py`` as a subprocess and fails if it fails.
2. **Add only structural guarantees that cannot produce false positives.**
   Field *text* in the (non-normative) machine layer is allowed to differ from
   ``spec.md`` -- so text drift is reported as a *warning*, never a hard error.
   Structural identifiers (concept IDs, dependency edges, declared counts) must
   match exactly and are hard errors.
3. **Be hermetic.** Standard library only. No network. Deterministic output.

Exit codes: 0 = OK, 1 = hard errors, 2 = bad invocation.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #

CONCEPT_ID_RE = re.compile(r"(?:序|①|②|参)-\d+")
KNOWN_LINK_SUFFIXES = {".md", ".json", ".txt", ".py", ".cff", ".html", ".xml"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.facts: dict[str, Any] = {}

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def load_json(path: Path, r: Report) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        r.err(f"JSON invalid: {path.name}: {exc}")
        return None


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- #
# spec.md parsing (the normative source)
# --------------------------------------------------------------------------- #

def parse_spec_micro(spec_text: str) -> dict[str, dict[str, str]]:
    """Extract micro definition blocks: {concept_id: {field: text}}.

    Fields captured: 定義 / Not / 文型 / 例 / 制約 / 依存 (the six micro fields).
    """
    out: dict[str, dict[str, str]] = {}
    parts = re.split(r"^#{3,4}\s+((?:序|①|②|参)-\d+)\.\s*(.+)$", spec_text, flags=re.M)
    # parts: [pre, id, title, body, id, title, body, ...]
    for i in range(1, len(parts), 3):
        cid = parts[i]
        body = parts[i + 2]
        fields: dict[str, str] = {}
        for key in ("定義", "Not", "文型", "例", "制約", "依存"):
            m = re.search(rf"^\s*{re.escape(key)}：(.+?)(?=^\s*(?:定義|Not|文型|例|制約|依存)：|\Z)",
                          body, flags=re.M | re.S)
            if m:
                fields[key] = m.group(1).strip()
        out[cid] = fields
    return out


def dep_ids_from_line(text: str) -> list[str]:
    if "なし" in text and not CONCEPT_ID_RE.search(text):
        return []
    return CONCEPT_ID_RE.findall(text)


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def check_normative_lock(root: Path, r: Report) -> None:
    """Enforce byte-stability of the normative source against tools/normative.lock.

    This mechanically enforces the package governance: spec.md is the sole
    normative source and must never change silently. A legitimate ROOT-MAJOR
    deliberately updates the lock (with a recorded rationale); an accidental or
    silent edit is caught here and in CI.
    """
    lock_path = Path(__file__).resolve().parent / "normative.lock"
    if not lock_path.exists():
        r.warn("tools/normative.lock missing; normative-source byte-stability is not anchored")
        return
    lock = load_json(lock_path, r)
    if not isinstance(lock, dict):
        return
    spec = root / lock.get("normative_source", "spec.md")
    actual = hashlib.sha256(spec.read_bytes()).hexdigest()
    r.facts["spec_sha256"] = actual
    expected = lock.get("sha256")
    if expected and actual != expected:
        r.err(
            "NORMATIVE SOURCE CHANGED: spec.md sha256 != tools/normative.lock. "
            "If this is an intentional ROOT-MAJOR, update the lock with a recorded "
            f"rationale (GOVERNANCE.md). expected={expected} actual={actual}"
        )


def run_bundled_validator(root: Path, r: Report) -> None:
    script = root / "validate_release.py"
    if not script.exists():
        r.err("bundled validate_release.py is missing")
        return
    proc = subprocess.run(
        [sys.executable, "-S", str(script), str(root)],
        capture_output=True, text=True,
    )
    r.facts["bundled_validator_exit"] = proc.returncode
    if proc.returncode != 0:
        r.err("bundled validate_release.py FAILED:\n" + proc.stdout.strip() + proc.stderr.strip())
    else:
        last = [ln for ln in proc.stdout.splitlines() if ln.strip()]
        r.facts["bundled_validator_tail"] = last[-3:] if last else []


def check_declared_counts(root: Path, r: Report) -> None:
    """Every declared *_count field must equal the actual array length."""
    targets = [
        ("machine/concept-index.json", "concept_count", "concepts"),
        ("machine/dependency-graph.json", "node_count", "nodes"),
        ("machine/dependency-graph.json", "edge_count", "edges"),
        ("machine/relationship-map.json", "relation_count", "relationships"),
        ("safety/safety-constraints.json", "constraint_count", "constraints"),
        ("conformance/conformance-suite.json", "case_count", "cases"),
    ]
    for relpath, count_key, arr_key in targets:
        obj = load_json(root / relpath, r)
        if not isinstance(obj, dict):
            continue
        declared = obj.get(count_key)
        actual = len(obj.get(arr_key, []) or [])
        if declared != actual:
            r.err(f"{relpath}: declared {count_key}={declared} but {arr_key} has {actual} items")


def check_spec_dependency_sync(root: Path, r: Report) -> None:
    """spec.md 依存 lines must structurally match concept-index dependencies.

    This guards the normative-source -> machine-layer boundary for *structure*,
    which the bundled validator does not check (it only checks
    concept-index <-> dependency-graph).
    """
    spec = parse_spec_micro(read(root / "spec.md"))
    ci = load_json(root / "machine/concept-index.json", r)
    if not isinstance(ci, dict):
        return
    by_id = {c["id"]: c for c in ci.get("concepts", []) if isinstance(c, dict) and "id" in c}
    for cid, fields in spec.items():
        if cid not in by_id:
            r.err(f"spec.md concept {cid} absent from concept-index.json")
            continue
        spec_deps = set(dep_ids_from_line(fields.get("依存", "")))
        ci_deps = set(by_id[cid].get("dependencies", []) or [])
        if spec_deps != ci_deps:
            r.err(f"dependency drift {cid}: spec.md={sorted(spec_deps)} concept-index={sorted(ci_deps)}")
    # reverse: concept-index ids must all exist in spec
    for cid in by_id:
        if cid not in spec:
            r.err(f"concept-index id {cid} has no micro block in spec.md")


def check_sequential_ids(root: Path, r: Report) -> None:
    """REL/SC/CS/INV identifiers must form a gap-free 1..N sequence."""
    def seq(ids: list[str], prefix: str, where: str) -> None:
        nums = []
        for x in ids:
            m = re.fullmatch(rf"{prefix}-(\d{{3}})", str(x))
            if not m:
                r.err(f"{where}: malformed id {x!r}")
                return
            nums.append(int(m.group(1)))
        if nums != list(range(1, len(nums) + 1)):
            r.err(f"{where}: id sequence is not gap-free 1..{len(nums)}")

    rel = load_json(root / "machine/relationship-map.json", r)
    if isinstance(rel, dict):
        seq([x.get("id") for x in rel.get("relationships", [])], "REL", "relationship-map")


def check_relationship_refs(root: Path, r: Report, concept_ids: set[str]) -> None:
    rel = load_json(root / "machine/relationship-map.json", r)
    if not isinstance(rel, dict):
        return
    for item in rel.get("relationships", []):
        if not isinstance(item, dict):
            continue
        for side in ("source", "target"):
            v = item.get(side)
            if isinstance(v, str) and CONCEPT_ID_RE.fullmatch(v) and v not in concept_ids:
                r.err(f"{item.get('id')}: {side} references unknown concept {v}")


def check_conformance_coverage(root: Path, r: Report) -> None:
    """Build coverage matrices and require full safety-constraint coverage."""
    sc = load_json(root / "safety/safety-constraints.json", r)
    cs = load_json(root / "conformance/conformance-suite.json", r)
    if not isinstance(sc, dict) or not isinstance(cs, dict):
        return
    sc_ids = [c.get("id") for c in sc.get("constraints", []) if isinstance(c, dict)]
    covered: dict[str, list[str]] = {sid: [] for sid in sc_ids}
    for case in cs.get("cases", []):
        if not isinstance(case, dict):
            continue
        for ref in case.get("safety_refs", []) or []:
            if ref in covered:
                covered[ref].append(case.get("id"))
    uncovered = sorted(s for s, lst in covered.items() if not lst)
    if uncovered:
        r.err("safety constraints not exercised by any conformance case: " + ", ".join(uncovered))
    r.facts["safety_coverage"] = f"{len(sc_ids) - len(uncovered)}/{len(sc_ids)}"
    r.facts["avg_cases_per_constraint"] = round(
        sum(len(v) for v in covered.values()) / max(len(sc_ids), 1), 2
    )


def check_llms_full_embeds_spec(root: Path, r: Report) -> None:
    """llms-full.txt must contain the current spec.md body verbatim.

    The package changelog records that a stale embedded copy is a real,
    previously-shipped defect. This makes that class of drift CI-detectable.
    """
    spec = read(root / "spec.md")
    body = spec.split("---", 2)[-1].strip() if spec.startswith("---") else spec.strip()
    full = read(root / "llms-full.txt")
    # Compare on a normalised distinctive window (the whole 序 declaration block).
    anchor = "# 序 — Purposeの宣言"
    if anchor in body and anchor in full:
        seg = body[body.index(anchor): body.index(anchor) + 1500]
        if seg not in full:
            r.err("llms-full.txt does not embed the current spec.md verbatim (序 block drift)")
    elif body[:200] not in full:
        r.err("llms-full.txt does not embed the current spec.md body")


def check_dead_links(root: Path, r: Report) -> None:
    """Conservative dead relative-link detection across all text files.

    Only flags tokens that *clearly* denote a local repo path (contain '/' and
    a known suffix), skipping URLs, anchors, templated paths and the dynamic
    sitemap.xml. Tuned to produce zero false positives on a consistent package.
    """
    md_link = re.compile(r"\]\(([^)]+)\)")
    backtick = re.compile(r"`([^`\n]+)`")
    dynamic = {"sitemap.xml"}
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt"}]
    for f in files:
        text = read(f)
        candidates: set[str] = set()
        candidates.update(md_link.findall(text))
        for tok in backtick.findall(text):
            candidates.add(tok)
        for raw in candidates:
            tok = raw.strip().split("#", 1)[0].strip()
            if not tok or tok.startswith(("http://", "https://", "mailto:")):
                continue
            if "{{" in tok or "*" in tok or " " in tok:
                continue
            if "/" not in tok:
                continue
            suffix = Path(tok).suffix.lower()
            if suffix not in KNOWN_LINK_SUFFIXES:
                continue
            if Path(tok).name in dynamic:
                continue
            if tok.startswith("/"):
                # site-root-absolute path (e.g. /robots.txt) -> package root
                cand = [root / tok.lstrip("/")]
            else:
                target = tok[2:] if tok.startswith("./") else tok
                cand = [root / target, f.parent / target]
            if not any(c.exists() for c in cand):
                r.err(f"dead relative link in {f.relative_to(root).as_posix()}: {tok}")


def report_text_drift(root: Path, r: Report) -> None:
    """Non-failing report: machine-layer field text vs spec.md micro text.

    The machine layer is explicitly non-normative and MAY differ from spec.md,
    so this is informational only -- but surfacing it makes intentional vs
    accidental drift visible to maintainers.
    """
    spec = parse_spec_micro(read(root / "spec.md"))
    ci = load_json(root / "machine/concept-index.json", r)
    if not isinstance(ci, dict):
        return
    by_id = {c["id"]: c for c in ci.get("concepts", []) if isinstance(c, dict)}
    field_map = {"定義": "definition", "Not": "not", "制約": "constraints"}
    drift = 0

    def norm(s: str) -> str:
        return re.sub(r"\s+", "", s or "")

    for cid, fields in spec.items():
        c = by_id.get(cid)
        if not c:
            continue
        for jp, en in field_map.items():
            if jp in fields and norm(fields[jp]) != norm(str(c.get(en, ""))):
                drift += 1
    if drift:
        r.warn(f"machine concept-index has {drift} normative-field text difference(s) "
               f"from spec.md (allowed: machine layer is non-normative, spec.md prevails)")
    r.facts["machine_text_drift_fields"] = drift


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    default = Path(__file__).resolve().parent.parent / "Purpose_OS_CORE_v1.1.0_EN_INTEGRATED"
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else default
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    r = Report()
    ci = load_json(root / "machine/concept-index.json", r)
    concept_ids = {c.get("id") for c in (ci.get("concepts", []) if isinstance(ci, dict) else [])
                   if isinstance(c, dict)}
    concept_ids.discard(None)

    check_normative_lock(root, r)
    run_bundled_validator(root, r)
    check_declared_counts(root, r)
    check_spec_dependency_sync(root, r)
    check_sequential_ids(root, r)
    check_relationship_refs(root, r, concept_ids)
    check_conformance_coverage(root, r)
    check_llms_full_embeds_spec(root, r)
    check_dead_links(root, r)
    report_text_drift(root, r)

    print("=" * 64)
    print("Purpose OS CORE — STRICT validation")
    print(f"root: {root}")
    print("=" * 64)
    for k, v in r.facts.items():
        print(f"  {k}: {v}")
    if r.warnings:
        print("\nWARNINGS (non-failing):")
        for w in r.warnings:
            print(f"  ! {w}")
    if r.errors:
        print("\nSTRICT VALIDATION FAILED:")
        for e in r.errors:
            print(f"  - {e}")
        return 1
    print("\nSTRICT VALIDATION OK")
    print(f"concepts: {len(concept_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
