# tdu_kernel_module

TDU Linux module with register/data operations, timing work, and driver documentation.

## Identity and scope

Repository: [NovaDAQ/tdu_kernel_module](https://github.com/NovaDAQ/tdu_kernel_module) · Reviewed commit: `43b9ed958186477b24109a10ac85e9e357e8d07f` · Domain: **Hardware**.

Tracked files: **16**. Production deployment and owner are **unconfirmed**.

## Operation

Build with the target kernel and confirm hardware/firmware compatibility. Review actual enabled workqueue behavior, device access permissions, and readback before timing tests. No module loading or board programming was performed during review.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/GNUmakefile) |
| [Makefile](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [tdu_data.h](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/tdu_data.h) | Functions, constants, or templates |
| [tdu_kernel.h](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/tdu_kernel.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `asm` | [tdu_data.c:8](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/tdu_data.c#L8) |
| `linux` | [tdu_data.c:1](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/tdu_data.c#L1) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:35](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/GNUmakefile#L35) |


Direct consumers: [TDUUtilities](TDUUtilities.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **1 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [doc/readme.nova-docdb.txt](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/doc/readme.nova-docdb.txt) |
| [doc/readme.txt](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/doc/readme.txt) |
| [doc/requirements.txt](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/doc/requirements.txt) |
| [readme.txt](https://github.com/NovaDAQ/tdu_kernel_module/blob/43b9ed958186477b24109a10ac85e9e357e8d07f/readme.txt) |
