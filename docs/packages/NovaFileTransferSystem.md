# NovaFileTransferSystem

Earlier shell-based file discovery, copying, bundling, metadata, and transfer orchestration.

## Identity and scope

Repository: [NovaDAQ/NovaFileTransferSystem](https://github.com/NovaDAQ/NovaFileTransferSystem) · Reviewed commit: `50fa25c0b329e180a3b7714d0a9c8645fff16e4d` · Domain: **Storage and metadata**.

Tracked files: **29**. Production deployment and owner are **unconfirmed**.

## Operation

Review absolute source/destination paths and completion-marker semantics before reuse. Validate on temporary files; never equate a marker file or successful final echo with verified durable transfer.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/java/unittest/GNUmakefile) |
| [scripts/GNUmakefile](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [scripts/BundleFiles.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/BundleFiles.sh) |
| [scripts/CreateMetadata.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/CreateMetadata.sh) |
| [scripts/FindAndCopy.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/FindAndCopy.sh) |
| [scripts/FixDates.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/FixDates.sh) |
| [scripts/RunMetrics.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/RunMetrics.sh) |
| [scripts/SetInitialEnv.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/SetInitialEnv.sh) |
| [scripts/SetMessageLogger.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/SetMessageLogger.sh) |
| [scripts/SetNovaEnv.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/SetNovaEnv.sh) |
| [scripts/SetServers.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/SetServers.sh) |
| [scripts/TransferData.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/TransferData.sh) |
| [scripts/daqlogs.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/daqlogs.sh) |
| [scripts/datalink.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/datalink.sh) |
| [scripts/fts.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/fts.sh) |
| [scripts/runFTS.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/runFTS.sh) |
| [scripts/set_ups.sh](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/set_ups.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/test/Metadata_dump.cc:12](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/Metadata_dump.cc#L12) |
| `sys` | [cxx/test/FTSReadRun.cc:7](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/FTSReadRun.cc#L7) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | test include | [cxx/test/FTSReadRun.cc:8](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/FTSReadRun.cc#L8) |
| [DAQDataFormats](DAQDataFormats.md) | test link | [cxx/test/GNUmakefile:26](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/GNUmakefile#L26) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **3 C/C++ translation units**, **15 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P2 | [NDAQ-030: Repair the incomplete data-link loop so the script parses](../review/issues/NDAQ-030.md) | [Issue](https://github.com/NovaDAQ/NovaFileTransferSystem/issues/1) |


Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/FTSReadRun.cc](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/FTSReadRun.cc) |
| [cxx/test/Metadata_dump.cc](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/Metadata_dump.cc) |
| [cxx/test/RunDuration.cc](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/cxx/test/RunDuration.cc) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
