# Maintaining this suite

## Build and read

From the `novadaq-documentation` repository:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/mkdocs build --strict
.venv/bin/mkdocs serve -a 127.0.0.1:8000
```

The generated site is in `site/`. Serve it over local HTTP to use the dependency explorer; browsers may block fetching local JSON from `file://` pages. Markdown pages remain directly readable on GitHub. Mermaid diagrams render through the viewer's Mermaid support; the interactive SVG explorer does not need a diagram CDN.

The MkDocs Material viewer loads Mermaid from unpkg.com, so its diagrams require network access. For repeatable browser checks, install the optional test dependencies and Chromium:

```sh
.venv/bin/pip install -r requirements-test.txt
.venv/bin/playwright install chromium
.venv/bin/python scripts/test_site.py
```

This check starts its own temporary HTTP server on loopback, exercises navigation, issue links, dependency filters, diagrams, search, and mobile layout, and writes screenshots to ignored `artifacts/browser/`. It does not start any DAQ software or contact detector services.

## Sources of truth

| File | Responsibility |
| --- | --- |
| `scripts/catalog_notes.py` | Curated package purpose, domain, and operating notes |
| `data/inventory.json` | Reviewed commits, tracked file inventory, initial local changes |
| `data/findings.json` | Verified findings, severity, source ranges, recommendations, acceptance cases, GitHub URL/state |
| `data/static-analysis.json` | Tool input lists, diagnostics, Python parsing failures |
| `scripts/generate.py` | Reproducible catalog, source/API/config inventory, dependency evidence, coverage, and ranked pages |
| `scripts/publish_issues.py` | Local issue drafts, deduplicated GitHub creation, status refresh |
| `docs/operations/`, `docs/architecture/index.md` | Curated system and operational procedures |

## Regenerate from sibling repositories

```sh
.venv/bin/python scripts/publish_issues.py
.venv/bin/python scripts/generate.py --workspace ..
.venv/bin/python scripts/validate.py --workspace ..
.venv/bin/mkdocs build --strict
```

The inventory is an intentional review snapshot. Before reviewing new revisions, capture a new inventory and static-analysis evidence; do not silently replace commit IDs while retaining old source ranges or claims. The generator requires source files matching the recorded commits for dependable pinned evidence. If a checkout differs, reconcile it deliberately and preserve existing work.

Package notes and operational pages require human review. Literal include/link extraction cannot resolve every macro, generated dependency, platform branch, shell invocation, or runtime service. Add explicit runtime edges only with source evidence and retain the edge type.

## GitHub issue workflow

Without `--apply`, the issue publisher only writes drafts. Authorized maintainers can create missing findings with:

```sh
python3 scripts/publish_issues.py --apply
```

It looks for the stable `novadaq-review:NDAQ-NNN` marker, including closed issues, and records the URL after each creation. It does not automatically reopen closed issues or assign users. To update the status snapshot:

```sh
python3 scripts/publish_issues.py --refresh
python3 scripts/generate.py --workspace ..
```

Existing issue content is not automatically overwritten. Correct inaccurate findings explicitly in GitHub and in `data/findings.json`, preserving the rationale and stable ID. Never publish an unvalidated analyzer diagnostic as a confirmed issue.

## CI and distribution

The included GitHub Actions workflow validates the committed documentation snapshot, builds the site strictly, and uploads an artifact. It does not publish GitHub Pages or change site visibility. Keep this suite within the same authorized audience as the private source repositories because it contains internal architecture and defect information.
