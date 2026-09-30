# NDAQ-012: Initialize and advance the status-read frame cursor

[GitHub issue](https://github.com/NovaDAQ/DataConcentratorModule/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-012 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `18dbefa32acb189d7861ec56a974a6960dc96766`. Source review dated 2026-09-30.

### Trigger and evidence

A userspace read requests no more words than are currently buffered. The else branch indexes using uninitialized words_to_copy; its while(1) never increments that variable.

- [dcm_kernel/dcm_status.c:205](https://github.com/NovaDAQ/DataConcentratorModule/blob/18dbefa32acb189d7861ec56a974a6960dc96766/dcm_kernel/dcm_status.c#L205-L241)

### Impact

The legacy driver can index outside its status ring or loop indefinitely in kernel context. Deployment of this driver, rather than dcm_kernel_module, must be confirmed when assigning urgency.

### Recommended change

Initialize the cursor, advance it by each validated frame length, enforce ring and request bounds, and handle requests too small for one frame. Audit byte-versus-word sizes in the following copy_to_user path.

### Validation / acceptance criteria

Use a driver unit harness with empty/full/wrapped rings and reads smaller than, equal to, and larger than available data. Every case must terminate and stay within both buffers.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-012`. Central review and package documentation: `novadaq-documentation`.
