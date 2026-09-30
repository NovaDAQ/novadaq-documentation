# NDAQ-020: Check open failure with a negative descriptor test

[GitHub issue](https://github.com/NovaDAQ/RawFileParser/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-020 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `c23da44c4ae2b7770204218a91eacf1b46db1da7`. Source review dated 2026-09-30.

### Trigger and evidence

open() returns descriptor 0 when stdin is closed, or -1 for a missing/unreadable file. The code tests if(!infile), treating descriptor 0 as failure and -1 as success.

- [cxx/src/RawFileParser.cpp:156](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/RawFileParser.cpp#L156-L174)

### Impact

Valid inputs can fail to open in daemon or redirected environments; invalid inputs are marked open before later errors, and the descriptor-0 path loses track of the open handle.

### Recommended change

Test infile < 0, preserve the failure result while resetting state, and close any acquired descriptor on subsequent initialization failures.

### Validation / acceptance criteria

In an isolated child process close stdin, open a temporary valid file, and confirm descriptor 0 works. Test missing, unreadable, and empty files for clean state and no descriptor leaks.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-020`. Central review and package documentation: `novadaq-documentation`.
