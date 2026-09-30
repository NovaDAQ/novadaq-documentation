# DataConcentratorModule

Earlier DCM userspace, CPLD/FPGA programming, and kernel-driver implementation.

## Identity and scope

Repository: [NovaDAQ/DataConcentratorModule](https://github.com/NovaDAQ/DataConcentratorModule) · Reviewed commit: `18dbefa32acb189d7861ec56a974a6960dc96766` · Domain: **Hardware**.

Tracked files: **27**. Production deployment and owner are **unconfirmed**.

## Operation

Determine whether deployment uses this tree or dcm_kernel_module before applying fixes. Match the old driver ABI and hardware image. Register/FIFO tests and flashing require a dedicated board and recovery procedure.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

| Build definition |
| --- |
| [dcm/GNUmakefile](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm/GNUmakefile) |
| [dcm_cpld/Makefile](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_cpld/Makefile) |
| [dcm_fpga/Makefile](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_fpga/Makefile) |
| [dcm_kernel/Makefile](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [dcm/cxx/src/dcmControl.cpp](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm/cxx/src/dcmControl.cpp) |
| [dcm_cpld/dcm_control.c](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_cpld/dcm_control.c) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [dcm_fpga/dcm_fpga.h](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_fpga/dcm_fpga.h) | `cdev`, `class`, `dcm_fpga_device`, `nanoslice`, `pointer_frame`, `resource`, `semaphore`, `sub_frame`, `subframe`, `subframe_header` |
| [dcm_kernel/dcm_control.h](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/dcm_control.h) | `mpc8347_gpio` |
| [dcm_kernel/dcm_data.h](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/dcm_data.h) | `dcm_microslice_header`, `dcm_pointer_frame`, `mpc8347_dma_descriptor` |
| [dcm_kernel/dcm_kernel.h](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/dcm_kernel.h) | `dcm_nanoslice` |
| [dcm_kernel/dcm_status.h](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/dcm_status.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `..` | [dcm/cxx/src/Dcm.cpp:13](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm/cxx/src/Dcm.cpp#L13) |
| `Dcm` | [dcm/cxx/src/Dcm.cpp:11](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm/cxx/src/Dcm.cpp#L11) |
| `asm` | [dcm_cpld/dcm_cpld.c:13](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_cpld/dcm_cpld.c#L13) |
| `linux` | [dcm_cpld/dcm_cpld.c:1](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_cpld/dcm_cpld.c#L1) |
| `sys` | [dcm/cxx/src/Dcm.cpp:5](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm/cxx/src/Dcm.cpp#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **9 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-012: Initialize and advance the status-read frame cursor](../review/issues/NDAQ-012.md) | [Issue](https://github.com/NovaDAQ/DataConcentratorModule/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [dcm_cpld/README](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_cpld/README) |
| [dcm_fpga/README](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_fpga/README) |
| [dcm_kernel/README](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/README) |
