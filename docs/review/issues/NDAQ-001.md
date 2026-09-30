# NDAQ-001: Require authorization for timing hardware mutations

[GitHub issue](https://github.com/NovaDAQ/TDUWeb/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-001 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `e9904eba0d5ef9da4adac18c3f6374523bc008f2`. Source review dated 2026-09-30.

### Trigger and evidence

A client that can reach port 8080 can issue GET requests to /tdu_sync, /tdu_init or /tdu_scrub. These handlers invoke tduControl directly; the server binds all interfaces and has no authentication or authorization checks.

- [server/tdu_webserver.py:26](https://github.com/NovaDAQ/TDUWeb/blob/e9904eba0d5ef9da4adac18c3f6374523bc008f2/server/tdu_webserver.py#L26-L43)
- [server/tdu_webserver.py:70](https://github.com/NovaDAQ/TDUWeb/blob/e9904eba0d5ef9da4adac18c3f6374523bc008f2/server/tdu_webserver.py#L70-L70)

### Impact

Reachable clients can change timing-control registers or scrub hardware during data taking. GET also allows unintended invocation by browsers and automated URL fetchers. Network exposure in the deployed environment has not been measured.

### Recommended change

Require authenticated, authorized POST requests for mutations, add CSRF protection where browser credentials are used, and bind to the intended management interface. Keep status endpoints separate from mutation handlers.

### Validation / acceptance criteria

Mock subprocess execution. Assert anonymous GET/POST requests never invoke tduControl, authorized POST does, and rejected requests leave hardware untouched. Do not reproduce against live timing hardware.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-001`. Central review and package documentation: `novadaq-documentation`.
