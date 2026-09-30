# NDAQ-019: Advance past rejected header candidates during marker searches

[GitHub issue](https://github.com/NovaDAQ/RawFileParser/issues/1) · Status: **open** · [Remediation priorities](../index.md)

<!-- novadaq-review:NDAQ-019 -->
Severity: **P1 — High** · Estimated scope: **M**

Reviewed revision: `c23da44c4ae2b7770204218a91eacf1b46db1da7`. Source review dated 2026-09-30.

### Trigger and evidence

A run or configuration search finds the first magic word followed by a nonmatching second word. The caller increments to check the second word, then decrements back to the first. wordsearch_mem returns the same match on the next iteration.

- [cxx/src/RawFileParser.cpp:397](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/RawFileParser.cpp#L397-L408)
- [cxx/src/RawFileParser.cpp:553](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/RawFileParser.cpp#L553-L563)
- [cxx/src/RawFileParser.cpp:1733](https://github.com/NovaDAQ/RawFileParser/blob/c23da44c4ae2b7770204218a91eacf1b46db1da7/cxx/src/RawFileParser.cpp#L1733-L1743)

### Impact

A damaged or coincidentally matching input file can trap parsing in an infinite CPU loop, blocking inspection and metadata pipelines that depend on RawFileParser.

### Recommended change

On a rejected pair advance past the candidate before resuming; enforce bounds for the adjacent-word check. Apply the same progress invariant to file-I/O variants.

### Validation / acceptance criteria

Parse synthetic files with isolated first markers, mismatched pairs, a bad pair before a valid pair, and a marker at EOF. Every search must terminate and find only valid pairs.

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `NDAQ-019`. Central review and package documentation: `novadaq-documentation`.
