# NDAQ-023: Reject incorrectly sized messages before exposing typed payloads

[GitHub issue](https://github.com/NovaDAQ/DAQMessagesZMQ/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-023 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `48d08a04ebd6e210afed254bb61c7638c9c206a4`. Source review dated 2026-09-30.

### Trigger and evidence

A peer sends a message shorter or longer than sizeof(T). socket_t::recv treats every nonnegative zmq_recv return as success. Short frames leave fields unchanged/uninitialized; oversized frames are truncated even though the returned original size is larger.

- [cxx/include/ZMQMailbox.hpp:63](https://github.com/NovaDAQ/DAQMessagesZMQ/blob/48d08a04ebd6e210afed254bb61c7638c9c206a4/cxx/include/ZMQMailbox.hpp#L63-L68)

### Impact

Typed consumers can interpret incomplete trigger messages as valid. NovaGlobalTrigger reuses ddtMessage and NovaSuperNova NSNInbox returns its message without checking byte count, so malformed frames can combine new and stale fields.

### Recommended change

Validate an exact wire size and reject malformed frames without publishing or mutating a usable object. Define a stable serialization contract instead of depending indefinitely on native struct layout.

### Validation / acceptance criteria

With in-process ZeroMQ sockets send zero, short, exact, and oversized frames; only the exact valid frame may produce a typed result. Verify a rejected frame cannot reuse fields from the preceding valid trigger.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-023`. Central review and package documentation: `novadaq-documentation`.
