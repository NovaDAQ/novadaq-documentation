# NDAQ-033: Stop release packaging when configure, build, or tests fail

[GitHub issue](https://github.com/NovaDAQ/ups/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-033 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `9695b34d7b9f7ee5ee61977d4473fe2eea2b114d`. Source review dated 2026-09-30.

### Trigger and evidence

cmake, make, or make test returns nonzero. The script has no failure guard and proceeds to make install. If pkgdir/lib already exists, it can announce success, package artifacts, and exit zero.

- [build_novadaq.sh:336](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/build_novadaq.sh#L336-L352)
- [build_novadaq.sh:359](https://github.com/NovaDAQ/ups/blob/9695b34d7b9f7ee5ee61977d4473fe2eea2b114d/build_novadaq.sh#L359-L370)

### Impact

Failed builds/tests can be reported as successful releases and stale or unvalidated artifacts can be distributed.

### Recommended change

Check each setup/configure/build/test/install command and stop immediately on failure. Validate artifacts from this build rather than relying on a preexisting lib directory.

### Validation / acceptance criteria

Use command stubs in a temporary build/product tree to fail each stage in turn. Require a nonzero exit, no later install/package invocation, and no success message; cover a preexisting lib directory.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-033`. Central review and package documentation: `novadaq-documentation`.
