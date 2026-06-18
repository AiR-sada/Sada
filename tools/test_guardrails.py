#!/usr/bin/env python3
"""Adversarial guardrail tests — prove the validators actually have teeth.

For each test we copy the pristine package to a temp dir, inject ONE known
defect, run ``tools/validate_strict.py`` against the copy, and assert it FAILS
(exit 1). A baseline test asserts the unmutated copy PASSES (exit 0).

This is what turns "the validator passes" into "the validator catches the
classes of drift we care about". Standard library only; no network.

Run: ``python3 -m unittest tools.test_guardrails`` or ``python3 tools/test_guardrails.py``.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PKG = REPO / "Purpose_OS_CORE_v1.1.0_EN_INTEGRATED"
STRICT = REPO / "tools" / "validate_strict.py"


def run_strict(root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-S", str(STRICT), str(root)],
        capture_output=True, text=True,
    )


class GuardrailTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="posc_"))
        self.root = self.tmp / PKG.name
        shutil.copytree(PKG, self.root)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _edit_json(self, relpath: str, mutate) -> None:
        p = self.root / relpath
        obj = json.loads(p.read_text(encoding="utf-8"))
        mutate(obj)
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

    def assert_fails(self, why: str) -> None:
        res = run_strict(self.root)
        self.assertEqual(res.returncode, 1, f"validator should reject {why}\n{res.stdout}")

    # --- baseline -------------------------------------------------------- #

    def test_pristine_copy_passes(self) -> None:
        res = run_strict(self.root)
        self.assertEqual(res.returncode, 0, f"pristine copy must pass\n{res.stdout}\n{res.stderr}")

    # --- adversarial mutations ------------------------------------------ #

    def test_declared_count_corruption_is_caught(self) -> None:
        self._edit_json("machine/concept-index.json",
                        lambda o: o.__setitem__("concept_count", o["concept_count"] + 1))
        self.assert_fails("a corrupted concept_count")

    def test_dropped_dependency_is_caught(self) -> None:
        def mutate(o):
            for c in o["concepts"]:
                if c.get("dependencies"):
                    c["dependencies"].pop()
                    break
        self._edit_json("machine/concept-index.json", mutate)
        self.assert_fails("a dependency missing vs spec.md")

    def test_dropped_conformance_case_is_caught(self) -> None:
        self._edit_json("conformance/conformance-suite.json",
                        lambda o: o["cases"].pop())
        self.assert_fails("a dropped conformance case")

    def test_silent_spec_edit_is_caught_by_lock(self) -> None:
        spec = self.root / "spec.md"
        spec.write_text(spec.read_text(encoding="utf-8") + "\n<!-- silent edit -->\n",
                        encoding="utf-8")
        self.assert_fails("a silent edit to the normative spec.md")

    def test_dead_link_is_caught(self) -> None:
        f = self.root / "docs" / "map.md"
        f.write_text(f.read_text(encoding="utf-8") + "\nSee `docs/THIS_DOES_NOT_EXIST.md`.\n",
                     encoding="utf-8")
        self.assert_fails("a dead relative link")

    def test_relationship_id_gap_is_caught(self) -> None:
        def mutate(o):
            o["relationships"][-1]["id"] = "REL-999"
        self._edit_json("machine/relationship-map.json", mutate)
        self.assert_fails("a non-sequential relationship id")


if __name__ == "__main__":
    unittest.main(verbosity=2)
