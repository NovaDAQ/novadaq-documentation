# EventDispatcher_Client

Packaged Qt event-dispatcher client and resources.

## Identity and scope

Repository: [NovaDAQ/EventDispatcher_Client](https://github.com/NovaDAQ/EventDispatcher_Client) · Reviewed commit: `06d5fd12d6a782b3f7cd377a321a3886b6a369b5` · Domain: **Data path**.

Tracked files: **27**. Production deployment and owner are **unconfirmed**.

## Operation

Set the target host/port and expected event format, then verify reception with a known event. Use GUI connection/error status to distinguish server unavailability from malformed data.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/GNUmakefile) |
| [cxx/src/DispatcherClient.pro](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/DispatcherClient.pro) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/GNUmakefile) |
| [cxx/src/Makefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/Makefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/EventDispatcher_Client.cc](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/EventDispatcher_Client.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/AboutDialog.h](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/include/AboutDialog.h) | `AboutDialog` |
| [cxx/include/DispatcherClient.h](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/include/DispatcherClient.h) | `DispatcherClient` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `..` | [cxx/src/DispatcherClient-moc.cpp:10](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/DispatcherClient-moc.cpp#L10) |
| `QtCore` | [cxx/src/qrc_DispatcherClient.cpp:10](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/qrc_DispatcherClient.cpp#L10) |
| `QtGui` | [cxx/include/AboutDialog.h:4](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/include/AboutDialog.h#L4) |
| `QtNetwork` | [cxx/include/DispatcherClient.h:6](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/include/DispatcherClient.h#L6) |
| `sys` | [cxx/src/EventDispatcher_Client.cc:7](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/EventDispatcher_Client.cc#L7) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["EventDispatcher_Client"]
  p1["EventDispatcher_CommandSet"]
  p0 --> p1
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/src/GNUmakefile#L36) |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | source include | [cxx/include/DispatcherClient.h:11](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/cxx/include/DispatcherClient.h#L11) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/EventDispatcher_Client/blob/06d5fd12d6a782b3f7cd377a321a3886b6a369b5/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **3 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
