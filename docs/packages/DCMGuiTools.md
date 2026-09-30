# DCMGuiTools

Qt DCM register viewer with hexadecimal controls and register display widgets.

## Identity and scope

Repository: [NovaDAQ/DCMGuiTools](https://github.com/NovaDAQ/DCMGuiTools) · Reviewed commit: `1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691` · Domain: **Hardware**.

Tracked files: **18**. Production deployment and owner are **unconfirmed**.

## Operation

Connect to the intended DCM and validate firmware/register-map compatibility. Register writes are hardware operations; separate inspection from editing. Capture before/after values and use a test board when changing control behavior.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/DCMRegisterView.cc](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/DCMRegisterView.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/DcmRegDumpGui.h](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/DcmRegDumpGui.h) | `DCMRegDumpGui` |
| [cxx/include/HexSpinBox.h](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/HexSpinBox.h) | `HexSpinBox`, `QRegExpValidator` |
| [cxx/include/RegisterDisplay.h](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/RegisterDisplay.h) | `RegisterDisplay` |
| [cxx/src/version.h](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/include/DcmRegDumpGui.h:4](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/DcmRegDumpGui.h#L4) |
| `QtGui` | [cxx/include/DcmRegDumpGui.h:5](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/DcmRegDumpGui.h#L5) |
| `sys` | [cxx/src/DCMRegisterView.cc:4](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/DCMRegisterView.cc#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DCMGuiTools"]
  p1["DCM_ProgUtils"]
  p2["PackageVersion"]
  p3["Trace"]
  p0 --> p1
  p0 --> p2
  p0 --> p3
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DCM_ProgUtils](DCM_ProgUtils.md) | build link | [cxx/src/GNUmakefile:32](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/GNUmakefile#L32) |
| [DCM_ProgUtils](DCM_ProgUtils.md) | source include | [cxx/include/DcmRegDumpGui.h:11](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/include/DcmRegDumpGui.h#L11) |
| [PackageVersion](PackageVersion.md) | build link | [cxx/src/GNUmakefile:32](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/GNUmakefile#L32) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/src/version.h:28](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/version.h#L28) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/GNUmakefile#L10) |
| [Trace](Trace.md) | build link | [cxx/src/GNUmakefile:32](https://github.com/NovaDAQ/DCMGuiTools/blob/1a3b588f5627a1d1d4b8e8cc6b193dea82ec9691/cxx/src/GNUmakefile#L32) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **4 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
