from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

def test_irr_script_runs(tmp_path):
    root=Path(__file__).resolve().parent
    out=tmp_path/'irr.json'
    p=root/'sample_annotations'/'sample_annotations_v3.csv'
    cmd=[sys.executable, str(root/'calculate_irr_v3.py'), '--annotations-csv', str(p), '--out', str(out)]
    subprocess.check_call(cmd)
    data=json.loads(out.read_text(encoding='utf-8'))
    assert data['n_annotations'] == 60
    assert data['summary']['expected_verdict_mean_kappa'] >= 0.9
    assert len(data['pairwise']) == 3
