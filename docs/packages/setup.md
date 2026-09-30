# setup

Release/package manifests and SRT/UPS setup scripts for online environments.

## Identity and scope

Repository: [NovaDAQ/setup](https://github.com/NovaDAQ/setup) · Reviewed commit: `05629b5b12121fb0b095b53577cfdbd35f8bbe7d` · Domain: **Build and release**.

Tracked files: **234**. Production deployment and owner are **unconfirmed**.

## Operation

Select a coherent release manifest and architecture/qualifier. Source the matching shell variant in a fresh environment, verify resolved paths/product versions, and preserve the prior release selection for rollback.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [resolve_baserel_link.csh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/resolve_baserel_link.csh) |
| [resolve_baserel_link.sh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/resolve_baserel_link.sh) |
| [setup_novadaq_jenkins.sh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/setup_novadaq_jenkins.sh) |
| [setup_novadaq_meta_nt1.sh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/setup_novadaq_meta_nt1.sh) |
| [setup_srt_ups.csh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/setup_srt_ups.csh) |
| [setup_srt_ups.sh](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/setup_srt_ups.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [BufferNodeEVB](BufferNodeEVB.md) | release manifest | [nova-online-packages-FD01_00_00:12](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L12) |
| [DAQApplicationManager](DAQApplicationManager.md) | release manifest | [nova-online-packages-FD01_00_00:13](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L13) |
| [DAQChannelMap](DAQChannelMap.md) | release manifest | [nova-online-packages-FD01_00_00:14](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L14) |
| [DAQDataFormats](DAQDataFormats.md) | release manifest | [nova-online-packages-FD01_00_00:15](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L15) |
| [DAQMessages](DAQMessages.md) | release manifest | [nova-online-packages-FD01_00_00:16](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L16) |
| [DAQMessagesZMQ](DAQMessagesZMQ.md) | release manifest | [nova-online-packages-R17_01_00:17](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-R17_01_00#L17) |
| [DAQNetworkUtils](DAQNetworkUtils.md) | release manifest | [nova-online-packages-FD02_01_00:17](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD02_01_00#L17) |
| [DAQOperationsTools](DAQOperationsTools.md) | release manifest | [nova-online-packages-FD01_00_00:17](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L17) |
| [DAQQualityCheck](DAQQualityCheck.md) | release manifest | [nova-online-packages-FD01_00_00:18](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L18) |
| [DAQSimulationManager](DAQSimulationManager.md) | release manifest | [nova-online-packages-FD01_00_00:19](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L19) |
| [DCMApplication](DCMApplication.md) | release manifest | [nova-online-packages-FD01_00_00:21](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L21) |
| [DCMBootLoader](DCMBootLoader.md) | release manifest | [nova-online-packages-FD01_00_00:22](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L22) |
| [DCM_ProgUtils](DCM_ProgUtils.md) | release manifest | [nova-online-packages-FD01_00_00:23](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L23) |
| [DDTManager](DDTManager.md) | release manifest | [nova-online-packages-FD04_00_00:25](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD04_00_00#L25) |
| [DatabaseUtils](DatabaseUtils.md) | release manifest | [nova-online-packages-FD01_00_00:20](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L20) |
| [DispatcherClientExampleApp](DispatcherClientExampleApp.md) | release manifest | [nova-online-packages-FD01_00_00:24](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L24) |
| [ErrorHandler](ErrorHandler.md) | release manifest | [nova-online-packages-FD01_00_00:25](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L25) |
| [EventBuilderClient](EventBuilderClient.md) | release manifest | [nova-online-packages-FD01_00_00:26](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L26) |
| [EventDispatcher](EventDispatcher.md) | release manifest | [nova-online-packages-FD01_00_00:27](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L27) |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | release manifest | [nova-online-packages-FD01_00_00:30](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L30) |
| [EventDispatcher_Server](EventDispatcher_Server.md) | release manifest | [nova-online-packages-FD01_00_00:28](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L28) |
| [EventDispatcher_Server_FMWK](EventDispatcher_Server_FMWK.md) | release manifest | [nova-online-packages-FD01_00_00:29](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L29) |
| [EventDump](EventDump.md) | release manifest | [nova-online-packages-FD01_00_00:33](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L33) |
| [EventMemoryViewer](EventMemoryViewer.md) | release manifest | [nova-online-packages-FD01_00_00:31](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L31) |
| [ExternalPackageTest](ExternalPackageTest.md) | release manifest | [nova-online-packages-FD01_00_00:34](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L34) |
| [MetaDataTools](MetaDataTools.md) | release manifest | [nova-online-packages-FD01_00_00:36](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L36) |
| [NDLTest](NDLTest.md) | release manifest | [nova-online-packages-FD01_00_00:37](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L37) |
| [NovaDAQCheckout](NovaDAQCheckout.md) | release manifest | [nova-online-packages-FD02_03_00:39](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD02_03_00#L39) |
| [NovaDAQConfiguration](NovaDAQConfiguration.md) | release manifest | [nova-online-packages-FD01_00_00:38](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L38) |
| [NovaDAQConventions](NovaDAQConventions.md) | release manifest | [nova-online-packages-FD01_00_00:39](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L39) |
| [NovaDAQMonitor](NovaDAQMonitor.md) | release manifest | [nova-online-packages-FD01_00_00:41](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L41) |
| [NovaDAQMonitorClient](NovaDAQMonitorClient.md) | release manifest | [nova-online-packages-FD01_00_00:42](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L42) |
| [NovaDAQTemplate](NovaDAQTemplate.md) | release manifest | [nova-online-packages-FD01_00_00:43](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L43) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | release manifest | [nova-online-packages-FD01_00_00:44](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L44) |
| [NovaDaqDcs](NovaDaqDcs.md) | release manifest | [nova-online-packages-FD01_00_00:40](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L40) |
| [NovaDataLogger](NovaDataLogger.md) | release manifest | [nova-online-packages-FD01_00_01:37](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_01#L37) |
| [NovaDatabase](NovaDatabase.md) | release manifest | [nova-online-packages-FD01_00_00:45](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L45) |
| [NovaFileTransferSystem](NovaFileTransferSystem.md) | release manifest | [nova-online-packages-FD01_00_00:46](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L46) |
| [NovaGlobalTrigger](NovaGlobalTrigger.md) | release manifest | [nova-online-packages-FD01_00_00:47](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L47) |
| [NovaMessageLogger](NovaMessageLogger.md) | release manifest | [nova-online-packages-FD01_00_00:48](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L48) |
| [NovaResourceManager](NovaResourceManager.md) | release manifest | [nova-online-packages-FD01_00_00:49](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L49) |
| [NovaRunControl](NovaRunControl.md) | release manifest | [nova-online-packages-FD01_00_00:50](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L50) |
| [NovaRunControlClient](NovaRunControlClient.md) | release manifest | [nova-online-packages-FD01_00_00:51](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L51) |
| [NovaSNEWSInterface](NovaSNEWSInterface.md) | release manifest | [nova-online-packages-R05_00_00:55](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-R05_00_00#L55) |
| [NovaSpillServer](NovaSpillServer.md) | release manifest | [nova-online-packages-FD01_00_00:52](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L52) |
| [NovaSuperNova](NovaSuperNova.md) | release manifest | [nova-online-packages-R07_00_00:57](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-R07_00_00#L57) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | release manifest | [nova-online-packages-FD01_00_00:53](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L53) |
| [PackageVersion](PackageVersion.md) | release manifest | [nova-online-packages-FD01_00_00:54](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L54) |
| [PedestalDataRunner](PedestalDataRunner.md) | release manifest | [nova-online-packages-FD01_00_00:55](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L55) |
| [PowerUtilities](PowerUtilities.md) | release manifest | [nova-online-packages-FD01_00_00:56](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L56) |
| [RawFileParser](RawFileParser.md) | release manifest | [nova-online-packages-FD01_00_00:32](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L32) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | release manifest | [nova-online-packages-FD01_00_00:11](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L11) |
| [SHM_Utilities](SHM_Utilities.md) | release manifest | [nova-online-packages-FD01_00_00:57](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L57) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:7](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/GNUmakefile#L7) |
| [SRT_ONLINE](SRT_ONLINE.md) | release manifest | [nova-online-packages-FD01_00_00:4](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L4) |
| [ShmMilliBlock](ShmMilliBlock.md) | release manifest | [nova-online-packages-FD01_00_00:58](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L58) |
| [ShmRdWr](ShmRdWr.md) | release manifest | [nova-online-packages-FD01_00_00:59](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L59) |
| [TDUControl](TDUControl.md) | release manifest | [nova-online-packages-FD01_00_00:61](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L61) |
| [TDUControlClient](TDUControlClient.md) | release manifest | [nova-online-packages-FD01_00_00:62](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L62) |
| [TDUUtilities](TDUUtilities.md) | release manifest | [nova-online-packages-FD01_00_00:63](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L63) |
| [TDUWeb](TDUWeb.md) | release manifest | [nova-online-packages-R07_00_00:69](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-R07_00_00#L69) |
| [Trace](Trace.md) | release manifest | [nova-online-packages-FD01_00_00:64](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L64) |
| [TriggerScalars](TriggerScalars.md) | release manifest | [nova-online-packages-FD01_00_00:65](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L65) |
| [XmlRpc](XmlRpc.md) | release manifest | [nova-online-packages-Online_development-Offline_S09.09.19:57](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-Online_development-Offline_S09.09.19#L57) |
| [benchmarks](benchmarks.md) | release manifest | [nova-online-packages-FD01_00_00:8](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L8) |
| [dcm_kernel_module](dcm_kernel_module.md) | release manifest | [nova-online-packages-FD01_00_00:9](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L9) |
| [linux_kernel_dcmtdu](linux_kernel_dcmtdu.md) | release manifest | [nova-online-packages-FD01_00_00:35](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L35) |
| [nova_gcn_trigger](nova_gcn_trigger.md) | release manifest | [nova-online-packages-R15_00_00:71](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-R15_00_00#L71) |
| [tdu_kernel_module](tdu_kernel_module.md) | release manifest | [nova-online-packages-FD01_00_00:60](https://github.com/NovaDAQ/setup/blob/05629b5b12121fb0b095b53577cfdbd35f8bbe7d/nova-online-packages-FD01_00_00#L60) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **5 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
