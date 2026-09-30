# NovaDAQUtilities

Shared process, cache, environment, location, partition, XML, time, and shared-memory conventions/utilities.

## Identity and scope

Repository: [NovaDAQ/NovaDAQUtilities](https://github.com/NovaDAQ/NovaDAQUtilities) · Reviewed commit: `6639f70fa710d28a3acf346bb2dff570914bc113` · Domain: **Core libraries**.

Tracked files: **91**. Production deployment and owner are **unconfirmed**.

## Operation

Changes have wide downstream reach. Validate process termination/exit status, URL/path resolution, and configuration caching with isolated processes and temporary files. A library update should be tested in representative control and data-path consumers.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/java/unittest/GNUmakefile) |
| [script/GNUmakefile](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/script/GNUmakefile) |
| [tools/CMakeLists.txt](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/tools/CMakeLists.txt) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/include/CppUnitTestDriver.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CppUnitTestDriver.h) |
| [script/archive_links.sh](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/script/archive_links.sh) |
| [script/make_ops_tag.sh](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/script/make_ops_tag.sh) |
| [tools/tailorXsdGeneratedClassesForNova.pl](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/tools/tailorXsdGeneratedClassesForNova.pl) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/BackgroundProcess.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/BackgroundProcess.h) | `BackgroundProcess` |
| [cxx/include/Cache.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/Cache.h) | `Cache` |
| [cxx/include/CacheManager.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CacheManager.h) | `CacheManager` |
| [cxx/include/CachePolicy.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CachePolicy.h) | `CachePolicy` |
| [cxx/include/ConcurrentQueue.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/ConcurrentQueue.h) | `ConcurrentQueue`, `FailIfFull`, `KeepNewest`, `RejectNewest` |
| [cxx/include/CppUnitTestDriver.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CppUnitTestDriver.h) | Functions, constants, or templates |
| [cxx/include/EnvVarCache.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/EnvVarCache.h) | `EnvVarCache` |
| [cxx/include/HexUtils.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/HexUtils.h) | Functions, constants, or templates |
| [cxx/include/LocationUtils.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/LocationUtils.h) | `LocationUtils` |
| [cxx/include/PartitionNumber.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/PartitionNumber.h) | `PartitionNumber` |
| [cxx/include/ProcessUtils.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/ProcessUtils.h) | `ProcessUtils` |
| [cxx/include/Runnable.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/Runnable.h) | `Runnable` |
| [cxx/include/SHMConvention.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/SHMConvention.h) | `IDMASKS`, `IDSHIFTS`, `OFFLINE_FRAMEWORK`, `SHMConvention` |
| [cxx/include/Status.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/Status.h) | `Status` |
| [cxx/include/TimeUtils.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/TimeUtils.h) | Functions, constants, or templates |
| [cxx/include/TimedCachePolicy.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/TimedCachePolicy.h) | `TimedCachePolicy` |
| [cxx/include/XMLDeserializationRegistry.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/XMLDeserializationRegistry.h) | `XMLDeserializationRegistry` |
| [cxx/include/XMLSerializable.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/XMLSerializable.h) | `XMLSerializable` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `HOME` | [cxx/unittest/GeneralTests.cpp:168](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/GeneralTests.cpp#L168) |
| `HOSTNAME` | [cxx/unittest/GeneralTests.cpp:172](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/GeneralTests.cpp#L172) |
| `NOVADAQXML_DIR` | [cxx/src/LocationUtils.cpp:64](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/LocationUtils.cpp#L64) |
| `SRT_PRIVATE_CONTEXT` | [cxx/src/LocationUtils.cpp:42](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/LocationUtils.cpp#L42) |
| `SRT_PUBLIC_CONTEXT` | [cxx/src/LocationUtils.cpp:44](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/LocationUtils.cpp#L44) |
| `USER` | [cxx/unittest/GeneralTests.cpp:159](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/GeneralTests.cpp#L159) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/include/BackgroundProcess.h:6](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/BackgroundProcess.h#L6) |
| `cppunit` | [cxx/include/CppUnitTestDriver.h:7](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/CppUnitTestDriver.h#L7) |
| `sys` | [cxx/include/TimeUtils.h:4](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/include/TimeUtils.h#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["NovaDAQUtilities"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | source include | [cxx/src/SHMConvention.cpp:16](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/src/SHMConvention.cpp#L16) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:16](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/GNUmakefile#L16) |


Direct consumers: [DAQApplicationManager](DAQApplicationManager.md), [DAQOperationsTools](DAQOperationsTools.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMApplication](DCMApplication.md), [DDTManager](DDTManager.md), [DatabaseUtils](DatabaseUtils.md), [DetectorPlotter](DetectorPlotter.md), [EventBuilder](EventBuilder.md), [ExternalPackageTest](ExternalPackageTest.md), [NDLTest](NDLTest.md), [NOvABeam](NOvABeam.md), [NovaDAQCheckout](NovaDAQCheckout.md), [NovaDAQConfiguration](NovaDAQConfiguration.md), [NovaDAQCrontab](NovaDAQCrontab.md), [NovaDAQMonitor](NovaDAQMonitor.md), [NovaDAQMonitorClient](NovaDAQMonitorClient.md), [NovaDaqDcs](NovaDaqDcs.md), [NovaDataLogger](NovaDataLogger.md), [NovaDatabase](NovaDatabase.md), [NovaEventBuilder](NovaEventBuilder.md), [NovaEventBuilderClient](NovaEventBuilderClient.md), [NovaGlobalTrigger](NovaGlobalTrigger.md), [NovaResourceManager](NovaResourceManager.md), [NovaResoureManager](NovaResoureManager.md), [NovaRunControl](NovaRunControl.md), [NovaRunControlClient](NovaRunControlClient.md), [NovaSNEWSInterface](NovaSNEWSInterface.md), [NovaSpillServer](NovaSpillServer.md), [PedestalDataRunner](PedestalDataRunner.md), [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md), [SRT_ONLINE](SRT_ONLINE.md), [TDUControl](TDUControl.md), [TDUUtilities](TDUUtilities.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **27 C/C++ translation units**, **2 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/FindFileLocationTest.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/test/FindFileLocationTest.cc) |
| [cxx/test/SHMConventionTest.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/test/SHMConventionTest.cc) |
| [cxx/unittest/CacheTests.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/CacheTests.cpp) |
| [cxx/unittest/ConcurrentQueue_t.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/ConcurrentQueue_t.cpp) |
| [cxx/unittest/GeneralTests.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/GeneralTests.cpp) |
| [cxx/unittest/HexUtilTests.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/HexUtilTests.cpp) |
| [cxx/unittest/SampleCppUnitIndividualTest1.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitIndividualTest1.cc) |
| [cxx/unittest/SampleCppUnitIndividualTest2.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitIndividualTest2.cc) |
| [cxx/unittest/SampleCppUnitPackageMain.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitPackageMain.cc) |
| [cxx/unittest/SampleCppUnitPackageTest1.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitPackageTest1.cpp) |
| [cxx/unittest/SampleCppUnitPackageTest2.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitPackageTest2.cpp) |
| [cxx/unittest/SampleCppUnitPackageTest2.h](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/SampleCppUnitPackageTest2.h) |
| [cxx/unittest/StatusTests.cpp](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/StatusTests.cpp) |
| [cxx/unittest/daqutilunittest.cc](https://github.com/NovaDAQ/NovaDAQUtilities/blob/6639f70fa710d28a3acf346bb2dff570914bc113/cxx/unittest/daqutilunittest.cc) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
