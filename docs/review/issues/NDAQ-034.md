# NDAQ-034: Close failed connection sockets before retry or destruction

[GitHub issue](https://github.com/NovaDAQ/EventBuilderClient/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-034 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `c09ce105f69b6c71d21b6c680d80db8b1d09b645`. Source review dated 2026-09-30.

### Trigger and evidence

Connect to an unavailable or unresolvable server. After socket creation, error paths mark the connection broken and return without closing the descriptor. Retry/destruction only calls disconnect when isOpen is set, which never occurs on the failed initial connection.

- [cxx/src/EvbcConnection.cpp:68](https://github.com/NovaDAQ/EventBuilderClient/blob/c09ce105f69b6c71d21b6c680d80db8b1d09b645/cxx/src/EvbcConnection.cpp#L68-L96)
- [cxx/src/EvbcConnection.cpp:110](https://github.com/NovaDAQ/EventBuilderClient/blob/c09ce105f69b6c71d21b6c680d80db8b1d09b645/cxx/src/EvbcConnection.cpp#L110-L115)
- [cxx/src/EvbcConnection.cpp:47](https://github.com/NovaDAQ/EventBuilderClient/blob/c09ce105f69b6c71d21b6c680d80db8b1d09b645/cxx/src/EvbcConnection.cpp#L47-L53)

### Impact

Repeated connection attempts leak descriptors and can eventually prevent the client process from opening other sockets or files.

### Recommended change

Release any owned socket on every failed connection path and on destruction regardless of protocol state, resetting the descriptor to -1. Prefer scoped ownership during connection setup.

### Validation / acceptance criteria

Repeatedly connect to a local closed port and an invalid address, then destroy the object; descriptor count must remain stable.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-034`. Central review and package documentation: `novadaq-documentation`.
