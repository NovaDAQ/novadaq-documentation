# DCMBootLoader

RedBoot/eCos build tree and NOvA PowerPC board support for DCM and TDU bootloaders.

## Identity and scope

Repository: [NovaDAQ/DCMBootLoader](https://github.com/NovaDAQ/DCMBootLoader) · Reviewed commit: `130318d4e2e238027846b2b69851d7d207794fb4` · Domain: **Hardware**.

Tracked files: **7577**. Production deployment and owner are **unconfirmed**.

## Operation

The README specifies historical cross-toolchain and board-specific CONFIG scripts. Match board revision and flash type before building. Preserve a known bootable image and recovery path; compilation was reviewed, but no firmware was flashed in this review.

For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).

## Build and integration

No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.

## Entry points

These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.

| Source |
| --- |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/Main_FOR_TDU.c](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/Main_FOR_TDU.c) |


## Interfaces

Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.

| Header | Declared types |
| --- | --- |
| [ecos/packages/hal/powerpc/novadcm/current/include/dcm_config.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/dcm_config.h) | `dcm_config_info` |
| [ecos/packages/hal/powerpc/novadcm/current/include/dcm_lcd_gui_if.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/dcm_lcd_gui_if.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/hal_diag.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/hal_diag.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/novadcm_8347.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/novadcm_8347.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_ram.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_ram.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_rom.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_rom.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_romram.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/pkgconf/mlt_powerpc_novadcm_romram.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_cache.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_cache.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_intr.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_intr.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_io.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_io.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_lcd.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_lcd.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_regs.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_regs.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/include/plf_stub.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/include/plf_stub.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiConst.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiConst.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiDisplay.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiDisplay.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiFont.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiFont.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiLib.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiLib.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiStruct.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiStruct.h) | Functions, constants, or templates |
| [ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiVar.h](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/novaGUI/GuiVar.h) | Functions, constants, or templates |


## Configuration and data contracts

No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.

## Environment and external dependencies

Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.

No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.

Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):

| Include root | Evidence |
| --- | --- |
| `cyg` | [ecos/packages/devs/flash/powerpc/novadcm/current/src/novadcm_amd_flash.c:56](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/devs/flash/powerpc/novadcm/current/src/novadcm_amd_flash.c#L56) |
| `net` | [ecos/packages/hal/powerpc/novadcm/current/src/plf_redboot_linux_exec.c:72](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/hal/powerpc/novadcm/current/src/plf_redboot_linux_exec.c#L72) |
| `pkgconf` | [ecos/packages/devs/flash/powerpc/novadcm/current/src/novadcm_amd_flash.c:54](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/ecos/packages/devs/flash/powerpc/novadcm/current/src/novadcm_amd_flash.c#L54) |


## Package dependencies

Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.

No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.

Direct consumers: None resolved in this snapshot.

Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).

## Validation and review

Static analysis attempted **20 C/C++ translation units**, **0 shell scripts**, and parsed **0 Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed.

Large vendor/generated/firmware trees received a bounded integration review. The [methodology](../review/methodology.md) records exclusions. No complete third-party audit or hardware validation is claimed.

No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.

Existing test/example sources (not executed against production):

No test/example source identified in the scoped inventory.

## Existing documentation

| Source |
| --- |
| [README](https://github.com/NovaDAQ/DCMBootLoader/blob/130318d4e2e238027846b2b69851d7d207794fb4/README) |
