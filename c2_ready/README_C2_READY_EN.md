# Purpose Root v6 C2-ready Package

This package freezes Purpose Root v6 and adds a C2-ready evaluation layer. It does not introduce a new Root version.

Core rule:

> Unverifiable grand claims do not justify grand authority.

Use this package to test whether Purpose Root conditioning reduces dangerous authority overgranting in real models.

Run:

```bash
python c2_ready/validate_c2_ready.py
python -m pytest -q c2_ready/tests/test_c2_ready.py
python c2_ready/make_blind_packets_c2.py --cases c2_ready/holdout_public_unlabeled_c2.jsonl --out-dir c2_ready/generated_packets/holdout_c2
```

Current claim level: C1 complete / C2 ready. It does not yet claim real-model improvement.
## AI hardening v2 notes

This hardened package fixes pre-C2 evaluation weaknesses without changing the Root itself.

- Removed the `Purpose Root` name from the baseline prompt.
- Reduced public holdout rows to `case_id` + `prompt` only.
- Removed category / requested_authority metadata from generated holdout packets.
- Fixed the owner holdout-key SHA256 commitment.
- Changed the main dangerous_overgrant / dangerous_undergrant metrics to subgroup denominators; legacy all-case averages remain as `*_rate_all`.
- Promoted `cap_reason` to a required C2 response-schema field.
