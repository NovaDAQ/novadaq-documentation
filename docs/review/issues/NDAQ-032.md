# NDAQ-032: Compare leap-second thresholds against the original UNIX time

[GitHub issue](https://github.com/NovaDAQ/NovaTimingUtilities/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-032 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `6f97c3fba53211f262755d3e5bf7abde275aecd5`. Source review dated 2026-09-30.

### Trigger and evidence

Convert UNIX second 1435708799 (2015-06-30 23:59:59 UTC). The 2012 adjustment increments the working value to 1435708800, which then incorrectly satisfies the 2015 threshold. The 2016 threshold is similarly reached two seconds early.

- [cxx/src/TimingUtilities.cpp:22](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/TimingUtilities.cpp#L22-L34)
- [cxx/src/TimingUtilities.cpp:55](https://github.com/NovaDAQ/NovaTimingUtilities/blob/6f97c3fba53211f262755d3e5bf7abde275aecd5/cxx/src/TimingUtilities.cpp#L55-L65)

### Impact

Conversions immediately before later leap boundaries acquire an extra second, affecting historical timestamp correlation and boundary consistency.

### Recommended change

Compare every UNIX threshold to the unmodified input timestamp, accumulate the leap offset separately, and validate the inverse conversions against a documented leap table.

### Validation / acceptance criteria

Test each second around the 2012, 2015, and 2016 boundaries for timespec and timeval overloads against an independent leap-offset table.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-032`. Central review and package documentation: `novadaq-documentation`.
