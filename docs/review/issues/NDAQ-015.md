# NDAQ-015: Assign failed-file destination before logging it

[GitHub issue](https://github.com/NovaDAQ/FileTransferService/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-015 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `073251b32cb943d58ade3fc2b32902258ba93b78`. Source review dated 2026-09-30.

### Trigger and evidence

All states of a file finish with a failure and shouldMoveFailed() is true. checkIfFinished formats a log message using movedir before its assignment on the next line.

- [python/fts/filestate.py:182](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/filestate.py#L182-L188)

### Impact

UnboundLocalError aborts the failed-file transition, preventing quarantine movement, finished-state bookkeeping, and completion callbacks.

### Recommended change

Resolve the failed destination before logging or scheduling the move; propagate configuration errors through the existing failure path.

### Validation / acceptance criteria

Use a mocked reactor and file-type config with shouldMoveFailed enabled. Verify the configured move is scheduled and completion bookkeeping executes without touching real archive files.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-015`. Central review and package documentation: `novadaq-documentation`.
