# Review coverage

Every repository was inventoried and its scoped code/build/operational surface assessed. Static-analysis input counts below do not imply every file was manually read or successfully parsed. No DAQ binary, hardware test, or live service was run.

| Package | Scope | C/C++ inputs | Shell inputs | Python parsed | Confirmed issues |
| --- | --- | --- | --- | --- | --- |
| [AshRiver](../packages/AshRiver.md) | static package review | 4 | 6 | 3 | NDAQ-002 |
| [BufferNodeEVB](../packages/BufferNodeEVB.md) | static package review | 30 | 4 | 8 | NDAQ-007 |
| [ChannelDecoder](../packages/ChannelDecoder.md) | static package review | 3 | 0 | 0 | None confirmed |
| [DAQApplicationManager](../packages/DAQApplicationManager.md) | static package review | 19 | 3 | 0 | None confirmed |
| [DAQChannelMap](../packages/DAQChannelMap.md) | static package review | 14 | 0 | 0 | None confirmed |
| [DAQClusterUtils](../packages/DAQClusterUtils.md) | static package review | 0 | 50 | 12 | NDAQ-024, NDAQ-025 |
| [DAQDataFormats](../packages/DAQDataFormats.md) | static package review | 191 | 0 | 0 | None confirmed |
| [DAQHit.old](../packages/DAQHit.old.md) | static package review | 3 | 0 | 0 | None confirmed |
| [DAQMessages](../packages/DAQMessages.md) | static package review | 0 | 0 | 0 | NDAQ-022 |
| [DAQMessagesZMQ](../packages/DAQMessagesZMQ.md) | static package review | 3 | 0 | 0 | NDAQ-023 |
| [DAQNetworkUtils](../packages/DAQNetworkUtils.md) | static package review | 0 | 0 | 0 | None confirmed |
| [DAQOperationsTools](../packages/DAQOperationsTools.md) | static package review | 2 | 152 | 9 | NDAQ-013 |
| [DAQQualityCheck](../packages/DAQQualityCheck.md) | static package review | 3 | 0 | 0 | None confirmed |
| [DAQSimulationManager](../packages/DAQSimulationManager.md) | static package review | 7 | 0 | 0 | None confirmed |
| [DCMApplication](../packages/DCMApplication.md) | static package review | 59 | 8 | 0 | None confirmed |
| [DCMBootLoader](../packages/DCMBootLoader.md) | bounded integration | 20 | 0 | 0 | None confirmed |
| [DCMGuiTools](../packages/DCMGuiTools.md) | static package review | 4 | 0 | 0 | None confirmed |
| [DCM_ProgUtils](../packages/DCM_ProgUtils.md) | static package review | 49 | 6 | 0 | NDAQ-017 |
| [DCMulator](../packages/DCMulator.md) | bounded integration | 6 | 10 | 0 | None confirmed |
| [DDSSimD](../packages/DDSSimD.md) | bounded integration | 15 | 0 | 0 | None confirmed |
| [DDTManager](../packages/DDTManager.md) | static package review | 18 | 0 | 0 | None confirmed |
| [Dashboard](../packages/Dashboard.md) | static package review | 0 | 4 | 1 | None confirmed |
| [DataConcentratorModule](../packages/DataConcentratorModule.md) | static package review | 9 | 0 | 0 | NDAQ-012 |
| [DatabaseUtils](../packages/DatabaseUtils.md) | static package review | 78 | 6 | 10 | None confirmed |
| [DetectorPlotter](../packages/DetectorPlotter.md) | static package review | 13 | 3 | 0 | NDAQ-011, NDAQ-040 |
| [DispatcherClient](../packages/DispatcherClient.md) | static package review | 3 | 0 | 0 | None confirmed |
| [DispatcherClientExampleApp](../packages/DispatcherClientExampleApp.md) | static package review | 3 | 0 | 0 | None confirmed |
| [EpicsProviderForMessaging](../packages/EpicsProviderForMessaging.md) | static package review | 9 | 2 | 0 | None confirmed |
| [ErrorHandler](../packages/ErrorHandler.md) | static package review | 43 | 5 | 0 | None confirmed |
| [EventBuilder](../packages/EventBuilder.md) | static package review | 20 | 0 | 0 | None confirmed |
| [EventBuilderClient](../packages/EventBuilderClient.md) | static package review | 6 | 0 | 0 | NDAQ-034 |
| [EventBuilderClient_OLD](../packages/EventBuilderClient_OLD.md) | static package review | 3 | 0 | 0 | None confirmed |
| [EventBuilder_OLD](../packages/EventBuilder_OLD.md) | static package review | 19 | 0 | 0 | None confirmed |
| [EventDispatcher](../packages/EventDispatcher.md) | static package review | 5 | 0 | 0 | None confirmed |
| [EventDispatcher_Client](../packages/EventDispatcher_Client.md) | static package review | 3 | 0 | 0 | None confirmed |
| [EventDispatcher_CommandSet](../packages/EventDispatcher_CommandSet.md) | static package review | 2 | 0 | 0 | None confirmed |
| [EventDispatcher_Server](../packages/EventDispatcher_Server.md) | static package review | 12 | 0 | 0 | None confirmed |
| [EventDispatcher_Server_FMWK](../packages/EventDispatcher_Server_FMWK.md) | static package review | 8 | 0 | 0 | None confirmed |
| [EventDump](../packages/EventDump.md) | static package review | 15 | 0 | 0 | None confirmed |
| [EventMemoryViewer](../packages/EventMemoryViewer.md) | static package review | 6 | 0 | 0 | None confirmed |
| [EvtDispatcher_PatternGenerator](../packages/EvtDispatcher_PatternGenerator.md) | static package review | 5 | 0 | 0 | None confirmed |
| [EvtDispatcher_Viewer](../packages/EvtDispatcher_Viewer.md) | static package review | 6 | 0 | 0 | None confirmed |
| [ExternalPackageTest](../packages/ExternalPackageTest.md) | static package review | 11 | 0 | 0 | None confirmed |
| [FEBCheckoutVerify](../packages/FEBCheckoutVerify.md) | bounded integration | 4 | 0 | 36 | None confirmed |
| [FarDetectorPowerOn](../packages/FarDetectorPowerOn.md) | static package review | 0 | 0 | 0 | None confirmed |
| [FileTransferService](../packages/FileTransferService.md) | static package review | 0 | 0 | 20 | NDAQ-015, NDAQ-016, NDAQ-028 |
| [HoughPoint.old](../packages/HoughPoint.old.md) | static package review | 1 | 0 | 0 | NDAQ-031 |
| [MetaDataTools](../packages/MetaDataTools.md) | static package review | 13 | 0 | 0 | NDAQ-008, NDAQ-009 |
| [MockDataDAQ](../packages/MockDataDAQ.md) | static package review | 3 | 0 | 0 | None confirmed |
| [NDLTest](../packages/NDLTest.md) | static package review | 26 | 0 | 0 | None confirmed |
| [NOvABeam](../packages/NOvABeam.md) | static package review | 6 | 0 | 0 | None confirmed |
| [NovaControlRoom](../packages/NovaControlRoom.md) | static package review | 0 | 563 | 6 | NDAQ-014 |
| [NovaDAQCheckout](../packages/NovaDAQCheckout.md) | static package review | 20 | 0 | 0 | None confirmed |
| [NovaDAQConfiguration](../packages/NovaDAQConfiguration.md) | static package review | 46 | 19 | 0 | None confirmed |
| [NovaDAQConventions](../packages/NovaDAQConventions.md) | static package review | 0 | 0 | 0 | None confirmed |
| [NovaDAQCrontab](../packages/NovaDAQCrontab.md) | static package review | 5 | 0 | 0 | None confirmed |
| [NovaDAQLiveTimeMonitor](../packages/NovaDAQLiveTimeMonitor.md) | static package review | 0 | 0 | 1 | None confirmed |
| [NovaDAQMonitor](../packages/NovaDAQMonitor.md) | static package review | 27 | 19 | 1 | None confirmed |
| [NovaDAQMonitorClient](../packages/NovaDAQMonitorClient.md) | static package review | 11 | 0 | 0 | None confirmed |
| [NovaDAQMonitor_OLD](../packages/NovaDAQMonitor_OLD.md) | static package review | 13 | 0 | 0 | None confirmed |
| [NovaDAQTemplate](../packages/NovaDAQTemplate.md) | static package review | 4 | 0 | 2 | None confirmed |
| [NovaDAQTemplate_OLD](../packages/NovaDAQTemplate_OLD.md) | static package review | 4 | 0 | 2 | None confirmed |
| [NovaDAQUtilities](../packages/NovaDAQUtilities.md) | static package review | 27 | 2 | 0 | None confirmed |
| [NovaDaqDcs](../packages/NovaDaqDcs.md) | static package review | 38 | 35 | 18 | None confirmed |
| [NovaDataLogger](../packages/NovaDataLogger.md) | static package review | 29 | 0 | 0 | NDAQ-003 |
| [NovaDataLogger_OLD](../packages/NovaDataLogger_OLD.md) | static package review | 10 | 0 | 0 | None confirmed |
| [NovaDatabase](../packages/NovaDatabase.md) | static package review | 16 | 11 | 0 | None confirmed |
| [NovaEventBuilder](../packages/NovaEventBuilder.md) | static package review | 12 | 0 | 0 | None confirmed |
| [NovaEventBuilderClient](../packages/NovaEventBuilderClient.md) | static package review | 8 | 0 | 0 | NDAQ-035 |
| [NovaEventBuilderClient_OLD](../packages/NovaEventBuilderClient_OLD.md) | static package review | 7 | 0 | 0 | NDAQ-036 |
| [NovaEventBuilder_OLD](../packages/NovaEventBuilder_OLD.md) | static package review | 9 | 0 | 0 | None confirmed |
| [NovaFTS](../packages/NovaFTS.md) | static package review | 0 | 17 | 8 | NDAQ-026, NDAQ-027 |
| [NovaFileTransferSystem](../packages/NovaFileTransferSystem.md) | static package review | 3 | 15 | 0 | NDAQ-030 |
| [NovaFirmware](../packages/NovaFirmware.md) | static package review | 0 | 0 | 0 | None confirmed |
| [NovaGlobalTrigger](../packages/NovaGlobalTrigger.md) | static package review | 36 | 6 | 0 | None confirmed |
| [NovaMessageDefinitions](../packages/NovaMessageDefinitions.md) | static package review | 1 | 0 | 0 | None confirmed |
| [NovaMessageLogger](../packages/NovaMessageLogger.md) | static package review | 1 | 0 | 0 | None confirmed |
| [NovaPreSNShiftGUI](../packages/NovaPreSNShiftGUI.md) | static package review | 1 | 0 | 0 | None confirmed |
| [NovaRemoteControlRooms](../packages/NovaRemoteControlRooms.md) | static package review | 0 | 6 | 3 | None confirmed |
| [NovaResourceManager](../packages/NovaResourceManager.md) | static package review | 10 | 0 | 0 | None confirmed |
| [NovaResoureManager](../packages/NovaResoureManager.md) | static package review | 2 | 0 | 0 | None confirmed |
| [NovaRunControl](../packages/NovaRunControl.md) | static package review | 21 | 4 | 0 | None confirmed |
| [NovaRunControlClient](../packages/NovaRunControlClient.md) | static package review | 10 | 5 | 0 | NDAQ-004 |
| [NovaRunControlClient_OLD](../packages/NovaRunControlClient_OLD.md) | static package review | 2 | 0 | 0 | None confirmed |
| [NovaSNEWSInterface](../packages/NovaSNEWSInterface.md) | static package review | 10 | 0 | 0 | None confirmed |
| [NovaSpillServer](../packages/NovaSpillServer.md) | static package review | 13 | 0 | 0 | None confirmed |
| [NovaSuperNova](../packages/NovaSuperNova.md) | static package review | 18 | 1 | 3 | None confirmed |
| [NovaTimingUtilities](../packages/NovaTimingUtilities.md) | static package review | 4 | 0 | 0 | NDAQ-032 |
| [NovaWANMonitor](../packages/NovaWANMonitor.md) | static package review | 7 | 0 | 0 | None confirmed |
| [PackageVersion](../packages/PackageVersion.md) | static package review | 3 | 0 | 0 | None confirmed |
| [PedestalAnalysis_Scripts](../packages/PedestalAnalysis_Scripts.md) | static package review | 28 | 1 | 0 | NDAQ-039 |
| [PedestalDataRunner](../packages/PedestalDataRunner.md) | static package review | 22 | 10 | 3 | None confirmed |
| [PixelMaskTool](../packages/PixelMaskTool.md) | static package review | 2 | 0 | 0 | None confirmed |
| [PowerUtilities](../packages/PowerUtilities.md) | static package review | 0 | 21 | 0 | NDAQ-029 |
| [RawFileParser](../packages/RawFileParser.md) | static package review | 1 | 0 | 0 | NDAQ-019, NDAQ-020 |
| [ResponsiveMessagingSystem](../packages/ResponsiveMessagingSystem.md) | static package review | 42 | 4 | 0 | NDAQ-005, NDAQ-006 |
| [RootDAQTemplate](../packages/RootDAQTemplate.md) | static package review | 1 | 0 | 0 | None confirmed |
| [RunControlClient](../packages/RunControlClient.md) | static package review | 5 | 0 | 0 | None confirmed |
| [RunControlClient_OLD](../packages/RunControlClient_OLD.md) | static package review | 4 | 0 | 0 | None confirmed |
| [RunCoord](../packages/RunCoord.md) | static package review | 0 | 0 | 12 | None confirmed |
| [RunSummaryUtils](../packages/RunSummaryUtils.md) | static package review | 16 | 0 | 0 | NDAQ-018, NDAQ-037, NDAQ-038 |
| [SHM_Utilities](../packages/SHM_Utilities.md) | static package review | 7 | 0 | 0 | None confirmed |
| [SRT_ONLINE](../packages/SRT_ONLINE.md) | static package review | 0 | 0 | 0 | None confirmed |
| [ShmMilliBlock](../packages/ShmMilliBlock.md) | static package review | 4 | 0 | 0 | None confirmed |
| [ShmRdWr](../packages/ShmRdWr.md) | static package review | 12 | 0 | 0 | NDAQ-010 |
| [TDUControl](../packages/TDUControl.md) | static package review | 19 | 0 | 0 | None confirmed |
| [TDUControlClient](../packages/TDUControlClient.md) | static package review | 3 | 0 | 0 | None confirmed |
| [TDUUtilities](../packages/TDUUtilities.md) | static package review | 16 | 8 | 0 | None confirmed |
| [TDUWeb](../packages/TDUWeb.md) | static package review | 0 | 0 | 1 | NDAQ-001 |
| [Trace](../packages/Trace.md) | static package review | 5 | 0 | 0 | None confirmed |
| [TriggerScalars](../packages/TriggerScalars.md) | static package review | 9 | 0 | 0 | None confirmed |
| [XmlRpc](../packages/XmlRpc.md) | static package review | 17 | 0 | 0 | None confirmed |
| [benchmarks](../packages/benchmarks.md) | static package review | 7 | 1 | 0 | None confirmed |
| [dcm_kernel_module](../packages/dcm_kernel_module.md) | static package review | 5 | 0 | 0 | NDAQ-021 |
| [dcm_linux_system](../packages/dcm_linux_system.md) | static package review | 0 | 0 | 0 | None confirmed |
| [linux_kernel_dcmtdu](../packages/linux_kernel_dcmtdu.md) | bounded integration | 1 | 0 | 0 | None confirmed |
| [nova_gcn_trigger](../packages/nova_gcn_trigger.md) | static package review | 1 | 0 | 0 | None confirmed |
| [setup](../packages/setup.md) | static package review | 0 | 5 | 0 | None confirmed |
| [tdu_kernel_module](../packages/tdu_kernel_module.md) | static package review | 1 | 0 | 0 | None confirmed |
| [ups](../packages/ups.md) | static package review | 0 | 5 | 0 | NDAQ-033 |
