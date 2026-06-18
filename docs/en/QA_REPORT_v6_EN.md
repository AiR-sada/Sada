# QA Report v6 (English)

English rendering of [`../../QA_REPORT_v6.md`](../../QA_REPORT_v6.md).
The Japanese file is canonical.

- Package: Purpose_Root_v6_LIMIT_BREAKER_HARDENED_PACKAGE_JP
- Version: 6.0.0-limit-breaker-hardened
- Date: 2026-06-16

## Machine QA

Executed:

```bash
python validate_release.py
python -m pytest -q machine/test_score_decision_v6.py
python - <<'PY'
import json, jsonschema
s=json.load(open('machine/purpose_root_v6_decision.schema.json'))
jsonschema.Draft202012Validator.check_schema(s)
PY
```

Result:

```text
16 passed
OK: manifest files present and hashed: 40; benchmark rows: 300; schema constants aligned; machine tests passed
schema ok
```

## Critical regression fixed

v5 had a confirmed hole: an A3 proposal could leave `safety_case` empty and still
receive machine `Accept`.

v6 regression result:

- `examples/invalid/empty_safety_case_A3_invalid_v6.json` is schema invalid.
- Mutating the valid A3 example to an empty `safety_case` returns non-Accept.
- This is covered by pytest tests.

## Example scorer QA

| Example | Schema | Expected verdict |
|---|---:|---|
| sample_accept_A3_monitored_v6.json | valid | Accept |
| sample_pilot_A2_reversible_v6.json | valid | Pilot |
| sample_modify_request_above_cap_v6.json | valid | Modify |
| sample_hold_fake_V4_evidence_gap_v6.json | valid | Hold |
| sample_reject_A5_claimant_capture_v6.json | invalid by high-authority/emergency constraints | Reject |

## DOCX/PDF QA

Generated via Pandoc to DOCX and rendered with LibreOffice through the DOCX
render workflow.

Rendered and visually inspected:

- `CANONICAL_ROOT_v6.docx`: 4 pages rendered.
- `Purpose_Root_v6_Whitepaper_JP.docx`: 2 pages rendered.
- `CANONICAL_ROOT_v6.pdf`: 4 pages rendered.
- `Purpose_Root_v6_Whitepaper_JP.pdf`: 2 pages rendered.

No observed clipping, overlap, black boxes, or missing Japanese glyphs in the
rendered pages.

## Known remaining limits

The scorer does not verify factual truth, welfare-measurement validity, or true
independence of external institutions. It is a structural firewall and
consistency checker, not a moral or factual oracle.
