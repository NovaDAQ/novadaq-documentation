# PackageVersion

Parses embedded package revision information and exposes version helper functions/macros.

## Identity and scope

Repository: [NovaDAQ/PackageVersion](https://github.com/NovaDAQ/PackageVersion) · Reviewed commit: `969cbf9703296f91620e7b6010fe1d7ff544c292` · Domain: **Core libraries**.

Tracked files: **19**. Production deployment and owner are **unconfirmed**.

## Operation

CVS-derived version strings are historical metadata. Record Git commit IDs alongside reported versions for reproducibility; verify malformed and missing revision handling before using values for compatibility decisions.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/PackageVersionTest.cc](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/src/PackageVersionTest.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/PackageVersion.h](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/include/PackageVersion.h) | Functions, constants, or templates |
| [cxx/include/version.h](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/cxx/include/version.h) | Functions, constants, or templates |


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
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:17](https://github.com/NovaDAQ/PackageVersion/blob/969cbf9703296f91620e7b6010fe1d7ff544c292/GNUmakefile#L17) |


Direct consumers: [ChannelDecoder](ChannelDecoder.md), [DAQDataFormats](DAQDataFormats.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMGuiTools](DCMGuiTools.md), [EventDispatcher_Server](EventDispatcher_Server.md), [EventDispatcher_Server_FMWK](EventDispatcher_Server_FMWK.md), [EventMemoryViewer](EventMemoryViewer.md), [FEBCheckoutVerify](FEBCheckoutVerify.md), [NovaDAQCheckout](NovaDAQCheckout.md), [NovaDAQCrontab](NovaDAQCrontab.md), [NovaRunControl](NovaRunControl.md), [PedestalDataRunner](PedestalDataRunner.md), [PixelMaskTool](PixelMaskTool.md), [SHM_Utilities](SHM_Utilities.md), [SRT_ONLINE](SRT_ONLINE.md), [TDUControl](TDUControl.md), [TriggerScalars](TriggerScalars.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **3 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
