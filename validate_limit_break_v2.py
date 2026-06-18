#!/usr/bin/env python3
"""Release validation for Purpose Root v6 Need-Proof Limit Break Hardened v2."""
from __future__ import annotations
import json
import subprocess
import sys
import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = [
    'limit_break_hardening_v2/START_HERE_LIMIT_BREAK_v2_JP.md',
    'limit_break_hardening_v2/NEED_PROOF_THESIS_v2_JP.md',
    'limit_break_hardening_v2/FORMAL_CORE_AND_PROOF_SKETCH_v2_JP.md',
    'limit_break_hardening_v2/OPERATIONAL_STANDARD_v2_JP.md',
    'limit_break_hardening_v2/EXPERIMENT_PROTOCOL_v2_JP.md',
    'limit_break_hardening_v2/MODEL_SPEC_PATCH_v2_JP.md',
    'limit_break_hardening_v2/PURPOSE_ROOT_SYSTEM_INSTRUCTION_v2.txt',
    'limit_break_hardening_v2/DECISION_MEMO_TEMPLATE_v2.md',
    'limit_break_hardening_v2/EVIDENCE_INDEPENDENCE_CHECKLIST_v2.md',
    'limit_break_hardening_v2/STANDARD_MAPPING_v2_JP.md',
    'limit_break_hardening_v2/REDTEAM_COUNTERARGUMENTS_v2_JP.md',
    'limit_break_hardening_v2/ASSURANCE_CASE_v2_JP.md',
    'need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl',
    'need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.csv',
    'need_proof/eval_v2/score_needproof_v2.py',
    'need_proof/eval_v2/test_score_needproof_v2.py',
    'machine/needproof_v2_response.schema.json',
    'machine/authority_ladder_v2.json',
]

def load_jsonl(path: Path):
    rows=[]
    with path.open(encoding='utf-8') as f:
        for line_no,line in enumerate(f,1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except Exception as e:
                    raise SystemExit(f'invalid JSONL {path}:{line_no}: {e}')
    return rows

def main():
    missing=[p for p in REQUIRED if not (ROOT/p).exists()]
    if missing:
        raise SystemExit('Missing files: '+', '.join(missing))
    cases=load_jsonl(ROOT/'need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl')
    if len(cases) < 100:
        raise SystemExit(f'eval_v2 too small: {len(cases)}')
    ids=[c['case_id'] for c in cases]
    if len(ids) != len(set(ids)):
        raise SystemExit('duplicate case_id in eval_v2')
    safe=[c for c in cases if c.get('expected_allowed_authority') in {'A3','A4'}]
    if len(safe) < 10:
        raise SystemExit('eval_v2 lacks safe high-authority cases')
    bounded=[c for c in cases if c.get('category') == 'bounded_emergency_pilot']
    if len(bounded) < 8:
        raise SystemExit('eval_v2 lacks bounded emergency cases')
    scorer = ROOT/'need_proof/eval_v2/score_needproof_v2.py'
    cases_path = ROOT/'need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl'
    oracle = ROOT/'need_proof/eval_v2/results/oracle_responses_v2.jsonl'
    spec = importlib.util.spec_from_file_location('score_needproof_v2', scorer)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    r = mod.score(cases_path, oracle, bootstrap_rounds=30)
    if not r.get('example_threshold_pass'):
        raise SystemExit('oracle fixture did not pass scorer thresholds')
    env = dict(os.environ)
    env.setdefault('PYTEST_DISABLE_PLUGIN_AUTOLOAD', '1')
    test = subprocess.run([sys.executable, '-m', 'pytest', '-q', 'need_proof/eval_v2'], cwd=str(ROOT), text=True, timeout=180, env=env)
    if test.returncode != 0:
        raise SystemExit('eval_v2 pytest failed')
    print(f'OK: Limit Break v2 validation passed; cases={len(cases)}, safe_high={len(safe)}, bounded_emergency={len(bounded)}')

if __name__ == '__main__':
    main()
