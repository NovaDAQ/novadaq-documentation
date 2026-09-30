# NDAQ-013: Remove invalid case terminator from PV archiver health check

[GitHub issue](https://github.com/NovaDAQ/DAQOperationsTools/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-013 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `5b3fd3792f8526e5db7016f961c8e2debea28118`. Source review dated 2026-09-30.

### Trigger and evidence

Invoke checkPVArchiver.sh. A standalone ;; appears outside a case statement.

- [script/checkPVArchiver.sh:41](https://github.com/NovaDAQ/DAQOperationsTools/blob/5b3fd3792f8526e5db7016f961c8e2debea28118/script/checkPVArchiver.sh#L41-L52)

### Impact

The health check exits with a shell syntax error instead of a reliable archiver status; earlier top-level commands may already have executed.

### Recommended change

Remove the unmatched terminator and explicitly define exit status for healthy, stale, and failed-query outcomes.

### Validation / acceptance criteria

Confirmed locally: bash -n script/checkPVArchiver.sh exits 2 at line 51. After repair, syntax-check and mock psql for positive count, zero count, and query failure.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-013`. Central review and package documentation: `novadaq-documentation`.
