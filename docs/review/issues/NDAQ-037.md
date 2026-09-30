# NDAQ-037: Initialize the DCM identifier before printing it in FEB macros

[GitHub issue](https://github.com/NovaDAQ/RunSummaryUtils/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-037 -->
Severity: **P3 — Low** · Estimated scope: **S**

Reviewed revision: `148d674e4d44ccea03f1375fdaec4242f8c390c2`. Source review dated 2026-09-30.

### Trigger and evidence

FebProcedure and FebProcedure2 print the automatic unsigned variable fdcm before the later assignment derived from idcm. Every invocation reaches this first diagnostic with an indeterminate value.

- [macros/FebProcedure.C:61](https://github.com/NovaDAQ/RunSummaryUtils/blob/148d674e4d44ccea03f1375fdaec4242f8c390c2/macros/FebProcedure.C#L61-L86)
- [macros/FebProcedure2.C:72](https://github.com/NovaDAQ/RunSummaryUtils/blob/148d674e4d44ccea03f1375fdaec4242f8c390c2/macros/FebProcedure2.C#L72-L98)

### Impact

The opening diagnostic can report a bogus DCM identifier and reads an uninitialized scalar. The later assignment corrects subsequent uses, so the demonstrated impact is limited to the initial diagnostic.

### Recommended change

Compute fdcm before the first printf, or remove the premature diagnostic in both macro versions.

### Validation / acceptance criteria

Run both macros with a known idcm using fixture files and verify that all reported real DCM identifiers equal idcm > 99 ? idcm - 100 : idcm. Compile with uninitialized-variable warnings enabled.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-037`. Central review and package documentation: `novadaq-documentation`.
