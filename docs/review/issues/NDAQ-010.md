# NDAQ-010: Pass real metadata storage to the convenience group-read overload

[GitHub issue](https://github.com/NovaDAQ/ShmRdWr/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-010 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `b5fdeeed788b701ebc4b8a2a2603a2203eb41518`. Source review dated 2026-09-30.

### Trigger and evidence

Call read_grp(dest, max_bytes, timeout, keep, group) with an attached group and readable data. It constructs a reference from a null ShmRdWr_Info pointer, which read_ later writes through.

- [cxx/src/ShmRdWr.cpp:428](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/ShmRdWr.cpp#L428-L432)
- [cxx/src/ShmRdWr.cpp:335](https://github.com/NovaDAQ/ShmRdWr/blob/b5fdeeed788b701ebc4b8a2a2603a2203eb41518/cxx/src/ShmRdWr.cpp#L335-L341)

### Impact

The advertised convenience overload can crash a shared-memory reader. It also ignores its semKeepAfterDataAvail argument by forwarding false.

### Recommended change

Create a local ShmRdWr_Info and forward it by reference; preserve the requested semaphore behavior. Remove null-reference sentinel conventions from this overload.

### Validation / acceptance criteria

Use a temporary isolated shared-memory group with one record and test both keep settings under UBSan/ASan; verify returned bytes and semaphore ownership.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-010`. Central review and package documentation: `novadaq-documentation`.
