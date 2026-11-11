# Library Release Process, Static Catalogs, and Key Custody

**Current release status:** **No wallpaper packages (`.asciiwall`), static catalogs (`catalog.json`), detached signatures (`catalog.sig`), or release tags have been published yet.** Signing key custody is **not configured**, and release automation is intentionally withheld until pinned engine dependencies (`LIB-002`, `LIB-003`), catalog tooling (`CAT-001`–`CAT-005`), and key rotation rehearsals (`LREL-003`) are complete.

Normative upstream specifications:
- [Static catalog schema and trust model](https://github.com/Astraive/asciiwall/blob/main/docs/library/catalog-and-index-schema.md)
- [Library build and release pipeline](https://github.com/Astraive/asciiwall/blob/main/docs/library/release-pipeline-and-distribution.md)
- [Package compatibility and migrations](https://github.com/Astraive/asciiwall/blob/main/docs/package/compatibility-and-migrations.md)
- [Supply chain, signatures, and updates](https://github.com/Astraive/asciiwall/blob/main/docs/security/supply-chain-and-updates.md)

## 1. Independent Versioning and Compatibility Matrix (`LIB-005`)

`Astraive/asciiwall-library` versions collections and static catalogs independently from AsciiWall application releases:

- **Application SemVer (`asciiwall`):** `MAJOR.MINOR.PATCH[-prerelease]` (unreleased)
- **`.asciiwall` format & `scene.json` schema:** `1.0` draft (frozen only after cross-platform conformance gate `PKG-012` + `LQA-004` passes across all 5 source kinds)
- **`catalog.json` schema:** `1.0` draft (`catalog_version: "1.0"`, monotonically increasing integer `sequence`, UTC `published_at` / `expires_at`)
- **Package `version`:** per-wallpaper SemVer compared with full prerelease ordering (never overwrite an existing `(id, version)` URL with different bytes)

Syntactic validity does not guarantee activation compatibility: an imported package may be importable yet non-activatable if the user's engine lacks a disabled codec, required capability, or newer format version.

## 2. Backend-Free Static Distribution Model (`LREL-002`)

- **Zero runtime backend:** No hosted API, user account, database server, or search server is required or used. After explicit user consent to refresh a static catalog, search and filtering run locally over downloaded static JSON.
- **Static artifact origins:** Versioned immutable packages, `.sha256` checksums, static previews, attribution sidecars, `catalog.json`, and `catalog.sig` distribute via explicit HTTPS release origins (such as versioned GitHub Release assets) — never via ordinary Git commit history for large media/archives, and never via `file://`, credentialed URLs, or private-network endpoints inside remote catalogs.
- **v1 offline distribution:** Users without network access import several ordinary validated `.asciiwall` files plus checksums and attribution directly through the normal offline importer. A dedicated offline multi-package bundle index (`LREL-005`) is deferred to `L4`.
- **Consentful download checks (upstream `LIBAPP` contract):** Clients display byte size, origin, author, license, required features, and trust state before download, validate TLS and every redirect strictly, reject captive-portal HTML, verify full-file SHA-256 before extraction, and keep already-installed local packages usable regardless of network availability.

## 3. Immutable Release Pipeline (`LREL-001`, Planned `L1`–`L3`)

Future trusted releases follow strict privilege separation:

1. **Protected reviewed commit:** Select audited wallpaper recipes and a pinned `schemas/engine-schema-lock.json` engine/schema release.
2. **Isolated worker build:** Unprivileged isolated workers verify `assets.lock.json` digests and `attribution.md` ledgers, pack via pinned `asciiwall package pack`, validate independently via `asciiwall package validate`, bake static previews, and emit `ArtifactReceipt` records derived strictly from final output bytes (`CAT-003`).
3. **Trusted re-verification & signing:** A protected release job (never triggered by untrusted PRs) re-verifies every final package and preview SHA-256/size against receipts, uploads immutable `slug-version.asciiwall`, checksums, previews, provenance, and `catalog.json` (sorted deterministically, `<= 16 MiB`), signs exact catalog bytes, and records a release build manifest (`LQA-L3`).
4. **Immutability invariant:** Never mutate bytes at an existing package ID/version URL. Corrections publish a new package `version` and increment catalog `sequence`. Downloading new metadata never silently mutates active user wallpaper assignments.

## 4. Exact-Byte Detached Signature Profile (`CAT-005`)

- **Algorithm & envelope:** Detached signature (`catalog.sig`) using fixed `ed25519`, a trusted `key_id`, and Base64-encoded 64-byte signature.
- **Signed message:** Exact ASCII domain prefix `asciiwall-catalog-v1` followed by one zero byte (`\0`) and the **exact original UTF-8 bytes** of `catalog.json` — never reserialized JSON (`CAT-005`).
- **Rollback & expiration semantics:** Clients track highest accepted `sequence` per trusted `catalog_id` to detect rollback. Expired catalogs may warn while remaining readable for inspection, blocking new automatic remote installs without explicit recovery; installed local packages keep working offline.
- **Honest trust-model limitation:** This signed static catalog profile is **not** full TUF (`S44`). An offline client cannot prove metadata freshness or immediately discover key compromise/revocation.

## 5. Key Custody, Rotation, and Recovery Readiness (`LREL-003`)

- **Current posture:** Production catalog signing keys are **not configured** and no key material exists in Git, CI secrets, or contributor workflows.
- **Pre-launch custody prerequisites:** Before `L3` / `Library 1.0`, maintainers must define authorized signers, protected tag/environment approvals, encrypted offline backup custody, and rehearsed recovery using **nonproduction test keys only**.
- **Trust-root rotation:** Trusted public keys ship inside authenticated AsciiWall application releases or explicit user trust actions — an unsigned or compromised catalog can **never** vouch for its own replacement `key_id`.
- **Release gate:** Library `1.0` (`LQA-L3`) cannot close until all 5 source-kind conformance fixtures (`LQA-004`), compatibility matrix (`LIB-005`), rights/codec reviews (`LLEG-003`), nonproduction key-rotation rehearsal (`LREL-003`), and release candidate BOM (`LREL-004`) hold exercised evidence.
