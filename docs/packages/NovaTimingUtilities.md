# NovaTimingUtilities

Converts UNIX, GPS-related, and NOvA clock representations and provides a conversion CLI.

## Identity and scope

Repository: [NovaDAQ/NovaTimingUtilities](https://github.com/NovaDAQ/NovaTimingUtilities) · Reviewed commit: `6f97c3fba53211f262755d3e5bf7abde275aecd5` · Domain: **Core libraries**.

Tracked files: **15**. Production deployment and owner are **unconfirmed**.

## Operation

Keep epoch, 64 MHz tick interpretation, fractional-second precision, and leap-second handling consistent across consumers. Include threshold-boundary and round-trip cases when changing conversions.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/NovaTimeConvert.cc](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/NovaTimeConvert.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/TimingUtilities.h](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/include/TimingUtilities.h) | `timespec`, `timeval`, `tm` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/src/NovaTimeConvert.cc:2](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/NovaTimeConvert.cc#L2) |
| `cppunit` | [cxx/unittest/TimingUtilitiesTests.cpp:1](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/unittest/TimingUtilitiesTests.cpp#L1) |
| `sys` | [cxx/include/TimingUtilities.h:5](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/include/TimingUtilities.h#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test include | [cxx/unittest/timeutilunittest.cc:1](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/unittest/timeutilunittest.cc#L1) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/GNUmakefile#L10) |


Direct consumers: [BufferNodeEVB](BufferNodeEVB.md), [DAQHit.old](DAQHit.old.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMApplication](DCMApplication.md), [DCM_ProgUtils](DCM_ProgUtils.md), [ErrorHandler](ErrorHandler.md), [EventDump](EventDump.md), [MetaDataTools](MetaDataTools.md), [NovaDAQMonitor](NovaDAQMonitor.md), [NovaGlobalTrigger](NovaGlobalTrigger.md), [NovaRunControl](NovaRunControl.md), [NovaSNEWSInterface](NovaSNEWSInterface.md), [NovaSpillServer](NovaSpillServer.md), [NovaSuperNova](NovaSuperNova.md), [RunSummaryUtils](RunSummaryUtils.md), [SHM_Utilities](SHM_Utilities.md), [ShmRdWr](ShmRdWr.md), [TDUControl](TDUControl.md), [TDUUtilities](TDUUtilities.md), [TriggerScalars](TriggerScalars.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **4 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P2 | [NDAQ-032: Compare leap-second thresholds against the original UNIX time](../review/issues/NDAQ-032.md) | [Issue](https://github.com/NovaDAQ/NovaTimingUtilities/issues/1) |


Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/unittest/TimingUtilitiesTests.cpp](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/unittest/TimingUtilitiesTests.cpp) |
| [cxx/unittest/timeutilunittest.cc](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/unittest/timeutilunittest.cc) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
