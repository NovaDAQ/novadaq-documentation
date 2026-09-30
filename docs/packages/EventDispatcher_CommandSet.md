# EventDispatcher_CommandSet

Command and acknowledgement definitions shared by event-dispatcher components.

## Identity and scope

Repository: [NovaDAQ/EventDispatcher_CommandSet](https://github.com/NovaDAQ/EventDispatcher_CommandSet) · Reviewed commit: `684c4a333c05cef5334c95e3199019c3246cb39b` · Domain: **Messaging**.

Tracked files: **18**. Production deployment and owner are **unconfirmed**.

## Operation

Treat command identifiers, payload shapes, and acknowledgement semantics as a wire contract. Rebuild and test server/client pairs together when changing this package; it has no independent daemon.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/DispatcherAck.h](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/include/DispatcherAck.h) | `DispatcherACK`, `DispatcherResponses` |
| [cxx/include/DispatcherCmd.h](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/include/DispatcherCmd.h) | `DispatcherCMD`, `DispatcherCommandDefaults`, `DispatcherCommands`, `DspCmd`, `MagicNumbers` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [cxx/include/DispatcherAck.h:4](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/cxx/include/DispatcherAck.h#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/EventDispatcher_CommandSet/blob/684c4a333c05cef5334c95e3199019c3246cb39b/GNUmakefile#L10) |


Direct consumers: [EventDispatcher_Client](EventDispatcher_Client.md), [EventDispatcher_Server](EventDispatcher_Server.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **2 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
