# NDAQ-011: Keep rrd_xport argument strings alive across vector growth

[GitHub issue](https://github.com/NovaDAQ/DetectorPlotter/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-011 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `e12078ae40e3f0071d5cfe3fb97e756ae7c97715`. Source review dated 2026-09-30.

### Trigger and evidence

GetSingleVarData takes c_str pointers after each push_back into vs, then continues adding strings. Reallocation can move short strings and invalidate previously stored argv pointers before rrd_xport.

- [cxx/src/NovaRRDReader.cpp:49](https://github.com/NovaDAQ/DetectorPlotter/blob/e12078ae40e3f0071d5cfe3fb97e756ae7c97715/cxx/src/NovaRRDReader.cpp#L49-L95)

### Impact

RRD reads can fail or read freed memory, especially on modern standard libraries with small-string optimization or when the number of requested variables grows.

### Recommended change

Build the complete vector of strings first, then construct argv without further mutations; avoid shared static scratch state if calls can run concurrently.

### Validation / acceptance criteria

Exercise first call and increasing variable counts with short and long arguments under ASan; a stub rrd_xport must receive every intact argument.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-011`. Central review and package documentation: `novadaq-documentation`.
