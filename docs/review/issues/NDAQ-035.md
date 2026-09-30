# NDAQ-035: Initialize the DCM descriptor before simulated-reader cleanup

[GitHub issue](https://github.com/NovaDAQ/NovaEventBuilderClient/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-035 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `e43f9a9047dc4e0d153159bd364441ca2f837f78`. Source review dated 2026-09-30.

### Trigger and evidence

Construct/configure a DCMReader with generateData=true and later destroy it. _dcmDataHandle is assigned only in hardware mode but is unconditionally passed to close in the destructor.

- [cxx/src/DCMReader.cpp:25](https://github.com/NovaDAQ/NovaEventBuilderClient/blob/e43f9a9047dc4e0d153159bd364441ca2f837f78/cxx/src/DCMReader.cpp#L25-L32)
- [cxx/src/DCMReader.cpp:61](https://github.com/NovaDAQ/NovaEventBuilderClient/blob/e43f9a9047dc4e0d153159bd364441ca2f837f78/cxx/src/DCMReader.cpp#L61-L65)
- [cxx/src/DCMReader.cpp:75](https://github.com/NovaDAQ/NovaEventBuilderClient/blob/e43f9a9047dc4e0d153159bd364441ca2f837f78/cxx/src/DCMReader.cpp#L75-L89)

### Impact

Simulated-reader cleanup uses an indeterminate descriptor and can close an unrelated file/socket or trigger undefined behavior.

### Recommended change

Initialize the descriptor to -1 and close only a valid owned descriptor. Preserve that invariant on construction/configuration failures.

### Validation / acceptance criteria

Use a simulated reader with unrelated sentinel descriptors open and verify construction/destruction leaves them usable; test failed hardware initialization separately.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-035`. Central review and package documentation: `novadaq-documentation`.
