# NDAQ-021: Validate register ioctl user copies and MMIO indices

[GitHub issue](https://github.com/NovaDAQ/dcm_kernel_module/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-021 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `e829ed41041a5d95f3f99d048cae63a503f64d79`. Source review dated 2026-09-30.

### Trigger and evidence

A process with access to the control device submits an invalid pointer or an index beyond the FPGA/time-command register mapping. The ioctl ignores copy_from_user failures and indexes the MMIO pointer directly.

- [dcm_control.c:553](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.c#L553-L575)
- [dcm_control.c:614](https://github.com/NovaDAQ/dcm_kernel_module/blob/e829ed41041a5d95f3f99d048cae63a503f64d79/dcm_control.c#L614-L623)

### Impact

Malformed local requests can read or write outside the mapped register block or use incomplete copied data in kernel context, risking kernel faults and unintended hardware writes. Device access is a prerequisite.

### Recommended change

Return -EFAULT for incomplete user copies, validate each index against the actual mapping and allowed register set before access, and propagate copy_to_user failures.

### Validation / acceptance criteria

Use a mocked MMIO region or dedicated driver test target; invalid user pointers and boundary/out-of-range indices must return errors with zero MMIO accesses. Do not probe a live detector.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-021`. Central review and package documentation: `novadaq-documentation`.
