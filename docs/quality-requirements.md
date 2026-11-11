# Quality Requirements and CI Validation Gates

This document defines what CI checks run **today** on the repository foundation, why package/catalog/preview gates fail closed when prerequisites are missing, and what automated + manual evidence is required across milestones `L0`–`L4`.

## 1. Current Runnable Repository CI (Foundation Baseline)

On a fresh clone with **zero secrets** and **zero dependency on external `../.issues/` or sibling `../asciiwall/`**, CI runs two workflows with `permissions: contents: read` (plus `security-events: write` only for CodeQL):

| Check Context | Workflow / Script | What It Actually Verifies Today |
| --- | --- | --- |
| `Repository quality` | `.github/workflows/repository-checks.yml` (`scripts/check-repository.py`, `ruby -ryaml`, `scripts/check-powershell.ps1`, `scripts/check-conventions.py`) | Standalone stdlib check of UTF-8 without BOM, LF line endings, balanced Markdown code fences, valid local links and heading anchors, kebab-case `docs/*.md` filenames, strict duplicate-key-free JSON parsing, YAML syntax across `.github/**/*.{yml,yaml}`, SHA-pinned workflow hygiene (no `pull_request_target`, least privilege, `timeout-minutes`, no inline PR expression injection), PowerShell AST parsing (`Parser::ParseFile` without executing scripts), PR title/body/commit `Co-authored-by` checks (re-triggered on `pull_request` `edited`), and **fail-closed rejection** of premature art/package/catalog inputs. |
| `Python security analysis` | `.github/workflows/security-analysis.yml` (CodeQL `python`, `+security-extended`) | Static security scanning across tracked Python repository tooling. |

**Automatic dependency PRs:** Weekly `.github/dependabot.yml` covers `github-actions` only. Dependabot cannot add `[TICKET-ID]` to PR titles automatically; no bot exemption exists, so maintainers triage and rename dependency PR titles to `type(scope): subject [TICKET-ID]` (for example `ci(deps): bump actions/checkout [LREL-006]`) before merge.

## 2. Fail-Closed Policy for Premature Art, Package, or Catalog Inputs

Automated package building (`LIB-003`), preview baking (`LQA-002`), asset lock verification (`LIB-004`), rights ledger validation (`LLEG-002`), duplicate detection (`LQA-003`), and catalog validation (`CAT-001`–`CAT-005`) require pinned AsciiWall engine binaries (`package pack`, `package validate`, `bake`) and reviewed `schemas/engine-schema-lock.json` contracts from `Astraive/asciiwall`.

- **No empty release workflow:** this repository intentionally omits release/publish workflows until those binaries and signing key custody exist.
- **No skipped-green passes:** `scripts/check-repository.py` rejects files under `wallpapers/`, `collections/`, `catalog/`, `packages/`, or with extensions `.asciiwall` / `.ascii-clip` while the artifact pipeline is unimplemented. It lists missing prerequisites and owning tickets (`LIB-002`, `PKG-001`, `CLI-001`, `PKG-010`, `LIB-003`, `LIB-004`, `LLEG-002`, `CAT-002`). Adding prerequisite-shaped files does not unlock acceptance: the L1 implementation must replace this guard with actual pinned-engine builds and independent semantic, integrity, and rights validation.

## 3. Hard Format and Resource Budgets (L1–L3 Gates)

Per [Format specification](https://github.com/Astraive/asciiwall/blob/main/docs/package/format-specification.md) and `LQA-002`, library gates enforce budgets at or below upstream ceilings:

| Resource | Hard v1 Ceiling | Enforcement Rule |
| --- | ---: | --- |
| Compressed `.asciiwall` archive | `1,073,741,824` bytes (`1 GiB`) | Checked by streamed count, not header claims alone |
| Total expanded file bytes | `2,147,483,648` bytes (`2 GiB`) | Reject bombs and cancel/clean staging on breach |
| Total ZIP entries | `4,096` entries | Includes manifest, assets, and optional dirs |
| Single ordinary asset | `1,073,741,824` bytes (`1 GiB`) | Large media stays in release assets, never Git history |
| `manifest.json` | `1,048,576` bytes (`1 MiB`) | Reject duplicate JSON keys and unknown fields |
| `scene.json` | `4,194,304` bytes (`4 MiB`) | `<= 128` nodes, `<= 256` edges, acyclic DAG |
| Embedded font asset | `16,777,216` bytes (`16 MiB`) | Redistribution license & `package-font` binding required |
| Static preview (`preview.png` / `fallback.png`) | `8,388,608` bytes (`8 MiB`) | Bounded render dimensions verified against declaration |
| JSON nesting depth | `32` levels | Enforced pre-semantic parse |
| Decoded raster asset | `64,000,000` pixels / `256 MiB` buffer | Inspect dimensions before full allocation |
| Static `catalog.json` | `16 MiB` (`16,777,216` bytes), `<= 10,000` entries | Bounded prior to JSON parsing (`CAT-002`) |

## 4. Privilege Separation and Subprocess Isolation (`LQA-001`)

- Untrusted contributor PR workflows run **without** signing keys, release tokens, or write credentials, and must **never** use `pull_request_target` with untrusted PR checkouts.
- Pinned `asciiwall package pack`, `package validate`, and `bake` subprocesses run inside bounded CPU, memory, and wall-clock limits with playback networking disabled.
- A failed thumbnail or decoder timeout is a hard build failure — never inspect or decode untrusted media inside the CI controller process.
- Trusted publishing runs only from protected, reviewed commits and re-verifies exact artifact SHA-256 digests and provenance independently before signing.

## 5. Planned Quality Evidence Matrix (`LQA-002`–`LQA-004`)

1. **Deterministic Builds & Static Previews (`LQA-002`):** Rebuild equivalent packages twice from identical pinned inputs/seeds; confirm identical `.asciiwall` archive bytes where promised; bake portrait and wide static previews (`network` and optional feeds off).
2. **Named Reference Hardware Resource Notes (`LQA-002`):** Record OS build, CPU, GPU/driver, pinned engine/source revision, FPS, cell dimensions, memory/CPU/GPU usage, low-power (`10 FPS`) behavior, and unchanged idle zero-redraw verification (`still-night`). **Never invent performance badges or copy unmeasured budgets as observed numbers.**
3. **Duplicate & Near-Clone Curation (`LQA-003`):** Enforce unique `(id, version)` pairs, deduplicate identical SHA-256 triples, fail on same `(id, version)` differing SHA-256 conflicts, and flag palette-only / near-duplicate variants for human curation so the featured starter set remains small, diverse, and low-power.
4. **Cross-Platform Conformance (`LQA-004`):** Freeze `1.0` compatibility only after real authorized examples of all 5 source kinds (`scene`, `image`, `video`, `ascii-clip`, `rendered-video`), malformed archive/bomb rejection, Windows/macOS/Linux portable path tests, offline clean-machine imports, and `ed25519` signature vectors agree with upstream `PKG-012` conformance.
