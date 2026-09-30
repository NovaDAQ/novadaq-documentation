# DAQDataFormats

Versioned raw run, event, trigger, data-block, microslice, and nanoslice representations, checksums, and simulation helpers.

## Identity and scope

Repository: [NovaDAQ/DAQDataFormats](https://github.com/NovaDAQ/DAQDataFormats) · Reviewed commit: `869a1fc336526c7cccb92bf7cbd31203745ce7c5` · Domain: **Core libraries**.

Tracked files: **371**. Production deployment and owner are **unconfirmed**.

## Operation

Keep producers and readers on compatible format versions. Validate marker pairs, lengths, run-size accounting, and checksums with known sample files before deployment. Format changes affect loggers, dispatchers, parsers, and analysis clients together.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/GNUmakefile) |
| [cxx/include/CMakeLists.txt](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/CMakeLists.txt) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/GNUmakefile) |
| [doc/DataFormatsDoc/Makefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/Makefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/DCMSimulatorExample.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/src/DCMSimulatorExample.cc) |
| [cxx/src/FEBSimulatorExample.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/src/FEBSimulatorExample.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/BitFields.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/BitFields.h) | Functions, constants, or templates |
| [cxx/include/DAQDataFormats.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/DAQDataFormats.h) | `DCMSimulator`, `FEBSimulator`, `RawDAQData`, `RawEvent`, `RawEventHeader`, `RawEventTail`, `RawMicroSlice`, `RawMicroSliceHeader`, `RawMilliDCMChan`, `RawMilliSlice`, `RawMilliSliceHeader`, `RawMilliSliceIndex`, `RawMilliSubframe`, `RawMilliSubframeHeader`, `RawNanoSlice`, `RawTimingMarker`, `RawTrigger`, `RawTriggerHeader`, `RawTriggerMask`, `RawTriggerRange`, `RawTriggerTime`, `RawTriggerTimingMarker` |
| [cxx/include/DCMSimulator.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/DCMSimulator.h) | `DCMSimulator` |
| [cxx/include/DataFormatException.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/DataFormatException.h) | `DataFormatException` |
| [cxx/include/FEBSimulator.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/FEBSimulator.h) | `FEBSimulator` |
| [cxx/include/FunctionBind.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/FunctionBind.h) | Functions, constants, or templates |
| [cxx/include/Macros.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/Macros.h) | Functions, constants, or templates |
| [cxx/include/NOvACheckSum.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/NOvACheckSum.h) | `NOvACheckSum` |
| [cxx/include/NanoSliceVersionConvention.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/NanoSliceVersionConvention.h) | `Encode_Type`, `FEBVersioningRegisters`, `NanoSliceVersionConvention` |
| [cxx/include/RawConfigurationBlock.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationBlock.h) | `RawConfigurationBlock` |
| [cxx/include/RawConfigurationBlockV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationBlockV0.h) | `RawConfigurationBlock`, `RawConfigurationSystemID`, `RawConfigurationTail` |
| [cxx/include/RawConfigurationBlockV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationBlockV1.h) | `RawConfigurationBlock` |
| [cxx/include/RawConfigurationHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationHeader.h) | `RawConfigurationHeader` |
| [cxx/include/RawConfigurationHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationHeaderV0.h) | `RawConfigurationHeader`, `RunHeaderMASKS`, `RunHeaderWORDS` |
| [cxx/include/RawConfigurationHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationHeaderV1.h) | `RawConfigurationHeader` |
| [cxx/include/RawConfigurationName.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationName.h) | `RawConfigurationName` |
| [cxx/include/RawConfigurationNameV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationNameV0.h) | `ConfNameMASKS`, `ConfNameWORDS`, `RawConfigurationName` |
| [cxx/include/RawConfigurationSystemID.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationSystemID.h) | `RawConfigurationSystemID` |
| [cxx/include/RawConfigurationSystemIDV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationSystemIDV0.h) | `RawConfigurationName`, `RawConfigurationSystemID`, `SysIDMASKS`, `SysIDWORDS` |
| [cxx/include/RawConfigurationTail.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationTail.h) | `RawConfigurationTail` |
| [cxx/include/RawConfigurationTailV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawConfigurationTailV0.h) | `ConfigurationTailMASKS`, `ConfigurationTailWORDS`, `RawConfigurationTail` |
| [cxx/include/RawDAQData.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDAQData.h) | `DataBlockReader`, `RawDAQData` |
| [cxx/include/RawDCMChan.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDCMChan.h) | `DCMChanMASKS`, `DCMChanWORDS`, `RawDCMChan` |
| [cxx/include/RawDataBlock.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlock.h) | `RawDataBlock` |
| [cxx/include/RawDataBlockHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockHeader.h) | `RawDataBlockHeader` |
| [cxx/include/RawDataBlockHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockHeaderV0.h) | `DataBlockHeaderMASKS`, `DataBlockHeaderWORDS`, `RawDataBlockHeader` |
| [cxx/include/RawDataBlockHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockHeaderV1.h) | `RawDataBlockHeader` |
| [cxx/include/RawDataBlockHeaderV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockHeaderV2.h) | `RawDataBlockHeader` |
| [cxx/include/RawDataBlockV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockV0.h) | `RawDataBlock`, `RawMicroBlock` |
| [cxx/include/RawDataBlockV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockV1.h) | `RawDataBlock` |
| [cxx/include/RawDataBlockV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawDataBlockV2.h) | `RawDataBlock` |
| [cxx/include/RawEvent.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEvent.h) | `RawEvent` |
| [cxx/include/RawEventHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventHeader.h) | `RawEventHeader` |
| [cxx/include/RawEventHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventHeaderV0.h) | `EventHeaderMASKS`, `EventHeaderWORDS`, `RawEventHeader` |
| [cxx/include/RawEventHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventHeaderV1.h) | `EventHeaderMASKS`, `EventHeaderWORDS`, `RawEventHeader` |
| [cxx/include/RawEventTail.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventTail.h) | `RawEventTail` |
| [cxx/include/RawEventTailV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventTailV0.h) | `EventTailMASKS`, `EventTailWORDS`, `RawEventTail` |
| [cxx/include/RawEventV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventV0.h) | `RawDataBlock`, `RawEvent`, `RawEventHeader`, `RawEventTail`, `RawTrigger` |
| [cxx/include/RawEventV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawEventV1.h) | `RawEvent` |
| [cxx/include/RawMicroBlock.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlock.h) | `RawMicroBlock` |
| [cxx/include/RawMicroBlockHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlockHeader.h) | `RawMicroBlockHeader` |
| [cxx/include/RawMicroBlockHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlockHeaderV0.h) | `MicroBlockHeaderMASKS`, `MicroBlockHeaderWORDS`, `RawMicroBlockHeader` |
| [cxx/include/RawMicroBlockHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlockHeaderV1.h) | `MicroBlockHeaderMASKS`, `MicroBlockHeaderWORDS`, `RawMicroBlockHeader` |
| [cxx/include/RawMicroBlockV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlockV0.h) | `RawMicroBlock` |
| [cxx/include/RawMicroBlockV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroBlockV1.h) | `RawMicroBlock` |
| [cxx/include/RawMicroSlice.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroSlice.h) | `RawMicroSlice` |
| [cxx/include/RawMicroSliceHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroSliceHeader.h) | `RawMicroSlice`, `RawMicroSliceHeader` |
| [cxx/include/RawMicroSliceHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroSliceHeaderV0.h) | `MicroSliceHeaderMASKS`, `MicroSliceHeaderWORDS`, `RawMicroSliceHeader` |
| [cxx/include/RawMicroSliceHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMicroSliceHeaderV1.h) | `MicroSliceHeaderMASKS`, `MicroSliceHeaderWORDS`, `RawMicroSliceHeader` |
| [cxx/include/RawMilliBlock.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliBlock.h) | `RawMilliBlock` |
| [cxx/include/RawMilliBlockHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliBlockHeader.h) | `RawMilliBlockHeader` |
| [cxx/include/RawMilliSlice.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliSlice.h) | `RawMilliSlice` |
| [cxx/include/RawMilliSliceHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliSliceHeader.h) | `MilliSliceHeaderMASKS`, `MilliSliceHeaderWORDS`, `Mode_t`, `RawMilliSliceHeader` |
| [cxx/include/RawMilliSliceIndex.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliSliceIndex.h) | `MilliSliceIndexMASKS`, `MilliSliceIndexWORDS`, `RawMilliSliceIndex` |
| [cxx/include/RawMilliSliceIndexHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawMilliSliceIndexHeader.h) | `MilliSliceIndexHeaderMASKS`, `MilliSliceIndexHeaderWORDS`, `RawMilliSliceIndexHeader` |
| [cxx/include/RawNanoSlice.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSlice.h) | `RawNanoSlice` |
| [cxx/include/RawNanoSliceHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeader.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV0.h) | `NanoSliceHeaderMASKS`, `NanoSliceHeaderWORDS`, `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV1.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV2.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV3.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV3.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV4.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV4.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceHeaderV5.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceHeaderV5.h) | `RawNanoSliceHeader` |
| [cxx/include/RawNanoSliceV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV0.h) | `NanoSliceMASKS`, `NanoSliceWORDS`, `RawNanoSlice` |
| [cxx/include/RawNanoSliceV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV1.h) | `NanoSliceMASKS`, `NanoSliceWORDS`, `RawNanoSlice` |
| [cxx/include/RawNanoSliceV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV2.h) | `NanoSliceMASKS`, `NanoSliceWORDS`, `RawNanoSlice` |
| [cxx/include/RawNanoSliceV3.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV3.h) | `RawNanoSlice` |
| [cxx/include/RawNanoSliceV4.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV4.h) | `RawNanoSlice` |
| [cxx/include/RawNanoSliceV5.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawNanoSliceV5.h) | `RawNanoSlice` |
| [cxx/include/RawRun.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawRun.h) | `RawRun` |
| [cxx/include/RawRunHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawRunHeader.h) | `RawRunHeader` |
| [cxx/include/RawRunHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawRunHeaderV0.h) | `RawRunHeader`, `RunHeaderMASKS`, `RunHeaderWORDS` |
| [cxx/include/RawRunTail.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawRunTail.h) | `RawRunTail` |
| [cxx/include/RawRunV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawRunV0.h) | `RawRunV0` |
| [cxx/include/RawSummaryDCMData.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMData.h) | `RawSummaryDCMData` |
| [cxx/include/RawSummaryDCMDataHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMDataHeader.h) | `RawSummaryDCMDataHeader` |
| [cxx/include/RawSummaryDCMDataHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMDataHeaderV0.h) | `RawSummaryDCMDataHeader`, `SummaryDCMDataHeaderMASKS`, `SummaryDCMDataHeaderWORDS` |
| [cxx/include/RawSummaryDCMDataPoint.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMDataPoint.h) | `RawSummaryDCMDataPoint` |
| [cxx/include/RawSummaryDCMDataPointV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMDataPointV0.h) | `DCMDataPointMASKS`, `DCMDataPointType`, `DCMDataPointWORDS`, `RawSummaryDCMDataPoint` |
| [cxx/include/RawSummaryDCMDataV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDCMDataV0.h) | `RawSummaryDCMData` |
| [cxx/include/RawSummaryDroppedMicroblock.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDroppedMicroblock.h) | `RawSummaryDroppedMicroblock` |
| [cxx/include/RawSummaryDroppedMicroblockV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawSummaryDroppedMicroblockV0.h) | `RawSummaryDroppedMicroblock`, `SummaryDroppedMicroblockMASKS`, `SummaryDroppedMicroblockWORDS` |
| [cxx/include/RawTimingMarker.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTimingMarker.h) | `RawTimingMarker`, `TimingMarker`, `TimingMarkerMASKS`, `TimingMarkerWord` |
| [cxx/include/RawTrigger.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTrigger.h) | `RawTrigger`, `TriggerVersion` |
| [cxx/include/RawTriggerHeader.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerHeader.h) | `RawTriggerHeader` |
| [cxx/include/RawTriggerHeaderV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerHeaderV0.h) | `RawTriggerHeader`, `TriggerHeaderMASKS`, `TriggerHeaderWORDS` |
| [cxx/include/RawTriggerHeaderV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerHeaderV1.h) | `RawTriggerHeader` |
| [cxx/include/RawTriggerHeaderV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerHeaderV2.h) | `RawTriggerHeader` |
| [cxx/include/RawTriggerMask.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerMask.h) | `RawTriggerMask` |
| [cxx/include/RawTriggerMaskV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerMaskV0.h) | `RawTriggerMask`, `TriggerMaskMASKS`, `TriggerMaskWORDS` |
| [cxx/include/RawTriggerRange.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerRange.h) | `RawTriggerRange` |
| [cxx/include/RawTriggerRangeV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerRangeV0.h) | `RawTriggerRange`, `TriggerRangeMASKS`, `TriggerRangeWORDS` |
| [cxx/include/RawTriggerTime.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerTime.h) | `RawTriggerTime` |
| [cxx/include/RawTriggerTimeV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerTimeV0.h) | `RawTriggerTime`, `TriggerTimeMASKS`, `TriggerTimeWORDS` |
| [cxx/include/RawTriggerTimingMarker.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerTimingMarker.h) | `RawTriggerTimingMarker` |
| [cxx/include/RawTriggerTimingMarkerV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerTimingMarkerV0.h) | `RawTriggerTimingMarker`, `TriggerTimeMarkerMASKS`, `TriggerTimeMarkerWORDS` |
| [cxx/include/RawTriggerV0.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerV0.h) | `RawTrigger`, `RawTriggerHeader`, `RawTriggerMask`, `RawTriggerRange`, `RawTriggerTime`, `RawTriggerTimingMarker`, `TriggerVersions` |
| [cxx/include/RawTriggerV1.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerV1.h) | `RawTrigger` |
| [cxx/include/RawTriggerV2.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/RawTriggerV2.h) | `RawTrigger` |
| [cxx/include/TimeStampCounter.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/TimeStampCounter.h) | Functions, constants, or templates |
| [cxx/include/TriggerDefines.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/TriggerDefines.h) | `trigBitID`, `trigClockSource`, `trigID`, `trigSource`, `trigSourceID`, `trigSourceSubID` |
| [cxx/include/version.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/version.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/include/NOvACheckSum.h:4](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/NOvACheckSum.h#L4) |
| `cppunit` | [cxx/unittest/RawDAQDataUnitTest.h:12](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataUnitTest.h#L12) |
| `messagefacility` | [cxx/unittest/RawDAQDataConstructor.h:14](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataConstructor.h#L14) |
| `netinet` | [cxx/test/DAQDataFormatDump.cc:19](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/DAQDataFormatDump.cc#L19) |
| `sys` | [cxx/include/BitFields.h:4](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/BitFields.h#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["PackageVersion"]
  p0 --> p1
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test include | [cxx/unittest/ddfunittest.cc:3](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ddfunittest.cc#L3) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test link | [cxx/unittest/GNUmakefile:17](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/GNUmakefile#L17) |
| [PackageVersion](PackageVersion.md) | build link | [cxx/src/CMakeLists.txt:4](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/src/CMakeLists.txt#L4) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/include/version.h:28](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/include/version.h#L28) |
| [PackageVersion](PackageVersion.md) | test link | [cxx/test/GNUmakefile:21](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/GNUmakefile#L21) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:16](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/GNUmakefile#L16) |
| [Trace](Trace.md) | test link | [cxx/unittest/GNUmakefile:18](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/GNUmakefile#L18) |


Direct consumers: [BufferNodeEVB](BufferNodeEVB.md), [DAQHit.old](DAQHit.old.md), [DAQMessagesZMQ](DAQMessagesZMQ.md), [DAQQualityCheck](DAQQualityCheck.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMApplication](DCMApplication.md), [DCM_ProgUtils](DCM_ProgUtils.md), [DispatcherClient](DispatcherClient.md), [EventBuilderClient](EventBuilderClient.md), [EventDispatcher_Server](EventDispatcher_Server.md), [EventDispatcher_Server_FMWK](EventDispatcher_Server_FMWK.md), [EventDump](EventDump.md), [EventMemoryViewer](EventMemoryViewer.md), [EvtDispatcher_PatternGenerator](EvtDispatcher_PatternGenerator.md), [EvtDispatcher_Viewer](EvtDispatcher_Viewer.md), [MetaDataTools](MetaDataTools.md), [MockDataDAQ](MockDataDAQ.md), [NDLTest](NDLTest.md), [NovaDAQCheckout](NovaDAQCheckout.md), [NovaDAQConfiguration](NovaDAQConfiguration.md), [NovaDAQUtilities](NovaDAQUtilities.md), [NovaDataLogger](NovaDataLogger.md), [NovaGlobalTrigger](NovaGlobalTrigger.md), [NovaRunControl](NovaRunControl.md), [NovaSuperNova](NovaSuperNova.md), [RawFileParser](RawFileParser.md), [RunSummaryUtils](RunSummaryUtils.md), [SHM_Utilities](SHM_Utilities.md), [ShmMilliBlock](ShmMilliBlock.md), [TriggerScalars](TriggerScalars.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **191 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/AndrewCRCTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/AndrewCRCTest.cc) |
| [cxx/test/BiteswapTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/BiteswapTest.cc) |
| [cxx/test/CRC_Table.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/CRC_Table.cc) |
| [cxx/test/DAQDataFormatDump.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/DAQDataFormatDump.cc) |
| [cxx/test/NanosliceVersionTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/NanosliceVersionTest.cc) |
| [cxx/test/RawConfigurationBlockTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawConfigurationBlockTest.cc) |
| [cxx/test/RawConfigurationHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawConfigurationHeaderTest.cc) |
| [cxx/test/RawConfigurationNameTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawConfigurationNameTest.cc) |
| [cxx/test/RawConfigurationSystemIDTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawConfigurationSystemIDTest.cc) |
| [cxx/test/RawConfigurationTailTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawConfigurationTailTest.cc) |
| [cxx/test/RawDCMChanTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawDCMChanTest.cc) |
| [cxx/test/RawDataBlockHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawDataBlockHeaderTest.cc) |
| [cxx/test/RawDataBlockTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawDataBlockTest.cc) |
| [cxx/test/RawEventHeadetTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawEventHeadetTest.cc) |
| [cxx/test/RawEventTailTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawEventTailTest.cc) |
| [cxx/test/RawEventTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawEventTest.cc) |
| [cxx/test/RawMicroBlockHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMicroBlockHeaderTest.cc) |
| [cxx/test/RawMicroBlockTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMicroBlockTest.cc) |
| [cxx/test/RawMicroSliceHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMicroSliceHeaderTest.cc) |
| [cxx/test/RawMicroSliceTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMicroSliceTest.cc) |
| [cxx/test/RawMilliSliceHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMilliSliceHeaderTest.cc) |
| [cxx/test/RawMilliSliceIndexTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMilliSliceIndexTest.cc) |
| [cxx/test/RawMilliSliceTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMilliSliceTest.cc) |
| [cxx/test/RawMilliSubframeHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMilliSubframeHeaderTest.cc) |
| [cxx/test/RawMilliSubframeTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawMilliSubframeTest.cc) |
| [cxx/test/RawNanoSliceHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawNanoSliceHeaderTest.cc) |
| [cxx/test/RawNanoSliceTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawNanoSliceTest.cc) |
| [cxx/test/RawRunHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawRunHeaderTest.cc) |
| [cxx/test/RawRunTailTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawRunTailTest.cc) |
| [cxx/test/RawRunTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawRunTest.cc) |
| [cxx/test/RawTimingMarkerTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTimingMarkerTest.cc) |
| [cxx/test/RawTriggerHeaderTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTriggerHeaderTest.cc) |
| [cxx/test/RawTriggerRangeTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTriggerRangeTest.cc) |
| [cxx/test/RawTriggerTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTriggerTest.cc) |
| [cxx/test/RawTriggerTimeTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTriggerTimeTest.cc) |
| [cxx/test/RawTriggerTimingMarkerTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/RawTriggerTimingMarkerTest.cc) |
| [cxx/test/ReadingDataLoggerTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/ReadingDataLoggerTest.cc) |
| [cxx/test/ReadingFileTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/ReadingFileTest.cc) |
| [cxx/test/ReadingMillisliceFileTest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/ReadingMillisliceFileTest.cc) |
| [cxx/test/crcmodel.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/crcmodel.h) |
| [cxx/test/testDataBlock.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/test/testDataBlock.cc) |
| [cxx/unittest/ConfigurationBlockConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationBlockConstructor.cpp) |
| [cxx/unittest/ConfigurationBlockConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationBlockConstructor.h) |
| [cxx/unittest/ConfigurationBlockUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationBlockUnitTest.cpp) |
| [cxx/unittest/ConfigurationHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationHeaderConstructor.cpp) |
| [cxx/unittest/ConfigurationHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationHeaderConstructor.h) |
| [cxx/unittest/ConfigurationHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationHeaderUnitTest.cpp) |
| [cxx/unittest/ConfigurationNameConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationNameConstructor.cpp) |
| [cxx/unittest/ConfigurationNameConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationNameConstructor.h) |
| [cxx/unittest/ConfigurationNameUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationNameUnitTest.cpp) |
| [cxx/unittest/ConfigurationSystemIDConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationSystemIDConstructor.cpp) |
| [cxx/unittest/ConfigurationSystemIDConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationSystemIDConstructor.h) |
| [cxx/unittest/ConfigurationSystemIDUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationSystemIDUnitTest.cpp) |
| [cxx/unittest/ConfigurationTailConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationTailConstructor.cpp) |
| [cxx/unittest/ConfigurationTailConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationTailConstructor.h) |
| [cxx/unittest/ConfigurationTailUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ConfigurationTailUnitTest.cpp) |
| [cxx/unittest/DataBlockConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockConstructor.cpp) |
| [cxx/unittest/DataBlockConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockConstructor.h) |
| [cxx/unittest/DataBlockHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockHeaderConstructor.cpp) |
| [cxx/unittest/DataBlockHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockHeaderConstructor.h) |
| [cxx/unittest/DataBlockHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockHeaderUnitTest.cpp) |
| [cxx/unittest/DataBlockUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/DataBlockUnitTest.cpp) |
| [cxx/unittest/EventConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventConstructor.cpp) |
| [cxx/unittest/EventConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventConstructor.h) |
| [cxx/unittest/EventHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventHeaderConstructor.cpp) |
| [cxx/unittest/EventHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventHeaderConstructor.h) |
| [cxx/unittest/EventHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventHeaderUnitTest.cpp) |
| [cxx/unittest/EventTailConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventTailConstructor.cpp) |
| [cxx/unittest/EventTailConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventTailConstructor.h) |
| [cxx/unittest/EventTailUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventTailUnitTest.cpp) |
| [cxx/unittest/EventUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/EventUnitTest.cpp) |
| [cxx/unittest/MicroBlockConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockConstructor.cpp) |
| [cxx/unittest/MicroBlockConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockConstructor.h) |
| [cxx/unittest/MicroBlockHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockHeaderConstructor.cpp) |
| [cxx/unittest/MicroBlockHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockHeaderConstructor.h) |
| [cxx/unittest/MicroBlockHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockHeaderUnitTest.cpp) |
| [cxx/unittest/MicroBlockUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroBlockUnitTest.cpp) |
| [cxx/unittest/MicroSliceConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceConstructor.cpp) |
| [cxx/unittest/MicroSliceConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceConstructor.h) |
| [cxx/unittest/MicroSliceHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceHeaderConstructor.cpp) |
| [cxx/unittest/MicroSliceHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceHeaderConstructor.h) |
| [cxx/unittest/MicroSliceHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceHeaderUnitTest.cpp) |
| [cxx/unittest/MicroSliceUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MicroSliceUnitTest.cpp) |
| [cxx/unittest/MilliSliceConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceConstructor.cpp) |
| [cxx/unittest/MilliSliceConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceConstructor.h) |
| [cxx/unittest/MilliSliceHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceHeaderConstructor.cpp) |
| [cxx/unittest/MilliSliceHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceHeaderConstructor.h) |
| [cxx/unittest/MilliSliceHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceHeaderUnitTest.cpp) |
| [cxx/unittest/MilliSliceUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/MilliSliceUnitTest.cpp) |
| [cxx/unittest/NanoSliceConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceConstructor.cpp) |
| [cxx/unittest/NanoSliceConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceConstructor.h) |
| [cxx/unittest/NanoSliceHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceHeaderConstructor.cpp) |
| [cxx/unittest/NanoSliceHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceHeaderConstructor.h) |
| [cxx/unittest/NanoSliceHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceHeaderUnitTest.cpp) |
| [cxx/unittest/NanoSliceUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/NanoSliceUnitTest.cpp) |
| [cxx/unittest/RawDAQDataConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataConstructor.cpp) |
| [cxx/unittest/RawDAQDataConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataConstructor.h) |
| [cxx/unittest/RawDAQDataUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataUnitTest.cpp) |
| [cxx/unittest/RawDAQDataUnitTest.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawDAQDataUnitTest.h) |
| [cxx/unittest/RawMilliSliceTests.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RawMilliSliceTests.cpp) |
| [cxx/unittest/RunHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RunHeaderConstructor.cpp) |
| [cxx/unittest/RunHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RunHeaderConstructor.h) |
| [cxx/unittest/RunHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/RunHeaderUnitTest.cpp) |
| [cxx/unittest/TimingMarkerConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TimingMarkerConstructor.cpp) |
| [cxx/unittest/TimingMarkerConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TimingMarkerConstructor.h) |
| [cxx/unittest/TimingMarkerUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TimingMarkerUnitTest.cpp) |
| [cxx/unittest/TriggerConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerConstructor.cpp) |
| [cxx/unittest/TriggerConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerConstructor.h) |
| [cxx/unittest/TriggerHeaderConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerHeaderConstructor.cpp) |
| [cxx/unittest/TriggerHeaderConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerHeaderConstructor.h) |
| [cxx/unittest/TriggerHeaderUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerHeaderUnitTest.cpp) |
| [cxx/unittest/TriggerMaskConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerMaskConstructor.cpp) |
| [cxx/unittest/TriggerMaskConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerMaskConstructor.h) |
| [cxx/unittest/TriggerMaskUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerMaskUnitTest.cpp) |
| [cxx/unittest/TriggerRangeConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerRangeConstructor.cpp) |
| [cxx/unittest/TriggerRangeConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerRangeConstructor.h) |
| [cxx/unittest/TriggerRangeUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerRangeUnitTest.cpp) |
| [cxx/unittest/TriggerTimeConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimeConstructor.cpp) |
| [cxx/unittest/TriggerTimeConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimeConstructor.h) |
| [cxx/unittest/TriggerTimeUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimeUnitTest.cpp) |
| [cxx/unittest/TriggerTimingMarkerConstructor.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimingMarkerConstructor.cpp) |
| [cxx/unittest/TriggerTimingMarkerConstructor.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimingMarkerConstructor.h) |
| [cxx/unittest/TriggerTimingMarkerUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerTimingMarkerUnitTest.cpp) |
| [cxx/unittest/TriggerUnitTest.cpp](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/TriggerUnitTest.cpp) |
| [cxx/unittest/UnitTestTrace.h](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/UnitTestTrace.h) |
| [cxx/unittest/ddfunittest.cc](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/cxx/unittest/ddfunittest.cc) |


## Existing documentation

| Source |
| --- |
| [doc/DataFormatsDoc/README](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/README) |
| [doc/DataFormatsDoc/beamdata.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/beamdata.tex) |
| [doc/DataFormatsDoc/config_block.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/config_block.tex) |
| [doc/DataFormatsDoc/datablock.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/datablock.tex) |
| [doc/DataFormatsDoc/event.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/event.tex) |
| [doc/DataFormatsDoc/general_macros.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/general_macros.tex) |
| [doc/DataFormatsDoc/intro.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/intro.tex) |
| [doc/DataFormatsDoc/meco.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/meco.tex) |
| [doc/DataFormatsDoc/method.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/method.tex) |
| [doc/DataFormatsDoc/microslice.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/microslice.tex) |
| [doc/DataFormatsDoc/milliblock.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/milliblock.tex) |
| [doc/DataFormatsDoc/millislice.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/millislice.tex) |
| [doc/DataFormatsDoc/models.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/models.tex) |
| [doc/DataFormatsDoc/monte_carlo_intro.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/monte_carlo_intro.tex) |
| [doc/DataFormatsDoc/nanoslice.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/nanoslice.tex) |
| [doc/DataFormatsDoc/nova-dataformatsdoc.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/nova-dataformatsdoc.tex) |
| [doc/DataFormatsDoc/overview.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/overview.tex) |
| [doc/DataFormatsDoc/physics_macros.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/physics_macros.tex) |
| [doc/DataFormatsDoc/run.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/run.tex) |
| [doc/DataFormatsDoc/summary_block.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/summary_block.tex) |
| [doc/DataFormatsDoc/trigger.tex](https://github.com/NovaDAQ/DAQDataFormats/blob/869a1fc336526c7cccb92bf7cbd31203745ce7c5/doc/DataFormatsDoc/trigger.tex) |
