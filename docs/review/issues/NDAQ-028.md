# NDAQ-028: Raise the declared unknown-transfer exception so retries run

[GitHub issue](https://github.com/NovaDAQ/FileTransferService/issues/3) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-028 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `073251b32cb943d58ade3fc2b32902258ba93b78`. Source review dated 2026-09-30.

### Trigger and evidence

SAM reports Unknown transfer id. The handler raises UnknownSamTransfer, but the defined exception and retry trap are named UnknownSAMTransfer.

- [python/fts/sam.py:16](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/sam.py#L16-L16)
- [python/fts/sam.py:184](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/sam.py#L184-L193)

### Impact

NameError bypasses the intended unknown-transfer recovery path, stopping status polling without resubmitting the transfer.

### Recommended change

Raise the declared UnknownSAMTransfer and retain the original context; verify the TransferState errback reschedules the transfer.

### Validation / acceptance criteria

Mock a SAM unknown-ID response and assert the intended exception reaches the retry handler and one retry is scheduled.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-028`. Central review and package documentation: `novadaq-documentation`.
