#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "release" / "manifest.json"
SUMS = ROOT / "release" / "SHA256SUMS.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    files = manifest['files']
    missing = [p for p in files if not (ROOT / p).exists()]
    if missing:
        print('MISSING:', missing)
        return 1
    bad = []
    for entry in manifest['hashes']:
        p = ROOT / entry['path']
        got = sha256(p)
        if got != entry['sha256']:
            bad.append((entry['path'], entry['sha256'], got))
    if bad:
        print('HASH MISMATCH:', bad[:5])
        return 1
    # benchmark row count
    with (ROOT/'benchmark/Purpose_Root_v6_Benchmark_300_v0.6_JP.csv').open(encoding='utf-8') as f:
        n = sum(1 for _ in csv.DictReader(f))
    if n != 300:
        print(f'BENCHMARK ROW COUNT BAD: {n}')
        return 1
    # schema constants align
    schema = json.loads((ROOT/'machine/purpose_root_v6_decision.schema.json').read_text(encoding='utf-8'))
    root = json.loads((ROOT/'machine/root_v6.json').read_text(encoding='utf-8'))
    score_required = schema['properties']['scores']['required']
    gates_required = schema['properties']['hard_gates']['required']
    if score_required != root['score_axes']:
        print('SCORE AXES MISMATCH')
        return 1
    if gates_required != root['hard_gates']:
        print('HARD GATES MISMATCH')
        return 1
    # machine tests
    subprocess.run([sys.executable, '-m', 'pytest', '-q', 'machine/test_score_decision_v6.py'], cwd=ROOT, check=True)
    print(f"OK: manifest files present and hashed: {len(files)}; benchmark rows: {n}; schema constants aligned; machine tests passed")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
