# nova_gcn_trigger

C program bridging external GCN notices into the NOvA trigger workflow.

## Identity and scope

Repository: [NovaDAQ/nova_gcn_trigger](https://github.com/NovaDAQ/nova_gcn_trigger) · Reviewed commit: `7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251` · Domain: **Timing and triggers**.

Tracked files: **3**. Production deployment and owner are **unconfirmed**.

## Operation

Validate notice type, timestamp, destination, and reconnection behavior against recorded notices on an isolated endpoint. External notices must be distinguishable from local test messages.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [nova_gcn_trigger.c](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/nova_gcn_trigger.c) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.

## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `arpa` | [nova_gcn_trigger.c:149](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/nova_gcn_trigger.c#L149) |
| `libxml` | [nova_gcn_trigger.c:150](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/nova_gcn_trigger.c#L150) |
| `sys` | [nova_gcn_trigger.c:144](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/nova_gcn_trigger.c#L144) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:7](https://github.com/NovaDAQ/nova_gcn_trigger/blob/7e4ac0b60808a6fbfa2c2a892e2ed1c6486ec251/GNUmakefile#L7) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **1 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.
