# NDAQ-031: Use signed arithmetic for Hough coordinate differences

[GitHub issue](https://github.com/NovaDAQ/HoughPoint.old/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-031 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `2b9784d0d5502fe53fe8c83218db613789272cdb`. Source review dated 2026-09-30.

### Trigger and evidence

Two hits have oppositely signed coordinate differences, for example cell/plane pairs (1,2) and (2,1). Coordinates are uint32_t, so a negative difference wraps before conversion to float.

- [cxx/src/HoughPoint.cpp:54](https://github.com/NovaDAQ/HoughPoint.old/blob/2b9784d0d5502fe53fe8c83218db613789272cdb/cxx/src/HoughPoint.cpp#L54-L76)

### Impact

The computed angle and signed distance can be wrong by orders of magnitude or have the wrong sign, corrupting the legacy reconstruction result.

### Recommended change

Convert coordinates to a sufficiently wide signed or floating type before subtraction and multiplication; define the intended angle/distance convention for degenerate cases.

### Validation / acceptance criteria

Use analytic point pairs in all quadrants and swapped point order; compare with a signed double-precision reference, including identical/horizontal/vertical pairs.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-031`. Central review and package documentation: `novadaq-documentation`.
