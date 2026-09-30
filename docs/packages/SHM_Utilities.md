# SHM_Utilities

Utilities copying files/patterns to shared memory, dumping memory, and inspecting spill history.

## Identity and scope

Repository: [NovaDAQ/SHM_Utilities](https://github.com/NovaDAQ/SHM_Utilities) · Reviewed commit: `06c491c98130fde4cb46d5f860eb5c991a4f6f2f` · Domain: **Data path**.

Tracked files: **19**. Production deployment and owner are **unconfirmed**.

## Operation

Verify segment key, size, writer ownership, and record layout before access. FileToSHM/PatternToSHM are writers and belong on isolated segments for tests. Use dump/spy tools for inspection without replacing a live producer.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/DumpSpillHistory.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/DumpSpillHistory.cc) |
| [cxx/src/EventFileToSHM.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/EventFileToSHM.cc) |
| [cxx/src/FileToSHM.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/FileToSHM.cc) |
| [cxx/src/PatternToSHM.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/PatternToSHM.cc) |
| [cxx/src/SHMDump.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/SHMDump.cc) |
| [cxx/src/SHMToFile.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/SHMToFile.cc) |
| [cxx/src/SpySpillHistory.cc](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/SpySpillHistory.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/version.h](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/include/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `NOVADAQ_ENVIRONMENT` | [cxx/src/DumpSpillHistory.cc:96](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/DumpSpillHistory.cc#L96) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [cxx/src/DumpSpillHistory.cc:2](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/DumpSpillHistory.cc#L2) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["NovaSpillServer"]
  p2["NovaTimingUtilities"]
  p3["PackageVersion"]
  p4["RawFileParser"]
  p5["SHM_Utilities"]
  p5 --> p0
  p5 --> p1
  p5 --> p2
  p5 --> p3
  p5 --> p4
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [cxx/src/GNUmakefile:18](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/GNUmakefile#L18) |
| [DAQDataFormats](DAQDataFormats.md) | source include | [cxx/src/EventFileToSHM.cc:39](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/EventFileToSHM.cc#L39) |
| [NovaSpillServer](NovaSpillServer.md) | source include | [cxx/src/DumpSpillHistory.cc:20](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/DumpSpillHistory.cc#L20) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | build link | [cxx/src/GNUmakefile:18](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/GNUmakefile#L18) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | source include | [cxx/src/DumpSpillHistory.cc:14](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/DumpSpillHistory.cc#L14) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/include/version.h:28](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/include/version.h#L28) |
| [RawFileParser](RawFileParser.md) | build link | [cxx/src/GNUmakefile:18](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/GNUmakefile#L18) |
| [RawFileParser](RawFileParser.md) | source include | [cxx/src/EventFileToSHM.cc:45](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/cxx/src/EventFileToSHM.cc#L45) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/SHM_Utilities/blob/06c491c98130fde4cb46d5f860eb5c991a4f6f2f/GNUmakefile#L10) |


Direct consumers: [TDUWeb](TDUWeb.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **7 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
