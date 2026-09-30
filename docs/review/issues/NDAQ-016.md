# NDAQ-016: Import error-path dependencies used by the file cleaner

[GitHub issue](https://github.com/NovaDAQ/FileTransferService/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-016 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `073251b32cb943d58ade3fc2b32902258ba93b78`. Source review dated 2026-09-30.

### Trigger and evidence

A candidate disappears before checkForDelete, or unlink raises OSError. These paths reference defer and errno, neither of which is imported in cleaner.py.

- [python/fts/cleaner.py:1](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/cleaner.py#L1-L7)
- [python/fts/cleaner.py:64](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/cleaner.py#L64-L69)
- [python/fts/cleaner.py:118](https://github.com/NovaDAQ/FileTransferService/blob/073251b32cb943d58ade3fc2b32902258ba93b78/python/fts/cleaner.py#L118-L125)

### Impact

Expected filesystem races raise NameError instead of returning a successful no-op or a logged deletion failure.

### Recommended change

Import twisted.internet.defer and errno, and keep the asynchronous return contract consistent across early exits.

### Validation / acceptance criteria

Mock nonexistent paths and unlink raising ENOENT/EACCES; verify clean completion or the intended failure result without NameError.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-016`. Central review and package documentation: `novadaq-documentation`.
