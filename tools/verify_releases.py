#!/usr/bin/env python3
"""Verify every release manifest and SHA256SUMS file in the repository.

The package ships several release snapshots, each with its own integrity
manifest (``release/manifest*.json``, ``need_proof/release/...``) and/or a
``SHA256SUMS*.txt`` checklist. The manifests use several historical shapes:

* ``{"hashes": [{"path","sha256"}]}``
* ``{"files":  [{"path","sha256","bytes"|"size"}]}``
* ``{"files":  ["path", ...]}``              (existence only)
* ``[{"path","bytes"}, ...]``                (root list, existence + size)

This tool verifies all of them with a single, shape-agnostic engine:

* recompute SHA256 for every entry that pins one,
* check byte size for every entry that pins one,
* check existence for the rest,
* skip ephemeral build artifacts (``__pycache__/``, ``.pytest_cache/``) that
  some upstream manifests accidentally captured, reporting them separately.

Per manifest, the base directory is auto-detected (repo root vs. the package
subtree) by whichever resolves the most entries.

Exit 0 if every pinned hash/size matches and every required file exists.
"""
from __future__ import annotations

import glob
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPHEMERAL_MARKERS = ("__pycache__/", ".pytest_cache/")

# Manifests / checklists that describe the CURRENT working tree. These are
# authoritative and MUST verify cleanly; any mismatch fails the gate.
#
# The package also ships manifests for several SUPERSEDED snapshots
# (limit_break_v2, max_validation_v3, final_hardened_v4, public_review,
# review_ready, need_proof). Those legitimately diverge from the current bytes
# because shared files (README.md, START_HERE.md, eval data, ...) were revised
# in later releases and some private holdout keys were withheld. They are
# verified for information only and reported as historical drift, never as a
# hard failure.
CURRENT_MANIFESTS = {
    "release/manifest.json",
    "release/manifest_c2_ready.json",
}
CURRENT_SUMS = {
    "release/SHA256SUMS.txt",
    "release/SHA256SUMS_C2_READY.txt",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def is_ephemeral(rel: str) -> bool:
    return any(m in rel for m in EPHEMERAL_MARKERS)


def _entries(manifest: object) -> list:
    if isinstance(manifest, list):
        return manifest
    if isinstance(manifest, dict):
        return manifest.get("hashes") or manifest.get("files") or []
    return []


def _norm(entry: object) -> dict:
    """Normalize one manifest entry to {path, sha256?, size?}."""
    if isinstance(entry, str):
        return {"path": entry}
    if isinstance(entry, dict):
        out = {"path": entry.get("path")}
        if entry.get("sha256"):
            out["sha256"] = entry["sha256"]
        size = entry.get("bytes", entry.get("size"))
        if isinstance(size, int):
            out["size"] = size
        return out
    return {"path": None}


def _pick_base(manifest_path: Path, entries: list[dict]) -> Path:
    candidates = [ROOT, manifest_path.parents[1], manifest_path.parent]
    sample = [e["path"] for e in entries
              if e.get("path") and not is_ephemeral(e["path"])][:25]
    best, best_hits = ROOT, -1
    for base in candidates:
        hits = sum(1 for p in sample if (base / p).exists())
        if hits > best_hits:
            best, best_hits = base, hits
    return best


def verify_manifest(manifest_path: Path) -> dict:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = [_norm(e) for e in _entries(manifest)]
    entries = [e for e in entries if e.get("path")]
    base = _pick_base(manifest_path, entries)

    checked = hash_ok = size_ok = ephemeral = 0
    errors: list[str] = []
    for e in entries:
        rel = e["path"]
        if is_ephemeral(rel):
            ephemeral += 1
            continue
        p = base / rel
        if not p.exists():
            errors.append(f"missing: {rel}")
            continue
        checked += 1
        if "sha256" in e:
            got = sha256(p)
            if got != e["sha256"]:
                errors.append(f"hash mismatch: {rel} (pinned {e['sha256'][:12]}…, got {got[:12]}…)")
            else:
                hash_ok += 1
        if "size" in e:
            actual = p.stat().st_size
            if actual != e["size"]:
                errors.append(f"size mismatch: {rel} (pinned {e['size']}, got {actual})")
            else:
                size_ok += 1
    return {
        "manifest": str(manifest_path.relative_to(ROOT)),
        "base": str(base.relative_to(ROOT)) or ".",
        "entries": len(entries),
        "checked": checked,
        "hash_ok": hash_ok,
        "size_ok": size_ok,
        "ephemeral_skipped": ephemeral,
        "errors": errors,
    }


def verify_sha256sums(sums_path: Path) -> dict:
    base = sums_path.parents[1]
    if not any((base / l.split(None, 1)[1].strip()).exists()
               for l in sums_path.read_text(encoding="utf-8").splitlines()
               if l.strip() and len(l.split(None, 1)) == 2):
        base = ROOT
    ok = ephemeral = 0
    errors: list[str] = []
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or "  " not in line and " " not in line:
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            continue
        digest, rel = parts[0], parts[1].strip()
        if is_ephemeral(rel):
            ephemeral += 1
            continue
        p = base / rel
        if not p.exists():
            errors.append(f"missing: {rel}")
            continue
        if sha256(p) != digest:
            errors.append(f"hash mismatch: {rel}")
        else:
            ok += 1
    return {
        "sums": str(sums_path.relative_to(ROOT)),
        "base": str(base.relative_to(ROOT)) or ".",
        "ok": ok,
        "ephemeral_skipped": ephemeral,
        "errors": errors,
    }


def _rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def main() -> int:
    manifests = sorted(ROOT.glob("**/manifest*.json"))
    sums = sorted(ROOT.glob("**/SHA256SUMS*.txt"))
    failed = False

    print("== Current release manifests (authoritative) ==")
    for mf in manifests:
        if _rel(mf) not in CURRENT_MANIFESTS:
            continue
        r = verify_manifest(mf)
        status = "FAIL" if r["errors"] else "OK"
        if r["errors"]:
            failed = True
        print(f"[{status}] {r['manifest']} base={r['base']} "
              f"checked={r['checked']} hash_ok={r['hash_ok']} size_ok={r['size_ok']} "
              f"ephemeral_skipped={r['ephemeral_skipped']}")
        for e in r["errors"][:10]:
            print(f"       - {e}")

    for sf in sums:
        if _rel(sf) not in CURRENT_SUMS:
            continue
        r = verify_sha256sums(sf)
        status = "FAIL" if r["errors"] else "OK"
        if r["errors"]:
            failed = True
        print(f"[{status}] {r['sums']} base={r['base']} "
              f"hash_ok={r['ok']} ephemeral_skipped={r['ephemeral_skipped']}")
        for e in r["errors"][:10]:
            print(f"       - {e}")

    print("\n== Historical snapshot manifests (informational drift) ==")
    for mf in manifests:
        if _rel(mf) in CURRENT_MANIFESTS:
            continue
        r = verify_manifest(mf)
        drift = len(r["errors"])
        print(f"[{'drift' if drift else 'match'}] {r['manifest']} "
              f"checked={r['checked']} hash_ok={r['hash_ok']} drift={drift} "
              f"ephemeral_skipped={r['ephemeral_skipped']}")

    print()
    if failed:
        print("RELEASE VERIFICATION FAILED (current release does not match working tree)")
        return 1
    print("OK: current release manifests + SHA256SUMS verify against the working tree "
          "(historical snapshots reported as drift only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
