# ErrorHandler

Message analyzer with rules, GUI, and actions that can send mail, scripts, or Run Control messages.

## Identity and scope

Repository: [NovaDAQ/ErrorHandler](https://github.com/NovaDAQ/ErrorHandler) · Reviewed commit: `2c97c6860306edd1ea217892d75d389733a39f88` · Domain: **Monitoring**.

Tracked files: **123**. Production deployment and owner are **unconfirmed**.

## Operation

Review action rules and destinations before enabling them. Check message ingestion and rule matches separately from action success. Exercise rules against captured messages with action execution mocked before changing production responses.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [cxx/config/send_mail.sh](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/config/send_mail.sh) |
| [cxx/src/MsgAnalyzer.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/MsgAnalyzer.cc) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/EHListener.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/EHListener.h) | `EHListener` |
| [cxx/include/MsgAnalyzerDlg.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/MsgAnalyzerDlg.h) | `MsgAnalyzerDlg`, `display_field_t` |
| [cxx/include/MsgBox.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/MsgBox.h) | `MsgBox` |
| [cxx/include/NodeInfo.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/NodeInfo.h) | `NodeInfo`, `node_status` |
| [cxx/include/ma_action.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_action.h) | `ma_action`, `ma_action_factory`, `ma_action_maker`, `ma_condition`, `ma_rule` |
| [cxx/include/ma_action_mail.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_action_mail.h) | `ma_action_mail` |
| [cxx/include/ma_action_rcmsg.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_action_rcmsg.h) | `ma_action_rcmsg` |
| [cxx/include/ma_action_script.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_action_script.h) | `ma_action_script` |
| [cxx/include/ma_boolean_andexpr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_boolean_andexpr.h) | `ma_boolean_andexpr` |
| [cxx/include/ma_boolean_cond.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_boolean_cond.h) | `ma_boolean_cond`, `ma_boolean_expr`, `ma_rule` |
| [cxx/include/ma_boolean_expr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_boolean_expr.h) | `ma_boolean_expr` |
| [cxx/include/ma_cell.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_cell.h) | `ma_cell` |
| [cxx/include/ma_cond_test_andexpr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_cond_test_andexpr.h) | `ma_cond_test_andexpr` |
| [cxx/include/ma_cond_test_expr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_cond_test_expr.h) | `ma_cond_test_expr` |
| [cxx/include/ma_cond_test_primary.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_cond_test_primary.h) | `ma_cond_test_expr`, `ma_cond_test_primary` |
| [cxx/include/ma_condition.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_condition.h) | `ma_condition` |
| [cxx/include/ma_domain_andexpr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_domain_andexpr.h) | `ma_domain_andexpr` |
| [cxx/include/ma_domain_cond.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_domain_cond.h) | `ma_domain_cond`, `ma_domain_expr`, `ma_rule` |
| [cxx/include/ma_domain_expr.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_domain_expr.h) | `ma_domain_expr` |
| [cxx/include/ma_domain_ops.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_domain_ops.h) | `domain_compare_result_t` |
| [cxx/include/ma_function.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_function.h) | `ma_condition`, `ma_function`, `ma_function_factory`, `ma_function_maker` |
| [cxx/include/ma_function_count.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_function_count.h) | `ma_func_count` |
| [cxx/include/ma_function_countpercent.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_function_countpercent.h) | `ma_func_count_percent` |
| [cxx/include/ma_function_is_syncd.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_function_is_syncd.h) | `ma_func_is_syncd` |
| [cxx/include/ma_hitmap.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_hitmap.h) | `ma_condition`, `ma_hitmap` |
| [cxx/include/ma_parse.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_parse.h) | `ma_cond_test_expr`, `ma_rule` |
| [cxx/include/ma_participants.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_participants.h) | `ma_participants` |
| [cxx/include/ma_rcclient.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_rcclient.h) | `RunControlReceiver`, `ma_rcclient` |
| [cxx/include/ma_richmsg.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_richmsg.h) | `ma_richmsg`, `ma_rule` |
| [cxx/include/ma_rule.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_rule.h) | `ma_rule` |
| [cxx/include/ma_rule_engine.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_rule_engine.h) | `ParameterSet`, `ma_rule_engine` |
| [cxx/include/ma_test_function.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_test_function.h) | `ma_condition`, `ma_test_function`, `ma_test_function_factory`, `ma_test_function_maker` |
| [cxx/include/ma_tf_grp_to_number.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_tf_grp_to_number.h) | `ma_tf_grp_to_number` |
| [cxx/include/ma_timing_event.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_timing_event.h) | `ma_condition`, `ma_timing_event`, `ma_timing_event_order`, `ma_timing_events` |
| [cxx/include/ma_types.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_types.h) | `action_type_t`, `arg_t`, `compare_op_t`, `cond_type_t`, `ma_condition`, `ma_rule`, `match_type_t`, `message_type_t`, `node_type_t`, `notify_t`, `rule_type_t` |
| [cxx/include/ma_utils.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_utils.h) | Functions, constants, or templates |
| [cxx/include/qt_log_reader.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/qt_log_reader.h) | `qt_log_reader` |
| [cxx/include/qt_rule_engine.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/qt_rule_engine.h) | `ParameterSet`, `qt_rule_engine` |
| [cxx/include/ui_MsgAnalyzerDlg.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ui_MsgAnalyzerDlg.h) | `MsgAnalyzerDlg`, `Ui_MsgAnalyzerDlg` |
| [cxx/include/ui_MsgBox.h](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ui_MsgBox.h) | `MsgBox`, `Ui_MsgBox` |


## Configuration and data contracts

| Source artifact |
| --- |
| [config/RCNamedConfigs.xml](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/config/RCNamedConfigs.xml) |
| [config/RCNamedConfigs.xsd](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/config/RCNamedConfigs.xsd) |
| [config/RunControlConfiguration.xml](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/config/RunControlConfiguration.xml) |
| [config/RunControlConfiguration.xsd](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/config/RunControlConfiguration.xsd) |
| [cxx/config/msganalyzer.fcl](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/config/msganalyzer.fcl) |
| [cxx/config/msganalyzer_FarDet.fcl](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/config/msganalyzer_FarDet.fcl) |
| [cxx/config/msganalyzer_mf.fcl](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/config/msganalyzer_mf.fcl) |
| [cxx/config/rules_test.fcl](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/config/rules_test.fcl) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `DAQ_LOG_ROOT` | [cxx/src/ma_action_rcmsg.cpp:27](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_action_rcmsg.cpp#L27) |
| `FHICL_FILE_PATH` | [cxx/src/ma_action_mail.cpp:47](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_action_mail.cpp#L47) |
| `NOVADAQ_PARTITION_NUMBER` | [cxx/src/MsgAnalyzer.cc:31](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/MsgAnalyzer.cc#L31) |
| `SRT_PRIVATE_CONTEXT` | [cxx/src/ma_action_mail.cpp:48](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_action_mail.cpp#L48) |
| `SRT_PUBLIC_CONTEXT` | [cxx/src/ma_action_mail.cpp:49](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_action_mail.cpp#L49) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `..` | [cxx/src/MsgAnalyzerDlg-moc.cpp:9](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/MsgAnalyzerDlg-moc.cpp#L9) |
| `Extensions` | [cxx/include/ma_types.h:12](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_types.h#L12) |
| `QtCore` | [cxx/include/MsgAnalyzerDlg.h:12](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/MsgAnalyzerDlg.h#L12) |
| `QtGui` | [cxx/include/MsgAnalyzerDlg.h:14](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/MsgAnalyzerDlg.h#L14) |
| `boost` | [cxx/include/EHListener.h:9](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/EHListener.h#L9) |
| `cetlib` | [cxx/src/MsgAnalyzerDlg.cpp:6](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/MsgAnalyzerDlg.cpp#L6) |
| `fhiclcpp` | [cxx/include/ma_action.h:10](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_action.h#L10) |
| `messagefacility` | [cxx/include/ma_types.h:13](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_types.h#L13) |
| `sys` | [cxx/include/ma_rule.h:18](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/ma_rule.h#L18) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

```mermaid
flowchart LR
  p0["DAQMessages"]
  p1["ErrorHandler"]
  p2["NovaRunControlClient"]
  p3["NovaTimingUtilities"]
  p4["ResponsiveMessagingSystem"]
  p1 --> p0
  p1 --> p2
  p1 --> p3
  p1 --> p4
```

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [DAQDataFormats](DAQDataFormats.md) | test link | [cxx/test/GNUmakefile:13](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/GNUmakefile#L13) |
| [DAQMessages](DAQMessages.md) | build link | [cxx/src/GNUmakefile:79](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/GNUmakefile#L79) |
| [DAQMessages](DAQMessages.md) | source include | [cxx/include/EHListener.h:7](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/EHListener.h#L7) |
| [DAQMessages](DAQMessages.md) | test include | [cxx/test/EHReceiver.cc:12](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReceiver.cc#L12) |
| [DAQMessages](DAQMessages.md) | test link | [cxx/test/GNUmakefile:13](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/GNUmakefile#L13) |
| [NovaRunControlClient](NovaRunControlClient.md) | source include | [cxx/src/ma_rcclient.cpp:2](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_rcclient.cpp#L2) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | build link | [cxx/src/GNUmakefile:79](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/GNUmakefile#L79) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | source include | [cxx/src/ma_action_rcmsg.cpp:5](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/src/ma_action_rcmsg.cpp#L5) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | test include | [cxx/test/EHReceiver.cc:10](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReceiver.cc#L10) |
| [NovaTimingUtilities](NovaTimingUtilities.md) | test link | [cxx/test/GNUmakefile:13](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/GNUmakefile#L13) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | source include | [cxx/include/EHListener.h:1](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/include/EHListener.h#L1) |
| [ResponsiveMessagingSystem](ResponsiveMessagingSystem.md) | test include | [cxx/test/EHReceiver.cc:5](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReceiver.cc#L5) |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/GNUmakefile#L10) |


Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **43 C/C++ translation units**, **5 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/EHReceiver.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReceiver.cc) |
| [cxx/test/EHReplier.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReplier.cc) |
| [cxx/test/EHReplyReceiver.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHReplyReceiver.cc) |
| [cxx/test/EHSender.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/EHSender.cc) |
| [cxx/test/mftest.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/mftest.cc) |
| [cxx/test/pop_dcm.sh](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/pop_dcm.sh) |
| [cxx/test/pop_main_comp.sh](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/pop_main_comp.sh) |
| [cxx/test/pop_main_error.sh](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/pop_main_error.sh) |
| [cxx/test/pop_main_warning.sh](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/test/pop_main_warning.sh) |
| [cxx/unittest/ma_domain_ops_test.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/unittest/ma_domain_ops_test.cc) |
| [cxx/unittest/ma_domain_test.cc](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/cxx/unittest/ma_domain_test.cc) |


## Existing documentation

| Source |
| --- |
| [doc/RuleEngineDocumentation.txt](https://github.com/NovaDAQ/ErrorHandler/blob/2c97c6860306edd1ea217892d75d389733a39f88/doc/RuleEngineDocumentation.txt) |
