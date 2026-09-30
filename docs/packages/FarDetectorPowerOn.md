# FarDetectorPowerOn

LaTeX recovery/power-on checklist and network validation helpers for the DAQ clusters.

## Identity and scope

Repository: [NovaDAQ/FarDetectorPowerOn](https://github.com/NovaDAQ/FarDetectorPowerOn) · Reviewed commit: `08324797c959ee3c6a1e6f1dd650327c0ca06edc` · Domain: **Operations**.

Tracked files: **29**. Production deployment and owner are **unconfirmed**.

## Operation

The README scopes the checklist to trained experts. Review power, management hosts, storage, and network readiness in documented order. Build a printable PDF with make pdf where the historical TeX dependencies are available.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

| Build definition |
| --- |
| [Makefile](https://github.com/NovaDAQ/FarDetectorPowerOn/blob/08324797c959ee3c6a1e6f1dd650327c0ca06edc/Makefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [Validate_NearDet_network.bash](https://github.com/NovaDAQ/FarDetectorPowerOn/blob/08324797c959ee3c6a1e6f1dd650327c0ca06edc/Validate_NearDet_network.bash) |
| [Validate_network.bash](https://github.com/NovaDAQ/FarDetectorPowerOn/blob/08324797c959ee3c6a1e6f1dd650327c0ca06edc/Validate_network.bash) |


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

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/FarDetectorPowerOn/blob/08324797c959ee3c6a1e6f1dd650327c0ca06edc/README) |
