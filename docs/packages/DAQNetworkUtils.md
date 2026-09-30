# DAQNetworkUtils

Header-only Qt SSH tunnel helper used by network-facing GUIs.

## Identity and scope

Repository: [NovaDAQ/DAQNetworkUtils](https://github.com/NovaDAQ/DAQNetworkUtils) · Reviewed commit: `3d568f6c4080f575377ed6c49dee69d55aa312b3` · Domain: **Messaging**.

Tracked files: **5**. Production deployment and owner are **unconfirmed**.

## Operation

Provide the gateway, target host, remote port, and local port; verify the forwarded endpoint independently after starting SSH. Process startup alone does not establish remote reachability. Stop the tunnel when its owning GUI is closed.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/cxx/src/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/SSHTunnel.h](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/cxx/include/SSHTunnel.h) | `SSHTunnel` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtCore` | [cxx/include/SSHTunnel.h:4](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/cxx/include/SSHTunnel.h#L4) |
| `QtNetwork` | [cxx/include/SSHTunnel.h:5](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/cxx/include/SSHTunnel.h#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:16](https://github.com/NovaDAQ/DAQNetworkUtils/blob/3d568f6c4080f575377ed6c49dee69d55aa312b3/GNUmakefile#L16) |


Direct consumers: [NovaResourceManager](NovaResourceManager.md), [NovaRunControl](NovaRunControl.md), [TDUControl](TDUControl.md), [TDUUtilities](TDUUtilities.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
