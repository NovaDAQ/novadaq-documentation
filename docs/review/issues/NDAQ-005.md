# NDAQ-005: Advance reply-map iterator safely when expiring requests

[GitHub issue](https://github.com/NovaDAQ/ResponsiveMessagingSystem/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-005 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `e7d72bb3b45279b9564d1dced3725428c3873eba`. Source review dated 2026-09-30.

### Trigger and evidence

RmsProducer::verify handles a successful reply while _replyIdTable contains an entry older than _replyTimeout. It erases replyIterator and then increments that same iterator.

- [cxx/src/RmsProducer.cpp:276](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/RmsProducer.cpp#L276-L296)

### Impact

A routine request timeout can trigger undefined behavior or crash the messaging producer, disrupting control traffic.

### Recommended change

Use the iterator returned by erase on a supported C++ standard, or increment before erasing. Preserve traversal of adjacent expired entries.

### Validation / acceptance criteria

Verify with checked iterators for empty, all-expired, and mixed expired/live tables; confirm the live correlation ID is accepted and expired IDs are removed.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-005`. Central review and package documentation: `novadaq-documentation`.
