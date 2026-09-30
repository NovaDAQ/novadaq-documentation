# NovaMessageLogger

Status logger clients, listeners, and notification demonstrations using RMS.

## Identity and scope

Repository: [NovaDAQ/NovaMessageLogger](https://github.com/NovaDAQ/NovaMessageLogger) · Reviewed commit: `14081c6b373ecb24e257be3d575af7fff2e54a92` · Domain: **Monitoring**.

Tracked files: **17**. Production deployment and owner are **unconfirmed**.

## Operation

Set the expected RMS destination and source application identity. Verify message receipt and persistence independently; demonstrations may require operational wrappers for long-running use.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/src/GNUmakefile) |
| [cxx/src/demo/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/src/demo/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/java/src/GNUmakefile) |
| [java/src/demo/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/java/src/demo/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

| Source artifact |
| --- |
| [config/TestStatusMessages.xsd](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/config/TestStatusMessages.xsd) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `boost` | [cxx/include/demo/StatusLoggerClient.h:18](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/include/demo/StatusLoggerClient.h#L18) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [NovaDAQUtilities](NovaDAQUtilities.md) | test include | [cxx/include/demo/StatusLoggerClient.h:16](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/include/demo/StatusLoggerClient.h#L16) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | test include | [cxx/include/demo/StatusLoggerClient.h:11](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/include/demo/StatusLoggerClient.h#L11) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **1 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/include/demo/StatusLoggerClient.h](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/include/demo/StatusLoggerClient.h) |
| [cxx/src/demo/StatusLoggerClient.cpp](https://github.com/NovaDAQ/NovaMessageLogger/blob/14081c6b373ecb24e257be3d575af7fff2e54a92/cxx/src/demo/StatusLoggerClient.cpp) |


## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
