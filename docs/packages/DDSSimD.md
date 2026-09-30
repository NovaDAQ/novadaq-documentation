# DDSSimD

Simulation DDS implementation, demos, and generated reference documentation.

## Identity and scope

Repository: [NovaDAQ/DDSSimD](https://github.com/NovaDAQ/DDSSimD) · Reviewed commit: `43effa759492e16859cc3ae0be98d6d113af33e6` · Domain: **Messaging**.

Tracked files: **849**. Production deployment and owner are **unconfirmed**.

This checkout had pre-existing local changes. Remote source links identify the committed revision; local changes were preserved. See the snapshot ledger for affected paths.

## Operation

Use its own CMake build and documented DDS compatibility surface. Treat it as an alternative messaging implementation requiring protocol/behavior checks against the intended peers. Review focused on implementation/build surfaces; generated HTML was not audited page by page.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.

| Build definition |
| --- |
| [CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/CMakeLists.txt) |
| [cmake/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/cmake/CMakeLists.txt) |
| [demo/ddj-series/01/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/CMakeLists.txt) |
| [demo/ddj-series/02/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/CMakeLists.txt) |
| [demo/ddj-series/03/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/CMakeLists.txt) |
| [demo/hello/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/CMakeLists.txt) |
| [demo/ishapes/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/CMakeLists.txt) |
| [demo/ishapes/ishapes.pro](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ishapes.pro) |
| [demo/ishapes/readerqos.pro](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/readerqos.pro) |
| [demo/latency/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/CMakeLists.txt) |
| [demo/ping/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/CMakeLists.txt) |
| [demo/tshapes/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/CMakeLists.txt) |
| [demo/tweet/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/CMakeLists.txt) |
| [demo/tweet/Makefile](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/Makefile) |
| [src/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/CMakeLists.txt) |
| [src/dds/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/CMakeLists.txt) |
| [ups/CMakeLists.txt](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/ups/CMakeLists.txt) |
| [ups/product_deps](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/ups/product_deps) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [src/boost/process.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process.hpp) | Functions, constants, or templates |
| [src/boost/process/child.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/child.hpp) | `child` |
| [src/boost/process/config.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/config.hpp) | Functions, constants, or templates |
| [src/boost/process/context.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/context.hpp) | `basic_context`, `basic_pipeline_entry`, `basic_work_directory_context`, `environment_context` |
| [src/boost/process/detail/file_handle.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/file_handle.hpp) | `file_handle` |
| [src/boost/process/detail/pipe.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/pipe.hpp) | `pipe` |
| [src/boost/process/detail/posix_ops.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/posix_ops.hpp) | `posix_setup` |
| [src/boost/process/detail/stream_info.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/stream_info.hpp) | `stream_info`, `type` |
| [src/boost/process/detail/systembuf.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/systembuf.hpp) | `postream`, `systembuf` |
| [src/boost/process/detail/win32_ops.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/detail/win32_ops.hpp) | `win32_setup` |
| [src/boost/process/environment.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/environment.hpp) | Functions, constants, or templates |
| [src/boost/process/operations.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/operations.hpp) | Functions, constants, or templates |
| [src/boost/process/pistream.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/pistream.hpp) | `pistream` |
| [src/boost/process/posix_child.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/posix_child.hpp) | `posix_child` |
| [src/boost/process/posix_context.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/posix_context.hpp) | `posix_basic_context` |
| [src/boost/process/posix_operations.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/posix_operations.hpp) | Functions, constants, or templates |
| [src/boost/process/posix_status.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/posix_status.hpp) | `posix_status` |
| [src/boost/process/postream.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/postream.hpp) | `postream` |
| [src/boost/process/process.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/process.hpp) | `process` |
| [src/boost/process/self.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/self.hpp) | `self` |
| [src/boost/process/status.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/status.hpp) | `child`, `status` |
| [src/boost/process/stream_behavior.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/stream_behavior.hpp) | `stream_behavior`, `stream_info`, `type` |
| [src/boost/process/win32_child.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/win32_child.hpp) | `win32_child` |
| [src/boost/process/win32_context.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/win32_context.hpp) | `win32_basic_context` |
| [src/boost/process/win32_operations.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/win32_operations.hpp) | Functions, constants, or templates |
| [src/dds/assertion.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/assertion.hpp) | `SIMD_API` |
| [src/dds/assertion_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/assertion_impl.hpp) | `SIMD_API` |
| [src/dds/condition.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/condition.hpp) | `SIMD_API`, `TGuardCondition`, `TReadCondition`, `TStatusCondition` |
| [src/dds/config.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/config.hpp) | Functions, constants, or templates |
| [src/dds/content_filtered_topic.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/content_filtered_topic.hpp) | `ContentFilteredTopic`, `ContentFilteredTopicImpl`, `dds` |
| [src/dds/dds.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/dds.hpp) | Functions, constants, or templates |
| [src/dds/domain.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/domain.hpp) | `SIMD_API` |
| [src/dds/exception.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/exception.hpp) | `SIMD_API` |
| [src/dds/instance_reader.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/instance_reader.hpp) | `DataInstanceReader`, `dds` |
| [src/dds/instance_writer.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/instance_writer.hpp) | `DataInstanceWriter` |
| [src/dds/memory.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/memory.hpp) | `GCondDeleter`, `RCondDeleter`, `SCondDeleter`, `SIMD_API` |
| [src/dds/os-linux.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/os-linux.hpp) | Functions, constants, or templates |
| [src/dds/os-win32.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/os-win32.hpp) | Functions, constants, or templates |
| [src/dds/osmacros.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/osmacros.hpp) | Functions, constants, or templates |
| [src/dds/peer/condition_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/condition_impl.hpp) | `SIMD_API`, `TGuardConditionImpl`, `TReadConditionImpl`, `TStatusConditionImpl` |
| [src/dds/peer/content_filtered_topic_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/content_filtered_topic_impl.hpp) | `ContentFilteredTopicImpl`, `dds` |
| [src/dds/peer/instance_writer_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/instance_writer_impl.hpp) | `DataInstanceWriterImpl`, `InstanceStatus_` |
| [src/dds/peer/reader_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/reader_impl.hpp) | `DataReaderImpl` |
| [src/dds/peer/runtime_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/runtime_impl.hpp) | `SIMD_API` |
| [src/dds/peer/topic_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/topic_impl.hpp) | `SIMD_API`, `TopicImpl`, `dds` |
| [src/dds/peer/writer_impl.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/peer/writer_impl.hpp) | `DataWriterImpl`, `dds` |
| [src/dds/publisher.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/publisher.hpp) | `SIMD_API` |
| [src/dds/qos.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/qos.hpp) | `BasePubSubQos`, `BaseTopicQos`, `SIMD_API` |
| [src/dds/reader.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/reader.hpp) | `DataInstanceReader`, `DataReader`, `dds` |
| [src/dds/runtime.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/runtime.hpp) | `Runtime`, `RuntimeImpl`, `SIMD_API` |
| [src/dds/signals.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/signals.hpp) | `SIGNAL` |
| [src/dds/subscriber.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/subscriber.hpp) | `SIMD_API` |
| [src/dds/topic.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/topic.hpp) | `Topic`, `TopicImpl`, `dds` |
| [src/dds/topic_description.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/topic_description.hpp) | `SIMD_API` |
| [src/dds/traits.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/traits.hpp) | `handle_body_ptr`, `handle_body_ref`, `handle_body_type`, `topic_data_reader`, `topic_data_seq`, `topic_data_writer`, `topic_type_support` |
| [src/dds/types.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/types.hpp) | Functions, constants, or templates |
| [src/dds/waitset.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/waitset.hpp) | `SIMD_API`, `WaitSet` |
| [src/dds/writer.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/dds/writer.hpp) | `DataInstanceWriter`, `DataWriter`, `dds` |


## Configuration and data contracts

| Source artifact |
| --- |
| [demo/ddj-series/01/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/TempControl.idl) |
| [demo/ddj-series/02/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/TempControl.idl) |
| [demo/ddj-series/03/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/TempControl.idl) |
| [demo/hello/hello.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/hello.idl) |
| [demo/ishapes/ishape.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ishape.idl) |
| [demo/latency/latency.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/latency.idl) |
| [demo/ping/ping.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/ping.idl) |
| [demo/tshapes/ishape.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/ishape.idl) |
| [demo/tweet/tweet.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/tweet.idl) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

| Variable | Evidence |
| --- | --- |
| `PATH` | [src/boost/process/operations.hpp:84](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/src/boost/process/operations.hpp#L84) |


Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `QtGui` | [demo/ishapes/Circle.cpp:8](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Circle.cpp#L8) |
| `boost` | [demo/ddj-series/01/tspub.cpp:6](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/tspub.cpp#L6) |
| `dds` | [demo/ddj-series/01/tspub.cpp:8](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/tspub.cpp#L8) |
| `gen` | [demo/ddj-series/01/tspub.cpp:10](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/tspub.cpp#L10) |
| `sys` | [demo/latency/latency-pub.cpp:3](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/latency-pub.cpp#L3) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: [SRT_ONLINE](SRT_ONLINE.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **15 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

Large vendor/generated/firmware trees received a bounded integration review. The [methodology](../review/methodology.md) records exclusions. No complete third-party audit or hardware validation is claimed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [demo/ddj-series/01/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/TempControl.idl) |
| [demo/ddj-series/01/tspub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/tspub.cpp) |
| [demo/ddj-series/01/tssub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/tssub.cpp) |
| [demo/ddj-series/01/util.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/util.cpp) |
| [demo/ddj-series/01/util.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/util.hpp) |
| [demo/ddj-series/02/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/TempControl.idl) |
| [demo/ddj-series/02/tspub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/tspub.cpp) |
| [demo/ddj-series/02/tssub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/tssub.cpp) |
| [demo/ddj-series/02/util.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/util.cpp) |
| [demo/ddj-series/02/util.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/util.hpp) |
| [demo/ddj-series/03/TempControl.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/TempControl.idl) |
| [demo/ddj-series/03/tspub-ia.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/tspub-ia.cpp) |
| [demo/ddj-series/03/tspub-log.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/tspub-log.cpp) |
| [demo/ddj-series/03/tspub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/tspub.cpp) |
| [demo/ddj-series/03/tssub-async.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/tssub-async.cpp) |
| [demo/ddj-series/03/tssub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/tssub.cpp) |
| [demo/ddj-series/03/util.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/util.cpp) |
| [demo/ddj-series/03/util.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/03/util.hpp) |
| [demo/hello/hello-pub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/hello-pub.cpp) |
| [demo/hello/hello-sub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/hello-sub.cpp) |
| [demo/hello/hello-traits.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/hello-traits.hpp) |
| [demo/hello/hello.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/hello/hello.idl) |
| [demo/ishapes/BouncingShapeDynamics.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/BouncingShapeDynamics.cpp) |
| [demo/ishapes/BouncingShapeDynamics.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/BouncingShapeDynamics.hpp) |
| [demo/ishapes/Circle.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Circle.cpp) |
| [demo/ishapes/Circle.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Circle.hpp) |
| [demo/ishapes/DDSShapeDynamics.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/DDSShapeDynamics.cpp) |
| [demo/ishapes/DDSShapeDynamics.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/DDSShapeDynamics.hpp) |
| [demo/ishapes/FilterDialog.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/FilterDialog.cpp) |
| [demo/ishapes/FilterDialog.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/FilterDialog.hpp) |
| [demo/ishapes/ReaderQosDialog.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ReaderQosDialog.cpp) |
| [demo/ishapes/ReaderQosDialog.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ReaderQosDialog.hpp) |
| [demo/ishapes/Shape.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Shape.cpp) |
| [demo/ishapes/Shape.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Shape.hpp) |
| [demo/ishapes/ShapeDynamics.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapeDynamics.cpp) |
| [demo/ishapes/ShapeDynamics.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapeDynamics.hpp) |
| [demo/ishapes/ShapesDialog.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapesDialog.cpp) |
| [demo/ishapes/ShapesDialog.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapesDialog.hpp) |
| [demo/ishapes/ShapesWidget.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapesWidget.cpp) |
| [demo/ishapes/ShapesWidget.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ShapesWidget.hpp) |
| [demo/ishapes/Square.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Square.cpp) |
| [demo/ishapes/Square.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Square.hpp) |
| [demo/ishapes/Triangle.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Triangle.cpp) |
| [demo/ishapes/Triangle.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/Triangle.hpp) |
| [demo/ishapes/WriterQosDialog.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/WriterQosDialog.cpp) |
| [demo/ishapes/WriterQosDialog.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/WriterQosDialog.hpp) |
| [demo/ishapes/ishape.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/ishape.idl) |
| [demo/ishapes/main.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/main.cpp) |
| [demo/ishapes/moc_ShapesDialog.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/moc_ShapesDialog.cpp) |
| [demo/ishapes/moc_ShapesWidget.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/moc_ShapesWidget.cpp) |
| [demo/ishapes/topic-traits.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/topic-traits.hpp) |
| [demo/latency/latency-pub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/latency-pub.cpp) |
| [demo/latency/latency-sub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/latency-sub.cpp) |
| [demo/latency/latency.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/latency/latency.idl) |
| [demo/ping/ping-asub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/ping-asub.cpp) |
| [demo/ping/ping-pub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/ping-pub.cpp) |
| [demo/ping/ping-sub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/ping-sub.cpp) |
| [demo/ping/ping.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/ping.idl) |
| [demo/tshapes/ishape.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/ishape.idl) |
| [demo/tshapes/tspub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/tspub.cpp) |
| [demo/tshapes/tssub-async.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/tssub-async.cpp) |
| [demo/tshapes/tssub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/tssub.cpp) |
| [demo/tshapes/util.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/util.cpp) |
| [demo/tshapes/util.hpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tshapes/util.hpp) |
| [demo/tweet/tweet-pub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/tweet-pub.cpp) |
| [demo/tweet/tweet-sub.cpp](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/tweet-sub.cpp) |
| [demo/tweet/tweet.idl](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/tweet/tweet.idl) |


## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/README) |
| [README.WINDOWS](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/README.WINDOWS) |
| [demo/ddj-series/01/README](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/01/README) |
| [demo/ddj-series/02/README](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ddj-series/02/README) |
| [demo/ishapes/README](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ishapes/README) |
| [demo/ping/README](https://github.com/NovaDAQ/DDSSimD/blob/43effa759492e16859cc3ae0be98d6d113af33e6/demo/ping/README) |
