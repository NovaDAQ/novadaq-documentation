# NovaDAQCrontab

Parses DAQ/cron configuration and drives scheduled operational commands.

## Identity and scope

Repository: [NovaDAQ/NovaDAQCrontab](https://github.com/NovaDAQ/NovaDAQCrontab) · Reviewed commit: `a76ae472ce40022c603473db1ce84f22097c3e49` · Domain: **Operations**.

Tracked files: **20**. Production deployment and owner are **unconfirmed**.

## Operation

Review command definitions and scheduling context before installation. Match detector/partition environment and log destinations; verify exit codes and prevent overlapping operations that target the same DAQ process.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/novadaqcrontab.cc](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/novadaqcrontab.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/CommandLineParser.h](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/CommandLineParser.h) | `CommandLineParser` |
| [cxx/include/NovaDAQ.h](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/NovaDAQ.h) | `NovaDAQ` |
| [cxx/include/NovaDAQConfigParser.h](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/NovaDAQConfigParser.h) | `NovaDAQConfigParser` |
| [cxx/include/NovaDAQCrontabConfigParser.h](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/NovaDAQCrontabConfigParser.h) | `NovaDAQCrontabConfigParser` |
| [cxx/include/version.h](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/version.h) | Functions, constants, or templates |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/NovaDAQConfig.xml](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/config/NovaDAQConfig.xml) |
| [config/NovaDAQConfig.xsd](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/config/NovaDAQConfig.xsd) |
| [config/NovaDAQCrontabConfig.xml](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/config/NovaDAQCrontabConfig.xml) |
| [config/NovaDAQCrontabConfig.xsd](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/config/NovaDAQCrontabConfig.xsd) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/src/CommandLineParser.cpp:7](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/CommandLineParser.cpp#L7) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["NovaDAQCrontab"]
  p1["NovaDAQUtilities"]
  p2["PackageVersion"]
  p3["PedestalDataRunner"]
  p0 --> p1
  p0 --> p2
  p0 --> p3
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | build link | [cxx/src/GNUmakefile:30](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/GNUmakefile#L30) |
| [NovaDAQUtilities](NovaDAQUtilities.md) | source include | [cxx/src/CommandLineParser.cpp:10](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/CommandLineParser.cpp#L10) |
| [PackageVersion](PackageVersion.md) | source include | [cxx/include/version.h:28](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/include/version.h#L28) |
| [PedestalDataRunner](PedestalDataRunner.md) | build link | [cxx/src/GNUmakefile:30](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/GNUmakefile#L30) |
| [PedestalDataRunner](PedestalDataRunner.md) | source include | [cxx/src/CommandLineParser.cpp:1](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/cxx/src/CommandLineParser.cpp#L1) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaDAQCrontab/blob/a76ae472ce40022c603473db1ce84f22097c3e49/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **5 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
