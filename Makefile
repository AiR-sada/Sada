# Purpose OS — CORE : verification & artifact build
# Non-normative tooling. The sole normative source is the Japanese spec.md.

PKG := Purpose_OS_CORE_v1.1.0_EN_INTEGRATED
PY  := python3 -S

.DEFAULT_GOAL := verify

.PHONY: help validate strict conformance build checksums verify ci clean

help:                ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

validate:            ## Run the package's own bundled validator
	$(PY) $(PKG)/validate_release.py $(PKG)

strict:              ## Run the strict superset validator
	$(PY) tools/validate_strict.py $(PKG)

conformance:         ## Run the conformance test runner
	$(PY) tools/conformance_runner.py $(PKG)

build:               ## Regenerate the machine/AI artifact layer in dist/
	$(PY) tools/build_artifacts.py $(PKG)

checksums:           ## Verify bundled SHA-256 integrity
	cd $(PKG) && sha256sum -c SHA256SUMS.txt >/dev/null && echo "SHA256SUMS OK"

verify: validate strict conformance checksums build ## Full local verification
	@git diff --quiet -- dist 2>/dev/null && echo "dist/ artifacts are up to date" || \
	  { echo "NOTE: dist/ changed after build (commit the regenerated artifacts)"; }
	@echo "ALL CHECKS PASSED"

ci: validate strict conformance checksums ## CI gate (asserts artifact freshness separately)
	$(PY) tools/build_artifacts.py $(PKG)
	@git diff --exit-code -- dist || \
	  { echo "ERROR: dist/ is stale. Run 'make build' and commit."; exit 1; }
	@echo "CI CHECKS PASSED"

clean:               ## Remove generated artifacts
	rm -f dist/*.mmd dist/*.dot dist/*.svg dist/*.bundle.json dist/ai-manifest.json \
	      dist/AGENT_GUIDE.md dist/conformance-report.json
