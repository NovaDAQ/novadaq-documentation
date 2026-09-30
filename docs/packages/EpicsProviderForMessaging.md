# EpicsProviderForMessaging

EPICS Channel Access servers and clients that carry RMS messaging through process variables.

## Identity and scope

Repository: [NovaDAQ/EpicsProviderForMessaging](https://github.com/NovaDAQ/EpicsProviderForMessaging) · Reviewed commit: `fb6ddc349448d4d15077292cf0d6dbe3b4b4b565` · Domain: **Messaging**.

Tracked files: **19**. Production deployment and owner are **unconfirmed**.

## Operation

Set RMS_CUSTOM_ENVIRONMENT and the EPICS runtime correctly; namespace collisions can connect unrelated clients. Validate PV discovery and end-to-end message delivery before starting consumers. Rotate CAS logs using the provided operational scripts only after checking their paths.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/GNUmakefile) |
| [autoCas/GNUmakefile](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/autoCas/GNUmakefile) |
| [directMsgCas/GNUmakefile](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/directMsgCas/GNUmakefile) |
| [testClients/GNUmakefile](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/GNUmakefile) |
| [testClients/mods/Makefile](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [autoCas/mods/main.cc](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/autoCas/mods/main.cc) |
| [directMsgCas/removeOldCasLogFiles.sh](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/directMsgCas/removeOldCasLogFiles.sh) |
| [directMsgCas/startCas.sh](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/directMsgCas/startCas.sh) |
| [testClients/mods/epmMonitorByteArray.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmMonitorByteArray.c) |
| [testClients/mods/epmMonitorDouble.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmMonitorDouble.c) |
| [testClients/mods/epmMonitorString.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmMonitorString.c) |
| [testClients/mods/epmPutByteArray.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmPutByteArray.c) |
| [testClients/mods/epmPutDouble.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmPutDouble.c) |
| [testClients/mods/epmPutString.c](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/testClients/mods/epmPutString.c) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [autoCas/mods/exServer.h](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/autoCas/mods/exServer.h) | `epicsTimer`, `exAsyncCreateIO`, `exAsyncExistIO`, `exAsyncPV`, `exAsyncReadIO`, `exAsyncWriteIO`, `exChannel`, `exPV`, `exScalarPV`, `exServer`, `exVectorPV`, `excasIoType`, `pvEntry`, `pvInfo` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `RMS_CUSTOM_ENVIRONMENT` | [autoCas/mods/exServer.cc:29](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/autoCas/mods/exServer.cc#L29) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:7](https://github.com/NovaDAQ/EpicsProviderForMessaging/blob/fb6ddc349448d4d15077292cf0d6dbe3b4b4b565/GNUmakefile#L7) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **9 C/C++ translation units**, **2 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
