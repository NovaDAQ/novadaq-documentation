# EventDump

Command-line tools to inspect run headers, events, configurations, trigger livetime, and incomplete data.

## Identity and scope

Repository: [NovaDAQ/EventDump](https://github.com/NovaDAQ/EventDump) · Reviewed commit: `e4fad299cf6b9390d4f75dc65871f67a90a4b30d` · Domain: **Analysis**.

Tracked files: **27**. Production deployment and owner are **unconfirmed**.

## Operation

Work from an immutable copy of a raw file when diagnosing corruption. Compare parser status, declared lengths, and file size; malformed input must fail or terminate predictably. Keep output artifacts alongside the exact input revision/checksum.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/DDTLiveTime.cc](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/DDTLiveTime.cc) |
| [cxx/src/EventDump.cc](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/EventDump.cc) |
| [cxx/src/IncompleteEvents.cc](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/IncompleteEvents.cc) |
| [cxx/src/RunSummary.cc](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/RunSummary.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [cxx/src/DDTLiveTime.cc:1](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/DDTLiveTime.cc#L1) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQDataFormats"]
  p1["EventDump"]
  p2["NovaTimingUtilities"]
  p3["RawFileParser"]
  p1 --> p0
  p1 --> p2
  p1 --> p3
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | build link | [cxx/src/GNUmakefile:17](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/GNUmakefile#L17) |
| [DAQDataFormats](DAQDataFormats.md) | source include | [cxx/src/DDTLiveTime.cc:17](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/DDTLiveTime.cc#L17) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | build link | [cxx/src/GNUmakefile:17](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/GNUmakefile#L17) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | source include | [cxx/src/IncompleteEvents.cc:28](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/IncompleteEvents.cc#L28) |
| [RawFileParser](RawFileParser.md) | build link | [cxx/src/GNUmakefile:17](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/GNUmakefile#L17) |
| [RawFileParser](RawFileParser.md) | source include | [cxx/src/DDTLiveTime.cc:28](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/cxx/src/DDTLiveTime.cc#L28) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/EventDump/blob/e4fad299cf6b9390d4f75dc65871f67a90a4b30d/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **15 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
