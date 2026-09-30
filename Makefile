PYTHON ?= .venv/bin/python
MKDOCS ?= .venv/bin/mkdocs

.PHONY: build check serve generate
build: check
	$(MKDOCS) build --strict
check:
	$(PYTHON) scripts/validate.py
serve:
	$(MKDOCS) serve -a 127.0.0.1:8000
generate:
	$(PYTHON) scripts/publish_issues.py
	$(PYTHON) scripts/generate.py --workspace ..
