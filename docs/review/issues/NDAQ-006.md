# NDAQ-006: Delete the completed EPICS assembler before invalidating its iterator

[GitHub issue](https://github.com/NovaDAQ/ResponsiveMessagingSystem/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-006 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `e7d72bb3b45279b9564d1dced3725428c3873eba`. Source review dated 2026-09-30.

### Trigger and evidence

An incoming fragment completes an existing assembler. monitorChanged erases its vector iterator, notifies listeners, then dereferences the invalidated iterator in delete *i.

- [cxx/src/provider/EpicsMessenger.cpp:164](https://github.com/NovaDAQ/ResponsiveMessagingSystem/blob/e7d72bb3b45279b9564d1dced3725428c3873eba/cxx/src/provider/EpicsMessenger.cpp#L164-L179)

### Impact

Completion can delete the next assembler or dereference past the vector end, causing crashes, lost messages, or later double deletion.

### Recommended change

Save the completed assembler pointer, remove it from the vector, and release that saved object with a clear ownership policy. Account for listener callbacks re-entering the code.

### Validation / acceptance criteria

Complete the only assembler and then the first of two assemblers under AddressSanitizer; verify one notification, destruction of only the completed object, and successful later completion of the second message.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-006`. Central review and package documentation: `novadaq-documentation`.
