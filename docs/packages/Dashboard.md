# Dashboard

Python/Tk and PHP operational dashboard with message-analyzer launch and alarm/email helpers.

## Identity and scope

Repository: [NovaDAQ/Dashboard](https://github.com/NovaDAQ/Dashboard) · Reviewed commit: `5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9` · Domain: **Monitoring**.

Tracked files: **10**. Production deployment and owner are **unconfirmed**.

## Operation

Verify the status-file producer and consumer paths, update cadence, and display environment. An old status file must not be treated as current health. Alarm helpers can send messages; configure destinations deliberately before enabling them.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [dashboard_alarms2email.sh](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/dashboard_alarms2email.sh) |
| [dashboard_statusfilefill.sh](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/dashboard_statusfilefill.sh) |
| [startDashboard.sh](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/startDashboard.sh) |
| [startMsgAnalyzer0.sh](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/startMsgAnalyzer0.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

| Source artifact |
| --- |
| [msganalyzer_dashboard.fcl](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/msganalyzer_dashboard.fcl) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `DAQ_HOST` | [dashboard.py:11](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/dashboard.py#L11) |
| `DAQ_LOG_ROOT` | [dashboard.py:10](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/dashboard.py#L10) |
| `NOVADAQ_ENVIRONMENT` | [dashboard.py:229](https://github.com/NovaDAQ/Dashboard/blob/5bdd427a6f4d9eda47ff9d9d3feda04527d7f9b9/dashboard.py#L229) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **4 shell scripts**, and parsed **1 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
