# Trace

Trace logging support and Qt trace-manager application.

## Identity and scope

Repository: [NovaDAQ/Trace](https://github.com/NovaDAQ/Trace) · Reviewed commit: `b646c76c0a0c311b7a7dd783580c0776b3d40513` · Domain: **Monitoring**.

Tracked files: **22**. Production deployment and owner are **unconfirmed**.

## Operation

Select trace levels and destinations deliberately; high-volume trace can affect throughput and disk use. Verify that changing verbosity reaches the intended process and restore normal levels after diagnosis.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/GNUmakefile) |
| [TraceManager/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/GNUmakefile) |
| [TraceManager/src/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/GNUmakefile) |
| [TraceManager/src/TraceManager.pro](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/TraceManager.pro) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [TraceManager/src/tracemanager.cc](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/tracemanager.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [TraceManager/include/AboutDialog.h](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/include/AboutDialog.h) | `AboutDialog` |
| [TraceManager/include/TraceManager.h](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/include/TraceManager.h) | `StandardMASKS`, `TraceManager` |
| [TraceManager/src/BitFields.h](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/BitFields.h) | Functions, constants, or templates |
| [cxx/include/Trace.h](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/include/Trace.h) | `s_traceControl`, `timeval` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `..` | [cxx/src/Trace.cpp:33](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/src/Trace.cpp#L33) |
| `QtCore` | [TraceManager/src/qrc_TraceManager.cpp:10](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/qrc_TraceManager.cpp#L10) |
| `QtGui` | [TraceManager/include/AboutDialog.h:4](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/include/AboutDialog.h#L4) |
| `QtNetwork` | [TraceManager/include/TraceManager.h:5](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/include/TraceManager.h#L5) |
| `linux` | [cxx/include/Trace.h:98](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/include/Trace.h#L98) |
| `messagefacility` | [cxx/include/Trace.h:23](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/include/Trace.h#L23) |
| `sys` | [TraceManager/src/BitFields.h:4](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/TraceManager/src/BitFields.h#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:14](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/GNUmakefile#L14) |


Direct consumers: [BufferNodeEVB](BufferNodeEVB.md), [DAQApplicationManager](DAQApplicationManager.md), [DAQSimulationManager](DAQSimulationManager.md), [DCMApplication](DCMApplication.md), [DCMGuiTools](DCMGuiTools.md), [DCM_ProgUtils](DCM_ProgUtils.md), [NDLTest](NDLTest.md), [NovaDaqDcs](NovaDaqDcs.md), [NovaDataLogger](NovaDataLogger.md), [NovaRunControl](NovaRunControl.md), [PedestalDataRunner](PedestalDataRunner.md), [TDUUtilities](TDUUtilities.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **5 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/TraceTest.cc](https://github.com/NovaDAQ/Trace/blob/b646c76c0a0c311b7a7dd783580c0776b3d40513/cxx/test/TraceTest.cc) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
