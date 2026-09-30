# Review methodology and limits

## Scope

All 120 sibling repositories were inventoried by tracked file list, commit, origin, and initial working-tree status. Review combined package build/interface/operational assessment, automated static analysis, and manual control-flow checks of candidate defects. This was a broad, bounded review, not a line-by-line audit of every file.

All findings in the issue register have a concrete trigger, impact, source location, recommended correction, and acceptance criteria. Potential diagnostics without sufficient evidence were not presented as confirmed bugs. A package with no filed issue means no actionable defect was confirmed within this review's coverage.

## Tools and evidence

- Cppcheck 2.22.0: C/C++ translation units, warning/performance checks, normal check level, concurrent analysis. No complete compile database or installed DAQ dependencies were available, so configuration-sensitive results needed manual validation.
- ShellCheck: error-level inspection of 1,017 `.sh` scripts excluding csh shebangs. Shell parsing was additionally checked with `bash -n` for reported syntax defects. Source-only scripts without a shebang are not automatically defects.
- Pyflakes: selected Python source parsed directly, or translated from Python 2 syntax **in memory** with Fissix for analysis. No production Python files were rewritten. Python 2/3 compatibility warnings alone were not reported as product bugs.
- Manual inspection: iterator lifetime, buffer sizes and units, file/checkpoint persistence, typed message framing, recovery branches, hardware-command argument validation, and source/build/configuration relationships.
- Exact tool input lists and raw diagnostics are retained in `data/static-analysis.json`; package counts are summarized in [coverage](coverage.md). Raw analyzer severities are not the human-ranked issue severities.

Python parsing failures are retained separately. Embedded EPICS/Jython scripts can receive names such as `widget`, `display`, and `pvArray` from their host; undefined-name warnings for such injected globals were not blindly filed. C/C++ macro and platform errors may reflect the incomplete target environment.

## Large trees and exclusions

| Package/content | Coverage boundary |
| --- | --- |
| linux_kernel_dcmtdu | Historical kernel integration, build/version, selected PowerPC board/device-tree surfaces; no exhaustive upstream kernel audit |
| DCMBootLoader | NOvA `novadcm` board code and build/configuration instructions; the full eCos distribution was not manually audited |
| DDSSimD | Implementation/build surfaces; generated HTML/LaTeX reference output was not reviewed page by page |
| DCMulator | Own USB/test-stand code and configuration; bundled libusb and existing local MATLAB edits are distinguished |
| FEBCheckoutVerify | NOvA-facing integration and selected scripts; bundled imaging/XML/document/spreadsheet libraries are not claimed as completely audited |
| NovaFirmware | Image/artifact inventory and operational selection concerns; binary firmware cannot establish RTL correctness |
| dcm_linux_system archives | Reconstruction inputs and patch/document inventory; compressed upstream source was not expanded into a new full audit |
| Generated UI/resources and deliberate negative tests | Not treated as production defects without a reachable operational path |

Some automated inputs include vendor/test files; that does not expand the manual coverage boundary. Original local changes in DCMulator, DDSSimD, NovaControlRoom, and linux_kernel_dcmtdu were preserved.

## Rejected examples

- A bootloader LCD loop stops reading after a null character; an analyzer's out-of-bounds candidate did not establish a reachable defect for the supplied terminated strings.
- TDU register diagnostics contain a sentinel in the constant address array; the nominal loop bound alone did not establish an out-of-bounds access.
- Uninitialized `ver`/`ctrl` references following an unconditional return in the TDU work function are unreachable in the reviewed code.
- Repeated `errorString.length()` conditions in configuration error aggregation may be redundant but do not establish a functional failure.
- A deliberately invalid-pointer test in BufferNodeEVB is a negative test, not an acquisition-path finding.

## Validation limits

No live detector command, database mutation, firmware flash, module load, email action, or DAQ process startup was performed. Native DAQ builds and system/hardware integration tests were not run because the required release/toolchain/runtime environment was not established on this macOS host. Issue acceptance cases are proposed future checks unless explicitly identified as executed.

The documentation itself is built with strict MkDocs validation and checked for internal links, package completeness, dependency endpoints/evidence, finding IDs, issue URLs, and source-location bounds. The issue publisher deduplicates by stable review marker and stores each result immediately after creation.

## Severity and scheduling

Severity describes the demonstrated potential impact under the stated trigger. It is separate from current exposure or production urgency. No P0 finding was established. Confirm actual deployment and ownership before prioritizing legacy or test-stand packages; record that decision in GitHub. Rough effort S/M/L describes implementation scope rather than elapsed time.
