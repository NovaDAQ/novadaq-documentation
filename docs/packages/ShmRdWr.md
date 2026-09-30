# ShmRdWr

Shared-memory ring transport with grouped readers, semaphores, overwrite tracking, and inspection utilities.

## Identity and scope

Repository: [NovaDAQ/ShmRdWr](https://github.com/NovaDAQ/ShmRdWr) · Reviewed commit: `b5fdeeed788b701ebc4b8a2a2603a2203eb41518` · Domain: **Data path**.

Tracked files: **26**. Production deployment and owner are **unconfirmed**.

## Operation

Match segment key/geometry and reader group IDs. Monitor overwrite counts and reader lag, and coordinate all owners before deleting or recreating a segment. Group-read semaphore behavior matters during stop/drain.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/ShmRdWrShow.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/ShmRdWrShow.cc) |
| [cxx/src/compat_reader.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/compat_reader.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/ShmRdWr.h](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/include/ShmRdWr.h) | `ShmRdWr`, `ShmRdWr_BufMetadata`, `ShmRdWr_Header`, `ShmRdWr_Info`, `ShmRdWr_Rdr`, `shmrw_gid_t` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `..` | [cxx/src/ShmRdWr.cpp:35](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/ShmRdWr.cpp#L35) |
| `netinet` | [cxx/include/ShmRdWr.h:13](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/include/ShmRdWr.h#L13) |
| `sys` | [cxx/src/ShmRdWr.cpp:28](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/ShmRdWr.cpp#L28) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["NovaTimingUtilities"]
  p1["ShmRdWr"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaTimingUtilities](NovaTimingUtilities.md) | build link | [cxx/src/CMakeLists.txt:10](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/CMakeLists.txt#L10) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/GNUmakefile#L10) |


Direct consumers: [BufferNodeEVB](BufferNodeEVB.md), [NovaDAQLiveTimeMonitor](NovaDAQLiveTimeMonitor.md), [ShmMilliBlock](ShmMilliBlock.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **12 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-010: Pass real metadata storage to the convenience group-read overload](../review/issues/NDAQ-010.md) | [Issue](https://github.com/NovaDAQ/ShmRdWr/issues/1) |


Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/TCAttrib.h](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/TCAttrib.h) |
| [cxx/test/compat_writer.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/compat_writer.cc) |
| [cxx/test/fast_rd.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/fast_rd.cc) |
| [cxx/test/fast_wr.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/fast_wr.cc) |
| [cxx/test/shm_rd.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/shm_rd.cc) |
| [cxx/test/shm_wr.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/shm_wr.cc) |
| [cxx/test/simple_read_grper.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/simple_read_grper.cc) |
| [cxx/test/simple_reader.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/simple_reader.cc) |
| [cxx/test/simple_writer.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/simple_writer.cc) |
| [cxx/test/test_shmrw.cc](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/test/test_shmrw.cc) |


## Existing documentation

| Source |
| --- |
| [doc/README](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/doc/README) |
| [doc/testing_results.txt](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/doc/testing_results.txt) |
