# RunControlClient_OLD

Earlier generic run-control client with state-manager/listener tests.

## Identity and scope

Repository: [NovaDAQ/RunControlClient_OLD](https://github.com/NovaDAQ/RunControlClient_OLD) · Reviewed commit: `f543a972032362de6225efeae39f6df1afe3dbac` · Domain: **Control**.

Tracked files: **16**. Production deployment and owner are **unconfirmed**. The directory name marks a legacy variant; retirement has not been independently verified.

## Operation

Treat this as a distinct historical contract and verify deployment before migration. Preserve the accompanying tests as reference for expected legacy behavior.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/inc/RunControlClient/Defs.hpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/Defs.hpp) | `ReturnValue`, `TraceLevel` |
| [cxx/inc/RunControlClient/StateChangeListener.hpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/StateChangeListener.hpp) | `StateChangeListener`, `StateChangeListenerTest` |
| [cxx/inc/RunControlClient/StateManager.hpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/StateManager.hpp) | `StateManager`, `StateManagerTest` |
| [cxx/inc/RunControlClient/Trace.hpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/Trace.hpp) | `timeval` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/jcsc.xml](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/config/jcsc.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `cppunit` | [test/cxx/src/StateChangeListenerTest.cpp:7](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/test/cxx/src/StateChangeListenerTest.cpp#L7) |
| `linux` | [cxx/inc/RunControlClient/Trace.hpp:35](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/Trace.hpp#L35) |
| `sys` | [cxx/inc/RunControlClient/Trace.hpp:37](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/Trace.hpp#L37) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["RunControlClient"]
  p1["RunControlClient_OLD"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [RunControlClient](RunControlClient.md) | source include | [cxx/inc/RunControlClient/StateChangeListener.hpp:9](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/cxx/inc/RunControlClient/StateChangeListener.hpp#L9) |
| [RunControlClient](RunControlClient.md) | test include | [test/cxx/src/StateChangeListenerTest.cpp:12](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/test/cxx/src/StateChangeListenerTest.cpp#L12) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **4 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [test/cxx/src/StateChangeListenerTest.cpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/test/cxx/src/StateChangeListenerTest.cpp) |
| [test/cxx/src/StateManagerTest.cpp](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/test/cxx/src/StateManagerTest.cpp) |


## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/RunControlClient_OLD/blob/f543a972032362de6225efeae39f6df1afe3dbac/README) |
