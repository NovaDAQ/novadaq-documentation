# NDAQ-002: Preserve alarm checkpoint when SQLite persistence fails

[GitHub issue](https://github.com/NovaDAQ/AshRiver/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-002 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `d54623861b9a2f0e2432374e3c5f4f522826aa2a`. Source review dated 2026-09-30.

### Trigger and evidence

sqlite3_exec fails while inserting an event or its alarm occurrences, for example because the database is locked or full. write_changes_to_sql logs the failure and returns; main unconditionally replaces previousData.txt with the new counters.

- [CM3350/src/run_logger.cpp:197](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/run_logger.cpp#L197-L202)
- [CM3350/src/run_logger.cpp:221](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/run_logger.cpp#L221-L226)
- [CM3350/src/run_logger.cpp:171](https://github.com/NovaDAQ/AshRiver/blob/d54623861b9a2f0e2432374e3c5f4f522826aa2a/CM3350/src/run_logger.cpp#L171-L176)

### Impact

The next poll compares against the advanced checkpoint and never retries the lost alarm increments. Event and occurrence inserts can also be partially committed.

### Recommended change

Write the event and occurrences in one transaction, return an explicit failure on any SQLite error, and advance the checkpoint atomically only after a successful commit. Preserve the old checkpoint on failure.

### Validation / acceptance criteria

Use a temporary SQLite database and checkpoint. Inject failure into each INSERT and verify rollback plus unchanged checkpoint; retry and verify exactly one complete event with its occurrences.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-002`. Central review and package documentation: `novadaq-documentation`.
