# Governance

## Governance Model

`Astraive/asciiwall-library` operates under a **single-maintainer bootstrap governance model** led by organization owner and repository administrator **`@NeerajCodz`** (`https://github.com/NeerajCodz`) under the `Astraive` organization.

This repository is intentionally independent from [`Astraive/asciiwall`](https://github.com/Astraive/asciiwall) so artwork curation, attribution ledgers, and static catalog releases evolve cleanly on their own cadence without forking the AsciiWall engine or runtime.

## Roles and Accountability

Even during single-maintainer bootstrap, responsibilities are separated logically across four accountability functions mapped to library milestones (`L0`–`L4`):

1. **Library Foundation & Tooling Maintainer:** owns repository layout, CI workflow trust boundaries, `.githooks/` and `scripts/` checkers, and reviewed updates to pinned upstream engine/schema digests (`schemas/engine-schema-lock.json`).
2. **Rights & Provenance Reviewer:** audits per-asset licenses, attribution texts, font redistribution permissions, native dependency notices, and private-proof handling (`LLEG-001`–`LLEG-004`).
3. **Human Curator & QA Evidence Reviewer:** reviews visual legibility, restrained motion, portrait/wide & low-power presets, unavailable-feed fallbacks, and milestone gate sign-offs (`LQA-L0`–`LQA-L4`, `LCOM-001`–`LCOM-003`).
4. **Release & Catalog Key Custodian:** oversees protected release commits, immutable package/catalog publication, and pre-launch key backup/rotation/recovery drills (`LREL-001`–`LREL-006`). Signing key custody is **not configured** yet and no production keys exist in this foundation state.

## Cross-Repository Contract Boundaries

- **Engine authority:** `Astraive/asciiwall` owns `.asciiwall` format specs, `manifest.json` / `scene.json` schemas, `package pack` / `package validate` / `bake` commands, and the optional desktop catalog client.
- **Engine pin upgrades:** updating the library's pinned engine release or schema digest is an explicit reviewed maintenance change (`LIB-002`, `LIB-005`). Contributor PRs cannot override the pinned engine binary or point validation at an unreviewed branch.
- **No shadow runtime:** library scripts orchestrate pinned upstream tools and static metadata; they never implement an independent conversion engine or hosted server backend.

## Branch Protection and Review Policy

- **Protected `main` branch:** changes merge via pull requests using squash merges, linear history, resolved conversations, and required passing CI checks (`Repository quality` and `Python security analysis`).
- **Bootstrap approval count:** because GitHub forbids a sole maintainer from approving their own pull request, required approvals start at `0` during bootstrap while retaining full `.github/CODEOWNERS` ownership tracking and mandatory PR checklists. Approval count will increase (`>= 1`) once additional trusted maintainers hold write access.
- **Maintainer triage of dependency PRs:** Dependabot updates for GitHub Actions cannot automatically include `[TICKET-ID]`, so maintainers verify and rename dependency PR titles before squash-merging.
- **High-scrutiny changes:** changes to `.github/workflows/`, `scripts/`, `schemas/engine-schema-lock.json`, licensing policy, or signing/release configuration require explicit trust-boundary verification and fail-closed checks.

## Licensing and Non-Destructive Moderation

- **MIT repository + per-asset rights:** repository tooling, docs, templates, and schemas remain MIT-licensed (`LICENSE`), while every future wallpaper asset retains its explicit declared license (`CC0-1.0`, `CC BY 4.0`, etc.) and provenance ledger.
- **Immutable history & user sovereignty:** deprecations, security advisories, and rights takedowns update future catalog sequences and advisory records cleanly ([docs/licensing-and-review.md](docs/licensing-and-review.md)). Moderators never silently mutate prior published bytes or remotely delete local files installed on user machines.
