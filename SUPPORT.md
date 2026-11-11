# Support Policy

## Scope of This Repository

`Astraive/asciiwall-library` hosts the community wallpaper recipes, provenance/attribution records, static collection schemas, and catalog release tooling for AsciiWall.

| Topic | Where to Route |
| --- | --- |
| Policies, validation scripts, CI workflows, schemas, or recipe authoring docs in this repo | Open an issue using the structured forms in `.github/ISSUE_TEMPLATE/` |
| Future curated wallpaper recipe submissions or attribution corrections | Use the **Wallpaper recipe submission** issue form or `?template=art.md` PR template |
| AsciiWall Rust engine, image/video converter, CLI, GPU preview, or Windows/macOS/Linux desktop host | Route to [`Astraive/asciiwall` Issues](https://github.com/Astraive/asciiwall/issues) |
| Undisclosed security flaw, malicious archive/media trigger, or CI privilege bug | Report **privately** via [Security Advisories](https://github.com/Astraive/asciiwall-library/security/advisories/new) ([SECURITY.md](SECURITY.md)) |
| Copyright, attribution, font license, or consent takedown dispute | Follow [docs/licensing-and-review.md](docs/licensing-and-review.md#rights-disputes-and-takedown-process) |

## Current Support Status

- **No published wallpapers or catalogs exist yet:** this repository is at the `L0` foundation baseline (`LIB-001`). Do not treat the 36 upstream recipe briefs as downloadable packages or verified runtime demos.
- **No runtime backend or user accounts:** AsciiWall is local-first and offline-capable; this repository provides optional static distribution tooling only when future releases ship.
- **No platform support certifications:** curated wallpaper compatibility and reference hardware measurements remain pending pinned engine releases (`L1`–`L3`).

## Disclosure and Privacy Rules for Issues

When opening any public issue here:

- Never attach secrets, tokens, private host filesystem paths, or personal media files.
- Never attach private model/subject permission proof containing personal data (PII); keep private proofs off public threads and reference only immutable asset hashes where instructed by maintainers.
- Never paste third-party commercial movie/game media or unverified web-search images.
