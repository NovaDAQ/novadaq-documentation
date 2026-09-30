# NDAQ-014: Close the outer confirmation block in the internal-timing launcher

[GitHub issue](https://github.com/NovaDAQ/NovaControlRoom/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-014 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `86247acc81d9d311150ecedee08f03b70090d25b`. Source review dated 2026-09-30.

### Trigger and evidence

Invoke the Far Detector internal timing launcher. The outer if started at line 22 has no matching fi.

- [DAQ-Desktop-Utilities/FarDet/nova-daq-01/ExecuteInteralTimingMode.sh:22](https://github.com/NovaDAQ/NovaControlRoom/blob/86247acc81d9d311150ecedee08f03b70090d25b/DAQ-Desktop-Utilities/FarDet/nova-daq-01/ExecuteInteralTimingMode.sh#L22-L22)
- [DAQ-Desktop-Utilities/FarDet/nova-daq-01/ExecuteInteralTimingMode.sh:73](https://github.com/NovaDAQ/NovaControlRoom/blob/86247acc81d9d311150ecedee08f03b70090d25b/DAQ-Desktop-Utilities/FarDet/nova-daq-01/ExecuteInteralTimingMode.sh#L73-L76)

### Impact

The timing transition and its verification block cannot execute, preventing the operator workflow from completing.

### Recommended change

Close the outer block and verify confirmation/cancellation behavior with all external commands mocked.

### Validation / acceptance criteria

Confirmed locally: bash -n reports unexpected end of file and exits 2. Test cancel at both confirmations and authorized success with mocked kdialog and remote command runners.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-014`. Central review and package documentation: `novadaq-documentation`.
