# NovaRunControlClient_OLD

Historical Nova state-manager/client implementation.

## Identity and scope

Repository: [NovaDAQ/NovaRunControlClient_OLD](https://github.com/NovaDAQ/NovaRunControlClient_OLD) · Reviewed commit: `0e8aeb3d9b06787819d3483eecf61f7a1246a94b` · Domain: **Control**.

Tracked files: **13**. Production deployment and owner are **unconfirmed**. The directory name marks a legacy variant; retirement has not been independently verified.

## Operation

Use its matching message definitions and state-transition semantics for reproduction. Verify current deployment before scheduling migration to the newer RMS client.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/inc/NovaRunControlClient/Defs.hpp](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/Defs.hpp) | `ReturnValue`, `TraceLevel` |
| [cxx/inc/NovaRunControlClient/NovaStateManager.hpp](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/NovaStateManager.hpp) | `NovaStateManager`, `NovaStateManagerTest` |
| [cxx/inc/NovaRunControlClient/Trace.hpp](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/Trace.hpp) | `timeval` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/jcsc.xml](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/config/jcsc.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `HOSTNAME` | [cxx/src/NovaStateManager.cpp:167](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/src/NovaStateManager.cpp#L167) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/inc/NovaRunControlClient/NovaStateManager.hpp:18](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/NovaStateManager.hpp#L18) |
| `linux` | [cxx/inc/NovaRunControlClient/Trace.hpp:16](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/Trace.hpp#L16) |
| `novaMsg` | [cxx/src/NovaStateManager.cpp:15](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/src/NovaStateManager.cpp#L15) |
| `sys` | [cxx/inc/NovaRunControlClient/Trace.hpp:18](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/Trace.hpp#L18) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["NovaRunControlClient"]
  p1["NovaRunControlClient_OLD"]
  p2["ResponsiveMessagingSystem"]
  p3["RunControlClient"]
  p1 --> p0
  p1 --> p2
  p1 --> p3
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaRunControlClient](NovaRunControlClient.md) | source include | [cxx/inc/NovaRunControlClient/NovaStateManager.hpp:9](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/NovaStateManager.hpp#L9) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | build link | [GNUmakefile:139](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/GNUmakefile#L139) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | source include | [cxx/inc/NovaRunControlClient/NovaStateManager.hpp:13](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/NovaStateManager.hpp#L13) |
| [RunControlClient](RunControlClient.md) | build link | [GNUmakefile:145](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/GNUmakefile#L145) |
| [RunControlClient](RunControlClient.md) | source include | [cxx/inc/NovaRunControlClient/NovaStateManager.hpp:10](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/cxx/inc/NovaRunControlClient/NovaStateManager.hpp#L10) |
| [RunControlClient](RunControlClient.md) | test include | [test/cxx/src/StateReceiver.cpp:3](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/test/cxx/src/StateReceiver.cpp#L3) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **2 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [test/cxx/src/StateReceiver.cpp](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/test/cxx/src/StateReceiver.cpp) |


## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/NovaRunControlClient_OLD/blob/0e8aeb3d9b06787819d3483eecf61f7a1246a94b/README) |
