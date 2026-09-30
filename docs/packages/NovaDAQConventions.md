# NovaDAQConventions

Shared detector/subdetector identifiers, run types, and string conversion conventions.

## Identity and scope

Repository: [NovaDAQ/NovaDAQConventions](https://github.com/NovaDAQ/NovaDAQConventions) · Reviewed commit: `a0e5f7ab5d2c523698bb25346ab08cac5532a973` · Domain: **Core libraries**.

Tracked files: **7**. Production deployment and owner are **unconfirmed**.

## Operation

Treat enum values and canonical names as compatibility-sensitive across messages, configuration, and metadata. Unknown values should remain distinguishable from valid detector selections.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/cxx/include/CMakeLists.txt) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/DAQConventions.h](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/cxx/include/DAQConventions.h) | `DetId`, `DetInfo`, `RunInfo`, `RunType`, `SubDetId`, `SubDetInfo` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaDAQConventions/blob/a0e5f7ab5d2c523698bb25346ab08cac5532a973/GNUmakefile#L10) |


Direct consumers: [DAQChannelMap](DAQChannelMap.md), [DAQMessagesZMQ](DAQMessagesZMQ.md), [DatabaseUtils](DatabaseUtils.md), [DetectorPlotter](DetectorPlotter.md), [NDLTest](NDLTest.md), [NovaDAQCheckout](NovaDAQCheckout.md), [NovaDataLogger](NovaDataLogger.md), [NovaDatabase](NovaDatabase.md), [NovaResourceManager](NovaResourceManager.md), [NovaRunControl](NovaRunControl.md), [NovaSuperNova](NovaSuperNova.md), [PedestalDataRunner](PedestalDataRunner.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
