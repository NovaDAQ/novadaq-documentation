# NDAQ-007: Handle summary windows older than retained missed-buffer history

[GitHub issue](https://github.com/NovaDAQ/BufferNodeEVB/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-007 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `9c9c0f3b21e37f9e726fa651c6b99284f2a5a14d`. Source review dated 2026-09-30.

### Trigger and evidence

A summary trigger has an end timestamp earlier than every retained missed-buffer entry. The loop advances it to end(), then line 878 dereferences it. The earlier missingData flag does not stop this path.

- [cxx/src/MegaPool.cpp:842](https://github.com/NovaDAQ/BufferNodeEVB/blob/9c9c0f3b21e37f9e726fa651c6b99284f2a5a14d/cxx/src/MegaPool.cpp#L842-L848)
- [cxx/src/MegaPool.cpp:868](https://github.com/NovaDAQ/BufferNodeEVB/blob/9c9c0f3b21e37f9e726fa651c6b99284f2a5a14d/cxx/src/MegaPool.cpp#L868-L885)

### Impact

An out-of-history trigger can crash the buffer-node process while reporting incomplete data, interrupting event building.

### Recommended change

Check for end() before dereference and produce an explicit incomplete summary for unavailable history. Also define behavior for an empty history before front/back access.

### Validation / acceptance criteria

Cover windows before all history, overlapping history, after history, and empty history with checked iterators. Require a valid incomplete-data result without process termination.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-007`. Central review and package documentation: `novadaq-documentation`.
