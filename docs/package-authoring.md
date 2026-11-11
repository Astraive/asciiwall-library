# Package Authoring Guide

This guide defines how contributors author portable wallpaper recipes for AsciiWall and curated `Astraive/asciiwall-library` submissions once the pinned engine packer (`package pack`, `package validate`, `bake`) ships under `LIB-002` and `LIB-003`.

Normative upstream specifications live in `Astraive/asciiwall`:
- [Format specification](https://github.com/Astraive/asciiwall/blob/main/docs/package/format-specification.md)
- [Manifest JSON Schema](https://github.com/Astraive/asciiwall/blob/main/docs/package/manifest-schema.md)
- [Declarative scene schema](https://github.com/Astraive/asciiwall/blob/main/docs/package/scene-schema.md)
- [Export and reproducibility](https://github.com/Astraive/asciiwall/blob/main/docs/package/export-and-reproducibility.md)
- [Examples and test vectors](https://github.com/Astraive/asciiwall/blob/main/docs/package/examples-and-test-vectors.md)

## 1. Local Authoring vs. Curated Repository Submissions

- **Private local authoring works independently:** You do not need to submit a pull request to `Astraive/asciiwall-library` to pack, validate, import, or share personal `.asciiwall` packages locally.
- **Curated repository intake:** Submissions to `Astraive/asciiwall-library` undergo automated pinned-engine validation, rights/provenance checks, resource-budget inspection, and human curation review.

## 2. Wallpaper Directory Layout (`wallpapers/<slug>/`)

Directory slugs and documentation files must be **lowercase kebab-case** (`a-z`, `0-9`, `-`):

```text
wallpapers/<slug>/
  manifest-source.json    # Build-input descriptor (distinct from published manifest.json)
  scene.json              # Required when source.kind = "scene"
  assets.lock.json        # Digest-pinned origins, byte ceilings, and license refs for fetched inputs
  presets/                # Optional quality, low-power, and reduced-motion preset descriptors
  preview.png             # Static preview image (portrait and wide previews required for featured L2+ review)
  fallback.png            # Static reduced-motion / incompatible fallback image
  attribution.md          # Human-readable credits, origins, modifications, and license obligations
  licenses/               # Full license text files referenced by license_files
```

### Build Inputs (`manifest-source.json`) vs. Strict Published `manifest.json`

- Authoring inputs (`manifest-source.json`) describe source metadata, compatible engine/features, portable settings, declared capabilities, and license files, and may omit final computed inventory SHA-256 digests and byte lengths prior to packing.
- **Never distribute `manifest-source.json` as a finished package.** Only the pinned upstream packer (`asciiwall package pack`) resolves all inventoried files and emits strict closed-world `manifest.json` (`format: "asciiwall"`, `format_version: "1.0"`) with actual SHA-256 digests and exact file sizes.
- Never embed the outer `.asciiwall` archive's own SHA-256 inside `manifest.json`; outer archive digests are external to the archive (`ArtifactReceipt` and `catalog.json`).

## 3. Five Source Kinds and Representation Honesty

Per [Wallpaper modes and editing capabilities](https://github.com/Astraive/asciiwall/blob/main/docs/product/mode-comparison.md):

| `source.kind` | Contents | Editing & Control Honesty |
| --- | --- | --- |
| `scene` | `scene.json` built-in declarative node graph (`scene_version: "1.0"`) | Full character-grid, color, and declared `controls` bound to recognized portable settings |
| `image` | Local decoded raster (`assets/<name>.png`, etc.) converted live | Grid/charset/conversion/color adjustments supported |
| `video` | Local video source decoded in restricted worker | Live playback & conversion settings; codec/license audited |
| `ascii-clip` | Precomputed `.ascii-clip` character stream | Palette/rendering adjustments; **cannot recover lost source pixel detail** |
| `rendered-video` | Pre-baked pixels already showing ASCII graphics | Playback only; **must not advertise editable glyph/charset sliders that cannot change baked pixels** (e.g. `ink-loop`) |

## 4. Portable Path and Archive Safety Rules

Every path inside a recipe and packed `.asciiwall` ZIP must strictly obey:

- Lowercase ASCII only (`[a-z0-9][a-z0-9./-]*`), forward slashes `/`, `<= 240` characters, `<= 8` path components
- **Forbidden:** leading `/`, backslashes `\`, drive letters or colons (`C:`, `:stream`), `..` traversal, `.` components, trailing dots/spaces, duplicate/case-colliding names, Windows reserved device basenames (`con`, `prn`, `aux`, `nul`, `com1`–`com9`, `lpt1`–`lpt9`), symlinks, hard links, encrypted ZIP entries, or nested archives disguised as sources
- **Zero hidden code:** v1 packages cannot contain build scripts, shell commands, JavaScript, WebAssembly, native libraries, plugins, or arbitrary user shaders

## 5. Closed v1 Scene Graph and Portable Controls (`scene.json`)

- **Approved v1 built-in node kinds only:** generators (`solid`, `matrix-rain`, `starfield`, `waves`, `noise-field`, `cube-wireframe`, `image-source`, `video-source`), unary character/pixel effects, passive observers (`pointer-force`, `click-ripple`, `window-avoid`), and binary `composite` (`slot: 0` base, `slot: 1` overlay). Unknown node kinds (including later-capability ideas like `lorenz-attractor` or `ascii-fire`) fail closed in v1.
- **Graph topology:** unique node IDs, acyclic DAG (`<= 128` nodes, `<= 256` edges), strict slot arity (`0` inputs for generators, `1` for unary, `2` for `composite`), and every node must contribute to `output`.
- **Registry-backed controls (`controls[]`):** may bind **only** to the 80 recognized portable visual settings defined in the manifest schema (`grid.*`, `font.*`, `charset.*`, `conversion.*`, `color.*`, `playback.*`, `scene.*`, `effects.*`, `interaction.*`, `transition.*`). A package can **never** set privacy, network, autostart, output assignment, or permission keys.

## 6. Fonts, Locked Assets (`assets.lock.json`), and Private Paths

- **Fonts:** Use approved built-in engine fonts by default. Setting `settings.font.face` to `package-font` requires an inventoried redistributable font file (`<= 16 MiB`) and its full license file in `licenses/` (respecting OFL reserved font names if modified). Never reference creator-local paths or scan system fonts.
- **Fetched media (`assets.lock.json`):** Every externally fetched source asset must declare an approved immutable HTTPS origin, exact `sha256`, maximum `size` ceiling, immutable version, and license ledger reference. Mutable `"latest"` URLs, `file://` URIs, URL userinfo, private/local network targets, and creator-local absolute paths are rejected.

## 7. Required Metadata, Presets, Capabilities, and Acceptance Examples

Per `AST-037` and [Starter wallpaper catalog](https://github.com/Astraive/asciiwall/blob/main/docs/library/starter-wallpaper-catalog.md), every curated recipe requires:

- Name, short summary, real author declaration, SPDX license identifier, source provenance, tags, minimum engine version & required features, required/optional capabilities, quality preset, low-power preset, reduced-motion static fallback, portrait & wide static previews (`preview.png`, `fallback.png`), and measured resource observations from a named reference machine (once measurable with real engine builds — never fabricated badges).
- **Disjoint capabilities:** `capabilities.required` and `capabilities.optional` cannot overlap (`pointer-position`, `pointer-buttons`, `window-rectangles`, `window-state`, `local-clock`). Optional feeds must render cleanly as pass-throughs when denied or offline:
  - `desktop-ripples` must run cleanly as ordinary waves without `pointer-buttons`.
  - `window-wake` must disclose that plain Wayland compositors may not provide `window-rectangles`.
  - `ink-loop` (`rendered-video`) must not expose glyph controls that cannot affect baked pixels.
  - `still-night` must stop continuous redraw when unchanged.
