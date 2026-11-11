# AsciiWall Community Wallpaper Library (`Astraive/asciiwall-library`)

**Repository status: foundation baseline only.** This repository currently establishes governance, contributor policies, issue and pull request workflows, local read-only validation scripts, and library engineering documentation. **No generated wallpaper packages (`.asciiwall`), published media assets, embedded fonts, static catalogs (`catalog.json`), detached signatures (`catalog.sig`), or release artifacts exist yet.**

`Astraive/asciiwall-library` is the companion community wallpaper recipe and static catalog repository for [AsciiWall](https://github.com/Astraive/asciiwall). It does not fork the Rust conversion engine or ship an independent runtime backend.

## Architecture and Ownership Separation

Per [ADR 0004 - Offline core and static community library](https://github.com/Astraive/asciiwall/blob/main/docs/decisions/0004-offline-core-and-static-library.md) and [The asciiwall-library repository](https://github.com/Astraive/asciiwall/blob/main/docs/library/repository-structure.md):

- **`Astraive/asciiwall` owns** the Rust engine, image/video conversion algorithms, scene runtime, `.asciiwall` packer/validator/importer (`package pack`, `package validate`, `bake`), manifest/scene schemas, and native desktop application.
- **`Astraive/asciiwall-library` owns** community wallpaper recipes (`wallpapers/<slug>/`), per-asset rights and attribution ledgers, digest-pinned asset lockfiles, static collection descriptors, static catalog metadata (`catalog.json` + detached `catalog.sig`), and curation/release tooling.
- **Offline-first, backend-free distribution:** core AsciiWall import, conversion, playback, editing, and local search operate completely offline. Optional online catalog access is off by default and consumes static JSON plus detached signatures over explicit HTTPS origins — never user accounts, database servers, analytics endpoints, or remote runtime APIs.
- **Local-only authoring works independently:** creators can author and import private local `.asciiwall` packages directly in AsciiWall without submitting them to this curated repository.

## Licensing Boundary

- **Repository files (`LICENSE`):** scripts, policies, templates, schemas, and documentation authored in this repository are licensed under the [MIT License](LICENSE).
- **Submitted artwork, media, fonts, and previews:** future wallpaper recipes, source photographs or videos, fonts, audio, and static preview renders carry **their own explicit per-asset licenses and attribution ledgers** ([docs/licensing-and-review.md](docs/licensing-and-review.md)). The repository's MIT license does **not** automatically relicense third-party artwork or bundled media.

## Starter Collection Briefs vs. Actual Assets

The upstream specification defines **36 proposed original recipe briefs** in [Starter wallpaper catalog and recipe briefs](https://github.com/Astraive/asciiwall/blob/main/docs/library/starter-wallpaper-catalog.md):

- **20 v1 procedural scene candidates** (`matrix-rain` through `slow-tide`) expressed with proposed draft-v1 built-in scene nodes
- **8 rights-cleared media candidates** (`mountain-study` through `ink-loop`) requiring authorized source media
- **8 later-capability candidates** (`lorenz-attractor` through `day-night-field`) blocked on future upstream engine generators/signals

Those 36 rows are **design briefs only**, not published wallpapers, downloaded media, or measured performance results. See [docs/roadmap.md](docs/roadmap.md) for the complete disposition matrix and `L0`–`L4` milestones.

## Repository Layout

### Tracked Today (Foundation Baseline)

- `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CHANGELOG.md`, `LICENSE` — policies, licensing boundaries, and governance
- `.editorconfig`, `.gitattributes`, `.gitignore` — cross-platform LF/UTF-8 formatting and defensive ignore rules
- `.github/` — issue forms, default & art PR templates, `CODEOWNERS`, release notes config, weekly Actions Dependabot, and least-privileged SHA-pinned CI workflows
- `.githooks/` — opt-in local `pre-commit` and `commit-msg` hooks plus `.githooks/install.ps1`
- `scripts/` — standalone stdlib validation checkers (`check-repository.py`, `check-conventions.py`, `check-powershell.ps1`)
- `docs/` — independent library planning, authoring, quality, licensing/moderation, and release documentation

### Planned Structure (Blocked Pending Pinned Engine and Reviewed Assets)

Once upstream `Astraive/asciiwall` delivers reviewed schema/packer binaries (`PKG-001`, `CLI-001`, `PKG-010`) and `L0`/`L1` prerequisites (`LIB-002`, `LIB-003`, `LIB-004`, `LLEG-002`, `CAT-001`..`CAT-005`), the repository will host `schemas/engine-schema-lock.json`, `wallpapers/<slug>/`, `collections/`, `tests/`, build/catalog scripts, and static release outputs outside ordinary Git history. New art/package inputs added before those validation gates exist **fail closed** in CI rather than passing unvalidated.

## Local Documentation (`docs/`)

| Document | Purpose |
| --- | --- |
| [docs/development-plan.md](docs/development-plan.md) | Ownership boundaries, `L0`–`L4` workstreams, cross-repo blockers, and external backlog layout |
| [docs/roadmap.md](docs/roadmap.md) | Milestones `L0`–`L4`, gates `LQA-L0`–`LQA-L4`, and the 36 recipe-brief dispositions |
| [docs/package-authoring.md](docs/package-authoring.md) | Recipe layout, build inputs vs. strict manifests, portable paths, and presets |
| [docs/quality-requirements.md](docs/quality-requirements.md) | Current CI checks, fail-closed missing-engine rules, hard budgets, and hardware evidence |
| [docs/licensing-and-review.md](docs/licensing-and-review.md) | Separate rights layers, asset ledgers, human curation, moderation, and takedowns |
| [docs/release-process.md](docs/release-process.md) | Immutable releases, static catalog schema, Ed25519 signature profile, and key custody |

## Upstream Reference Specifications (`Astraive/asciiwall`)

Authoritative design specifications live in the main application repository on `main`:

- **Library specifications:** [repository-structure](https://github.com/Astraive/asciiwall/blob/main/docs/library/repository-structure.md), [starter-wallpaper-catalog](https://github.com/Astraive/asciiwall/blob/main/docs/library/starter-wallpaper-catalog.md), [catalog-and-index-schema](https://github.com/Astraive/asciiwall/blob/main/docs/library/catalog-and-index-schema.md), [licensing-and-attribution](https://github.com/Astraive/asciiwall/blob/main/docs/library/licensing-and-attribution.md), [contribution-and-review](https://github.com/Astraive/asciiwall/blob/main/docs/library/contribution-and-review.md), [release-pipeline-and-distribution](https://github.com/Astraive/asciiwall/blob/main/docs/library/release-pipeline-and-distribution.md)
- **Package format contracts:** [format-specification](https://github.com/Astraive/asciiwall/blob/main/docs/package/format-specification.md), [manifest-schema](https://github.com/Astraive/asciiwall/blob/main/docs/package/manifest-schema.md), [scene-schema](https://github.com/Astraive/asciiwall/blob/main/docs/package/scene-schema.md), [import-and-validation](https://github.com/Astraive/asciiwall/blob/main/docs/package/import-and-validation.md), [export-and-reproducibility](https://github.com/Astraive/asciiwall/blob/main/docs/package/export-and-reproducibility.md), [compatibility-and-migrations](https://github.com/Astraive/asciiwall/blob/main/docs/package/compatibility-and-migrations.md), [examples-and-test-vectors](https://github.com/Astraive/asciiwall/blob/main/docs/package/examples-and-test-vectors.md)
- **Security & contributor workflow:** [threat-model](https://github.com/Astraive/asciiwall/blob/main/docs/security/threat-model.md), [untrusted-media-and-packages](https://github.com/Astraive/asciiwall/blob/main/docs/security/untrusted-media-and-packages.md), [supply-chain-and-updates](https://github.com/Astraive/asciiwall/blob/main/docs/security/supply-chain-and-updates.md), [privacy-and-network-policy](https://github.com/Astraive/asciiwall/blob/main/docs/security/privacy-and-network-policy.md), [plugin-and-shader-policy](https://github.com/Astraive/asciiwall/blob/main/docs/security/plugin-and-shader-policy.md), [contributor-workflow](https://github.com/Astraive/asciiwall/blob/main/docs/delivery/contributor-workflow.md)

## Local Backlog Workspace vs. Fresh-Clone CI

Detailed planning tickets (`78` library items across `L0`–`L4`, including `1` roadmap `LIB-ROADMAP-001`, `7` epics, `65` tasks, and `5` gates `LQA-L0`–`LQA-L4`) live **externally** in a local workspace sibling directory `../.issues/` outside both Git repositories (`0` GitHub issues have been published). That external folder is never committed, pushed, or linked as a GitHub URL, and fresh-clone CI in `asciiwall-library` never depends on `../.issues/` or a sibling `../asciiwall/` checkout.

When both sibling checkouts and the external workspace exist locally on a maintainer machine, read-only cross-repo backlog validation runs from `../asciiwall`:

```sh
python ../asciiwall/scripts/validate-backlog.py --backlog-root ../.issues --source-root ../asciiwall
```

## Current Runnable Verification Commands

Run these standalone checks locally from the `asciiwall-library` root:

```sh
python scripts/check-repository.py
python scripts/check-conventions.py --title "docs(library): document repository foundation [LIB-001]"
pwsh -NoProfile -File scripts/check-powershell.ps1
```

Opt in to local Git hooks (configures repository-local `core.hooksPath` only):

```powershell
pwsh -NoProfile -File .githooks/install.ps1
```
