# Package catalog

All **120** sibling repositories are included. Descriptions are source-derived; production ownership/lifecycle remains to be confirmed.

## Analysis

| Package | Purpose | Findings |
| --- | --- | --- |
| [ChannelDecoder](ChannelDecoder.md) | Qt utility for translating logical and electronics channel identifiers. | 0 |
| [DAQHit.old](DAQHit.old.md) | Legacy hit representation and extraction tools for raw files and shared-memory data. | 0 |
| [DetectorPlotter](DetectorPlotter.md) | Readers for DCS/round-robin data and tools producing time-series/ROOT diagnostic output. | 2 |
| [EventDump](EventDump.md) | Command-line tools to inspect run headers, events, configurations, trigger livetime, and incomplete data. | 0 |
| [EventMemoryViewer](EventMemoryViewer.md) | Qt tools for viewing event content from shared memory. | 0 |
| [EvtDispatcher_Viewer](EvtDispatcher_Viewer.md) | Legacy Qt shared-memory/event-dispatch viewer. | 0 |
| [HoughPoint.old](HoughPoint.old.md) | Legacy two-hit Hough-transform geometry representation. | 1 |
| [PedestalAnalysis_Scripts](PedestalAnalysis_Scripts.md) | ROOT/C++ pedestal, DSO, FFT, and plotting macros and orchestration scripts. | 1 |
| [RunCoord](RunCoord.md) | Run-coordination scripts for active/filled detector channels, POT, uptime, duration, and run lists. | 0 |
| [RunSummaryUtils](RunSummaryUtils.md) | Raw-file summary and trigger-count/timing tools plus FEB link-error extraction and ROOT macros. | 3 |


## Build and release

| Package | Purpose | Findings |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | SoftRelTools make fragments and release-building scripts used across the online packages. | 0 |
| [setup](setup.md) | Release/package manifests and SRT/UPS setup scripts for online environments. | 0 |
| [ups](ups.md) | UPS product dependencies and scripts for building, bootstrapping, tagging, and packaging novadaq. | 1 |


## Control

| Package | Purpose | Findings |
| --- | --- | --- |
| [DAQApplicationManager](DAQApplicationManager.md) | Qt process-management application with host/process grouping, status watchers, and a Run Control interface. | 0 |
| [DDTManager](DDTManager.md) | Qt application for managing data-driven trigger processes and monitoring their states. | 0 |
| [DatabaseUtils](DatabaseUtils.md) | Typed DAQ configuration, application-manager, DCS, and run-history database access plus configuration editors. | 0 |
| [NovaDAQConfiguration](NovaDAQConfiguration.md) | Configuration manager translating named/database settings and partition resources into per-application connection, hardware, and run XML. | 0 |
| [NovaDatabase](NovaDatabase.md) | Database table/row/column abstraction, CSV/SSV import-export tools, and schema scripts. | 0 |
| [NovaResourceManager](NovaResourceManager.md) | Qt TCP resource manager with partition reservation, resource XML persistence, and GUI clients. | 0 |
| [NovaResoureManager](NovaResoureManager.md) | Earlier, misspelled resource-manager package implementing RMS discovery/reserve/release handlers. | 0 |
| [NovaRunControl](NovaRunControl.md) | Run-control server, GUI/CLI clients, state machine, run configuration, and resource selection. | 0 |
| [NovaRunControlClient](NovaRunControlClient.md) | RMS-based run-control and global-trigger receivers with shared message-client connection management. | 1 |
| [NovaRunControlClient_OLD](NovaRunControlClient_OLD.md) | Historical Nova state-manager/client implementation. | 0 |
| [PixelMaskTool](PixelMaskTool.md) | Interface/tool for creating or updating pixel masks through the DAQ configuration layer. | 0 |
| [RunControlClient](RunControlClient.md) | Generic older run-control state manager and state-change listener. | 0 |
| [RunControlClient_OLD](RunControlClient_OLD.md) | Earlier generic run-control client with state-manager/listener tests. | 0 |


## Core libraries

| Package | Purpose | Findings |
| --- | --- | --- |
| [DAQChannelMap](DAQChannelMap.md) | Maps detector, plane, cell, DCM, FEB, and pixel identifiers for Far Detector, Near Detector, NDOS, and Test Beam geometries. | 0 |
| [DAQDataFormats](DAQDataFormats.md) | Versioned raw run, event, trigger, data-block, microslice, and nanoslice representations, checksums, and simulation helpers. | 0 |
| [DAQQualityCheck](DAQQualityCheck.md) | Checks internal consistency of raw events and, where enabled, run structures. | 0 |
| [NovaDAQConventions](NovaDAQConventions.md) | Shared detector/subdetector identifiers, run types, and string conversion conventions. | 0 |
| [NovaDAQUtilities](NovaDAQUtilities.md) | Shared process, cache, environment, location, partition, XML, time, and shared-memory conventions/utilities. | 0 |
| [NovaTimingUtilities](NovaTimingUtilities.md) | Converts UNIX, GPS-related, and NOvA clock representations and provides a conversion CLI. | 1 |
| [PackageVersion](PackageVersion.md) | Parses embedded package revision information and exposes version helper functions/macros. | 0 |
| [RawFileParser](RawFileParser.md) | Memory-mapped and file-I/O reader/indexer for NOvA run and event files. | 2 |


## Data path

| Package | Purpose | Findings |
| --- | --- | --- |
| [BufferNodeEVB](BufferNodeEVB.md) | Receives DCM millislices, assembles milliblocks in MegaPool, retains recent data, and selects windows requested by global triggers. | 1 |
| [DCMApplication](DCMApplication.md) | DCM state machine, hardware/simulated readers, monitoring, and dispatch of detector data to event-builder clients. | 0 |
| [DispatcherClient](DispatcherClient.md) | Framework client and event handle for receiving dispatched raw events into analysis modules. | 0 |
| [EventBuilder](EventBuilder.md) | Generic TCP event builder with per-connection circular buffers, event assembly, and reporting. | 0 |
| [EventBuilderClient](EventBuilderClient.md) | TCP connection and sender library for delivering subevents to EventBuilder. | 1 |
| [EventBuilderClient_OLD](EventBuilderClient_OLD.md) | Earlier event-builder client implementation and tests retained for historical compatibility. | 0 |
| [EventBuilder_OLD](EventBuilder_OLD.md) | Earlier generic event-builder implementation with connection-buffer and event-manager tests. | 0 |
| [EventDispatcher](EventDispatcher.md) | Qt event-dispatcher application with memory model, configuration window, and daemon support. | 0 |
| [EventDispatcher_Client](EventDispatcher_Client.md) | Packaged Qt event-dispatcher client and resources. | 0 |
| [EventDispatcher_Server](EventDispatcher_Server.md) | Standalone event-dispatch server with shared-memory inspection, dispatch threads, GUI, and pattern-source utility. | 0 |
| [EventDispatcher_Server_FMWK](EventDispatcher_Server_FMWK.md) | Framework-integrated event-dispatch server variant. | 0 |
| [NovaDataLogger](NovaDataLogger.md) | Receives selected event data, pools fragments, and writes versioned run/subrun streams to disk. | 1 |
| [NovaDataLogger_OLD](NovaDataLogger_OLD.md) | Earlier listener/event-manager data logger implementation. | 0 |
| [NovaEventBuilder](NovaEventBuilder.md) | NOvA-specific event assembly, selection, connection handling, and logger components layered on generic event building. | 0 |
| [NovaEventBuilderClient](NovaEventBuilderClient.md) | DCM client, reader, generator, and dispatcher for the NOvA event-builder path. | 1 |
| [NovaEventBuilderClient_OLD](NovaEventBuilderClient_OLD.md) | Historical NOvA DCM/event-builder client with generator tests. | 1 |
| [NovaEventBuilder_OLD](NovaEventBuilder_OLD.md) | Historical NOvA event builder and data-selector tests. | 0 |
| [SHM_Utilities](SHM_Utilities.md) | Utilities copying files/patterns to shared memory, dumping memory, and inspecting spill history. | 0 |
| [ShmMilliBlock](ShmMilliBlock.md) | Shared-memory wrapper for milliblock publication/consumption. | 0 |
| [ShmRdWr](ShmRdWr.md) | Shared-memory ring transport with grouped readers, semaphores, overwrite tracking, and inspection utilities. | 1 |


## Hardware

| Package | Purpose | Findings |
| --- | --- | --- |
| [DCMBootLoader](DCMBootLoader.md) | RedBoot/eCos build tree and NOvA PowerPC board support for DCM and TDU bootloaders. | 0 |
| [DCMGuiTools](DCMGuiTools.md) | Qt DCM register viewer with hexadecimal controls and register display widgets. | 0 |
| [DCM_ProgUtils](DCM_ProgUtils.md) | DCM/FEB register access, programming, DSO readout, timing, and temperature utilities. | 1 |
| [DCMulator](DCMulator.md) | USB/MATLAB-based DCM/FEB checkout and programming environment with USB support code and bundled libraries. | 0 |
| [DataConcentratorModule](DataConcentratorModule.md) | Earlier DCM userspace, CPLD/FPGA programming, and kernel-driver implementation. | 1 |
| [FEBCheckoutVerify](FEBCheckoutVerify.md) | FEB checkout verification and report tooling, including bundled Python imaging, XML, spreadsheet, and document libraries. | 0 |
| [NovaDAQCheckout](NovaDAQCheckout.md) | DAQ hardware checkout orchestration and GUI for DCM, FEB, APD, and process checks. | 0 |
| [NovaFirmware](NovaFirmware.md) | Versioned DCM, FEB, and TDU firmware images and associated configuration artifacts. | 0 |
| [PedestalDataRunner](PedestalDataRunner.md) | GUI/CLI DSO acquisition, selection, reprocessing, and pedestal-analysis workflow. | 0 |
| [dcm_kernel_module](dcm_kernel_module.md) | DCM Linux driver for control/status/data devices, FPGA access, DMA, and board utilities. | 1 |
| [dcm_linux_system](dcm_linux_system.md) | Instructions, patches, and source archives for rebuilding the DCM PowerPC toolchain and Linux userspace. | 0 |
| [linux_kernel_dcmtdu](linux_kernel_dcmtdu.md) | Full historical Linux kernel tree used for DCM/TDU platforms. | 0 |
| [tdu_kernel_module](tdu_kernel_module.md) | TDU Linux module with register/data operations, timing work, and driver documentation. | 0 |


## Messaging

| Package | Purpose | Findings |
| --- | --- | --- |
| [DAQMessages](DAQMessages.md) | DDS IDL contracts for Run Control, global triggers, DCS, DDT, spill, SNEWS, and supernova traffic, plus mailbox helpers and status codes. | 1 |
| [DAQMessagesZMQ](DAQMessagesZMQ.md) | ZeroMQ context/socket and typed mailbox wrappers with DDT and supernova message structures. | 1 |
| [DAQNetworkUtils](DAQNetworkUtils.md) | Header-only Qt SSH tunnel helper used by network-facing GUIs. | 0 |
| [DDSSimD](DDSSimD.md) | Simulation DDS implementation, demos, and generated reference documentation. | 0 |
| [EpicsProviderForMessaging](EpicsProviderForMessaging.md) | EPICS Channel Access servers and clients that carry RMS messaging through process variables. | 0 |
| [EventDispatcher_CommandSet](EventDispatcher_CommandSet.md) | Command and acknowledgement definitions shared by event-dispatcher components. | 0 |
| [NovaMessageDefinitions](NovaMessageDefinitions.md) | Earlier RMS/XML message classes and message-registration constants. | 0 |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | RMS producers/consumers, message/destination/status abstractions, DDS/EPICS/local providers, and XML support. | 2 |
| [XmlRpc](XmlRpc.md) | XML-RPC client/server, HTTP/socket dispatch, value serialization, and sample applications. | 0 |


## Monitoring

| Package | Purpose | Findings |
| --- | --- | --- |
| [Dashboard](Dashboard.md) | Python/Tk and PHP operational dashboard with message-analyzer launch and alarm/email helpers. | 0 |
| [ErrorHandler](ErrorHandler.md) | Message analyzer with rules, GUI, and actions that can send mail, scripts, or Run Control messages. | 0 |
| [NovaDAQLiveTimeMonitor](NovaDAQLiveTimeMonitor.md) | Scrapes ShmRdWrShow statistics and Run Control resource state into livetime logs. | 0 |
| [NovaDAQMonitor](NovaDAQMonitor.md) | DAQ/cluster monitoring state machine, RRD thresholds, Ganglia integration, and monitoring scripts. | 0 |
| [NovaDAQMonitorClient](NovaDAQMonitorClient.md) | Client library/service for publishing participant monitoring data to NovaDAQMonitor. | 0 |
| [NovaDAQMonitor_OLD](NovaDAQMonitor_OLD.md) | Earlier DAQ monitor, RRD storage, thresholds, and state-manager tests. | 0 |
| [NovaDaqDcs](NovaDaqDcs.md) | EPICS IOCs, detector-control records/widgets, PV archivers, and control-room launch utilities. | 0 |
| [NovaMessageLogger](NovaMessageLogger.md) | Status logger clients, listeners, and notification demonstrations using RMS. | 0 |
| [NovaPreSNShiftGUI](NovaPreSNShiftGUI.md) | GTK interface for monitoring a pre-supernova shift status file. | 0 |
| [NovaWANMonitor](NovaWANMonitor.md) | Ping source/receiver and site-monitor GUI for WAN connectivity checks. | 0 |
| [Trace](Trace.md) | Trace logging support and Qt trace-manager application. | 0 |
| [TriggerScalars](TriggerScalars.md) | Qt trigger scalar displays, listener/examiner threads, and visual counter widgets. | 0 |


## Operations

| Package | Purpose | Findings |
| --- | --- | --- |
| [AshRiver](AshRiver.md) | Site services: CM3350 Modbus alarm collection into SQLite, Raspberry Pi UPS shutdown monitoring, and a containerized Redmine instance. | 1 |
| [DAQClusterUtils](DAQClusterUtils.md) | Site-specific farm inventory, host checks, mount management, and message-logger balancing scripts. | 2 |
| [DAQOperationsTools](DAQOperationsTools.md) | Startup, shutdown, health checking, recovery, environment setup, and distributed process orchestration for DAQ services. | 1 |
| [FarDetectorPowerOn](FarDetectorPowerOn.md) | LaTeX recovery/power-on checklist and network validation helpers for the DAQ clusters. | 0 |
| [NovaControlRoom](NovaControlRoom.md) | Site- and workstation-specific desktop launchers, operator utilities, snapshots, and display setup. | 1 |
| [NovaDAQCrontab](NovaDAQCrontab.md) | Parses DAQ/cron configuration and drives scheduled operational commands. | 0 |
| [NovaRemoteControlRooms](NovaRemoteControlRooms.md) | Remote-control-room setup, SSH tunnels, gateway options, and one-button GUI helpers. | 0 |
| [PowerUtilities](PowerUtilities.md) | Detector power-supply, PDU, load-shedding, and power sequencing scripts. | 1 |


## Simulation and examples

| Package | Purpose | Findings |
| --- | --- | --- |
| [DAQSimulationManager](DAQSimulationManager.md) | Coordinates simulation modes, synthetic data sources, and trigger scheduling. | 0 |
| [DispatcherClientExampleApp](DispatcherClientExampleApp.md) | Qt example application for connecting to an event dispatcher. | 0 |
| [EvtDispatcher_PatternGenerator](EvtDispatcher_PatternGenerator.md) | Qt/shared-memory pattern producer used to exercise dispatching. | 0 |
| [ExternalPackageTest](ExternalPackageTest.md) | Small checks demonstrating integration of external libraries such as Boost, CppUnit, and Xerces. | 0 |
| [MockDataDAQ](MockDataDAQ.md) | Framework modules for simulated detector data, channel-map additions, and synthetic event timing. | 0 |
| [NDLTest](NDLTest.md) | Alternative/test data logger with event pooling and run-stream output. | 0 |
| [NovaDAQTemplate](NovaDAQTemplate.md) | C++/Python coding examples and package-layout/build templates. | 0 |
| [NovaDAQTemplate_OLD](NovaDAQTemplate_OLD.md) | Historical C++/Python package template and CppUnit examples. | 0 |
| [RootDAQTemplate](RootDAQTemplate.md) | Minimal ROOT-integrated online class and dictionary example. | 0 |
| [benchmarks](benchmarks.md) | Memory bandwidth, bit-reversal, stream, and memory-test programs with plotting helpers. | 0 |


## Storage and metadata

| Package | Purpose | Findings |
| --- | --- | --- |
| [FileTransferService](FileTransferService.md) | Twisted service coordinating metadata, SAM transfers, archive bundling, retries, and cleanup of completed files. | 3 |
| [MetaDataTools](MetaDataTools.md) | Extracts run-level metadata and validates header information from raw DAQ files. | 2 |
| [NovaFTS](NovaFTS.md) | Site configuration, metadata plugins, credential/setup helpers, and container deployment files for file transfer. | 2 |
| [NovaFileTransferSystem](NovaFileTransferSystem.md) | Earlier shell-based file discovery, copying, bundling, metadata, and transfer orchestration. | 1 |


## Timing and triggers

| Package | Purpose | Findings |
| --- | --- | --- |
| [NOvABeam](NOvABeam.md) | Beam bundle parsing and retrieval helpers, including XML and curl examples. | 0 |
| [NovaGlobalTrigger](NovaGlobalTrigger.md) | Global trigger service implementing calibration, data-driven, beam, manual, long-window, and SNEWS trigger flows. | 0 |
| [NovaSNEWSInterface](NovaSNEWSInterface.md) | SNEWS sender, XML-RPC forwarder/receiver, and DDS bridge to the global trigger. | 0 |
| [NovaSpillServer](NovaSpillServer.md) | Beam-spill/TCR receiver, forwarder, XML-RPC/DDS bridge, and TDU timing utilities. | 0 |
| [NovaSuperNova](NovaSuperNova.md) | Buffers hit-rate data, estimates background, processes candidate bursts, logs results, and sends supernova triggers. | 0 |
| [TDUControl](TDUControl.md) | Qt timing-control server/client, arm/register commands, synchronization, delay, GPS, and error monitoring. | 0 |
| [TDUControlClient](TDUControlClient.md) | Standalone Qt client for timing control. | 0 |
| [TDUUtilities](TDUUtilities.md) | TDU register/diagnostic commands and loading/validation of timing-delay constants. | 0 |
| [TDUWeb](TDUWeb.md) | Bottle HTTP wrapper around TDU status, timing-control, spill-history, and TCR commands. | 1 |
| [nova_gcn_trigger](nova_gcn_trigger.md) | C program bridging external GCN notices into the NOvA trigger workflow. | 0 |
