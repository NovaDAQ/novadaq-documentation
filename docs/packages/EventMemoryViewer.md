# EventMemoryViewer

Qt tools for viewing event content from shared memory.

## Identity and scope

Repository: [NovaDAQ/EventMemoryViewer](https://github.com/NovaDAQ/EventMemoryViewer) · Reviewed commit: `3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b` · Domain: **Analysis**.

Tracked files: **33**. Production deployment and owner are **unconfirmed**.

## Operation

Attach to the intended segment and verify source freshness before interpreting the display. Match record layout to the producer; visual inspection does not replace event consistency checks.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/GNUmakefile) |
| [cxx/src/EventMemoryViewer.pro](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryViewer.pro) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/GNUmakefile) |
| [cxx/src/Makefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/Makefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/EventMemoryView.cc](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryView.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/src/AboutDialog.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/AboutDialog.h) | `AboutDialog` |
| [cxx/src/EventMemoryViewer.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryViewer.h) | `EventMemoryViewer` |
| [cxx/src/MemoryModel.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/MemoryModel.h) | `EventPosition`, `MemoryModel` |
| [cxx/src/MemoryViewer.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/MemoryViewer.h) | `MemoryViewer` |
| [cxx/src/daemon_init.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/daemon_init.h) | Functions, constants, or templates |
| [cxx/src/old/DataSegment.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/old/DataSegment.h) | `nova_data`, `nova_data_header`, `nova_segment_header`, `segmentIdent` |
| [cxx/src/old/nova_datasegment.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/old/nova_datasegment.h) | `nova_data_header`, `nova_data_tail`, `nova_segment_header`, `segmentIdent` |
| [cxx/src/old/testpattern.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/old/testpattern.h) | Functions, constants, or templates |
| [cxx/src/version.h](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/src/EventMemoryViewer.cpp:16](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryViewer.cpp#L16) |
| `QtGui` | [cxx/src/AboutDialog.h:4](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/AboutDialog.h#L4) |
| `sys` | [cxx/src/EventMemoryView.cc:7](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryView.cc#L7) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["EventMemoryViewer"]
  p2["PackageVersion"]
  p1 --> p0
  p1 --> p2
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [cxx/src/EventMemoryViewer.pro:12](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/EventMemoryViewer.pro#L12) |
| [PackageVersion](PackageVersion.md) | build link | [cxx/src/GNUmakefile:39](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/GNUmakefile#L39) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/src/version.h:28](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/cxx/src/version.h#L28) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/EventMemoryViewer/blob/3a09ebcd5586afb9c3a80aa000a7c4bc4de2c24b/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **6 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
