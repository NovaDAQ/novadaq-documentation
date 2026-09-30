# Failure recovery

## Triage by symptom

| Symptom | First checks | Recovery and verification |
| --- | --- | --- |
| Participant cannot join/configure | Detector/DAQ/DDS partition, message schema/provider, resource reservation, generated configuration URL | Correct the mismatch, repeat the supported transition, and require acknowledgements from all intended participants |
| Buffer node reports missing data | DCM/FEB link status, receive rate/timeouts, history coverage, source/consumer counts | Preserve timestamps and counters, repair the input connection, then verify losses stop; restart only after accounting for lost retained history |
| Logger output stops or write errors appear | Filesystem space/mount/permissions, upstream connection, stream configuration | Stop/drain safely, preserve partial files, repair storage, validate finalized files before resuming transfer |
| Parser hangs on a damaged file | File checksum/length, repeated partial markers, RawFileParser findings | Work on a copy with a bounded test harness; quarantine from automatic metadata processing until parsing terminates safely |
| Transfer backlog grows | Metadata errors, catalog reachability, credentials, pending/failed state and retry logs | Resolve the cause, retry known failed entries, and verify actual archive/CRC state; preserve local data until confirmed |
| Timing or spill input is stale | TDU status/error counters, synchronization, source/forwarder registration, timestamp conversion | Inhibit affected triggering through the supported control path, recover timing input, and verify timestamps/counters before restart |
| DCS/display looks healthy but no updates arrive | PV/metric age, IOC/message server, process and log activity | Restore the producer/connection and verify a new sample; do not treat cached values as current health |
| Repeated shutdown/reconnect crashes | RMS and run-control cleanup findings, descriptors, outstanding callbacks | Preserve crash/log evidence, apply the lifecycle correction, and test multiple complete restart cycles |
| Power/recovery script fails | Argument validation, site target list, syntax, command return values | Inspect and reproduce with command stubs; use the trained-expert checklist for physical recovery |

## Minimum incident record

Capture UTC time and detector/site, run/subrun and partition IDs, affected host/process, software commits or release, configuration identity, relevant logs/counters, and the first observed failure. Record any intervention and whether buffered data, incomplete files, or calibration state may have been lost. Link the incident to the applicable GitHub issue rather than closing the issue because a restart temporarily helped.

## Shared-memory recovery

Use read-only inspection first. Verify segment geometry, ownership, active writer, reader groups, overwrite counts, and semaphore state. Stop all owners through the controlled lifecycle before recreating a segment. Recreating live shared memory discards retained data and can leave readers attached to an obsolete segment; restart/reconnect and verify every participant against the new instance.

## File and metadata reconciliation

Treat a file as complete only after logger finalization and format checks. Compare actual size, header/tail lengths, run/event counts, detector/DCM/buffer-node metadata, catalog state, and archive CRC. For files affected by metadata findings, preserve the original metadata and regenerate from the same immutable raw input after the fix. Do not delete a local source merely because a transfer request was accepted or a completion marker exists.

## Configuration and database recovery

Back up current state before restoration. Choose one coherent named/global configuration, its schema version, and its generated files. Reconcile resource reservations with live processes. Revalidate hardware settings and participant acknowledgements before data taking. Schema restoration and configuration rollback are different operations and should have separately recorded evidence.

## Hardware and site power recovery

Use the source-controlled [FarDetectorPowerOn package](../packages/FarDetectorPowerOn.md) and current expert procedure. Verify target identity, supply readback, cooling/interlocks where required by that procedure, network/storage readiness, and timing before enabling acquisition. The review did not validate a live power sequence or change any detector hardware.
