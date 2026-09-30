# NDAQ-039: Check the first-scan guard before reading previous channel state

[GitHub issue](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-039 -->
Severity: **P3 — Low** · Estimated scope: **S**

Reviewed revision: `b3fc11787f0cbc99ae0be1a0030706d744abe36a`. Source review dated 2026-09-30.

### Trigger and evidence

On the first analyzed scan, prevstate has not been initialized. Both transition conditions evaluate prevstate[idcm][ifeb][ipixel] as the left operand of && before evaluating iscan != startscan. The later assignment only initializes it after this read.

- [makeDsoPlots.C:880](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/makeDsoPlots.C#L880-L885)
- [makeDsoPlots.C:910](https://github.com/NovaDAQ/PedestalAnalysis_Scripts/blob/b3fc11787f0cbc99ae0be1a0030706d744abe36a/makeDsoPlots.C#L910-L947)

### Impact

First-scan processing reads an indeterminate scalar. The right-hand first-scan guard prevents the transition body from running in the apparent control flow, so no incorrect flip count is established; the defect is undefined behavior in the compiled macro.

### Recommended change

Evaluate iscan != startscan first, or explicitly initialize prevstate when setting up the first scan. Preserve the rule that the first observation is not a transition.

### Validation / acceptance criteria

Extract the channel-transition loop into a fixture harness or run an instrumented macro on a single scan and on known good/bad transitions. Verify no uninitialized reads, zero flips for one scan, and the expected count for subsequent changes.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-039`. Central review and package documentation: `novadaq-documentation`.
