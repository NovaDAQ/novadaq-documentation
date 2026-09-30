# FileTransferService

Twisted service coordinating metadata, SAM transfers, archive bundling, retries, and cleanup of completed files.

## Identity and scope

Repository: [NovaDAQ/FileTransferService](https://github.com/NovaDAQ/FileTransferService) · Reviewed commit: `073251b32cb943d58ade3fc2b32902258ba93b78` · Domain: **Storage and metadata**.

Tracked files: **33**. Production deployment and owner are **unconfirmed**.

## Operation

Use the supported Python 2/Twisted/SAM environment. Monitor pending, completed, failed, and forgotten states; verify archive presence and CRC before deleting local data. Restart with the configuration and catalog state preserved, then reconcile rather than blindly resubmitting everything.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

| Build definition |
| --- |
| [python/GNUmakefile](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [python/fts/archive_bundler.py](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/archive_bundler.py) |
| [python/fts/path_template.py](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/path_template.py) |
| [python/fts_nova/extract_meta.py](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts_nova/extract_meta.py) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `FILETRANSFERSERVICE_DIR` | [python/fts/web.py:9](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/web.py#L9) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **0 C/C++ translation units**, **0 shell scripts**, and parsed **20 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P2 | [NDAQ-015: Assign failed-file destination before logging it](../review/issues/NDAQ-015.md) | [Issue](https://github.com/NovaDAQ/FileTransferService/issues/1) |
| P2 | [NDAQ-016: Import error-path dependencies used by the file cleaner](../review/issues/NDAQ-016.md) | [Issue](https://github.com/NovaDAQ/FileTransferService/issues/2) |
| P2 | [NDAQ-028: Raise the declared unknown-transfer exception so retries run](../review/issues/NDAQ-028.md) | [Issue](https://github.com/NovaDAQ/FileTransferService/issues/3) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
