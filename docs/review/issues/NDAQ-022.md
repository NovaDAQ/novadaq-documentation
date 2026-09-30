# NDAQ-022: Initialize the receive timeout when copying DDSInbox

[GitHub issue](https://github.com/NovaDAQ/DAQMessages/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-022 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `cd0e5d09b401afc9f3dad448d7838f00cd60e778`. Source review dated 2026-09-30.

### Trigger and evidence

Copy-construct a DDSInbox and then call receiveMessage. The copy constructor initializes the base and receiver but leaves the unsigned _timeout member indeterminate.

- [cxx/include/DDSMailbox.hpp:69](https://github.com/NovaDAQ/DAQMessages/blob/cd0e5d09b401afc9f3dad448d7838f00cd60e778/cxx/include/DDSMailbox.hpp#L69-L75)
- [cxx/include/DDSMailbox.hpp:87](https://github.com/NovaDAQ/DAQMessages/blob/cd0e5d09b401afc9f3dad448d7838f00cd60e778/cxx/include/DDSMailbox.hpp#L87-L93)

### Impact

The copied inbox passes an undefined timeout to the RMS receiver, causing unpredictable blocking or polling behavior.

### Recommended change

Copy _timeout from the source (and explicitly initialize listening state), or delete copying if an inbox cannot be safely copied.

### Validation / acceptance criteria

Construct an inbox with a nondefault timeout, copy it, and use a stub receiver to verify the exact timeout passed on the first receive.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-022`. Central review and package documentation: `novadaq-documentation`.
