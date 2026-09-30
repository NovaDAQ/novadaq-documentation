# NDAQ-004: Avoid incrementing erased map iterators during client destruction

[GitHub issue](https://github.com/NovaDAQ/NovaRunControlClient/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-004 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `1005aac7bfaae11bac3032c20e50e0a7d4fdb221`. Source review dated 2026-09-30.

### Trigger and evidence

Destroy an RmsMessageClient after registering at least one receiver, sender, or DDS connection. Each destructor loop erases its current map iterator and the for-loop increments that invalidated iterator.

- [cxx/src/RmsMessageClient.cpp:67](https://github.com/NovaDAQ/NovaRunControlClient/blob/1005aac7bfaae11bac3032c20e50e0a7d4fdb221/cxx/src/RmsMessageClient.cpp#L67-L107)

### Impact

Undefined behavior can crash cleanup and prevent remaining connections from closing, affecting shutdown and restart of consumers throughout DAQ.

### Recommended change

Close entries without erasing inside traversal and clear afterward, or advance a valid iterator before erasing. Apply consistently to all three maps.

### Validation / acceptance criteria

Exercise destruction with zero, one, and multiple entries in each map using checked STL iterators and stub connections; verify every close runs once and no invalid iterator is accessed.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-004`. Central review and package documentation: `novadaq-documentation`.
