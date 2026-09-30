# dcm_kernel_module

DCM Linux driver for control/status/data devices, FPGA access, DMA, and board utilities.

## Identity and scope

Repository: [NovaDAQ/dcm_kernel_module](https://github.com/NovaDAQ/dcm_kernel_module) · Reviewed commit: `e829ed41041a5d95f3f99d048cae63a503f64d79` · Domain: **Hardware**.

Tracked files: **24**. Production deployment and owner are **unconfirmed**.

## Operation

Build against the exact target kernel/configuration and verify device permissions and register maps. Preserve loaded-module/firmware versions; driver replacement requires stopping device consumers and a tested rollback path.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/GNUmakefile) |
| [Makefile](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [DCM_SERIAL_NUM_TABLE.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/DCM_SERIAL_NUM_TABLE.h) | Functions, constants, or templates |
| [dcm_control.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.h) | `mpc8347_gpio` |
| [dcm_control_register_block.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control_register_block.h) | `DCMControlRegisterBlock` |
| [dcm_data.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_data.h) | `dcm_microslice_header`, `dcm_pointer_frame` |
| [dcm_kernel.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_kernel.h) | `cmdFPGAdump`, `cmdFPGAdump_extended`, `dcm_config`, `dcm_get_buffers`, `dcm_rd_timing_regs`, `dcm_rdwr_dcm_reg`, `dcm_rdwr_feb_reg`, `dcm_status`, `register_frame`, `timedcm`, `timeval` |
| [dcm_serialnum.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_serialnum.h) | `dcm_serial_info` |
| [dcm_status.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_status.h) | Functions, constants, or templates |
| [fsldma.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/fsldma.h) | `device`, `dma_async_tx_descriptor`, `dma_chan`, `dma_device`, `dma_pool`, `fsl_desc_sw`, `fsl_dma_chan`, `fsl_dma_chan_regs`, `fsl_dma_device`, `fsl_dma_ld_hw`, `list_head`, `resource`, `tasklet_struct` |
| [hal_io.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/hal_io.h) | Functions, constants, or templates |
| [mpc83xx.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/mpc83xx.h) | `upm_microcode`, `upms` |
| [novadcm_8347.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/novadcm_8347.h) | Functions, constants, or templates |
| [plf_regs.h](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/plf_regs.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `asm` | [dcm_control.c:17](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.c#L17) |
| `linux` | [dcm_control.c:1](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.c#L1) |
| `sys` | [dcm_kernel.h:10](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_kernel.h#L10) |
| `sysdev` | [dcm_control.c:25](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.c#L25) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:35](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/GNUmakefile#L35) |


Direct consumers: [DCMApplication](DCMApplication.md), [DCM_ProgUtils](DCM_ProgUtils.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **5 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-021: Validate register ioctl user copies and MMIO indices](../review/issues/NDAQ-021.md) | [Issue](https://github.com/NovaDAQ/dcm_kernel_module/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/README) |
