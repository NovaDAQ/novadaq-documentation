# Build and release

## Supported build families in this snapshot

| Family | Evidence | Required context |
| --- | --- | --- |
| SRT / SoftRelTools | Package `GNUmakefile` files; SRT_ONLINE/SoftRelTools | Public/private release contexts, architecture, compiler, external products and online flags |
| cetbuildtools / UPS CMake fragments | Package `CMakeLists.txt`; ups/product_deps | Complete parent project, supplied cet macros, generated DDS/XSD code and imported libraries |
| Independent CMake | DDSSimD | Its own project configuration and declared dependencies |
| Qt project/Makefile | Small standalone GUIs and viewers | Matching Qt/qmake and local library paths |
| Kernel / bootloader | dcm_kernel_module, tdu_kernel_module, linux_kernel_dcmtdu, DCMBootLoader | Exact target kernel/configuration, PowerPC cross-toolchain, board and firmware ABI |
| Scripts / report sources | Operational packages, Python tools, FarDetectorPowerOn | Supported interpreter, external commands, site config; TeX toolchain for the power checklist |

The workspace root is not a monorepository or a build root. The absence of a common top-level `CMakeLists.txt` is expected for this split repository layout. A package CMake file containing `add_subdirectory` or `cet_make_library` does not by itself define a standalone project.

## Reconstruct a reproducible software build

1. Choose the approved release manifest from `setup`, recording its exact Git revision and selected package revisions. Manifests include historical CVS tags and aliases; do not silently map every tag to Git `main`.
2. Establish the matching SRT/UPS product environment and compiler/architecture/qualifier. `ups/product_deps` in this snapshot declares parent `novadaq v18_00_00`, default qualifier `e19`, and dependencies including messagefacility, xerces_c, cstxsd, libwda, PostgreSQL, and cetbuildtools. These are source declarations, not validated current installation recommendations.
3. Assemble the parent release layout, headers, generated DDS/XSD sources, and external dependencies expected by the build definitions. Resolve `rms` to the intended provider and distinguish `SoftRelTools` paths from repository names.
4. Build in a separate output/staging tree, capture configure/build logs, and stop on every failure. The [ups review finding](../packages/ups.md) documents why an existing `lib` directory is not sufficient evidence of build success.
5. Run available package tests and meaningful integration cases: raw file write/read round-trip, message exchange, repeated connect/disconnect, process lifecycle, and simulated acquisition. The catalog distinguishes test sources from tests actually run during this review.
6. Stage artifacts with a manifest containing package commits, external product versions, compiler options, format/schema revisions, checksums, and validation evidence. Promote only the tested artifact set.

## Hardware builds

Match bootloader, kernel/device tree, root filesystem, firmware image, and out-of-tree module as one compatibility set. The DCMBootLoader README documents historical eCos build limitations and a known PowerPC compiler requirement. `dcm_linux_system` contains reconstruction instructions and source archives. Rebuilding these trees on the review host was not attempted because a matching target toolchain and hardware test setup were not established.

Compilation does not verify register semantics, interrupts, DMA coherency, timing, or flash compatibility. Use a test board with a known recovery path and record readback/version checks before considering deployment.

## Rollback and release verification

Keep the previous coherent artifact/configuration set and its launch environment. Stop/drain before changing data-path libraries, schemas, drivers, or firmware. After rollback, verify resource reservations, participant state, timing, file output, and transfer state rather than checking only process presence. Do not mix a previous binary with new generated schemas or an incompatible database migration.

The documentation package has an independent Python/MkDocs build described in [maintaining this suite](../contributing.md); it does not need the DAQ toolchain.
