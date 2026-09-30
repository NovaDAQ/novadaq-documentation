# EventDispatcher_Server

Standalone event-dispatch server with shared-memory inspection, dispatch threads, GUI, and pattern-source utility.

## Identity and scope

Repository: [NovaDAQ/EventDispatcher_Server](https://github.com/NovaDAQ/EventDispatcher_Server) · Reviewed commit: `5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2` · Domain: **Data path**.

Tracked files: **54**. Production deployment and owner are **unconfirmed**.

## Operation

Check the shared-memory segment identity, producer activity, listener port, and expected event format. Monitor dispatch threads and consumer connections. Use test patterns only on a dedicated segment/partition.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/GNUmakefile) |
| [cxx/src/EventDispatcher.pro](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/EventDispatcher.pro) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/GNUmakefile) |
| [cxx/src/unused/PatternGenerator.pro](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/PatternGenerator.pro) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/EventDispatcher.cc](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/EventDispatcher.cc) |
| [cxx/src/PatternFromSHM.cc](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/PatternFromSHM.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/AboutDialog.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/AboutDialog.h) | `AboutDialog` |
| [cxx/include/DataExamineThread.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DataExamineThread.h) | `DataExamineThread`, `Parameters` |
| [cxx/include/DispatchServer.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DispatchServer.h) | `DispatchServer` |
| [cxx/include/DispatchThread.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DispatchThread.h) | `DispatchThread`, `DispatcherBookKeeping` |
| [cxx/include/GraphicalDispatcher.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/GraphicalDispatcher.h) | `GraphicalDispatcher` |
| [cxx/include/MemorySettingsDialog.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/MemorySettingsDialog.h) | `MemorySettingsDialog` |
| [cxx/include/NetworkSettingsDialog.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/NetworkSettingsDialog.h) | `NetworkSettingsDialog` |
| [cxx/include/SHMSegment_Struct.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/SHMSegment_Struct.h) | `SHMSegment` |
| [cxx/include/SettingsDialog.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/SettingsDialog.h) | `SettingsDialog` |
| [cxx/include/cvstags.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/cvstags.h) | Functions, constants, or templates |
| [cxx/include/daemon_init.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/daemon_init.h) | Functions, constants, or templates |
| [cxx/include/version.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/version.h) | Functions, constants, or templates |
| [cxx/src/unused/DataSegment.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/DataSegment.h) | `nova_data`, `nova_data_header`, `nova_segment_header`, `segmentIdent` |
| [cxx/src/unused/DataSendThread.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/DataSendThread.h) | `DataSendThread` |
| [cxx/src/unused/MemoryModel.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/MemoryModel.h) | `MemoryModel` |
| [cxx/src/unused/PatternGenerator.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/PatternGenerator.h) | `PatternGenerator` |
| [cxx/src/unused/nova_datasegment.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/nova_datasegment.h) | `nova_data_header`, `nova_data_tail`, `nova_segment_header`, `segmentIdent` |
| [cxx/src/unused/testpattern.h](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/unused/testpattern.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/include/DataExamineThread.h:4](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DataExamineThread.h#L4) |
| `QtGui` | [cxx/include/AboutDialog.h:4](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/AboutDialog.h#L4) |
| `QtNetwork` | [cxx/include/DispatchServer.h:4](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DispatchServer.h#L4) |
| `sys` | [cxx/src/DispatchServer.cpp:10](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/DispatchServer.cpp#L10) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["EventDispatcher_CommandSet"]
  p2["EventDispatcher_Server"]
  p3["PackageVersion"]
  p2 --> p0
  p2 --> p1
  p2 --> p3
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [cxx/src/EventDispatcher.pro:19](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/EventDispatcher.pro#L19) |
| [DAQDataFormats](DAQDataFormats.md) | source include | [cxx/src/DataExamineThread.cpp:4](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/DataExamineThread.cpp#L4) |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | build link | [cxx/src/GNUmakefile:39](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/GNUmakefile#L39) |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | source include | [cxx/include/DispatchThread.h:7](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/DispatchThread.h#L7) |
| [PackageVersion](PackageVersion.md) | build link | [cxx/src/GNUmakefile:39](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/GNUmakefile#L39) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/include/version.h:28](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/include/version.h#L28) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **12 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [cxx/src/README](https://github.com/NovaDAQ/EventDispatcher_Server/blob/5a77e6af0491d9a6bdbe38d49bda9d6a2070dce2/cxx/src/README) |
