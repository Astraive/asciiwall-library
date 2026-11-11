# Changelog

All notable changes to `Astraive/asciiwall-library` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and future curated catalog/release tags will follow independent library versioning documented in [docs/release-process.md](docs/release-process.md).

## [Unreleased]

### Added

- Established independent repository foundations (`README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CHANGELOG.md`) preserving the root MIT `LICENSE` and `.gitignore`.
- Added `.editorconfig` and `.gitattributes` enforcing UTF-8, LF line endings for source/docs/scripts, and binary attributes for future media/package extensions.
- Added `.github/CODEOWNERS`, `.github/release.yml`, weekly GitHub Actions `.github/dependabot.yml`, default & art PR templates, structured issue forms (`wallpaper-submission`, `bug-report`, `feature-request`, `research-spike`, `qa-evidence`), and least-privileged SHA-pinned workflows (`repository-checks.yml`, `security-analysis.yml`).
- Added opt-in local `.githooks/` (`pre-commit`, `commit-msg`, `install.ps1`, `README.md`) and standalone stdlib validation scripts (`scripts/check-repository.py`, `scripts/check-conventions.py`, `scripts/check-powershell.ps1`) with a fail-closed gate if art/package inputs appear before pinned engine prerequisites.
- Authored independent library documentation under `docs/` (`development-plan.md`, `roadmap.md`, `package-authoring.md`, `quality-requirements.md`, `licensing-and-review.md`, `release-process.md`).

### Not Yet Implemented or Published

- **No curated wallpaper packages (`.asciiwall`), media assets, fonts, static `catalog.json` releases, or `catalog.sig` signatures exist yet.**
- Pinned upstream engine binaries (`package pack`, `package validate`, `bake`) and `schemas/engine-schema-lock.json` remain blocked on `Astraive/asciiwall` implementation milestones.
- Catalog signing key custody and nonproduction key rotation rehearsals (`LREL-003`) are planned and unconfigured.
