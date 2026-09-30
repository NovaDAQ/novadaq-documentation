# TDUControlClient

Standalone Qt client for timing control.

## Identity and scope

Repository: [NovaDAQ/TDUControlClient](https://github.com/NovaDAQ/TDUControlClient) · Reviewed commit: `ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09` · Domain: **Timing and triggers**.

Tracked files: **16**. Production deployment and owner are **unconfirmed**.

## Operation

Configure the intended host/tunnel and port and check live register/status readback. Treat synchronization and control actions as hardware mutations requiring the site's run-state procedure.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

| Build definition |
| --- |
| [Makefile](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/Makefile) |
| [TDUControlClient.pro](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/TDUControlClient.pro) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [main.cc](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/main.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [AboutDialog.h](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/AboutDialog.h) | `AboutDialog` |
| [SettingsDialog.h](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/SettingsDialog.h) | `SettingsDialog` |
| [TDUControlClient.h](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/TDUControlClient.h) | `TDUCommands`, `TDUControlClient` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [TDUControlClient.cpp:6](https://github.com/NovaDAQ/TDUControlClient/blob/ac2801d864cd4fd026374cd4a6ccd8d5e6b4ce09/TDUControlClient.cpp#L6) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **3 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
