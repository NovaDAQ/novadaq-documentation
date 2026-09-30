# EvtDispatcher_Viewer

Legacy Qt shared-memory/event-dispatch viewer.

## Identity and scope

Repository: [NovaDAQ/EvtDispatcher_Viewer](https://github.com/NovaDAQ/EvtDispatcher_Viewer) · Reviewed commit: `dbc09a158fd3c687d1918dfaf144340ffad948b6` · Domain: **Analysis**.

Tracked files: **24**. Production deployment and owner are **unconfirmed**.

## Operation

Select the correct memory source and validate the displayed pattern/event against its producer. Keep this viewer's protocol dependencies distinct from similarly named packaged clients.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

| Build definition |
| --- |
| [EventMemoryViewer.pro](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/EventMemoryViewer.pro) |
| [Makefile](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [main.cc](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/main.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [AboutDialog.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/AboutDialog.h) | `AboutDialog` |
| [DataSegment.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/DataSegment.h) | `nova_data`, `nova_data_header`, `nova_segment_header`, `segmentIdent` |
| [EvtDispatcher_Viewer.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/EvtDispatcher_Viewer.h) | `EvtDispatcher_Viewer` |
| [MemoryModel.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/MemoryModel.h) | `MemoryModel` |
| [MemoryViewer.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/MemoryViewer.h) | `MemoryViewer` |
| [daemon_init.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/daemon_init.h) | Functions, constants, or templates |
| [nova_datasegment.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/nova_datasegment.h) | `nova_data_header`, `nova_data_tail`, `nova_segment_header`, `segmentIdent` |
| [testpattern.h](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/testpattern.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [EvtDispatcher_Viewer.cpp:20](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/EvtDispatcher_Viewer.cpp#L20) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["EvtDispatcher_Viewer"]
  p1 --> p0
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [EventMemoryViewer.pro:12](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/EventMemoryViewer.pro#L12) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **6 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/EvtDispatcher_Viewer/blob/dbc09a158fd3c687d1918dfaf144340ffad948b6/README) |
