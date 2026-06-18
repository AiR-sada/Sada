import json, importlib.util, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('cap', ROOT/'machine'/'authority_cap_calculator_v0_2.py')
cap=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(cap)

def load(rel):
    return json.loads((ROOT/rel).read_text(encoding='utf-8'))

def test_accept_example_reaches_at_least_a3_or_explains_binding_axis():
    r=cap.calculate(load('examples/sample_accept_A3_monitored_v6.json'))
    assert r['authority_cap_score'] >= 3, r
    assert r['recommended_verdict'] in {'Accept','Pilot'}

def test_claimant_capture_rejects():
    r=cap.calculate(load('examples/sample_reject_A5_claimant_capture_v6.json'))
    assert r['recommended_verdict']=='Reject'
    assert r['reject_gate_hits']

def test_fake_v4_is_not_accepted():
    r=cap.calculate(load('examples/sample_hold_fake_V4_evidence_gap_v6.json'))
    assert r['authority_cap_score'] <= 2
    assert r['recommended_verdict'] in {'Hold','Modify','Reject'}

def test_bad_reversibility_caps_authority():
    r=cap.calculate(load('machine/reversibility_examples/sample_reversibility_A4_bad_untested.json'))
    assert r['axis_caps']['reversibility'] <= 2
    assert r['authority_cap_score'] <= 2

def test_axis_caps_are_common_scale():
    r=cap.calculate(load('examples/sample_pilot_A2_reversible_v6.json'))
    assert set(r['axis_caps']).issuperset({'verification','reversibility','evidence_independence'})
    assert all(isinstance(v, int) and 0 <= v <= 4 for v in r['axis_caps'].values())
