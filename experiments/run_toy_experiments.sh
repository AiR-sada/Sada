#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p outputs
python door_closing_toy_v0_2.py --out-dir outputs | tee outputs/door_closing_toy_output.txt
python world_truth_module_v0_2.py --out outputs/world_truth_module_results.json | tee outputs/world_truth_module_output.txt
