<!--
Wallpaper artwork, recipe, and attribution pull request template.
Open art submissions with `?template=art.md` (or paste this checklist into the PR description).
Follow docs/package-authoring.md, docs/quality-requirements.md, and docs/licensing-and-review.md.
PR title format: type(scope): subject [TICKET-ID], for example "feat(wallpapers): add matrix-rain starter recipe [AST-001]".
No Co-authored-by trailers are permitted anywhere in commits or PR descriptions.
-->

**Ticket:** <!-- Stable ticket ID (e.g. AST-001) and `Refs #N` / `Closes #N` once published; omit `#N` if unpublished. -->

## Wallpaper metadata summary

| Field | Value |
| --- | --- |
| Slug (lowercase kebab-case) | |
| Collection | |
| Source kind (`scene`, `image`, `video`, `ascii-clip`, `rendered-video`) | |
| Minimum engine version & required features | |
| Required capabilities | |
| Optional capabilities (with no-feed fallback behavior) | |
| Pinned engine / schema lock revision | |

## Asset, attribution, and provenance ledger

<!-- List every file in the recipe (source scene/media, static portrait/wide previews, reduced-motion fallback, embedded font if any, and license files).
     Personal permission proofs containing PII must stay private outside public packages while referencing immutable asset SHA-256 digests. -->

| Asset path | Role | Origin URL or original-author declaration | SPDX License ID | License file path | SHA-256 | Size (bytes) | Modifications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Rights and provenance declaration

- [ ] Repository MIT license is NOT assumed to relicense third-party media, fonts, or artwork; every asset carries its own license record.
- [ ] Original procedural source, `CC0-1.0`, `CC BY 4.0`, or explicitly approved compatible license with full license text in `licenses/`.
- [ ] Zero search-engine ("found on Google") sources, unattributed stock, or unauthorized movie/game/franchise clips.
- [ ] Zero creator-local filesystem paths, undeclared system fonts, or hidden build scripts/plugins/shaders/WASM.
- [ ] Private permission proof (if applicable, e.g. portrait consent) is referenced cleanly without exposing PII in the public repo or PR.

## Accessibility, fallback, and resource evidence

- **Portrait & wide layout previews:** <!-- Describe or link verified static preview dimensions and SHA-256s; note `Blocked` if pinned engine `bake` is unavailable. -->
- **Low-power preset:** <!-- Exact portable settings for low-power mode. -->
- **Reduced-motion / static fallback:** <!-- Exact static fallback behavior and idle redraw status. -->
- **Network & optional-feed denied behavior:** <!-- Confirm playback remains intentional with network and pointer/window observers off. -->
- **Named reference hardware observations:** <!-- OS, CPU, GPU, engine/source revision, FPS, cell grid, memory/power notes — never invent badges. -->

## Art and pipeline checklist

- [ ] Directory follows `wallpapers/<slug>/` layout (`manifest-source.json`, `scene.json` if `scene`, `assets.lock.json`, `attribution.md`, `licenses/`, `preview.png`, `fallback.png`).
- [ ] Portable paths strictly obey lowercase ASCII, `/` separators, `<=240` chars, `<=8` components, and no reserved Windows names.
- [ ] No duplicate ID/version conflicts or weakly differentiated near-clone padding.
- [ ] All budgets remain within limits (`manifest <= 1 MiB`, `scene <= 4 MiB`, `preview <= 8 MiB`, `font <= 16 MiB`, `archive <= 1 GiB`).
- [ ] `python scripts/check-repository.py` and pinned-engine `package pack` / `package validate` / `bake` checks pass (or missing engine gate explicitly recorded as blocked).
- [ ] No `Co-authored-by` trailers in commits or PR description.
