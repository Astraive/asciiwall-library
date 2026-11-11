# Licensing, Attribution, Curation Review, and Moderation

**Engineering compliance notice:** This policy defines repository rights verification and moderation rules. It is **not legal advice**. Before public binary or package releases, review exact bundled binaries, codec configure flags, notices, and jurisdictional considerations with qualified advice where needed.

Normative upstream references:
- [Code, media, fonts, and attribution](https://github.com/Astraive/asciiwall/blob/main/docs/library/licensing-and-attribution.md)
- [Wallpaper contribution and review policy](https://github.com/Astraive/asciiwall/blob/main/docs/library/contribution-and-review.md)

## Separate Rights Layers (`LLEG-001`)

1. **Repository foundation (`LICENSE`):** scripts, policies, documentation, schemas, and templates in `Astraive/asciiwall-library` are licensed under the **MIT License**.
2. **Upstream AsciiWall engine:** proposed `MIT OR Apache-2.0` code license (subject to dependency audit in `Astraive/asciiwall`).
3. **Per-asset artwork, media, fonts, audio, and previews:** every wallpaper recipe, source photograph/video, font, audio clip, thumbnail, and fallback image keeps **its own explicit license and attribution record**. The repository's MIT license **never** automatically relicenses submitted third-party artwork or media.

## Allowed Licenses and Strict Exclusions

| Submission Class | Policy | Required Evidence |
| --- | --- | --- |
| Original procedural `scene.json` (`CC0-1.0` / `MIT` / `CC BY 4.0`) | **Preferred** for starter collection | Original-author declaration, SPDX ID, full license file in `licenses/` |
| `CC0-1.0` / Public Domain media | **Preferred** for media candidates | Exact origin URL or original-author proof, full text/dedication |
| `CC BY 4.0` media | **Allowed** with complete credit | Author/rights holder, origin URL, modifications notice, full license text |
| `CC BY-SA` media | **Restricted / explicit review** | Explicit adaptation & share-alike compatibility review before curation |
| Custom `LicenseRef-*` | **Explicit review** | Complete custom license text in `licenses/` confirming redistribution rights |
| NonCommercial (`NC`) / NoDerivatives (`ND`) | **Excluded by default** | Rejected from default curated collection unless explicit policy approval granted |
| "Found on Google" / unattributed stock / commercial movie or game clips | **Always rejected** | Converting copyrighted video or imagery into ASCII glyphs does **not** extinguish source rights |

## Per-Asset Provenance Ledger and Privacy (`LLEG-002`)

Every inventoried file (`source`, `preview`, `fallback`, `font`, derivatives, and `license_files`) requires a ledger record across `assets.lock.json`, `attribution.md`, and `licenses/` recording:

- Exact origin URL or original-author declaration
- Author / rights holder name and attribution display text
- Valid SPDX license identifier and full license file in `licenses/`
- Explicit statement of modifications made and redistribution constraints
- **Private permission proof separation (no PII leaks):** where subject consent or private licensing proof contains personal information (such as model releases for `portrait-study`), keep personal documents **outside** public Git/packages and bind internal maintainer evidence to the asset's immutable SHA-256 digest without exposing PII publicly.
- Plain-text or PNG exports must preserve attribution via accompanying attribution sidecar/metadata rather than assuming an image watermark satisfies license duties.

## Fonts and Native Codec Obligations (`LLEG-003`)

- **Fonts:** Personal use of a local font does **not** grant permission to embed or redistribute that font in `.asciiwall` packages. Embedded fonts require verified redistribution rights, complete license files, and adherence to SIL OFL reserved-font-name clauses if modified. Otherwise use approved built-in engine fonts.
- **Native media dependencies (FFmpeg):** Wrapper crate licenses (`MIT` / `Apache-2.0`) do **not** determine combined-work obligations of linked codecs. Any future library/release tooling consuming a pinned engine build must record exact FFmpeg versions, configure flags, GPL/LGPL components, static vs. dynamic linking, required notices, and corresponding-source instructions.

## Human Curation Review Checklist (`LCOM-002`)

Automated schema/hash checks do not prove visual quality or safety. Before curated inclusion, human reviewers verify and record (tied to exact package SHA-256 and pinned engine revision):

- Visual legibility, restrained default motion intensity, and absence of high-contrast flashing defaults
- Legitimate original origin and plausible provenance (escalate uncertain rights — never launder uncertain media under a permissive package license)
- Intentional playback across **both** narrow/portrait and wide layouts
- Low-power preset and reduced-motion/static fallback behavior (including static idle zero-redraw where claimed)
- **Graceful denial:** full functionality with network blocked and optional observers (`pointer-position`, `pointer-buttons`, `window-rectangles`) denied or unavailable
- Real `Apply` and `Stop` verification on supported hosts without input interception or excessive resource use
- Non-duplicate collection curation (prevent padding featured lists with near-identical palette clones)

## Moderation, Deprecation, and Advisory Separation (`LCOM-003`)

Every curated package records a responsible maintainer, package ID/version/SHA-256, author credits, and compatibility matrix:

- **Quality deprecation / engine incompatibility:** removes recommendation from future catalog sequences with an explicit reason; never flags merely unsupported or superseded art as malware.
- **Security advisory:** flags a specific compromised/malicious package SHA-256 via authenticated advisory/catalog channels.
- **Non-destructive user sovereignty:** historical immutable releases remain auditable; moderation **never** alters running wallpaper assignments silently and **never** remotely deletes users' installed local packages without consent. Offline devices cannot receive instant revocation notices until refreshed.

## Rights Disputes and Takedown Process

1. **Report route:** Submit rights, copyright, font-license, or consent disputes privately by emailing maintainer `@NeerajCodz` at `neerajcodz@gmail.com` (or via [GitHub Private Vulnerability Reporting](https://github.com/Astraive/asciiwall-library/security/advisories/new) if confidential evidence must be shared before public notice). Include the claimed package ID, version, asset/package SHA-256, and basis of the claim without posting private PII in public issue threads.
2. **Immediate review & future catalog exclusion:** Maintainers retain an internal hash-bound audit trail (`LLEG-004`) while removing disputed entries from subsequent catalog sequences during investigation.
3. **Resolution & public notices:** Published takedown or reinstatement notices cite affected package IDs, versions, exact SHA-256 hashes, and resulting catalog sequence numbers while omitting private personal proofs.
4. **Offline limitation:** Removing a package from future catalogs stops new remote catalog distribution, **not** existing offline copies already saved on users' devices; documentation and advisories never claim retroactive deletion of local files.
