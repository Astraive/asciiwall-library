# Contributing to AsciiWall Library

Thank you for contributing to `Astraive/asciiwall-library`. Before proposing changes, read [README.md](README.md), [docs/package-authoring.md](docs/package-authoring.md), [docs/quality-requirements.md](docs/quality-requirements.md), and [docs/licensing-and-review.md](docs/licensing-and-review.md).

**Current status:** This repository is in its **foundation phase** (`LIB-001`). Pinned AsciiWall engine binaries (`package pack`, `package validate`, `bake`) and reviewed recipe/catalog build tooling (`LIB-002`, `LIB-003`, `CAT-001`–`CAT-005`) are not shipped yet, so curated wallpaper submissions cannot pass automated packaging gates until those prerequisites exist.

## What Belongs Here vs. `Astraive/asciiwall`

- **Submit here (`Astraive/asciiwall-library`):** repository policies, authoring/quality/release documentation, static catalog/collection schemas, validation/build scripts, and (once enabled) declarative wallpaper recipes, static previews, and attribution ledgers.
- **Submit to [`Astraive/asciiwall`](https://github.com/Astraive/asciiwall):** Rust engine crates, conversion algorithms, scene node implementations, `.asciiwall` schema definitions, CLI commands, GPU renderers, desktop hosts, and app library UI.
- **Local-only authoring:** You do not need to submit a pull request here to create and use personal `.asciiwall` packages locally in AsciiWall.

## Wallpaper Contribution Rules (Once Curated Intake Opens)

Every future curated wallpaper contribution under `wallpapers/<slug>/` must satisfy:

1. **Lowercase kebab-case naming:** directory slug and all documentation filenames must be lowercase kebab-case (`a-z`, `0-9`, `-`).
2. **Build-input vs. published manifest separation:** contributor directories use `manifest-source.json` (plus `scene.json` for procedural scenes, `assets.lock.json`, `attribution.md`, `licenses/`, `preview.png`, and `fallback.png`). Only the pinned upstream packer emits strict published `manifest.json` with computed final asset hashes and byte sizes.
3. **Declarative data only:** never submit executable build scripts, shell commands, plugins, arbitrary shaders, WebAssembly, remote code loaders, or dependency-install steps as wallpaper data.
4. **Portable assets and explicit fonts:** never reference creator-local filesystem paths or assume undeclared system fonts. Embedded fonts require explicit redistribution permission and full license text in `licenses/`; otherwise use approved built-in fonts.
5. **Digest-pinned origins and rights ledgers:** fetched inputs require `assets.lock.json` with approved HTTPS origins, exact SHA-256 digests, byte ceilings, and license evidence references (never mutable `"latest"` URLs, "found on Google" citations, or unconsented movie/game clips).
6. **Offline and unavailable-feed graceful behavior:** optional capabilities (`pointer-position`, `pointer-buttons`, `window-rectangles`, `window-state`, `local-clock`) must degrade cleanly when denied or offline. Include low-power and reduced-motion variants and avoid flashing defaults.

## Commit Messages, PR Titles, and Identity Rules

- **Author identity:** Contributors retain their own Git `user.name` and `user.email`. No script or hook in this repository forces a global Git identity or automatic DCO sign-off.
- **Required header format:** Commit messages and pull request titles must follow Conventional Commits with a trailing bracketed ticket ID:

  ```text
  type(scope): subject [TICKET-ID]
  ```

  - Allowed `type`: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
  - Required `scope`: lowercase kebab-case (for example `library`, `catalog`, `wallpapers`, `ci`, `docs`)
  - Required `TICKET-ID`: uppercase prefix + hyphenated suffix (for example `[LIB-001]`, `[AST-001]`, `[CAT-001]`, `[LQA-001]`, `[LREL-001]`, `[LIB-ROADMAP-001]`)
- **No `Co-authored-by:` trailers:** Any `Co-authored-by:` line or trailer (case-insensitive) in commit messages, PR titles, or PR descriptions is rejected by `.githooks/commit-msg` and CI.
- **Automatic dependency PRs (Dependabot):** GitHub Dependabot cannot append a trailing `[TICKET-ID]` natively. No bot exemption is added to CI; maintainers triage automatic dependency PRs and rename the PR title (for example `ci(deps): bump actions/checkout [LREL-006]`) before squash-merging. Editing a PR title automatically reruns the PR convention gate.
- **Existing history:** Early bootstrap commit history is left intact without history rewrites.

## Opt-In Local Git Hooks

To catch repository, PowerShell, and commit-message issues before pushing, opt in to the tracked hooks:

```powershell
pwsh -NoProfile -File .githooks/install.ps1
```

This sets **only** repository-local `core.hooksPath = .githooks` (see [.githooks/README.md](.githooks/README.md)). You can also run checks manually:

```sh
python scripts/check-repository.py
python scripts/check-conventions.py --title "docs(library): clarify authoring layout [LIB-001]"
pwsh -NoProfile -File scripts/check-powershell.ps1
```

## Pull Request Templates and Review Expectations

- **Art & recipe PRs:** open with `?template=art.md` ([.github/PULL_REQUEST_TEMPLATE/art.md](.github/PULL_REQUEST_TEMPLATE/art.md)) and complete the metadata, per-asset attribution ledger, accessibility/fallback, and resource evidence sections.
- **Metadata, policy, schema, script, or CI PRs:** use the default template ([.github/pull_request_template.md](.github/pull_request_template.md)).
- Record only actually observed checks and environments; mark blocked engine/asset gates honestly rather than fabricating results.
- Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and report security vulnerabilities privately per [SECURITY.md](SECURITY.md).
