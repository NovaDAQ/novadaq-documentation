# NovaFTS

Site configuration, metadata plugins, credential/setup helpers, and container deployment files for file transfer.

## Identity and scope

Repository: [NovaDAQ/NovaFTS](https://github.com/NovaDAQ/NovaFTS) · Reviewed commit: `a9c9400970f6431ca1b4d77ea2e046cd3bc3779c` · Domain: **Storage and metadata**.

Tracked files: **77**. Production deployment and owner are **unconfirmed**.

## Operation

Track the selected plugin/configuration and keep host and dd-03/dd-07 container copies consistent. Check credential lifetime, catalog registration, transfer backlog, and archive confirmation before local cleanup.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [bin/clean_fts_logs.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/clean_fts_logs.sh) |
| [bin/get_principal.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/get_principal.sh) |
| [bin/gridftp_ssh_wrapper.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/gridftp_ssh_wrapper.sh) |
| [bin/make_proxy.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/make_proxy.sh) |
| [bin/setup_fts_links.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/setup_fts_links.sh) |
| [bin/setup_sam_dev.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/setup_sam_dev.sh) |
| [bin/setup_sam_prd.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/setup_sam_prd.sh) |
| [bin/sync_laser_scanner_data.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/bin/sync_laser_scanner_data.sh) |
| [certs/update_certificate_links.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/certs/update_certificate_links.sh) |
| [plugins/raw_metadata.py](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/plugins/raw_metadata.py) |
| [podmanFTS/dd-03/plugins/novaraw.py](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/plugins/novaraw.py) |
| [podmanFTS/dd-03/plugins/raw_metadata.py](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/plugins/raw_metadata.py) |
| [podmanFTS/dd-07/plugins/novaraw.py](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-07/plugins/novaraw.py) |
| [podmanFTS/dd-07/plugins/raw_metadata.py](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-07/plugins/raw_metadata.py) |
| [podmanFTS/run_fts_datadisk-01.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_datadisk-01.sh) |
| [podmanFTS/run_fts_datadisk-02.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_datadisk-02.sh) |
| [podmanFTS/run_fts_datadisk-04.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_datadisk-04.sh) |
| [podmanFTS/run_fts_datadisk-05.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_datadisk-05.sh) |
| [podmanFTS/run_fts_dd-03.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_dd-03.sh) |
| [podmanFTS/run_fts_dd-07.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/run_fts_dd-07.sh) |
| [podmanFTS/setup_and_start_fts.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/setup_and_start_fts.sh) |
| [podmanFTS/setup_nova_forfts_SL7_container.sh](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/setup_nova_forfts_SL7_container.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

| Source artifact |
| --- |
| [fts_rundir-novadaq-ctrl-datadisk-02.fnal.gov/fts-novadaq-ctrl-datadisk-02.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-ctrl-datadisk-02.fnal.gov/fts-novadaq-ctrl-datadisk-02.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-01.fnal.gov/fts-novadaq-far-datadisk-01.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-01.fnal.gov/fts-novadaq-far-datadisk-01.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-01.fnal.gov/fts-novadaq-near-datadisk-01.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-01.fnal.gov/fts-novadaq-near-datadisk-01.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-02.fnal.gov/fts-novadaq-far-datadisk-02.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-02.fnal.gov/fts-novadaq-far-datadisk-02.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-03.fnal.gov/fts-novadaq-far-datadisk-03.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-03.fnal.gov/fts-novadaq-far-datadisk-03.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-04.fnal.gov/fts-novadaq-far-datadisk-04.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-04.fnal.gov/fts-novadaq-far-datadisk-04.fnal.gov.ini) |
| [fts_rundir-novadaq-far-datadisk-05.fnal.gov/fts-novadaq-far-datadisk-05.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/fts_rundir-novadaq-far-datadisk-05.fnal.gov/fts-novadaq-far-datadisk-05.fnal.gov.ini) |
| [podmanFTS/dd-03/config/fts-novadaq-far-dd-07.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/config/fts-novadaq-far-dd-07.fnal.gov.ini) |
| [podmanFTS/dd-03/config/fts-novadaq-near-dd-03.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/config/fts-novadaq-near-dd-03.fnal.gov.ini) |
| [podmanFTS/dd-03/plugins/gmond_nova.conf](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/plugins/gmond_nova.conf) |
| [podmanFTS/dd-07/config/fts-novadaq-far-dd-07.fnal.gov.ini](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-07/config/fts-novadaq-far-dd-07.fnal.gov.ini) |
| [podmanFTS/dd-07/plugins/gmond_nova.conf](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-07/plugins/gmond_nova.conf) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **17 shell scripts**, and parsed **8 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P2 | [NDAQ-026: Use a dictionary fallback when resolving ART process metadata](../review/issues/NDAQ-026.md) | [Issue](https://github.com/NovaDAQ/NovaFTS/issues/1) |
| P2 | [NDAQ-027: Flush the final JSON metadata field at end of input](../review/issues/NDAQ-027.md) | [Issue](https://github.com/NovaDAQ/NovaFTS/issues/2) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/README) |
