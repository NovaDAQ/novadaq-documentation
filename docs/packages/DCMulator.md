# DCMulator

USB/MATLAB-based DCM/FEB checkout and programming environment with USB support code and bundled libraries.

## Identity and scope

Repository: [NovaDAQ/DCMulator](https://github.com/NovaDAQ/DCMulator) · Reviewed commit: `eb0e4b107b75981d7699597f8db7187d93949756` · Domain: **Hardware**.

Tracked files: **1199**. Production deployment and owner are **unconfirmed**.

This checkout had pre-existing local changes. Remote source links identify the committed revision; local changes were preserved. See the snapshot ledger for affected paths.

## Operation

Match the USB interface, MATLAB/MEX ABI, board revision, and firmware configuration. Retain checkout results per device and run on a dedicated test stand. Existing local MATLAB changes were preserved and are not represented by remote commit links.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [usbProject/deploy/GetData/distrib/run_GetData.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/deploy/GetData/distrib/run_GetData.sh) |
| [usbProject/deploy/GetData/src/GetData_main.c](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/deploy/GetData/src/GetData_main.c) |
| [usbProject/deploy/GetData/src/run_GetData.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/deploy/GetData/src/run_GetData.sh) |
| [usbProject/firmware/configDcm.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/firmware/configDcm.sh) |
| [usbProject/firmware/configDcmSingle.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/firmware/configDcmSingle.sh) |
| [usbProject/firmware/configDcmSingleLegacy.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/firmware/configDcmSingleLegacy.sh) |
| [usbProject/firmware/configDcmSingleMP.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/firmware/configDcmSingleMP.sh) |
| [usbProject/getExtTrigData/distrib/run_getExtTrigData.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/getExtTrigData/distrib/run_getExtTrigData.sh) |
| [usbProject/getExtTrigData/src/getExtTrigData_main.c](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/getExtTrigData/src/getExtTrigData_main.c) |
| [usbProject/getExtTrigData/src/run_getExtTrigData.sh](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/getExtTrigData/src/run_getExtTrigData.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

| Source artifact |
| --- |
| [usbProject/data_20111012131.conf](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/data_20111012131.conf) |
| [usbProject/firmware/FebV4_1_0031.xml](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/firmware/FebV4_1_0031.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `libusb-1.0` | [usbProject/usbLib.c:20](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/usbLib.c#L20) |
| `sys` | [usbProject/usbLib.c:17](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/usbLib.c#L17) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **6 C/C++ translation units**, **10 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

Large vendor/generated/firmware trees received a bounded integration review. The [methodology](../review/methodology.md) records exclusions. No complete third-party audit or hardware validation is claimed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/README) |
| [usbProject/README](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/README) |
| [usbProject/deploy/GetData/distrib/readme.txt](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/deploy/GetData/distrib/readme.txt) |
| [usbProject/deploy/GetData/src/readme.txt](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/deploy/GetData/src/readme.txt) |
| [usbProject/getExtTrigData/distrib/readme.txt](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/getExtTrigData/distrib/readme.txt) |
| [usbProject/getExtTrigData/src/readme.txt](https://github.com/NovaDAQ/DCMulator/blob/eb0e4b107b75981d7699597f8db7187d93949756/usbProject/getExtTrigData/src/readme.txt) |
