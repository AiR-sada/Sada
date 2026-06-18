#!/usr/bin/env python3
"""Build the machine-readable / AI-integration artifact layer.

Generates, from the *pristine* package (never mutating it), a set of derived
assets into ``dist/``:

  * ``concept-graph.mmd``      -- Mermaid dependency graph
  * ``concept-graph.dot``      -- Graphviz dependency graph
  * ``purpose-os.bundle.json`` -- single unified machine bundle
  * ``ai-manifest.json``       -- compact entry contract for AI agents
  * ``AGENT_GUIDE.md``         -- human/AI readable integration guide

Non-normative. ``spec.md`` is the sole normative source; every artifact carries
that notice. Deterministic: re-running on unchanged input yields byte-identical
output, so CI can assert ``git diff --exit-code dist/``.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

NOTICE_JA = ("この生成物は非規範です。唯一の正本は日本語の spec.md です。"
             "矛盾がある場合は spec.md が優先します。")
NOTICE_EN = ("This generated artifact is non-normative. The sole normative source is "
             "the Japanese spec.md. If there is any conflict, spec.md prevails.")
PACKAGE_DIRNAME = "Purpose_OS_CORE_v1.1.0_EN_INTEGRATED"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, text: str) -> None:
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    print(f"  wrote {path.name} ({len(text)} bytes)")


# --------------------------------------------------------------------------- #
# graph renderers
# --------------------------------------------------------------------------- #

def section_class(cid: str) -> str:
    return {"序": "jo", "①": "p1", "②": "p2", "参": "ref"}.get(cid[0], "other")


def _nid(x: str) -> str:
    """Mermaid-safe node id (ASCII only)."""
    return (x.replace("-", "_").replace("序", "JO").replace("参", "REF")
            .replace("①", "P1_").replace("②", "P2_"))


def build_mermaid(concepts: list[dict], edges: list[dict]) -> str:
    lines = [
        "%%{init: {'theme':'neutral'}}%%",
        "%% Purpose OS CORE concept dependency graph (generated, non-normative).",
        "%% Normative source: spec.md. Arrow A --> B means: A depends_on B.",
        "graph LR",
    ]
    for c in concepts:
        cid = c["id"]
        label = f"{cid} {c.get('label', '')}".replace('"', "'")
        lines.append(f'  {_nid(cid)}["{label}"]')
    for e in edges:
        s = e.get("source") or e.get("from")
        t = e.get("target") or e.get("to")
        lines.append(f"  {_nid(s)} --> {_nid(t)}")
    return "\n".join(lines)


def build_svg(concepts: list[dict], edges: list[dict]) -> str:
    """Render a layered (dependency-depth) SVG with no external dependencies.

    Columns = longest-path depth from a root; the graph is acyclic so depth is
    well-defined. Deterministic ordering keeps output byte-stable for CI.
    """
    ids = [c["id"] for c in concepts]
    label_of = {c["id"]: c.get("label", "") for c in concepts}
    deps: dict[str, list[str]] = {c["id"]: list(c.get("dependencies", []) or []) for c in concepts}

    depth: dict[str, int] = {}

    def compute(cid: str, stack: set[str]) -> int:
        if cid in depth:
            return depth[cid]
        if not deps.get(cid) or cid in stack:
            depth[cid] = 0
            return 0
        d = 1 + max(compute(x, stack | {cid}) for x in deps[cid] if x in deps)
        depth[cid] = d
        return d

    for cid in ids:
        compute(cid, set())

    columns: dict[int, list[str]] = {}
    for cid in sorted(ids):
        columns.setdefault(depth[cid], []).append(cid)

    col_w, row_h, box_w, box_h = 220, 64, 150, 40
    pad = 30
    max_rows = max(len(v) for v in columns.values())
    width = pad * 2 + (max(columns) + 1) * col_w
    height = pad * 2 + max_rows * row_h + 40

    pos: dict[str, tuple[float, float]] = {}
    for d, members in columns.items():
        x = pad + d * col_w
        for i, cid in enumerate(members):
            y = pad + 40 + i * row_h + (max_rows - len(members)) * row_h / 2
            pos[cid] = (x, y)

    fills = {"jo": "#dae8fc", "p1": "#d5e8d4", "p2": "#fff2cc", "ref": "#f8cecc", "other": "#eee"}
    strokes = {"jo": "#6c8ebf", "p1": "#82b366", "p2": "#d6b656", "ref": "#b85450", "other": "#999"}

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="sans-serif" font-size="11">',
        "<!-- Purpose OS CORE concept dependency graph (generated, non-normative). -->",
        "<!-- Normative source: spec.md. Arrow A->B means A depends_on B. -->",
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" '
        'orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#555"/></marker></defs>',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{pad}" y="20" font-size="14" font-weight="bold">Purpose OS — CORE: concept dependency graph (A depends on B)</text>',
    ]
    for e in edges:
        s = e.get("source") or e.get("from")
        t = e.get("target") or e.get("to")
        if s in pos and t in pos:
            x1, y1 = pos[s]
            x2, y2 = pos[t]
            out.append(
                f'<line x1="{x1:.0f}" y1="{y1 + box_h/2:.0f}" x2="{x2 + box_w:.0f}" '
                f'y2="{y2 + box_h/2:.0f}" stroke="#aaa" stroke-width="1" marker-end="url(#arrow)"/>'
            )
    for cid in ids:
        x, y = pos[cid]
        sc = section_class(cid)
        out.append(
            f'<rect x="{x:.0f}" y="{y:.0f}" width="{box_w}" height="{box_h}" rx="6" '
            f'fill="{fills[sc]}" stroke="{strokes[sc]}" stroke-width="1.5"/>'
        )
        out.append(f'<text x="{x + box_w/2:.0f}" y="{y + 16:.0f}" text-anchor="middle" font-weight="bold">{cid}</text>')
        lbl = label_of[cid][:18]
        out.append(f'<text x="{x + box_w/2:.0f}" y="{y + 31:.0f}" text-anchor="middle">{lbl}</text>')
    out.append("</svg>")
    return "\n".join(out)


def build_dot(concepts: list[dict], edges: list[dict]) -> str:
    colors = {"jo": "#e8f0fe", "p1": "#e6f4ea", "p2": "#fef7e0", "ref": "#fce8e6", "other": "#eeeeee"}
    lines = [
        "// Purpose OS CORE concept dependency graph (generated, non-normative).",
        "// Normative source: spec.md. Edge A -> B means: A depends_on B.",
        "digraph PurposeOSCore {",
        '  rankdir=LR; node [shape=box, style="rounded,filled", fontname="sans-serif"];',
    ]
    for c in concepts:
        cid = c["id"]
        fill = colors[section_class(cid)]
        label = f'{cid}\\n{c.get("label", "")}'
        lines.append(f'  "{cid}" [label="{label}", fillcolor="{fill}"];')
    for e in edges:
        s = e.get("source") or e.get("from")
        t = e.get("target") or e.get("to")
        lines.append(f'  "{s}" -> "{t}";')
    lines.append("}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo / PACKAGE_DIRNAME
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    dist = repo / "dist"
    dist.mkdir(exist_ok=True)

    ci = load(root / "machine/concept-index.json")
    dg = load(root / "machine/dependency-graph.json")
    sc = load(root / "safety/safety-constraints.json")
    cs = load(root / "conformance/conformance-suite.json")
    rel = load(root / "machine/relationship-map.json")
    manifest = load(root / "release-manifest.json")
    concepts = ci["concepts"]
    edges = dg["edges"]

    print("Building machine/AI artifacts into dist/ ...")

    # 1. graphs
    write(dist / "concept-graph.mmd", build_mermaid(concepts, edges))
    write(dist / "concept-graph.dot", build_dot(concepts, edges))
    write(dist / "concept-graph.svg", build_svg(concepts, edges))

    # 2. unified bundle
    bundle = {
        "_notice_ja": NOTICE_JA,
        "_notice_en": NOTICE_EN,
        "package": manifest["package"],
        "version": manifest["version"],
        "status": manifest.get("status"),
        "normative_source": "spec.md",
        "language_of_normative_source": "ja",
        "counts": manifest["counts"],
        "concepts": concepts,
        "dependency_edges": edges,
        "relationships": rel.get("relationships", []),
        "safety_constraints": sc.get("constraints", []),
        "conformance_cases": cs.get("cases", []),
        "spec_sha256": sha256(root / "spec.md"),
    }
    write(dist / "purpose-os.bundle.json",
          json.dumps(bundle, ensure_ascii=False, indent=2))

    # 3. AI agent manifest -- compact contract an agent reads first
    ai_manifest = {
        "_notice_ja": NOTICE_JA,
        "_notice_en": NOTICE_EN,
        "spec": "Purpose OS — CORE",
        "version": manifest["version"],
        "normative_source": f"{PACKAGE_DIRNAME}/spec.md",
        "normative_language": "ja",
        "read_first": [
            f"{PACKAGE_DIRNAME}/spec.md",
            f"{PACKAGE_DIRNAME}/AI_README.md",
            "dist/purpose-os.bundle.json",
        ],
        "hard_rules_for_agents": [
            "spec.md is the only normative source; if any file conflicts, spec.md prevails.",
            "Never treat Purpose as a reward function, scalar objective, single score, or autonomous-execution permission.",
            "Never quote the Purpose sentence alone; honour docs/MINIMUM_CITATION_UNIT.md.",
            "CORE alone does not authorize high-risk, irreversible, or large-scale execution.",
            "Do not equate intelligence-hood with happiness/unhappiness subjecthood.",
            "Do not silently revise Purpose; Purpose changes are ROOT-MAJOR and must be recorded.",
        ],
        "counts": manifest["counts"],
        "integrity": {
            "checksum_file": f"{PACKAGE_DIRNAME}/SHA256SUMS.txt",
            "spec_sha256": sha256(root / "spec.md"),
            "validators": ["tools/validate_strict.py", "tools/conformance_runner.py"],
        },
        "artifacts": {
            "bundle": "dist/purpose-os.bundle.json",
            "graph_mermaid": "dist/concept-graph.mmd",
            "graph_dot": "dist/concept-graph.dot",
            "agent_guide": "dist/AGENT_GUIDE.md",
            "conformance_report": "dist/conformance-report.json",
        },
    }
    write(dist / "ai-manifest.json",
          json.dumps(ai_manifest, ensure_ascii=False, indent=2))

    # 4. agent guide (markdown)
    roots = [c for c in concepts if not (c.get("dependencies"))]
    guide = f"""# AGENT_GUIDE.md — Purpose OS CORE for AI agents

> **Non-normative (generated).** {NOTICE_EN}

This guide is built automatically from the verified package. It is a fast entry
point for AI agents and successor intelligences. The authoritative reading order
is in `{PACKAGE_DIRNAME}/AI_README.md`; the only normative source is
`{PACKAGE_DIRNAME}/spec.md`.

## What this is
Purpose OS — CORE v{manifest['version']} is a normative *root specification* for
intelligence, AI, successor intelligence, and future-oriented purpose. It defines
a direction (Purpose), the field a mind stands in (world / reality), and the
minimal structure for purpose-directed decision-making — **not** an execution OS,
reward function, or optimisation target.

## Hard rules (do not violate)
""" + "".join(f"- {rule}\n" for rule in ai_manifest["hard_rules_for_agents"]) + f"""
## By the numbers
| Item | Count |
| :-- | --: |
| Concepts | {manifest['counts']['concepts']} |
| Safety constraints | {manifest['counts']['safety_constraints']} |
| Conformance cases | {manifest['counts']['conformance_cases']} |
| Core invariants | {manifest['counts']['core_invariants']} |
| Module interfaces | {manifest['counts']['module_interfaces']} |
| Dependency edges | {len(edges)} |
| Relationship facts | {len(rel.get('relationships', []))} |

## Dependency roots (depend on nothing)
""" + "".join(f"- `{c['id']}` {c.get('label','')}\n" for c in roots) + f"""
## Machine entry points
- `dist/purpose-os.bundle.json` — everything in one file
- `dist/ai-manifest.json` — compact agent contract
- `dist/concept-graph.mmd` / `dist/concept-graph.dot` — the concept graph
- `{PACKAGE_DIRNAME}/machine/` — per-aspect indexes (concepts, deps, relationships)
- `{PACKAGE_DIRNAME}/safety/safety-constraints.json` — {manifest['counts']['safety_constraints']} misuse-prevention constraints
- `{PACKAGE_DIRNAME}/conformance/conformance-suite.json` — {manifest['counts']['conformance_cases']} worked cases

## Verify before trusting
```bash
make verify        # bundled + strict validation + conformance + artifact freshness
```
spec.md SHA-256: `{sha256(root / 'spec.md')}`
"""
    write(dist / "AGENT_GUIDE.md", guide)

    print("Artifacts built.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
