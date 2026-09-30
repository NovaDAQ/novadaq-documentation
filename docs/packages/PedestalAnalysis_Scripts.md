# PedestalAnalysis_Scripts

ROOT/C++ pedestal, DSO, FFT, and plotting macros and orchestration scripts.

## Identity and scope

Repository: [NovaDAQ/PedestalAnalysis_Scripts](https://github.com/NovaDAQ/PedestalAnalysis_Scripts) · Reviewed commit: `b3fc11787f0cbc99ae0be1a0030706d744abe36a` · Domain: **Analysis**.

Tracked files: **47**. Production deployment and owner are **unconfirmed**.

## Operation

Record raw input, channel/scan selection, calibration settings, and output directory. Verify macros compile/load with the intended ROOT version and compare plots with a known reference before deriving thresholds.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [runDsoScripts.sh](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/runDsoScripts.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [CanvasManager.h](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/CanvasManager.h) | `CanvasManager` |
| [PedestalAnalizer.h](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/PedestalAnalizer.h) | `PedestalAnalizer` |
| [PedestalUtilities.h](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/PedestalUtilities.h) | `PedestalUtilities` |
| [version.h](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `HOSTNAME` | [PedestalUtilities.cpp:36](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/PedestalUtilities.cpp#L36) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [PedestalUtilities.cpp:15](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/PedestalUtilities.cpp#L15) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **28 C/C++ translation units**, **1 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P3 | [NDAQ-039: Check the first-scan guard before reading previous channel state](../review/issues/NDAQ-039.md) | [Issue](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/README) |
