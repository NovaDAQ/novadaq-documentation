# NDAQ-029: Reject invalid DCM power-on arguments before issuing hardware commands

[GitHub issue](https://github.com/NovaDAQ/PowerUtilities/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-029 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `18754bf9a24c298bc02de4debe0cddd930992560`. Source review dated 2026-09-30.

### Trigger and evidence

Invoke DCM_On.sh with three arguments whose first two form a valid address. The wrong-argument branch tries to execute exit/Users/... instead of exit, then falls through to the power commands. Nonnumeric arguments also make the numeric tests fail without terminating.

- [scripts/DCM_On.sh:1](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/DCM_On.sh#L1-L5)
- [scripts/DCM_On.sh:6](https://github.com/NovaDAQ/PowerUtilities/blob/18754bf9a24c298bc02de4debe0cddd930992560/scripts/DCM_On.sh#L6-L26)

### Impact

An invalid invocation can still issue voltage and power-switch commands to detector supplies, despite the printed argument error.

### Recommended change

Fail with a nonzero exit before side effects unless there are exactly two validated integers in range. Apply equivalent validation to related power scripts.

### Validation / acceptance criteria

Run with snmpset/snmpget/bc replaced by local recording stubs. Zero, one, three, nonnumeric, and out-of-range arguments must never reach a hardware-command stub.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-029`. Central review and package documentation: `novadaq-documentation`.
