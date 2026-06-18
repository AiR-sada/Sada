# Purpose Root v6 — reproducibility entry points.
# Usage: make <target>

PYTHON ?= python3

.DEFAULT_GOAL := help
.PHONY: help install install-dev test validate canonical releases score all clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install runtime dependencies (jsonschema)
	$(PYTHON) -m pip install -r requirements.txt

install-dev: ## Install runtime + test dependencies (jsonschema, pytest)
	$(PYTHON) -m pip install -r requirements-dev.txt

test: ## Run the full pytest suite
	$(PYTHON) -m pytest

canonical: ## Verify CANONICAL_ROOT_v6 doctrine SHA256 commitments
	$(PYTHON) tools/verify_canonical.py

releases: ## Verify current release manifests + SHA256SUMS
	$(PYTHON) tools/verify_releases.py

validate: ## Run the package's own release self-check
	$(PYTHON) validate_release.py

score: ## Score the canonical Accept example (robust scorer)
	$(PYTHON) tools/score_robust.py examples/sample_accept_A3_monitored_v6.json

all: ## Run every reproducibility gate (CI entry point)
	$(PYTHON) tools/run_all.py

clean: ## Remove Python build caches
	find . -depth -type d -name '__pycache__' -exec rm -rf {} +
	find . -depth -type d -name '.pytest_cache' -exec rm -rf {} +
