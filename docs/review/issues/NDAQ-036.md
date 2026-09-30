# NDAQ-036: Initialize the DCM descriptor before simulated-reader cleanup

[GitHub issue](https://github.com/NovaDAQ/NovaEventBuilderClient_OLD/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-036 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `d0de530f1417315ca2cbc92688c3d222ecbcaa36`. Source review dated 2026-09-30.

### Trigger and evidence

Construct/configure a DCMReader with generateData=true and later destroy it. _dcmDataHandle is assigned only in hardware mode but is unconditionally passed to close in the destructor.

- [cxx/src/DCMReader.cpp:28](https://github.com/NovaDAQ/NovaEventBuilderClient_OLD/blob/d0de530f1417315ca2cbc92688c3d222ecbcaa36/cxx/src/DCMReader.cpp#L28-L35)
- [cxx/src/DCMReader.cpp:64](https://github.com/NovaDAQ/NovaEventBuilderClient_OLD/blob/d0de530f1417315ca2cbc92688c3d222ecbcaa36/cxx/src/DCMReader.cpp#L64-L68)
- [cxx/src/DCMReader.cpp:78](https://github.com/NovaDAQ/NovaEventBuilderClient_OLD/blob/d0de530f1417315ca2cbc92688c3d222ecbcaa36/cxx/src/DCMReader.cpp#L78-L92)

### Impact

Simulated-reader cleanup uses an indeterminate descriptor and can close an unrelated file/socket or trigger undefined behavior.

### Recommended change

Initialize the descriptor to -1 and close only a valid owned descriptor. Preserve that invariant on construction/configuration failures.

### Validation / acceptance criteria

Use a simulated reader with unrelated sentinel descriptors open and verify construction/destruction leaves them usable; test failed hardware initialization separately.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-036`. Central review and package documentation: `novadaq-documentation`.
