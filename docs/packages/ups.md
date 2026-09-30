# ups

UPS product dependencies and scripts for building, bootstrapping, tagging, and packaging novadaq.

## Identity and scope

Repository: [NovaDAQ/ups](https://github.com/NovaDAQ/ups) · Reviewed commit: `9695b34d7b9f7ee5ee61977d4473fe2eea2b114d` · Domain: **Build and release**.

Tracked files: **14**. Production deployment and owner are **unconfirmed**.

## Operation

Use product_deps as the declared external dependency/qualifier source; the snapshot names novadaq v18_00_00 and e19. Resolve the complete release source layout before invoking build scripts and retain build logs/artifacts for rollback.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/CMakeLists.txt) |
| [product_deps](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/product_deps) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [bootstrap.sh](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/bootstrap.sh) |
| [build_novadaq.sh](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/build_novadaq.sh) |
| [ddsidl_tailor.sh](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/ddsidl_tailor.sh) |
| [ups_product_tag.sh](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/ups_product_tag.sh) |


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

Static analysis attempted **0 C/C++ translation units**, **5 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-033: Stop release packaging when configure, build, or tests fail](../review/issues/NDAQ-033.md) | [Issue](https://github.com/NovaDAQ/ups/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/README) |
