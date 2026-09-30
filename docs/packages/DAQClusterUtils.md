# DAQClusterUtils

Site-specific farm inventory, host checks, mount management, and message-logger balancing scripts.

## Identity and scope

Repository: [NovaDAQ/DAQClusterUtils](https://github.com/NovaDAQ/DAQClusterUtils) · Reviewed commit: `c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d` · Domain: **Operations**.

Tracked files: **107**. Production deployment and owner are **unconfirmed**.

## Operation

Select FarDet, NearDet, or TestBeam explicitly and inspect the host list before a distributed command. Check mounts and logging destinations before restarting farm processes. Host lists in source are historical configuration, not proof of current membership.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [FarDet/GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/GNUmakefile) |
| [FarDet/host_check/GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/host_check/GNUmakefile) |
| [FarDet/msglogger_balancing/GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/GNUmakefile) |
| [GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/GNUmakefile) |
| [NearDet/GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/NearDet/GNUmakefile) |
| [TestBeam/GNUmakefile](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/TestBeam/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [FarDet/check_functions.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/check_functions.sh) |
| [FarDet/disk-mount-scripts/datadisks/mount-nova-daqlog-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/datadisks/mount-nova-daqlog-disks.sh) |
| [FarDet/disk-mount-scripts/datadisks/mount-nova-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/datadisks/mount-nova-disks.sh) |
| [FarDet/disk-mount-scripts/farm/mount-nova-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/farm/mount-nova-disks.sh) |
| [FarDet/disk-mount-scripts/master/mount-nova-daqlog-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/master/mount-nova-daqlog-disks.sh) |
| [FarDet/disk-mount-scripts/nearline/mount-nova-daqlog-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/nearline/mount-nova-daqlog-disks.sh) |
| [FarDet/disk-mount-scripts/nearline/mount-nova-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/nearline/mount-nova-disks.sh) |
| [FarDet/disk-mount-scripts/other_named_except_msglogger/mount-nova-daqlog-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/other_named_except_msglogger/mount-nova-daqlog-disks.sh) |
| [FarDet/disk-mount-scripts/other_named_except_msglogger/mount-nova-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/disk-mount-scripts/other_named_except_msglogger/mount-nova-disks.sh) |
| [FarDet/far-cluster-cp.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-cp.sh) |
| [FarDet/far-cluster-farm-x.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-farm-x.sh) |
| [FarDet/far-cluster-mounts.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-mounts.sh) |
| [FarDet/far-cluster-parallel-cp.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-parallel-cp.sh) |
| [FarDet/far-cluster-parallel-x.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-parallel-x.sh) |
| [FarDet/far-cluster-x.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/far-cluster-x.sh) |
| [FarDet/fardet_clusterlist.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/fardet_clusterlist.py) |
| [FarDet/fd_node_network_monitor.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/fd_node_network_monitor.py) |
| [FarDet/fd_node_network_monitor_wrapper.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/fd_node_network_monitor_wrapper.sh) |
| [FarDet/fd_node_temperature_monitor.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/fd_node_temperature_monitor.py) |
| [FarDet/fd_node_temperature_monitor_wrapper.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/fd_node_temperature_monitor_wrapper.sh) |
| [FarDet/gen_fd_node_list_v2.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/gen_fd_node_list_v2.py) |
| [FarDet/host_check/host_check.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/host_check/host_check.py) |
| [FarDet/host_check/ip_host_check.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/host_check/ip_host_check.py) |
| [FarDet/host_check/ip_host_check_for_datadisk.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/host_check/ip_host_check_for_datadisk.py) |
| [FarDet/mount-nova-disks-gmond-nova.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/mount-nova-disks-gmond-nova.sh) |
| [FarDet/mount-nova-disks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/mount-nova-disks.sh) |
| [FarDet/msglogger_balancing/DAQClusterUtils.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/DAQClusterUtils.py) |
| [FarDet/msglogger_balancing/msglogger_load_balancing.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/msglogger_load_balancing.py) |
| [FarDet/msglogger_balancing/umount_link.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/umount_link.py) |
| [FarDet/power-off-all-fardet.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/power-off-all-fardet.sh) |
| [FarDet/power-on-all-3v-fardet.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/power-on-all-3v-fardet.sh) |
| [FarDet/power-on-all-fardet.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/power-on-all-fardet.sh) |
| [FarDet/power-on-all-hv-fardet.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/power-on-all-hv-fardet.sh) |
| [FarDet/rename-ddt-logfile.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/rename-ddt-logfile.py) |
| [FarDet/revert-ddt-logfile.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/revert-ddt-logfile.py) |
| [FarDet/server_check_pssh.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/server_check_pssh.sh) |
| [FarDet/server_check_wrapper.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/server_check_wrapper.sh) |
| [FarDet/server_checks.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/server_checks.sh) |
| [FarDet/switch-power.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/switch-power.sh) |
| [HostFiles/make_host.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/HostFiles/make_host.sh) |
| [NearDet/ND_DAQ_Recovery.py](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/NearDet/ND_DAQ_Recovery.py) |
| [NearDet/check_functions_nd.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/NearDet/check_functions_nd.sh) |
| [NearDet/server_check_pssh_nd.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/NearDet/server_check_pssh_nd.sh) |
| [NearDet/server_checks_nd.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/NearDet/server_checks_nd.sh) |
| [TestBeam/check_functions_tb.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/TestBeam/check_functions_tb.sh) |
| [TestBeam/server_checks_tb.sh](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/TestBeam/server_checks_tb.sh) |


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

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [FarDet/GNUmakefile:9](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/GNUmakefile#L9) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **50 shell scripts**, and parsed **12 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P2 | [NDAQ-024: Construct manager hostnames without the numeric farm formatter](../review/issues/NDAQ-024.md) | [Issue](https://github.com/NovaDAQ/DAQClusterUtils/issues/1) |
| P2 | [NDAQ-025: Use the defined FarmNodes inventory in logger assignment](../review/issues/NDAQ-025.md) | [Issue](https://github.com/NovaDAQ/DAQClusterUtils/issues/2) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
