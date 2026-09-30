# NovaDAQTemplate

C++/Python coding examples and package-layout/build templates.

## Identity and scope

Repository: [NovaDAQ/NovaDAQTemplate](https://github.com/NovaDAQ/NovaDAQTemplate) · Reviewed commit: `583982b12985801f9feaaa22f27661d93c17e0e4` · Domain: **Simulation and examples**.

Tracked files: **25**. Production deployment and owner are **unconfirmed**.

## Operation

Use as a starting point only after updating names, external dependencies, and build rules. Example behavior is not an operational service specification.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/src/CPPStandardsExampleMain.cc](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/src/CPPStandardsExampleMain.cc) |
| [python/src/BuildInitFile.py](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/python/src/BuildInitFile.py) |
| [python/src/PythonStandardsExample.py](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/python/src/PythonStandardsExample.py) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/CPPStandardsExample.h](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/include/CPPStandardsExample.h) | `CPPStandardsExample` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/jcsc.xml](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/config/jcsc.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `cppunit` | [cxx/unittest/CPPStandardsExampleTest.h:4](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/unittest/CPPStandardsExampleTest.h#L4) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/GNUmakefile#L10) |


Direct consumers: [NovaDAQTemplate_OLD](NovaDAQTemplate_OLD.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **4 C/C++ translation units**, **0 shell scripts**, and parsed **2 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/unittest/CPPStandardsExampleTest.cpp](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/unittest/CPPStandardsExampleTest.cpp) |
| [cxx/unittest/CPPStandardsExampleTest.h](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/unittest/CPPStandardsExampleTest.h) |
| [cxx/unittest/CPPUnitTestMain.cc](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/cxx/unittest/CPPUnitTestMain.cc) |


## Existing documentation

| Source |
| --- |
| [README_BUILD](https://github.com/NovaDAQ/NovaDAQTemplate/blob/583982b12985801f9feaaa22f27661d93c17e0e4/README_BUILD) |
