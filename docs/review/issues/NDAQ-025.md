# NDAQ-025: Use the defined FarmNodes inventory in logger assignment

[GitHub issue](https://github.com/NovaDAQ/DAQClusterUtils/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-025 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d`. Source review dated 2026-09-30.

### Trigger and evidence

Call assignmsgloggertofarm after module initialization is repaired. It looks up farmnodes, but the module defines only FarmNodes.

- [FarDet/msglogger_balancing/DAQClusterUtils.py:29](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/DAQClusterUtils.py#L29-L36)

### Impact

The assignment helper raises NameError instead of selecting a logger, independently of the module hostname construction defect.

### Recommended change

Use the canonical FarmNodes list and provide a clear error for an unknown node.

### Validation / acceptance criteria

Call the function for the first three valid farm nodes and an unknown node; verify the intended round-robin mapping and explicit unknown-node handling.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-025`. Central review and package documentation: `novadaq-documentation`.
