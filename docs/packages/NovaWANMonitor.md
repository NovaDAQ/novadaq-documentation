# NovaWANMonitor

Ping source/receiver and site-monitor GUI for WAN connectivity checks.

## Identity and scope

Repository: [NovaDAQ/NovaWANMonitor](https://github.com/NovaDAQ/NovaWANMonitor) · Reviewed commit: `014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602` · Domain: **Monitoring**.

Tracked files: **21**. Production deployment and owner are **unconfirmed**.

## Operation

Set source/destination endpoints and expected cadence. Distinguish delayed/missing samples from server downtime; capture both endpoint logs when diagnosing latency changes.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/WANMonitor_PingReceiver.cc](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/WANMonitor_PingReceiver.cc) |
| [cxx/src/WANMonitor_PingSource.cc](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/WANMonitor_PingSource.cc) |
| [cxx/src/WANSiteMonitor.cc](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/WANSiteMonitor.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/PingReceiver.h](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/PingReceiver.h) | `PingReceiver`, `PingRecord`, `subStates` |
| [cxx/include/PingSource.h](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/PingSource.h) | `PingSource`, `subStates` |
| [cxx/include/SiteMonitorGUI.h](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/SiteMonitorGUI.h) | `SiteMonitorGUI` |
| [cxx/include/daemon_init.h](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/daemon_init.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `Qt` | [cxx/src/SiteMonitorGUI.cpp:13](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/SiteMonitorGUI.cpp#L13) |
| `QtCore` | [cxx/include/PingReceiver.h:4](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/PingReceiver.h#L4) |
| `QtGui` | [cxx/include/PingReceiver.h:5](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/PingReceiver.h#L5) |
| `QtNetwork` | [cxx/include/PingReceiver.h:7](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/include/PingReceiver.h#L7) |
| `sys` | [cxx/src/PingReceiver.cpp:14](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/cxx/src/PingReceiver.cpp#L14) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaWANMonitor/blob/014fc2ea62e75a3b2ddaa6f2317ab3b1f56b7602/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **7 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
