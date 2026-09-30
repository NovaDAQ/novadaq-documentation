# PowerUtilities

Detector power-supply, PDU, load-shedding, and power sequencing scripts.

## Identity and scope

Repository: [NovaDAQ/PowerUtilities](https://github.com/NovaDAQ/PowerUtilities) · Reviewed commit: `18754bf9a24c298bc02de4debe0cddd930992560` · Domain: **Operations**.

Tracked files: **126**. Production deployment and owner are **unconfirmed**.

## Operation

Validate detector/diblock/channel inputs and target inventory before any write. Confirm readback and sequence using the expert power checklist. These scripts alter physical equipment; review and test changes with command stubs first.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/GNUmakefile) |
| [scripts/GNUmakefile](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/GNUmakefile) |
| [scripts/loadshed/GNUmakefile](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [scripts/DCM_Off.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/DCM_Off.sh) |
| [scripts/DCM_On.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/DCM_On.sh) |
| [scripts/Diblock_Off.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/Diblock_Off.sh) |
| [scripts/Diblock_On.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/Diblock_On.sh) |
| [scripts/PDUconfig/getconfig_all.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/getconfig_all.sh) |
| [scripts/PDUconfig/getconfig_script.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/getconfig_script.sh) |
| [scripts/PDUconfig/powerallPDUs.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/powerallPDUs.sh) |
| [scripts/PDUconfig/poweralloutlets.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/poweralloutlets.sh) |
| [scripts/PDUconfig/pushconfig_all.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/pushconfig_all.sh) |
| [scripts/PDUconfig/pushconfig_script.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/pushconfig_script.sh) |
| [scripts/PDUconfig/shutdownmostPDUs.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/shutdownmostPDUs.sh) |
| [scripts/PDUconfig/shutdownmostoutlets.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/shutdownmostoutlets.sh) |
| [scripts/loadshed/get_temps.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/get_temps.sh) |
| [scripts/loadshed/loadshed.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed.sh) |
| [scripts/loadshed/loadshed_function.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed_function.sh) |
| [scripts/loadshed/loadshed_node_list.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed_node_list.sh) |
| [scripts/loadshed/loadshed_node_list_ipmi_test.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed_node_list_ipmi_test.sh) |
| [scripts/loadshed/loadshed_tests.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed_tests.sh) |
| [scripts/loadshed/loadshed_wrapper.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/loadshed_wrapper.sh) |
| [scripts/loadshed/power_off_cluster.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/power_off_cluster.sh) |
| [scripts/loadshed/power_on_cluster.sh](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/loadshed/power_on_cluster.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

| Source artifact |
| --- |
| [scripts/PDUconfig/config_192.168.136.235.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.235.ini) |
| [scripts/PDUconfig/config_192.168.136.236.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.236.ini) |
| [scripts/PDUconfig/config_192.168.136.237.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.237.ini) |
| [scripts/PDUconfig/config_192.168.136.238.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.238.ini) |
| [scripts/PDUconfig/config_192.168.136.239.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.239.ini) |
| [scripts/PDUconfig/config_192.168.136.240.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.240.ini) |
| [scripts/PDUconfig/config_192.168.136.241.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.241.ini) |
| [scripts/PDUconfig/config_192.168.136.242.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.242.ini) |
| [scripts/PDUconfig/config_192.168.136.243.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.243.ini) |
| [scripts/PDUconfig/config_192.168.136.244.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.244.ini) |
| [scripts/PDUconfig/config_192.168.136.245.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.245.ini) |
| [scripts/PDUconfig/config_192.168.136.246.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.246.ini) |
| [scripts/PDUconfig/config_192.168.136.247.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.247.ini) |
| [scripts/PDUconfig/config_192.168.136.248.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.248.ini) |
| [scripts/PDUconfig/config_192.168.136.249.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.249.ini) |
| [scripts/PDUconfig/config_192.168.136.250.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.250.ini) |
| [scripts/PDUconfig/config_192.168.136.251.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.251.ini) |
| [scripts/PDUconfig/config_192.168.136.252.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.252.ini) |
| [scripts/PDUconfig/config_192.168.136.253.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.253.ini) |
| [scripts/PDUconfig/config_192.168.136.254.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.136.254.ini) |
| [scripts/PDUconfig/config_192.168.137.190.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.137.190.ini) |
| [scripts/PDUconfig/config_192.168.137.191.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.137.191.ini) |
| [scripts/PDUconfig/config_192.168.137.253.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.137.253.ini) |
| [scripts/PDUconfig/config_192.168.137.254.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_192.168.137.254.ini) |
| [scripts/PDUconfig/config_common.ini](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/PDUconfig/config_common.ini) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:5](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/GNUmakefile#L5) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **21 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-029: Reject invalid DCM power-on arguments before issuing hardware commands](../review/issues/NDAQ-029.md) | [Issue](https://github.com/NovaDAQ/PowerUtilities/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
