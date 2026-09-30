# NDAQ-026: Use a dictionary fallback when resolving ART process metadata

[GitHub issue](https://github.com/NovaDAQ/NovaFTS/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-026 -->
Severity: **P2 — Medium** · Estimated scope: **S**

Reviewed revision: `a9c9400970f6431ca1b4d77ea2e046cd3bc3779c`. Source review dated 2026-09-30.

### Trigger and evidence

sam_metadata_dumper emits ProcessName before any Application fields. md.get("application", []) returns a list, then the parser calls .get("name") on it.

- [plugins/nova_art_metadata.py:44](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/plugins/nova_art_metadata.py#L44-L47)
- [podmanFTS/dd-03/plugins/nova_art_metadata.py:44](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-03/plugins/nova_art_metadata.py#L44-L47)
- [podmanFTS/dd-07/plugins/nova_art_metadata.py:44](https://github.com/NovaDAQ/NovaFTS/blob/a9c9400970f6431ca1b4d77ea2e046cd3bc3779c/podmanFTS/dd-07/plugins/nova_art_metadata.py#L44-L47)

### Impact

Metadata extraction raises AttributeError for an ordinary field ordering, blocking registration/transfer of the affected ART file.

### Recommended change

Use a dictionary fallback and handle the absence or malformed type of application metadata. Keep both container copies synchronized.

### Validation / acceptance criteria

Extract metadata from ProcessName-only input and from ProcessName preceding/following ApplicationName. Require a valid application mapping without exceptions.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-026`. Central review and package documentation: `novadaq-documentation`.
