# XmlRpc

XML-RPC client/server, HTTP/socket dispatch, value serialization, and sample applications.

## Identity and scope

Repository: [NovaDAQ/XmlRpc](https://github.com/NovaDAQ/XmlRpc) · Reviewed commit: `dd0f907f8942b72d88467ee45ded5308dd6c71f7` · Domain: **Messaging**.

Tracked files: **58**. Production deployment and owner are **unconfirmed**.

## Operation

Consumers must validate method arguments and define their authentication/network boundary. Test partial HTTP messages, disconnects, oversized bodies, and fault responses using a local server before online integration.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).

| Build definition |
| --- |
| [GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/GNUmakefile) |
| [cxx/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/GNUmakefile) |
| [cxx/src/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/GNUmakefile) |
| [cxx/test/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/GNUmakefile) |
| [cxx/unittest/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/unittest/GNUmakefile) |
| [java/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/java/GNUmakefile) |
| [java/src/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/java/src/GNUmakefile) |
| [java/test/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/java/test/GNUmakefile) |
| [java/unittest/GNUmakefile](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/java/unittest/GNUmakefile) |


## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.

## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [cxx/include/XmlRpc.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpc.h) | `XmlRpcErrorHandler`, `XmlRpcLogHandler` |
| [cxx/include/XmlRpcClient.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcClient.h) | `ClientConnectionState`, `XmlRpcClient`, `XmlRpcValue` |
| [cxx/include/XmlRpcDispatch.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcDispatch.h) | `EventType`, `MonitoredSource`, `XmlRpcDispatch`, `XmlRpcSource` |
| [cxx/include/XmlRpcException.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcException.h) | `XmlRpcException` |
| [cxx/include/XmlRpcServer.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcServer.h) | `XmlRpcServer`, `XmlRpcServerConnection`, `XmlRpcServerMethod`, `XmlRpcValue` |
| [cxx/include/XmlRpcServerConnection.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcServerConnection.h) | `ServerConnectionState`, `XmlRpcServer`, `XmlRpcServerConnection`, `XmlRpcServerMethod` |
| [cxx/include/XmlRpcServerMethod.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcServerMethod.h) | `XmlRpcServer`, `XmlRpcServerMethod`, `XmlRpcValue` |
| [cxx/include/XmlRpcSocket.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcSocket.h) | `XmlRpcSocket` |
| [cxx/include/XmlRpcSource.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcSource.h) | `XmlRpcSource` |
| [cxx/include/XmlRpcUtil.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcUtil.h) | `XmlRpcUtil` |
| [cxx/include/XmlRpcValue.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/XmlRpcValue.h) | `Type`, `XmlRpcValue`, `tm` |
| [cxx/include/base64.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/include/base64.h) | `base64`, `crlf`, `crlfsp`, `noline`, `three2four` |
| [cxx/src/XmlRpc.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpc.h) | `XmlRpcErrorHandler`, `XmlRpcLogHandler` |
| [cxx/src/XmlRpcClient.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcClient.h) | `ClientConnectionState`, `XmlRpcClient`, `XmlRpcValue` |
| [cxx/src/XmlRpcDispatch.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcDispatch.h) | `EventType`, `MonitoredSource`, `XmlRpcDispatch`, `XmlRpcSource` |
| [cxx/src/XmlRpcException.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcException.h) | `XmlRpcException` |
| [cxx/src/XmlRpcServer.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcServer.h) | `XmlRpcServer`, `XmlRpcServerConnection`, `XmlRpcServerMethod`, `XmlRpcValue` |
| [cxx/src/XmlRpcServerConnection.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcServerConnection.h) | `ServerConnectionState`, `XmlRpcServer`, `XmlRpcServerConnection`, `XmlRpcServerMethod` |
| [cxx/src/XmlRpcServerMethod.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcServerMethod.h) | `XmlRpcServer`, `XmlRpcServerMethod`, `XmlRpcValue` |
| [cxx/src/XmlRpcSocket.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcSocket.h) | `XmlRpcSocket` |
| [cxx/src/XmlRpcSource.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcSource.h) | `XmlRpcSource` |
| [cxx/src/XmlRpcUtil.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcUtil.h) | `XmlRpcUtil` |
| [cxx/src/XmlRpcValue.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcValue.h) | `Type`, `XmlRpcValue`, `tm` |
| [cxx/src/base64.h](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/base64.h) | `base64`, `crlf`, `crlfsp`, `noline`, `three2four` |


## Configuration and data contracts

| Source artifact |
| --- |
| [cxx/test/arrayOfStructsTest.xml](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/arrayOfStructsTest.xml) |
| [cxx/test/countTheEntities.xml](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/countTheEntities.xml) |
| [cxx/test/easyStructTest.xml](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/easyStructTest.xml) |
| [cxx/test/echo.xml](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/echo.xml) |
| [cxx/test/echoStructTest.xml](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/echoStructTest.xml) |


## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `netinet` | [cxx/src/XmlRpcSocket.cpp:21](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcSocket.cpp#L21) |
| `sys` | [cxx/src/XmlRpcDispatch.cpp:7](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/src/XmlRpcDispatch.cpp#L7) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

| Dependency | Relationship | Evidence |
| --- | --- | --- |
| [SRT_ONLINE](SRT_ONLINE.md) | build tool | [GNUmakefile:10](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/GNUmakefile#L10) |


Direct consumers: [NovaSNEWSInterface](NovaSNEWSInterface.md), [NovaSpillServer](NovaSpillServer.md), [SRT_ONLINE](SRT_ONLINE.md).

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **17 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

| Source |
| --- |
| [cxx/test/FileClient.cpp](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/FileClient.cpp) |
| [cxx/test/HelloClient.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/HelloClient.cc) |
| [cxx/test/HelloServer.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/HelloServer.cc) |
| [cxx/test/TestBase64Client.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/TestBase64Client.cc) |
| [cxx/test/TestBase64Server.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/TestBase64Server.cc) |
| [cxx/test/TestValues.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/TestValues.cc) |
| [cxx/test/TestXml.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/TestXml.cc) |
| [cxx/test/Validator.cc](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/test/Validator.cc) |


## Existing documentation

| Source |
| --- |
| [cxx/README.html](https://github.com/NovaDAQ/XmlRpc/blob/dd0f907f8942b72d88467ee45ded5308dd6c71f7/cxx/README.html) |
