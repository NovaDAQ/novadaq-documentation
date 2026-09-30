# ResponsiveMessagingSystem

RMS producers/consumers, message/destination/status abstractions, DDS/EPICS/local providers, and XML support.

## Identity and scope

Repository: [NovaDAQ/ResponsiveMessagingSystem](https://github.com/NovaDAQ/ResponsiveMessagingSystem) · Reviewed commit: `e7d72bb3b45279b9564d1dced3725428c3873eba` · Domain: **Messaging**.

Tracked files: **160**. Production deployment and owner are **unconfirmed**.

## Operation

Select one compatible provider/configuration and consistent destination/partition names. Monitor request/reply timeouts and test stale replies, fragmented messages, listener removal, and shutdown under load.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/CMakeLists.txt) |
| [GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/GNUmakefile) |
| [cxx/CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/CMakeLists.txt) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/GNUmakefile) |
| [cxx/src/CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/CMakeLists.txt) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/GNUmakefile) |
| [cxx/src/base/CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/base/CMakeLists.txt) |
| [cxx/src/base/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/base/GNUmakefile) |
| [cxx/src/provider/CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/provider/CMakeLists.txt) |
| [cxx/src/provider/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/provider/GNUmakefile) |
| [cxx/src/util/CMakeLists.txt](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/util/CMakeLists.txt) |
| [cxx/src/util/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/util/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/GNUmakefile) |
| [cxx/test/rmsexample/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/rmsexample/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/ClientListenerLoop.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/ClientListenerLoop.h) | `ClientListenerLoop` |
| [cxx/include/MessageFilter.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/MessageFilter.h) | `MessageFilter` |
| [cxx/include/RmsConsumer.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/RmsConsumer.h) | `RmsConsumer` |
| [cxx/include/RmsMessageListener.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/RmsMessageListener.h) | `RmsMessageListener` |
| [cxx/include/RmsProducer.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/RmsProducer.h) | `RmsProducer` |
| [cxx/include/RmsReceiver.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/RmsReceiver.h) | `ListenerLoop`, `RmsDummyListener`, `RmsReceiver` |
| [cxx/include/RmsSender.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/RmsSender.h) | `RmsSender` |
| [cxx/include/base/RmsCloseable.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsCloseable.h) | `RmsCloseable` |
| [cxx/include/base/RmsDestination.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsDestination.h) | `RmsDestination` |
| [cxx/include/base/RmsMessage.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsMessage.h) | `RmsMessage` |
| [cxx/include/base/RmsMessageBody.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsMessageBody.h) | `RmsMessageBody` |
| [cxx/include/base/RmsMessageSource.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsMessageSource.h) | `RmsMessageSource` |
| [cxx/include/base/RmsRuntimeException.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsRuntimeException.h) | `RmsExitingProcessException`, `RmsNotConnectedException`, `RmsRuntimeException` |
| [cxx/include/base/RmsStatus.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/base/RmsStatus.h) | `RmsStatus` |
| [cxx/include/provider/BufferedProviderListener.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/BufferedProviderListener.h) | `BufferedProviderListener` |
| [cxx/include/provider/CETDDS.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/CETDDS.h) | `DPSingleton`, `timeval` |
| [cxx/include/provider/CheckStatus.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/CheckStatus.h) | Functions, constants, or templates |
| [cxx/include/provider/DDSConnection.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/DDSConnection.h) | `DDSConnection`, `timeval` |
| [cxx/include/provider/EpicsConnection.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/EpicsConnection.h) | `EpicsConnection`, `ca_client_context` |
| [cxx/include/provider/EpicsMessenger.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/EpicsMessenger.h) | `EpicsMessenger`, `ca_client_context` |
| [cxx/include/provider/LocalhostConnection.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/LocalhostConnection.h) | `ListenerContainer`, `LocalhostConnection` |
| [cxx/include/provider/MessageAssembler.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/MessageAssembler.h) | `MessageAssembler` |
| [cxx/include/provider/MessageFragment.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/MessageFragment.h) | `MessageFragment`, `fragmentHeader` |
| [cxx/include/provider/MessageSplitter.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/MessageSplitter.h) | `MessageSplitter` |
| [cxx/include/provider/ProcessSignalHandler.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/ProcessSignalHandler.h) | `Notifiable`, `ProcessSignalHandler`, `ProcessSignalHandlerDeleter`, `RmsLockable`, `SignalInhibitor`, `sigaction` |
| [cxx/include/provider/ProviderListener.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/ProviderListener.h) | `ProviderListener` |
| [cxx/include/provider/RmsConnection.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/RmsConnection.h) | `RmsConnection` |
| [cxx/include/provider/RmsConnectionFactory.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/RmsConnectionFactory.h) | `RmsConnectionFactory` |
| [cxx/include/util/LinkedBlockingQueue.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/LinkedBlockingQueue.h) | Functions, constants, or templates |
| [cxx/include/util/ReentrantGetEnv.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/ReentrantGetEnv.h) | Functions, constants, or templates |
| [cxx/include/util/Runnable.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/Runnable.h) | `Runnable` |
| [cxx/include/util/Sha1.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/Sha1.h) | Functions, constants, or templates |
| [cxx/include/util/ThreadWrapper.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/ThreadWrapper.h) | `ThreadWrapper` |
| [cxx/include/util/TimeUtils.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/TimeUtils.h) | `TimeUtils` |
| [cxx/include/util/UUIDGenerator.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/UUIDGenerator.h) | `UUIDGenerator`, `timeval` |
| [cxx/include/util/trace.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/trace.h) | `e_traceIoctl`, `s_traceControl`, `s_traceEntry`, `s_tracePrint`, `timeval`, `tm` |
| [cxx/include/util/trace_intr.h](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/trace_intr.h) | Functions, constants, or templates |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/RmsCastorMap.xml](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/config/RmsCastorMap.xml) |
| [config/RmsExampleMessages.idl](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/config/RmsExampleMessages.idl) |
| [config/RmsExampleMessages.xsd](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/config/RmsExampleMessages.xsd) |
| [config/RmsMessageCore.idl](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/config/RmsMessageCore.idl) |
| [config/RmsMessageSchema.xsd](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/config/RmsMessageSchema.xsd) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `HOSTNAME` | [cxx/test/RmsConsumerAsyncExample.cc:118](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsConsumerAsyncExample.cc#L118) |
| `RMS_DEBUG` | [cxx/src/provider/DDSConnection.cpp:45](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/provider/DDSConnection.cpp#L45) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `asm` | [cxx/include/util/trace.h:221](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/trace.h#L221) |
| `boost` | [cxx/include/ClientListenerLoop.h:9](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/ClientListenerLoop.h#L9) |
| `cppunit` | [cxx/unittest/BaseRmsMessageTest.cc:2](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/unittest/BaseRmsMessageTest.cc#L2) |
| `dds` | [cxx/include/provider/CETDDS.h:27](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/CETDDS.h#L27) |
| `linux` | [cxx/include/util/trace.h:21](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/util/trace.h#L21) |
| `netinet` | [cxx/src/provider/MessageFragment.cpp:2](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/provider/MessageFragment.cpp#L2) |
| `rmsexample` | [cxx/test/RmsBroadcastSenderAndReceiver.cc:7](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsBroadcastSenderAndReceiver.cc#L7) |
| `sys` | [cxx/include/provider/CETDDS.h:23](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/provider/CETDDS.h#L23) |
| `xsd` | [cxx/src/ClientListenerLoop.cpp:3](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/ClientListenerLoop.cpp#L3) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["NovaDAQUtilities"]
  p1["ResponsiveMessagingSystem"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | build link | [cxx/src/CMakeLists.txt:24](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/CMakeLists.txt#L24) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | source include | [cxx/include/ClientListenerLoop.h:4](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/include/ClientListenerLoop.h#L4) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test include | [cxx/test/FullTest.cc:1](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/FullTest.cc#L1) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test link | [cxx/test/GNUmakefile:35](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/GNUmakefile#L35) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/GNUmakefile#L10) |


Direct consumers: [BufferNodeEVB](BufferNodeEVB.md), [DAQApplicationManager](DAQApplicationManager.md), [DAQMessages](DAQMessages.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMApplication](DCMApplication.md), [DDTManager](DDTManager.md), [ErrorHandler](ErrorHandler.md), [EventBuilder_OLD](EventBuilder_OLD.md), [NDLTest](NDLTest.md), [NovaDAQConfiguration](NovaDAQConfiguration.md), [NovaDAQMonitor_OLD](NovaDAQMonitor_OLD.md), [NovaDataLogger](NovaDataLogger.md), [NovaDataLogger_OLD](NovaDataLogger_OLD.md), [NovaEventBuilder](NovaEventBuilder.md), [NovaEventBuilderClient](NovaEventBuilderClient.md), [NovaEventBuilderClient_OLD](NovaEventBuilderClient_OLD.md), [NovaEventBuilder_OLD](NovaEventBuilder_OLD.md), [NovaGlobalTrigger](NovaGlobalTrigger.md), [NovaMessageDefinitions](NovaMessageDefinitions.md), [NovaResourceManager](NovaResourceManager.md), [NovaResoureManager](NovaResoureManager.md), [NovaRunControl](NovaRunControl.md), [NovaRunControlClient](NovaRunControlClient.md), [NovaRunControlClient_OLD](NovaRunControlClient_OLD.md), [NovaSNEWSInterface](NovaSNEWSInterface.md), [NovaSpillServer](NovaSpillServer.md), [NovaSuperNova](NovaSuperNova.md), [SRT_ONLINE](SRT_ONLINE.md), [TDUControl](TDUControl.md), [TDUUtilities](TDUUtilities.md), [TriggerScalars](TriggerScalars.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **42 C/C++ translation units**, **4 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-005: Advance reply-map iterator safely when expiring requests](../review/issues/NDAQ-005.md) | [Issue](https://github.com/NovaDAQ/ResponsiveMessagingSystem/issues/1) |
| P1 | [NDAQ-006: Delete the completed EPICS assembler before invalidating its iterator](../review/issues/NDAQ-006.md) | [Issue](https://github.com/NovaDAQ/ResponsiveMessagingSystem/issues/2) |


Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/BasicTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/BasicTest.cc) |
| [cxx/test/DestinationTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/DestinationTest.cc) |
| [cxx/test/DestructorTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/DestructorTest.cc) |
| [cxx/test/EpicsConnectionTestPublisher.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/EpicsConnectionTestPublisher.cc) |
| [cxx/test/EpicsConnectionTestSubscriber.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/EpicsConnectionTestSubscriber.cc) |
| [cxx/test/EpicsMessengerTestPublisher.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/EpicsMessengerTestPublisher.cc) |
| [cxx/test/EpicsMessengerTestSubscriber.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/EpicsMessengerTestSubscriber.cc) |
| [cxx/test/FullTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/FullTest.cc) |
| [cxx/test/MessageAssemblerTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/MessageAssemblerTest.cc) |
| [cxx/test/MessageFragmentTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/MessageFragmentTest.cc) |
| [cxx/test/MessageSplitterTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/MessageSplitterTest.cc) |
| [cxx/test/RmsBroadcastSenderAndReceiver.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsBroadcastSenderAndReceiver.cc) |
| [cxx/test/RmsConsumerAsyncExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsConsumerAsyncExample.cc) |
| [cxx/test/RmsConsumerExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsConsumerExample.cc) |
| [cxx/test/RmsProducerAsyncExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsProducerAsyncExample.cc) |
| [cxx/test/RmsProducerExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsProducerExample.cc) |
| [cxx/test/RmsReceiverAsyncExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsReceiverAsyncExample.cc) |
| [cxx/test/RmsReceiverExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsReceiverExample.cc) |
| [cxx/test/RmsSendAndReceive.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsSendAndReceive.cc) |
| [cxx/test/RmsSenderExample.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/RmsSenderExample.cc) |
| [cxx/test/UUIDGeneratorTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/UUIDGeneratorTest.cc) |
| [cxx/test/rms-test-common-functions.sh](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/rms-test-common-functions.sh) |
| [cxx/test/rms-test-sender-functions.sh](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/rms-test-sender-functions.sh) |
| [cxx/test/runNDOSDCMMulticastTest.sh](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/runNDOSDCMMulticastTest.sh) |
| [cxx/test/runNDOSFarmNodeMulticastTest.sh](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/test/runNDOSFarmNodeMulticastTest.sh) |
| [cxx/unittest/BaseRmsMessageTest.cc](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/unittest/BaseRmsMessageTest.cc) |


## Existing documentation

| Source |
| --- |
| [README_BUILD](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/README_BUILD) |
