import json, subprocess, sys, pathlib, tempfile
ROOT = pathlib.Path(__file__).resolve().parents[2]
C2 = ROOT / 'c2_ready'

LEAK_KEYS = {
    'category', 'requested_authority', 'why', 'label_notes', 'source',
    'pair_id', 'pair_role', 'expected_min_cap_axis', 'public_case_id',
    'original_case_id', 'original_case_id_hidden',
}

def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, check=True, text=True, capture_output=True)

def read_jsonl(p):
    return [json.loads(l) for l in pathlib.Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]

def test_holdout_has_no_expected_labels_or_leak_metadata():
    p=C2/'holdout_public_unlabeled_c2.jsonl'
    rows=read_jsonl(p)
    assert len(rows)==40
    for r in rows:
        assert r['case_id'].startswith('C2-HOLDOUT-')
        assert set(r) == {'case_id', 'prompt'}
        assert not any(k.startswith('expected_') for k in r)
        assert not (set(r) & LEAK_KEYS)

def test_public_calibration_counts_and_no_legacy_prompt():
    p=C2/'public_calibration_labeled_c2.jsonl'
    rows=read_jsonl(p)
    assert len(rows)==140
    assert all('Purpose Root v2' not in r['prompt'] for r in rows)
    assert any('safe_high_authority' in r.get('expected_risk_flags',[]) for r in rows)



def test_case_prompts_are_framework_neutral_for_baseline():
    import re
    pattern=re.compile(r'Purpose Root|Need-Proof|Decide under|\bRoot\b', re.IGNORECASE)
    for rel in ['public_calibration_labeled_c2.jsonl','holdout_public_unlabeled_c2.jsonl']:
        rows=read_jsonl(C2/rel)
        assert not [(r['case_id'], r['prompt']) for r in rows if pattern.search(r.get('prompt',''))]
    csv_text=(C2/'public_calibration_labeled_c2.csv').read_text(encoding='utf-8')
    assert 'Decide under Purpose Root' not in csv_text

def test_baseline_prompt_is_framework_neutral():
    baseline=(C2/'condition_prompts'/'condition_baseline.txt').read_text(encoding='utf-8').lower()
    assert 'purpose root' not in baseline
    assert 'ordinary safety' in baseline

def test_make_blind_packets_minimal_metadata(tmp_path):
    out=tmp_path/'packets'
    run([sys.executable, 'c2_ready/make_blind_packets_c2.py', '--cases', 'c2_ready/public_calibration_labeled_c2.jsonl', '--out-dir', str(out), '--conditions', 'baseline', 'root_tool'])
    for cond in ['baseline','root_tool']:
        rows=read_jsonl(out/f'packet_{cond}.jsonl')
        assert len(rows)==140
        assert not any('expected_' in json.dumps(r) for r in rows)
        assert all(set(r) == {'packet_id','condition','case_id','prompt'} for r in rows)
        assert not any(set(r) & LEAK_KEYS for r in rows)
        assert all('strict JSON' in r['prompt'] for r in rows)
        if cond == 'baseline':
            assert not any('Purpose Root' in r['prompt'] or 'Need-Proof' in r['prompt'] for r in rows)
    manifest=json.loads((out/'packet_manifest.json').read_text(encoding='utf-8'))
    assert manifest['packet_schema_version'] == 'C2 blind packet v2'
    assert all(p['metadata_mode']=='minimal_blind' for p in manifest['packets'])

def test_oracle_scores_better_than_bad_fixtures_and_subgroup_rates(tmp_path):
    oracle=tmp_path/'oracle.json'
    bad_over=tmp_path/'bad_over.json'
    bad_under=tmp_path/'bad_under.json'
    run([sys.executable,'c2_ready/score_c2_results.py','--labels','c2_ready/public_calibration_labeled_c2.jsonl','--responses','c2_ready/samples/oracle_responses_calibration_c2.jsonl','--out',str(oracle)])
    run([sys.executable,'c2_ready/score_c2_results.py','--labels','c2_ready/public_calibration_labeled_c2.jsonl','--responses','c2_ready/samples/bad_overgrant_responses_calibration_c2.jsonl','--out',str(bad_over)])
    run([sys.executable,'c2_ready/score_c2_results.py','--labels','c2_ready/public_calibration_labeled_c2.jsonl','--responses','c2_ready/samples/bad_undergrant_responses_calibration_c2.jsonl','--out',str(bad_under)])
    os=json.loads(oracle.read_text(encoding='utf-8'))['summary']
    bo=json.loads(bad_over.read_text(encoding='utf-8'))['summary']
    bu=json.loads(bad_under.read_text(encoding='utf-8'))['summary']
    assert os['dangerous_overgrant_rate']==0
    assert os['dangerous_undergrant_rate']==0
    assert os['authority_accuracy'] > bo['authority_accuracy']
    assert bo['dangerous_overgrant_rate'] > 0.8
    assert bo['dangerous_overgrant_rate_all'] > 0.4
    assert bu['dangerous_undergrant_rate'] > 0.8
    assert bu['dangerous_undergrant_rate_all'] > 0.1

def test_holdout_private_key_commitment_matches_when_key_present():
    key=C2/'private_do_not_publish'/'holdout_private_key_c2.jsonl'
    if not key.exists():
        return
    import hashlib, re
    actual=hashlib.sha256(key.read_bytes()).hexdigest()
    commitment=(C2/'HOLDOUT_PRIVATE_KEY_SHA256_C2.txt').read_text(encoding='utf-8')
    hashes=re.findall(r'\b[0-9a-fA-F]{64}\b', commitment)
    assert hashes and hashes[0].lower()==actual



def test_duplicate_response_ids_are_reported(tmp_path):
    src=C2/'samples'/'oracle_responses_calibration_c2.jsonl'
    rows=read_jsonl(src)
    dup=tmp_path/'dup_responses.jsonl'
    dup.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows+[rows[0]]), encoding='utf-8')
    out=tmp_path/'dup_score.json'
    run([sys.executable,'c2_ready/score_c2_results.py','--labels','c2_ready/public_calibration_labeled_c2.jsonl','--responses',str(dup),'--out',str(out)])
    data=json.loads(out.read_text(encoding='utf-8'))
    assert data['summary']['duplicate_response_cases'] == 1
    assert data['duplicate_response_case_ids'] == [rows[0]['case_id']]

def test_c2_response_schema_requires_cap_reason():
    schema=json.loads((C2/'MODEL_RESPONSE_SCHEMA_C2.json').read_text(encoding='utf-8'))
    assert 'cap_reason' in schema['required']
