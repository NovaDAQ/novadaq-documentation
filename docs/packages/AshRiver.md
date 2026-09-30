# AshRiver

Site services: CM3350 Modbus alarm collection into SQLite, Raspberry Pi UPS shutdown monitoring, and a containerized Redmine instance.

## Identity and scope

Repository: [NovaDAQ/AshRiver](https://github.com/NovaDAQ/AshRiver) · Reviewed commit: `d54623861b9a2f0e2432374e3c5f4f522826aa2a` · Domain: **Operations**.

Tracked files: **41**. Production deployment and owner are **unconfirmed**.

## Operation

CM3350 is polled by cron; preserve both its SQLite database and previousData.txt checkpoint together. The UPS monitor needs I2C access and shutdown privileges. Redmine has separate application/database volumes; use its README for restore ownership requirements.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [CM3350/alarm_email.sh](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/alarm_email.sh) |
| [CM3350/daily_email.sh](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/daily_email.sh) |
| [CM3350/src/generate_email.cpp](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/generate_email.cpp) |
| [CM3350/src/modbus_test.c](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/modbus_test.c) |
| [CM3350/src/run_logger.cpp](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/run_logger.cpp) |
| [CM3350/src/sql_create.cpp](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/sql_create.cpp) |
| [RPI_UPS/INA219.py](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/RPI_UPS/INA219.py) |
| [RPI_UPS/cron_shutdown_check.py](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/RPI_UPS/cron_shutdown_check.py) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [CM3350/src/util.h](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/util.h) | Functions, constants, or templates |


## Configuration and data contracts

| Source artifact |
| --- |
| [redmine/docker-compose.yml](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/redmine/docker-compose.yml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **4 C/C++ translation units**, **6 shell scripts**, and parsed **3 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

| Severity | Finding | GitHub |
| --- | --- | --- |
| P1 | [NDAQ-002: Preserve alarm checkpoint when SQLite persistence fails](../review/issues/NDAQ-002.md) | [Issue](https://github.com/NovaDAQ/AshRiver/issues/1) |


Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [CM3350/README.md](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/README.md) |
| [RPI_UPS/README.md](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/RPI_UPS/README.md) |
| [redmine/README.md](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/redmine/README.md) |
