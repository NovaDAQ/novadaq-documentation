# NDAQ-009: Retain every active DCM in generated metadata

[GitHub issue](https://github.com/NovaDAQ/MetaDataTools/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-009 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `3693eca92edd78c9c7fd55975fbdbddd9766b30e`. Source review dated 2026-09-30.

### Trigger and evidence

A run contains more than one active DCM. The first-entry branch uses firstdcm==true instead of assigning firstdcm=true, so every active DCM clears dcmlist again.

- [cxx/src/MetaDataRunTool.cc:879](https://github.com/NovaDAQ/MetaDataTools/blob/3693eca92edd78c9c7fd55975fbdbddd9766b30e/cxx/src/MetaDataRunTool.cc#L879-L891)

### Impact

ActiveDCMs metadata contains only the final DCM encountered, understating detector participation.

### Recommended change

Set the first-entry flag or build the list with a string/container join that handles separators without repeated clearing.

### Validation / acceptance criteria

Generate metadata for zero, one, and several active DCMs; verify all expected names appear exactly once.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-009`. Central review and package documentation: `novadaq-documentation`.
