# NDAQ-008: Bound buffer-node metadata traversal to the allocated counter array

[GitHub issue](https://github.com/NovaDAQ/MetaDataTools/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-008 -->
Severity: **P1 — High** · Estimated scope: **S**

Reviewed revision: `3693eca92edd78c9c7fd55975fbdbddd9766b30e`. Source review dated 2026-09-30.

### Trigger and evidence

Metadata generation iterates ibuff from 1 through 199, but buffIDs is declared with 100 elements.

- [cxx/src/MetaDataRunTool.cc:261](https://github.com/NovaDAQ/MetaDataTools/blob/3693eca92edd78c9c7fd55975fbdbddd9766b30e/cxx/src/MetaDataRunTool.cc#L261-L261)
- [cxx/src/MetaDataRunTool.cc:910](https://github.com/NovaDAQ/MetaDataTools/blob/3693eca92edd78c9c7fd55975fbdbddd9766b30e/cxx/src/MetaDataRunTool.cc#L910-L919)

### Impact

The normal metadata output path reads outside the array and can report nonexistent buffer nodes or crash. Real buffer IDs above the allocation also need an explicit policy.

### Recommended change

Use one detector-appropriate capacity shared by allocation, initialization, increment, and output, and validate observed IDs before indexing.

### Validation / acceptance criteria

Generate metadata for synthetic runs with boundary buffer IDs under AddressSanitizer; assert no out-of-bounds access and an exact BufferNodeList.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-008`. Central review and package documentation: `novadaq-documentation`.
