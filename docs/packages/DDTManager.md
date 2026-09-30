# DDTManager

Qt application for managing data-driven trigger processes and monitoring their states.

## Identity and scope

Repository: [NovaDAQ/DDTManager](https://github.com/NovaDAQ/DDTManager) · Reviewed commit: `c028da53626cb4ca611c3d8e8780efa7ed78fa0c` · Domain: **Control**.

Tracked files: **45**. Production deployment and owner are **unconfirmed**.

## Operation

Check configured hosts, process definitions, partition, and status-message freshness before group operations. Validate expected DDT instance counts and trigger delivery downstream after restart.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/DDTManager.cc](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/DDTManager.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/ApplicationGroupBox.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ApplicationGroupBox.h) | `ApplicationGroupBox` |
| [cxx/include/CustomTabWidget.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/CustomTabWidget.h) | `CustomTabWidget` |
| [cxx/include/DAQProcessPanel.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/DAQProcessPanel.h) | `DAQProcessPanel` |
| [cxx/include/KrbTicketRenewer.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/KrbTicketRenewer.h) | `KrbTicketRenewer` |
| [cxx/include/LayeredSubsystemDisplay.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/LayeredSubsystemDisplay.h) | `LayeredSubsystemDisplay` |
| [cxx/include/PSBroker.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/PSBroker.h) | `PSBroker` |
| [cxx/include/PSRunner.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/PSRunner.h) | `PSRunner` |
| [cxx/include/ProcessGroupWidget.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ProcessGroupWidget.h) | `ProcessGroupWidget` |
| [cxx/include/ProcessStates.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ProcessStates.h) | `ProcessStates` |
| [cxx/include/ProcessWidget.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ProcessWidget.h) | `ProcessWidget` |
| [cxx/include/RCHandler.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RCHandler.h) | `RCHandler` |
| [cxx/include/RmsReceiverDemultiplexer.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RmsReceiverDemultiplexer.h) | `RmsReceiverDemultiplexer` |
| [cxx/include/RunningProcessWatchdog.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RunningProcessWatchdog.h) | `RunningProcessWatchdog` |
| [cxx/include/ShellCommand.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ShellCommand.h) | `ShellCommand` |
| [cxx/include/ShellCommandSet.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ShellCommandSet.h) | `ShellCommandSet` |
| [cxx/include/SimpleGroup.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/SimpleGroup.h) | `SimpleGroup` |
| [cxx/include/StatusMessageWatchdog.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/StatusMessageWatchdog.h) | `StatusMessageWatchdog` |
| [cxx/include/SubsystemGroupBox.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/SubsystemGroupBox.h) | `SubsystemGroupBox` |
| [cxx/include/TabDisplay.h](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/TabDisplay.h) | `TabDisplay` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/DDTConfig.xml](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/config/DDTConfig.xml) |
| [config/DDTConfig.xsd](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/config/DDTConfig.xsd) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/include/ApplicationGroupBox.h:8](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ApplicationGroupBox.h#L8) |
| `QtGui` | [cxx/include/ApplicationGroupBox.h:9](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ApplicationGroupBox.h#L9) |
| `boost` | [cxx/include/KrbTicketRenewer.h:5](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/KrbTicketRenewer.h#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQMessages"]
  p1["DAQOperationsTools"]
  p2["DDTManager"]
  p3["DatabaseUtils"]
  p4["NovaDAQUtilities"]
  p5["NovaResourceManager"]
  p6["NovaRunControlClient"]
  p7["ResponsiveMessagingSystem"]
  p2 --> p0
  p2 --> p1
  p2 --> p3
  p2 --> p4
  p2 --> p5
  p2 --> p6
  p2 --> p7
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQMessages](DAQMessages.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile#L36) |
| [DAQMessages](DAQMessages.md) | source include | [cxx/include/RCHandler.h:5](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RCHandler.h#L5) |
| [DAQOperationsTools](DAQOperationsTools.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile#L36) |
| [DAQOperationsTools](DAQOperationsTools.md) | source include | [cxx/src/TabDisplay.cpp:24](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/TabDisplay.cpp#L24) |
| [DatabaseUtils](DatabaseUtils.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile#L36) |
| [DatabaseUtils](DatabaseUtils.md) | source include | [cxx/include/ApplicationGroupBox.h:7](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/ApplicationGroupBox.h#L7) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile#L36) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | source include | [cxx/include/KrbTicketRenewer.h:4](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/KrbTicketRenewer.h#L4) |
| [NovaResourceManager](NovaResourceManager.md) | build link | [cxx/src/GNUmakefile:36](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/GNUmakefile#L36) |
| [NovaResourceManager](NovaResourceManager.md) | source include | [cxx/src/RCHandler.cpp:10](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/src/RCHandler.cpp#L10) |
| [NovaRunControlClient](NovaRunControlClient.md) | source include | [cxx/include/RCHandler.h:4](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RCHandler.h#L4) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | source include | [cxx/include/RmsReceiverDemultiplexer.h:4](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/cxx/include/RmsReceiverDemultiplexer.h#L4) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/DDTManager/blob/c028da53626cb4ca611c3d8e8780efa7ed78fa0c/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **18 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
