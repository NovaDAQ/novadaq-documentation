# PixelMaskTool

Interface/tool for creating or updating pixel masks through the DAQ configuration layer.

## Identity and scope

Repository: [NovaDAQ/PixelMaskTool](https://github.com/NovaDAQ/PixelMaskTool) · Reviewed commit: `a2b10779c37e0e248f031fdc8c296f38acd97f7d` · Domain: **Control**.

Tracked files: **14**. Production deployment and owner are **unconfirmed**.

## Operation

Confirm detector and source configuration, inspect changed channels, and keep a previous mask/configuration for rollback. Validate mask bounds and representation before activating it in a run.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/PixelMaskTool.cc](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/PixelMaskTool.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/PixelMaskInterface.h](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/include/PixelMaskInterface.h) | `PixelMaskInterface` |
| [cxx/src/version.h](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/include/PixelMaskInterface.h:4](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/include/PixelMaskInterface.h#L4) |
| `QtGui` | [cxx/include/PixelMaskInterface.h:5](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/include/PixelMaskInterface.h#L5) |
| `sys` | [cxx/src/PixelMaskInterface.cpp:1](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/PixelMaskInterface.cpp#L1) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["PackageVersion"]
  p1["PixelMaskTool"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [PackageVersion](PackageVersion.md) | build link | [cxx/src/GNUmakefile:30](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/GNUmakefile#L30) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/src/version.h:28](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/cxx/src/version.h#L28) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/PixelMaskTool/blob/a2b10779c37e0e248f031fdc8c296f38acd97f7d/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **2 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
