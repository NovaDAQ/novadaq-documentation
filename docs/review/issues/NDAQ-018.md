# NDAQ-018: Skip the first event-size delta until a previous size exists

[GitHub issue](https://github.com/NovaDAQ/RunSummaryUtils/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-018 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `148d674e4d44ccea03f1375fdaec4242f8c390c2`. Source review dated 2026-09-30.

### Trigger and evidence

Process the first event in each input file. s_last is uninitialized when ds = s_last - s is evaluated.

- [cxx/src/RunSummary.cc:383](https://github.com/NovaDAQ/RunSummaryUtils/blob/148d674e4d44ccea03f1375fdaec4242f8c390c2/cxx/src/RunSummary.cc#L383-L400)

### Impact

The delta-size histogram receives an undefined first sample, compromising diagnostic summaries and potentially introducing NaN or extreme values.

### Recommended change

Track whether a previous event exists, fill the delta histogram only for event pairs, and reset that state between files.

### Validation / acceptance criteria

For known sizes [100, 120, 90], verify exactly two delta samples with the documented sign convention; cover empty and single-event files.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-018`. Central review and package documentation: `novadaq-documentation`.
