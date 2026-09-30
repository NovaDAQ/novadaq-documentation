# benchmarks

Memory bandwidth, bit-reversal, stream, and memory-test programs with plotting helpers.

## Identity and scope

Repository: [NovaDAQ/benchmarks](https://github.com/NovaDAQ/benchmarks) · Reviewed commit: `a9fd55fd331d3fec4f82d18f5f885a15e2706f03` · Domain: **Simulation and examples**.

Tracked files: **26**. Production deployment and owner are **unconfirmed**.

## Operation

Run on an isolated node because tests consume CPU/memory bandwidth and may allocate large buffers. Record architecture, compiler options, memory size, and workload to make results comparable.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/GNUmakefile) |
| [c/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/GNUmakefile) |
| [c/src/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/GNUmakefile) |
| [c/test/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/test/GNUmakefile) |
| [c/unittest/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/unittest/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/cxx/unittest/GNUmakefile) |
| [scripts/GNUmakefile](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/scripts/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [c/src/MemBench.c](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/MemBench.c) |
| [c/src/mem_l2_bandwidth.c](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/mem_l2_bandwidth.c) |
| [c/src/memtester.c](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/memtester.c) |
| [c/src/stream_d.c](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/stream_d.c) |
| [scripts/bench_mem_plot.sh](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/scripts/bench_mem_plot.sh) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [c/src/bitrev.h](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/bitrev.h) | Functions, constants, or templates |
| [c/src/memtester.h](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/memtester.h) | Functions, constants, or templates |
| [c/src/sizes.h](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/sizes.h) | Functions, constants, or templates |
| [c/src/tests.h](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/tests.h) | Functions, constants, or templates |
| [c/src/types.h](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/types.h) | `test` |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `sys` | [c/src/MemBench.c:5](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/c/src/MemBench.c#L5) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **7 C/C++ translation units**, **1 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [doc/README.stream](https://github.com/NovaDAQ/benchmarks/blob/a9fd55fd331d3fec4f82d18f5f885a15e2706f03/doc/README.stream) |
