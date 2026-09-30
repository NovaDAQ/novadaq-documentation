# ExternalPackageTest

Small checks demonstrating integration of external libraries such as Boost, CppUnit, and Xerces.

## Identity and scope

Repository: [NovaDAQ/ExternalPackageTest](https://github.com/NovaDAQ/ExternalPackageTest) · Reviewed commit: `60a498f2baf645b3a5571a17501ac3bf88519068` · Domain: **Simulation and examples**.

Tracked files: **31**. Production deployment and owner are **unconfirmed**.

## Operation

Build in the intended release environment to diagnose toolchain or external dependency failures. Passing these tests establishes basic linkage/use, not DAQ system readiness.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/Ept.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/Ept.h) | Functions, constants, or templates |
| [cxx/include/EptBoostFileSystem.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/EptBoostFileSystem.h) | `EptBoostFileSystem` |
| [cxx/include/EptBoostThread.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/EptBoostThread.h) | `EptBoostThread` |
| [cxx/include/EptCppUnit.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/EptCppUnit.h) | `EptCppUnit` |
| [cxx/include/EptXercesc.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/EptXercesc.h) | `EptXercesc` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/EptXercescConfiguration.xsd](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/config/EptXercescConfiguration.xsd) |
| [config/EptXercescTestConfiguration.xml](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/config/EptXercescTestConfiguration.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `SRT_PRIVATE_CONTEXT` | [cxx/src/Ept.cpp:35](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/Ept.cpp#L35) |
| `SRT_PUBLIC_CONTEXT` | [cxx/src/Ept.cpp:39](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/Ept.cpp#L39) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/src/EptBoostFileSystem.cpp:1](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/EptBoostFileSystem.cpp#L1) |
| `cppunit` | [cxx/unittest/EptBoostFileSystemTest.h:4](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptBoostFileSystemTest.h#L4) |
| `messagefacility` | [cxx/src/Ept.cpp:7](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/Ept.cpp#L7) |
| `sys` | [cxx/src/Ept.cpp:5](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/src/Ept.cpp#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["ExternalPackageTest"]
  p1["NovaDAQUtilities"]
  p0 --> p1
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | source include | [cxx/include/EptBoostThread.h:4](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/include/EptBoostThread.h#L4) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test include | [cxx/unittest/eptunittest.cc:13](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/eptunittest.cc#L13) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test link | [cxx/unittest/GNUmakefile:19](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/GNUmakefile#L19) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **11 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/eptendian.cc](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/test/eptendian.cc) |
| [cxx/unittest/EptBoostFileSystemTest.cpp](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptBoostFileSystemTest.cpp) |
| [cxx/unittest/EptBoostFileSystemTest.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptBoostFileSystemTest.h) |
| [cxx/unittest/EptBoostThreadTest.cpp](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptBoostThreadTest.cpp) |
| [cxx/unittest/EptBoostThreadTest.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptBoostThreadTest.h) |
| [cxx/unittest/EptCppUnitTest.cpp](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptCppUnitTest.cpp) |
| [cxx/unittest/EptCppUnitTest.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptCppUnitTest.h) |
| [cxx/unittest/EptXercescTest.cpp](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptXercescTest.cpp) |
| [cxx/unittest/EptXercescTest.h](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/EptXercescTest.h) |
| [cxx/unittest/eptunittest.cc](https://github.com/NovaDAQ/ExternalPackageTest/blob/60a498f2baf645b3a5571a17501ac3bf88519068/cxx/unittest/eptunittest.cc) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
