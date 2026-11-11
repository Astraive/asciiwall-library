# Library Roadmap (`L0`–`L4`) and 36 Recipe Briefs

**Planning notice:** Milestones `L0`–`L4` define dependency order, entry/exit criteria, and mandatory evidence gates (`LQA-L0`–`LQA-L4`). Effort figures are planning estimates in atomic engineering days, not calendar delivery dates. **All 36 starter recipes remain design briefs only; zero wallpapers or catalogs are published today.**

## 1. Independent Library Milestones (`L0`–`L4`)

`Astraive/asciiwall-library` follows five independent milestones coordinated against [upstream application milestones](https://github.com/Astraive/asciiwall/blob/main/docs/delivery/milestones-and-dependencies.md):

| Milestone | Title | Target Release | Items | Atomic Effort | Gate | Core Exit Criteria |
| --- | --- | --- | --- | --- | --- | --- |
| `L0` | Library Foundation | `library-foundation` | `10` | `17` days (+`40` coord.) | `LQA-L0` | Repository/source/artifact separation, intake/review/licensing policies, secretless CI boundaries, and reviewed engine/schema pin ownership (`PKG-001` required to finalize `LIB-002` pin). |
| `L1` | Package and Catalog Tooling | `library-alpha` | `15` | `54` days (+`24` coord.) | `LQA-L1` | Digest-pinned `assets.lock.json` resolver, per-asset rights validator (`LLEG-002`), P07 reproducible packer orchestration (`LIB-003`), closed catalog 1.0 schema/semantic validator (`CAT-001`–`CAT-004`), and exact-byte `ed25519` signature vectors (`CAT-005`). |
| `L2` | Starter Collection Alpha | `library-alpha` | `24` | `116` days | `LQA-L2` | All `20` v1 procedural briefs (`AST-001`–`AST-020`) authored with deterministic presets, portrait/wide static previews, reduced-motion fallbacks, named reference hardware measurements (`LQA-002`), duplicate curation (`LQA-003`), and human review (`LCOM-002`). |
| `L3` | Compatible Library 1.0 | `library-1.0.0` | `16` | `76` days | `LQA-L3` | All `8` rights-cleared media candidates (`AST-021`–`AST-028`) authored with verified source consent/rights, 5-source-kind cross-platform conformance (`LQA-004`), embedded font & native codec review (`LLEG-003`), compatibility matrix (`LIB-005`), nonproduction key rotation drill (`LREL-003`), and immutable `1.0` candidate BOM (`LREL-004`). |
| `L4` | Maintenance | `library-post-1.0` | `13` | `61` days | `LQA-L4` | Upstream readiness matrix for the `8` later recipes (`AST-038`, `AST-029`–`AST-036`), hash-based takedown operations (`LLEG-004`), optional offline bundle index (`LREL-005`), and recurring compatibility/provenance maintenance cycles (`LREL-006`). |

**Totals across `78` local library tickets:** `324` atomic engineering days plus `64` container coordination days across `1` roadmap (`LIB-ROADMAP-001`), `7` epics, `65` tasks, and `5` milestone gates (`LQA-L0`–`LQA-L4`).

## 2. Gate Progression Rules (`LQA-L0`–`LQA-L4`)

- Every gate remains `Backlog` until all hard-blocker tasks link exercised evidence (exact source commit SHA, fixture/artifact SHA-256 digests, commands executed, and actual OS/hardware tuples).
- Foundation documentation, GitHub configuration, or dry-run validation is **not** milestone completion evidence for packaging or artwork gates.
- Zero unresolved P0 security, archive-escape, unauthorized-rights, or hash-mismatch failures may be waived.

## 3. Disposition of All 36 Starter Recipe Briefs

Source specification: [Starter wallpaper catalog and recipe briefs](https://github.com/Astraive/asciiwall/blob/main/docs/library/starter-wallpaper-catalog.md).

### 3.1 Twenty v1 Procedural Scene Candidates (`L2`, `AST-001`–`AST-020`)

These 20 candidates target proposed draft-v1 built-in scene nodes (`matrix-rain`, `starfield`, `waves`, `noise-field`, `cube-wireframe`, `composite`, passive reactions). They remain blocked on `AST-037`, `LIB-003`, and upstream engine nodes (`SCN-002`–`SCN-006`, `FX-003`–`FX-005`, `FX-007`).

| Ticket | Slug | Collection | Built-in Generator / Nodes | Required Fallback / Acceptance Rule | Disposition |
| --- | --- | --- | --- | --- | --- |
| `AST-001` | `matrix-rain` | Rain | `matrix-rain` + optional `click-ripple` | Intentional base rain with click feed denied; ripple count bounded | Brief only (`L2`, blocked on `SCN-002`, `FX-004`) |
| `AST-002` | `quiet-waves` | Minimal | `waves` | Slow low-density monochrome; static reduced-motion frame | Brief only (`L2`, blocked on `SCN-004`) |
| `AST-003` | `deep-starfield` | Space | `starfield` | Bounded parallax; intentional static depth without feed | Brief only (`L2`, blocked on `SCN-003`) |
| `AST-004` | `wireframe-cube` | Geometry | `cube-wireframe` | Slow rotation, adjustable scale, zero global observers | Brief only (`L2`, blocked on `SCN-006`) |
| `AST-005` | `mist-field` | Abstract | `noise-field` | Soft density drift; no high-contrast flashes | Brief only (`L2`, blocked on `SCN-005`) |
| `AST-006` | `amber-terminal` | Minimal | `matrix-rain` | Amber palette, sparse streams, distinct from `matrix-rain` | Brief only (`L2`, blocked on `SCN-002`) |
| `AST-007` | `paper-waves` | Minimal | `waves` | Dark glyphs on light background; legible contrast | Brief only (`L2`, blocked on `SCN-004`) |
| `AST-008` | `blue-hour` | Abstract | `noise-field` | Duotone low-frequency drift | Brief only (`L2`, blocked on `SCN-005`) |
| `AST-009` | `constellation-drift` | Space | `starfield` | Lower star count and slow depth motion | Brief only (`L2`, blocked on `SCN-003`) |
| `AST-010` | `forest-rain` | Rain | `matrix-rain` | Green palette, long trails, curated variant rationale | Brief only (`L2`, blocked on `SCN-002`) |
| `AST-011` | `magnetic-stars` | Reactive | `starfield` + optional pointer attraction | Neutral coherent starfield when pointer feed denied | Brief only (`L2`, blocked on `SCN-003`, `FX-003`) |
| `AST-012` | `desktop-ripples` | Reactive | `waves` + optional `click-ripple` | **Must continue as ordinary waves without `pointer-buttons`** | Brief only (`L2`, blocked on `SCN-004`, `FX-004`) |
| `AST-013` | `window-wake` | Reactive | `noise-field` + optional `window-avoid` | **Must disclose plain Wayland lacks window rectangles** | Brief only (`L2`, blocked on `SCN-005`, `FX-005`) |
| `AST-014` | `monochrome-orbit` | Geometry | `cube-wireframe` | White line geometry on black; zero global feeds | Brief only (`L2`, blocked on `SCN-006`) |
| `AST-015` | `solar-haze` | Abstract | `noise-field` | Warm tones with constrained contrast | Brief only (`L2`, blocked on `SCN-005`) |
| `AST-016` | `ocean-lines` | Minimal | `waves` + `composite` | Layered binary composites within aggregate budget | Brief only (`L2`, blocked on `SCN-004`, `FX-007`) |
| `AST-017` | `rain-duet` | Rain | `matrix-rain` + `composite` | Two independently seeded layers within aggregate budget | Brief only (`L2`, blocked on `SCN-002`, `FX-007`) |
| `AST-018` | `still-night` | Low power | `starfield` | **Must stop continuous redraw when unchanged** | Brief only (`L2`, blocked on `SCN-003`) |
| `AST-019` | `paper-cube` | Low power | `cube-wireframe` | Static geometric composition; event-driven idle | Brief only (`L2`, blocked on `SCN-006`) |
| `AST-020` | `slow-tide` | Low power | `waves` | `10 FPS` preset without trails or bloom | Brief only (`L2`, blocked on `SCN-004`) |

### 3.2 Eight Rights-Cleared Media Candidates (`L3`, `AST-021`–`AST-028`)

These 8 candidates require creating or acquiring original/CC0/authorized media with full provenance ledgers, subject consent (where applicable), and verified source-kind support (`image`, `video`, `ascii-clip`, `rendered-video`).

| Ticket | Slug | Collection | Source Kind | Rights & Fidelity Requirements | Disposition |
| --- | --- | --- | --- | --- | --- |
| `AST-021` | `mountain-study` | Image | `image` | Original or CC0 landscape; edge-aware conversion; portrait/wide crop safety | Brief only (`L3`, `asset-needed`) |
| `AST-022` | `botanical-study` | Image | `image` | Original leaf photograph with reviewed attribution ledger | Brief only (`L3`, `asset-needed`) |
| `AST-023` | `city-outline` | Image | `image` | Original architectural silhouette; crop-safe framing | Brief only (`L3`, `asset-needed`) |
| `AST-024` | `portrait-study` | Image | `image` | Consented original portrait; private proof kept outside public repo without PII | Brief only (`L3`, `asset-needed`) |
| `AST-025` | `cloud-loop` | Video | `video` | Original short cloud clip; clean loop boundary & codec audit | Brief only (`L3`, `asset-needed`) |
| `AST-026` | `ocean-loop` | Video | `video` | Original/authorized waves with muted playback and codec audit | Brief only (`L3`, `asset-needed`) |
| `AST-027` | `ember-loop` | Video | `ascii-clip` | Precomputed character clip; editable palette only; blocked on `VID-009` | Brief only (`L3`, `asset-needed`) |
| `AST-028` | `ink-loop` | Video | `rendered-video` | Baked pixels; **must not expose editable glyph controls**; blocked on `VID-013` | Brief only (`L3`, `asset-needed`) |

### 3.3 Eight Later-Capability Candidates (`L4`, `AST-029`–`AST-036`)

These 8 candidates remain **unavailable in draft v1** (`AST-038`). Unknown node or signal kinds are rejected by the closed v1 schema and cannot be shipped via library scripts or shims.

| Ticket | Slug | Collection | Required Upstream Feature (`asciiwall`) | Hard Gate Before Authoring | Disposition |
| --- | --- | --- | --- | --- | --- |
| `AST-029` | `lorenz-attractor` | Math | Bounded deterministic ODE integration | Fixed step, finite clamp, bounded point history | Unavailable in v1 (`L4`, `AST-038`) |
| `AST-030` | `boid-garden` | Simulation | Capped particle/boid simulation (`SCN-009`) | Particle count & neighbor force caps; optional pointer neutral | Unavailable in v1 (`L4`, `AST-038`, `SCN-009`) |
| `AST-031` | `reaction-diffusion` | Simulation | Stable-step reaction-diffusion grid | Explicit compute/grid budget & timestep stability | Unavailable in v1 (`L4`, `AST-038`) |
| `AST-032` | `cellular-life` | Simulation | Deterministic fixed-grid cellular automaton | Fixed grid ceiling, deterministic seed, safe wrap/boundary | Unavailable in v1 (`L4`, `AST-038`) |
| `AST-033` | `ascii-fire` | Simulation | Bounded first-party fire simulation (`SCN-008`) | No-flash defaults & static reduced-motion fallback | Unavailable in v1 (`L4`, `AST-038`, `SCN-008`) |
| `AST-034` | `wireframe-torus` | Geometry | 3D glyph rasterization research | Clipping, depth budget, deterministic projection | Unavailable in v1 (`L4`, `AST-038`) |
| `AST-035` | `audio-spectrum` | Audio | Chosen-file audio analysis (no microphone default) | Explicit file input boundary & privacy isolation | Unavailable in v1 (`L4`, `AST-038`) |
| `AST-036` | `day-night-field` | Schedule | Local-clock palette / schedule rules (`SCN-010`) | Explicit local-clock capability & DST/timezone semantics | Unavailable in v1 (`L4`, `AST-038`, `SCN-010`) |
