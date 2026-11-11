# Library Development Plan

**Status:** Pre-implementation foundation (`LIB-001`). This plan defines the engineering structure, cross-repository dependencies, and operational boundaries of `Astraive/asciiwall-library`. **No curated packages, media assets, static catalogs, or engine binaries exist yet.**

## 1. Repository Ownership and Separation

Per [The asciiwall-library repository](https://github.com/Astraive/asciiwall/blob/main/docs/library/repository-structure.md) and [ADR 0004 - Offline core and static community library](https://github.com/Astraive/asciiwall/blob/main/docs/decisions/0004-offline-core-and-static-library.md):

- **`Astraive/asciiwall` owns** the Rust workspace, image/video conversion algorithms, GPU glyph presenter, native desktop hosts, local library index (`LIBAPP`), optional catalog client (`P06`), `.asciiwall` packer/validator/importer (`P02`–`P04`), preview baker (`bake`), and normative JSON schemas (`manifest.json`, `scene.json`, `catalog.json`).
- **`Astraive/asciiwall-library` owns** community wallpaper recipe inputs (`wallpapers/<slug>/`), curated static collections (`collections/`), digest-pinned asset lockfiles (`assets.lock.json`), per-asset rights and provenance ledgers (`attribution.md`, `licenses/`), pinned upstream engine digests (`schemas/engine-schema-lock.json`), catalog build/validation scripts (`P07`), human curation records (`reviews/`), and immutable static catalog releases.
- **No engine fork or backend:** library scripts orchestrate reviewed upstream AsciiWall contracts and immutable artifacts. They never implement a shadow conversion runtime, hosted account server, search backend, database server, or telemetry endpoint.
- **Independent local authoring:** creators can always author and import private `.asciiwall` packages locally with AsciiWall without submitting them to `Astraive/asciiwall-library`.

## 2. Workstreams and Library Epics

The library backlog defines **78 local planning items** under `LIB-ROADMAP-001` (`1` roadmap, `7` epics, `65` tasks, and `5` milestone gates `LQA-L0`–`LQA-L4`):

| Epic ID | Area | Milestone Scope | Core Ownership |
| --- | --- | --- | --- |
| `LIB-EPIC` | `library-foundation` | `L0`, `L1`, `L3` | Repository layout (`LIB-001`), pinned engine/schema verification (`LIB-002`), reproducible P07 package builds (`LIB-003`), digest-pinned asset resolution (`LIB-004`), compatibility matrices & migrations (`LIB-005`) |
| `CAT-EPIC` | `catalog` | `L1` | Closed draft catalog 1.0 schema & fixtures (`CAT-001`), bounded 16 MiB semantic validation (`CAT-002`), receipt-derived `build_catalog` generation (`CAT-003`), offline searchable static collections (`CAT-004`), exact-byte Ed25519 signature vectors (`CAT-005`) |
| `AST-EPIC` | `starter-artwork` | `L1`–`L4` | Reproducible recipe metadata & preset contract (`AST-037`), 20 v1 procedural briefs (`AST-001`–`AST-020`), 8 rights-cleared media briefs (`AST-021`–`AST-028`), upstream readiness matrix (`AST-038`), 8 later-capability briefs (`AST-029`–`AST-036`) |
| `LQA-EPIC` | `library-quality` | `L0`–`L4` | Secretless PR CI isolation (`LQA-001`), preview/aggregate resource measurements (`LQA-002`), duplicate & near-clone curation detection (`LQA-003`), 5-source-kind cross-platform conformance (`LQA-004`), and milestone gates `LQA-L0`–`LQA-L4` |
| `LREL-EPIC` | `library-release` | `L1`, `L3`, `L4` | Immutable package/catalog publishing (`LREL-001`), static HTTPS origins & v1 offline multi-file kits (`LREL-002`), key rotation & recovery drills (`LREL-003`), Library 1.0 candidate BOM (`LREL-004`), optional offline bundle index (`LREL-005`), maintenance cycles (`LREL-006`) |
| `LCOM-EPIC` | `community` | `L0`, `L2`, `L3` | Contributor intake templates & local-authoring flow (`LCOM-001`), human curation & accessibility/permission reviews (`LCOM-002`), maintainer tracking & non-destructive moderation (`LCOM-003`) |
| `LLEG-EPIC` | `licensing` | `L0`, `L1`, `L3`, `L4` | Separate code/metadata/artwork license policy (`LLEG-001`), per-asset rights ledgers without PII exposure (`LLEG-002`), embedded font & native media dependency review (`LLEG-003`), hash-based rights disputes & takedown records (`LLEG-004`) |

## 3. Target Repository Layout vs. Current Baseline

Today (`L0` foundation under `LIB-001` and `LQA-001`), only root policies, `.editorconfig`, `.gitattributes`, `.gitignore`, `.github/` templates/workflows/Dependabot, `.githooks/` opt-in hooks, standalone `scripts/` checkers, and these `docs/` planning guides exist.

Once upstream engine dependencies land and `L0`–`L1` tooling is built, the repository grows toward the target structure specified in [The asciiwall-library repository](https://github.com/Astraive/asciiwall/blob/main/docs/library/repository-structure.md):

```text
asciiwall-library/
  README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md, GOVERNANCE.md, CHANGELOG.md, LICENSE
  docs/                                 # Foundation guides (present today)
  scripts/                              # Foundation checkers today; build/attribution/catalog scripts in L1
  schemas/                              # engine-schema-lock.json & catalog schemas once PKG-001 / LIB-002 ship
  collections/                          # minimal.json, reactive.json, low-power.json (CAT-004, L1)
  wallpapers/<slug>/                    # manifest-source.json, scene.json, presets/, preview.png, fallback.png, attribution.md, assets.lock.json, licenses/ (L2+)
  tests/                                # catalog-fixtures/, license-fixtures/ (L1+)
  reviews/                              # curation records, resource-notes, gates/L0..L4 signoffs (L0–L4)
```

Large built `.asciiwall` archives and heavy source media belong in versioned static release artifacts — **not** ordinary Git history.

## 4. Build-Input Descriptors vs. Strict Published Manifests

- Authoring directories store **`manifest-source.json`** (build-input descriptors), which may omit computed asset hashes and sizes during authoring.
- Published `.asciiwall` archives contain strict **`manifest.json`** generated solely by the pinned upstream packer (`asciiwall package pack`), containing exact recomputed SHA-256 hashes, byte sizes, and closed-world validated fields ([Manifest schema](https://github.com/Astraive/asciiwall/blob/main/docs/package/manifest-schema.md)).
- The complete archive SHA-256 lives **outside** the archive in `ArtifactReceipt` records and `catalog.json`, never inside `manifest.json`.

## 5. Cross-Repository Hard Blockers from `Astraive/asciiwall`

Library repository foundations (`LIB-001`, `LCOM-001`, `LLEG-001`, `LQA-001` policy/CI scaffold) do **not** wait for desktop application completion. However, engine-pin verification, package building, catalog conformance, and recipe releases explicitly depend on **38 hard cross-repository edges** from **19 upstream `asciiwall` tickets**:

| Upstream Blocker (`asciiwall`) | Milestone | Downstream Library Work Blocked |
| --- | --- | --- |
| `PKG-001` (draft v1 manifest & scene schema types) | `M2` | `LIB-002`, `CAT-001`, `AST-037` |
| `CLI-001` (standalone conversion CLI contract) | `M1` | `LIB-003` |
| `PKG-010` (reproducible portable archive packer) | `M6` | `LIB-003` |
| `PKG-012` (cross-platform package conformance / format freeze) | `M6` | `LQA-004` |
| `VID-009` (`ascii-clip` deterministic writer) | `M4` | `AST-027` (`ember-loop`) |
| `VID-012` (deterministic bake jobs) | `M6` | `LQA-002` |
| `VID-013` (supported rendered-video encoding) | `M6` | `AST-028` (`ink-loop`) |
| `SCN-002`..`SCN-006` (v1 procedural scene generators) | `M2` | `AST-001`–`AST-020` |
| `FX-007` (two-input character-frame composite) | `M4` | `AST-016`, `AST-017` |
| `FX-003`..`FX-005` (pointer force, click ripple, window avoid) | `M5` | `AST-011`, `AST-012`, `AST-013` |
| `SCN-008`..`SCN-010` (later fire, particle garden, text/clock) | `M10` | `AST-033`, `AST-030`, `AST-036` |

Until those pinned engine contracts land, `scripts/check-repository.py` enforces a **fail-closed gate**: adding files under `wallpapers/`, `collections/`, `catalog/`, `packages/`, or `*.asciiwall` / `*.ascii-clip` archives fails CI with the exact missing prerequisites rather than reporting a fake green build.

## 6. External Planning Workspace (`.issues`)

All `356` local planning pairs (`278` `asciiwall` + `78` `asciiwall-library`, `0` remote GitHub issues published) and generated audit reports reside **externally** in `../.issues/` outside both Git repositories. That directory is never committed, never pushed, and never referenced as a GitHub URL.

When both sibling repositories (`../asciiwall` and `asciiwall-library`) and `../.issues/` are present in a maintainer's local workspace, read-only cross-repo backlog validation and report regeneration use:

```sh
python ../asciiwall/scripts/validate-backlog.py --backlog-root ../.issues --source-root ../asciiwall
python ../asciiwall/scripts/validate-backlog.py --backlog-root ../.issues --source-root ../asciiwall --write-reports
```

Fresh clones and GitHub Actions CI run standalone checks (`python scripts/check-repository.py`, `pwsh -NoProfile -File scripts/check-powershell.ps1`) with zero external `.issues` or sibling-checkout dependency.
