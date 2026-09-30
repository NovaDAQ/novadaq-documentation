# NDAQ-017: Initialize output-file state before DSO readout and scope output

[GitHub issue](https://github.com/NovaDAQ/DCM_ProgUtils/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-017 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `e294d36d974d7b60042df6e6030fc558acb26a2c`. Source review dated 2026-09-30.

### Trigger and evidence

Enable output-file mode. Both tools use for(int i; i<64; ++i) without initializing i. When scan_flag is false, suffix is also concatenated without being initialized.

- [cxx/src/dcmDSOReadout.cc:880](https://github.com/NovaDAQ/DCM_ProgUtils/blob/e294d36d974d7b60042df6e6030fc558acb26a2c/cxx/src/dcmDSOReadout.cc#L880-L903)
- [cxx/src/dcmScope.cc:772](https://github.com/NovaDAQ/DCM_ProgUtils/blob/e294d36d974d7b60042df6e6030fc558acb26a2c/cxx/src/dcmScope.cc#L772-L795)

### Impact

Output setup can index outside outputfiles or construct a filename from uninitialized stack data, causing failed or misdirected diagnostic output.

### Recommended change

Initialize the loop counter to zero and construct a defined suffix for every supported mode, ideally using bounded C++ strings.

### Validation / acceptance criteria

Exercise output mode with scan on/off and mock device access; require deterministic filenames, initialized handles, and clean ASan/UBSan runs.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-017`. Central review and package documentation: `novadaq-documentation`.
