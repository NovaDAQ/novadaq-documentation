# NovaRemoteControlRooms

Remote-control-room setup, SSH tunnels, gateway options, and one-button GUI helpers.

## Identity and scope

Repository: [NovaDAQ/NovaRemoteControlRooms](https://github.com/NovaDAQ/NovaRemoteControlRooms) · Reviewed commit: `6630ffebc9d73fb1d2a20ed0b4014395b420cc30` · Domain: **Operations**.

Tracked files: **37**. Production deployment and owner are **unconfirmed**.

## Operation

Check user credentials, gateway reachability, and local port collisions. Verify each tunnel's destination before opening operator displays; close obsolete tunnels when leaving the session.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [GetTicket.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/GetTicket.sh) |
| [JustDoIt.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/JustDoIt.sh) |
| [ListGatewayTunnels.py](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/ListGatewayTunnels.py) |
| [ListLocalPorts.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/ListLocalPorts.sh) |
| [OpenTunnels.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/OpenTunnels.sh) |
| [ResetLocalPorts.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/ResetLocalPorts.sh) |
| [SetupROCOptions.sh](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/SetupROCOptions.sh) |


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

Static analysis attempted **0 C/C++ translation units**, **6 shell scripts**, and parsed **3 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/NovaRemoteControlRooms/blob/6630ffebc9d73fb1d2a20ed0b4014395b420cc30/README) |
