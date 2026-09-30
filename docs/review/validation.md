# Validation record

Snapshot and checks dated **2026-09-30**.

## Source review evidence

| Check | Result |
| --- | --- |
| Repository inventory | 120 original repositories, revision and initial working-tree state recorded |
| Cppcheck inputs | 1,438 translation units: 1,387 `.c/.cc/.cpp` inputs plus 51 `.cxx/.C` inputs analyzed as C++ |
| ShellCheck inputs | 1,017 shell scripts at error level |
| Python static analysis | 159 parsed files; 17 parsing failures retained in the evidence |
| Manual triage | 40 confirmed findings filed in 30 owning GitHub repositories |
| Issue severity | 0 critical, 15 high, 22 medium, 3 low |
| Source preservation | All 120 working-tree status records match the initial inventory; finding evidence files match their pinned revisions |

Static analysis is incomplete without the original target build environment. The Cppcheck evidence includes 30 syntax-error diagnostics and one analyzer internal error; these are limitations or triage inputs, not a count of confirmed product defects. See the [methodology](methodology.md) and [package coverage](coverage.md).

## Documentation checks executed

- `python scripts/validate.py --workspace ..` passed: 120 package pages, 40 finding records with matching GitHub URLs, 849 typed dependency relationships, local Markdown links, source revision and line-bound checks.
- `mkdocs build --strict` passed.
- `python scripts/test_site.py` passed in headless Chromium: home/catalog/priorities, all ranked issue links, finding detail link, 120-package explorer, optional relationship toggle, package selection, graph navigation, Mermaid rendering on architecture/dependency/operations/package pages, search, and a 390-pixel mobile viewport.
- Desktop and mobile screenshots were inspected. Browser captures are generated locally in ignored `artifacts/browser/`.
- GitHub issue states were refreshed and confirmed open when the snapshot was generated. The register is a snapshot; GitHub remains the authority for subsequent changes.

The browser test uses local static documentation and the diagram library CDN. It does not exercise any DAQ component. Full DAQ builds, hardware tests, production services, and the proposed issue acceptance tests were **not run**. Deployment status and ownership remain unconfirmed.

## Reproduce

See [maintaining this suite](../contributing.md) for dependencies, build commands, browser setup, and issue-status refresh. CI validates and builds the committed snapshot without needing the 120 source checkouts.
