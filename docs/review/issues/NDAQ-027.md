# NDAQ-027: Flush the final JSON metadata field at end of input

[GitHub issue](https://github.com/NovaDAQ/NovaFTS/issues/2) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-027 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `a9c9400970f6431ca1b4d77ea2e046cd3bc3779c`. Source review dated 2026-09-30.

### Trigger and evidence

The final metadata field is Runs or Parents and input ends without a subsequent numbered field or separator. The parser enters json mode and commits it only when a later delimiter is encountered.

- [plugins/nova_art_metadata.py:27](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/plugins/nova_art_metadata.py#L27-L34)
- [plugins/nova_art_metadata.py:54](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/plugins/nova_art_metadata.py#L54-L64)

### Impact

Valid trailing run or parent metadata is silently omitted, potentially losing file lineage or preventing correct catalog registration.

### Recommended change

Flush the pending JSON accumulator at EOF, validate malformed JSON, and apply the correction to the dd-03 and dd-07 copies.

### Validation / acceptance criteria

Verify Runs and Parents as the last field, with and without trailing newline/separator, and confirm identical parsed metadata.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-027`. Central review and package documentation: `novadaq-documentation`.
