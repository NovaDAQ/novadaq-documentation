# NDAQ-040: Check ROOT canvas lookups before cloning them

[GitHub issue](https://github.com/NovaDAQ/DetectorPlotter/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-040 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `e12078ae40e3f0071d5cfe3fb97e756ae7c97715`. Source review dated 2026-09-30.

### Trigger and evidence

getCanvai calls f.Get for cFebMask, cPixelMask, and cThresholds and immediately dereferences each result with canv->Clone(). Its not-found checks examine the clone only after that dereference. A ROOT file missing any expected canvas reaches the null dereference.

- [scripts/showDSOHistos.C:62](https://github.com/NovaDAQ/DetectorPlotter/blob/e12078ae40e3f0071d5cfe3fb97e756ae7c97715/scripts/showDSOHistos.C#L62-L85)

### Impact

Viewing an incomplete or incompatible DSO histogram file can crash the ROOT session instead of reporting the missing canvas. Existing diagnostic messages do not protect this path.

### Recommended change

Validate each f.Get result and its type before cloning or reading its name. Return a clear incomplete-input result and make callers skip any absent canvases safely.

### Validation / acceptance criteria

Create a ROOT fixture with all canvases, then fixtures missing each expected canvas and an unreadable file. Verify the valid file renders and the invalid inputs produce diagnostics without crashing.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-040`. Central review and package documentation: `novadaq-documentation`.
