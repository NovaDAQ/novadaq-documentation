# NDAQ-003: Write one CRC word when finalizing a run file

[GitHub issue](https://github.com/NovaDAQ/NovaDataLogger/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-003 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `e048941cdef398dce47cba02cb8adad3d93945a2`. Source review dated 2026-09-30.

### Trigger and evidence

RunStream finalizes a nonempty run: size becomes sizeof(uint32_t), then fwrite(&crc, 4, size, ...) requests four four-byte elements from a single four-byte variable.

- [cxx/src/RunStream.cpp:219](https://github.com/NovaDAQ/NovaDataLogger/blob/e048941cdef398dce47cba02cb8adad3d93945a2/cxx/src/RunStream.cpp#L219-L226)

### Impact

Every execution of this path reads twelve bytes past crc and appends sixteen bytes instead of the one CRC word counted in the run size. This corrupts the file trailer and can leak adjacent stack contents.

### Recommended change

Write exactly one uint32_t and compare the result against one element, or use byte-sized elements consistently. Verify run-size accounting and downstream parser expectations.

### Validation / acceptance criteria

Finalize a small synthetic run under AddressSanitizer; assert the trailer contains exactly four CRC bytes and that reported run size equals actual bytes. Reopen it with RawFileParser.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-003`. Central review and package documentation: `novadaq-documentation`.
