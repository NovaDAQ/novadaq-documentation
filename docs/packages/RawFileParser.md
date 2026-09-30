# RawFileParser

Memory-mapped and file-I/O reader/indexer for NOvA run and event files.

## Identity and scope

Repository: [NovaDAQ/RawFileParser](https://github.com/NovaDAQ/RawFileParser) · Reviewed commit: `c23da44c4ae2b7770204218a91eacf1b46db1da7` · Domain: **Core libraries**.

Tracked files: **16**. Production deployment and owner are **unconfirmed**.

## Operation

Open immutable completed files or controlled copies. Validate malformed markers, truncated records, event indices, and end-of-file progress; every search must terminate. It is a shared dependency of metadata and inspection tools.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/RawFileParser.h](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/include/RawFileParser.h) | `EVENT_INDEX_STATE`, `NOVA_FILE_DELIMITERS`, `NOVA_FILE_TYPES`, `RawConfigurationBlock`, `RawEvent`, `RawFileParser`, `RawRunHeader` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [cxx/include/RawFileParser.h:9](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/include/RawFileParser.h#L9) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["RawFileParser"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [cxx/src/CMakeLists.txt:10](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/CMakeLists.txt#L10) |
| [DAQDataFormats](DAQDataFormats.md) | source include | [cxx/src/RawFileParser.cpp:14](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/RawFileParser.cpp#L14) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/GNUmakefile#L10) |


Direct consumers: [DAQHit.old](DAQHit.old.md), [EventDump](EventDump.md), [MetaDataTools](MetaDataTools.md), [RunSummaryUtils](RunSummaryUtils.md), [SHM_Utilities](SHM_Utilities.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **1 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-019: Advance past rejected header candidates during marker searches](../review/issues/NDAQ-019.md) | [Issue](https://github.com/NovaDAQ/RawFileParser/issues/1) |
| P2 | [NDAQ-020: Check open failure with a negative descriptor test](../review/issues/NDAQ-020.md) | [Issue](https://github.com/NovaDAQ/RawFileParser/issues/2) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
