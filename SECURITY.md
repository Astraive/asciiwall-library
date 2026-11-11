# Security Policy

## Current Status and Supported Targets

`Astraive/asciiwall-library` is currently in a **pre-release foundation phase** (`main`). **No curated wallpaper packages (`.asciiwall`), signed static catalogs (`catalog.json` / `catalog.sig`), media assets, or font bundles have been published yet.**

| Target / Artifact | Supported | Notes |
| --- | --- | --- |
| Curated catalogs & `.asciiwall` releases | None yet | Blocked on pinned engine packer/validator (`LIB-002`, `LIB-003`), catalog tooling (`CAT-001`–`CAT-005`), and signing key custody (`LREL-003`). |
| `main` (policies, docs, CI, scripts) | Active baseline | Foundation policies, documentation, and read-only Python/PowerShell CI checks only. |

Signed catalog key custody is **not configured** yet, and no test signing keys are trusted for production use.

## Reporting a Vulnerability (Private Route Only)

**Do not open a public GitHub issue, pull request, or discussion** for an undisclosed security vulnerability, malicious archive/media fixture trigger, CI privilege escalation, workflow injection flaw, signing-key risk, or compromised artifact report.

Report vulnerabilities privately through:

1. **GitHub Private Vulnerability Reporting (preferred):** submit a draft security advisory at [Astraive/asciiwall-library Security Advisories](https://github.com/Astraive/asciiwall-library/security/advisories/new).
2. **Engine / application runtime vulnerabilities:** defects in the Rust engine, archive extractor, media decoder sandbox, CLI, or desktop hosts should be reported privately to [Astraive/asciiwall Security Advisories](https://github.com/Astraive/asciiwall/security/advisories/new).
3. **Maintainer private fallback:** if GitHub Private Vulnerability Reporting is unavailable, email maintainer `@NeerajCodz` privately at `neerajcodz@gmail.com` before posting any details publicly.

### What to include

- Affected repository (`Astraive/asciiwall-library`), commit SHA (or future catalog sequence / package ID and version), and affected file or workflow
- Minimal **synthetic, rights-cleared** reproduction input (never attach personal media, proprietary fonts, or private host paths)
- Expected vs. observed security boundary behavior and potential impact

## Incident Distinction: Security vs. Rights Takedown vs. Deprecation

`Astraive/asciiwall-library` keeps three operational tracks clearly separated ([docs/licensing-and-review.md](docs/licensing-and-review.md)):

1. **Security Advisory:** dangerous payload, parser-exploit trigger, compromised artifact SHA-256, or supply-chain/CI defect. Handled privately via Security Advisories and published with exact affected package hashes/versions once remediated.
2. **Rights / Provenance Dispute:** copyright, attribution, font redistribution, or subject-consent takedown. Handled via the hash-based takedown workflow ([docs/licensing-and-review.md](docs/licensing-and-review.md#rights-disputes-and-takedown-process)) while keeping private PII proof confidential.
3. **Quality Deprecation / Incompatibility:** visual defects or engine version skew (`LCOM-003`), handled by removing future catalog recommendations without treating an incompatible package as malware.

## Library Security Boundaries

- **Privilege separation in CI:** untrusted PR validation runs secretless with `contents: read` and never executes `pull_request_target` with secrets or production signing keys ([docs/quality-requirements.md](docs/quality-requirements.md)).
- **Data-only packages & pinned origins:** recipes cannot supply arbitrary scripts, plugins, shaders, WebAssembly, or mutable `"latest"` asset URLs ([Astraive/asciiwall plugin policy](https://github.com/Astraive/asciiwall/blob/main/docs/security/plugin-and-shader-policy.md)).
- **Exact-byte catalog signatures:** future static catalogs use detached `ed25519` signatures over `asciiwall-catalog-v1\0` plus exact UTF-8 catalog bytes with monotonic sequences and expiration bounds ([docs/release-process.md](docs/release-process.md)).
- **Offline limitation:** removing or flagging an entry in a future signed catalog cannot automatically revoke cached metadata on an offline device or remotely delete already-installed local artwork without user consent.
