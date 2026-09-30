# NDAQ-030: Repair the incomplete data-link loop so the script parses

[GitHub issue](https://github.com/NovaDAQ/NovaFileTransferSystem/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-030 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `50fa25c0b329e180a3b7714d0a9c8645fff16e4d`. Source review dated 2026-09-30.

### Trigger and evidence

Invoke datalink.sh. The for data in $(find ...) expression has no closing parenthesis or complete loop before the next statements.

- [scripts/datalink.sh:6](https://github.com/NovaDAQ/NovaFileTransferSystem/blob/50fa25c0b329e180a3b7714d0a9c8645fff16e4d/scripts/datalink.sh#L6-L12)

### Impact

The script exits with a syntax error and cannot perform its linking/backup workflow.

### Recommended change

Complete or remove the abandoned loop and define the intended input list before restoring operation; test with temporary directories and mocked external paths.

### Validation / acceptance criteria

Confirmed locally: bash -n scripts/datalink.sh exits 2 for an unmatched command substitution. Require syntax success and a temporary-directory workflow test after correction.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-030`. Central review and package documentation: `novadaq-documentation`.
