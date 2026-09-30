# NDAQ-024: Construct manager hostnames without the numeric farm formatter

[GitHub issue](https://github.com/NovaDAQ/DAQClusterUtils/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-024 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d`. Source review dated 2026-09-30.

### Trigger and evidence

Import the balancing helper. ManagerName contains strings such as master, but ManagerNodes calls make_hostname, whose branches both use numeric %d formatting. On Python 2 this raises TypeError during formatting; Python 3 also rejects the comparison (and requires adapting the earlier range concatenation).

- [FarDet/msglogger_balancing/DAQClusterUtils.py:5](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/DAQClusterUtils.py#L5-L9)
- [FarDet/msglogger_balancing/DAQClusterUtils.py:16](https://github.com/NovaDAQ/DAQClusterUtils/blob/c4b4a0fed76f3aa605ebf0cc9d4a24dd11713f7d/FarDet/msglogger_balancing/DAQClusterUtils.py#L16-L24)

### Impact

Import fails before message-logger balancing can run.

### Recommended change

Use a separate formatter for named manager hosts and retain numeric formatting for farm nodes. Verify the resulting host inventory against the intended site configuration.

### Validation / acceptance criteria

Import under the supported interpreter with subprocess mocked; verify numeric farm names and named manager names, including exclusions.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-024`. Central review and package documentation: `novadaq-documentation`.
