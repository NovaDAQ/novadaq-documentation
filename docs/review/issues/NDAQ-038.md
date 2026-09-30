# NDAQ-038: Close the input file when FEB macro output creation fails

[GitHub issue](https://github.com/NovaDAQ/RunSummaryUtils/issues/3) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-038 -->
Severity: **P3 — Low** · Estimated scope: **S**

Reviewed revision: `148d674e4d44ccea03f1375fdaec4242f8c390c2`. Source review dated 2026-09-30.

### Trigger and evidence

With isNtupleCreated enabled, the input fopen can succeed while the output fopen fails (for example, insufficient directory permissions). Both macro versions return immediately from that branch without closing file1; their normal fclose is below the processing loop.

- [macros/FebProcedure4.C:244](https://github.com/NovaDAQ/RunSummaryUtils/blob/148d674e4d44ccea03f1375fdaec4242f8c390c2/macros/FebProcedure4.C#L244-L260)
- [macros/FebProcedure5.C:266](https://github.com/NovaDAQ/RunSummaryUtils/blob/148d674e4d44ccea03f1375fdaec4242f8c390c2/macros/FebProcedure5.C#L266-L282)

### Impact

Each failed invocation retains an input descriptor in the ROOT session. Repeated retries can accumulate descriptors until subsequent file opens fail.

### Recommended change

Close the already-open input before the failure return, or use a scoped file owner that closes both streams on all exits.

### Validation / acceptance criteria

Use an existing fixture input and an unwritable output directory, invoke repeatedly in one process, and verify the descriptor count stays constant. Verify the successful output path still closes both streams.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-038`. Central review and package documentation: `novadaq-documentation`.
