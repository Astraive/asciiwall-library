<!--
Default pull request template for metadata, policies, pipeline scripts, CI, schemas, and docs.
For wallpaper recipe / artwork submissions, open the PR with `?template=art.md` instead.
PR title format: type(scope): subject [TICKET-ID], for example "docs(library): clarify catalog schema limits [CAT-001]".
No Co-authored-by trailers are permitted anywhere in commits or PR descriptions.
-->

**Ticket:** <!-- Stable ticket ID (e.g. LIB-001, CAT-001, LQA-001, LREL-001) and `Refs #N` / `Closes #N` once published; omit `#N` if unpublished. -->

## What and why

<!-- What changes, why, and which docs/package/library contracts it satisfies. -->

## Change scope

- [ ] Root policies, governance, or community documentation (`README.md`, `CONTRIBUTING.md`, `docs/`)
- [ ] Validation, asset-resolution, attribution, or catalog scripts (`scripts/`)
- [ ] CI workflows, Dependabot, or GitHub templates (`.github/`)
- [ ] Pinned engine/schema lock or catalog/collection schemas (`schemas/`, `collections/`)

## Pipeline, trust, and rights boundary checklist

- [ ] No runtime backend, hosted API, user account, or forked AsciiWall engine code introduced.
- [ ] Untrusted PR validation remains secretless and never uses `pull_request_target` or unpinned actions.
- [ ] Engine/schema pin updates (if any) come from reviewed upstream releases only, never PR-selected branches.
- [ ] No unverified placeholder packages, invented catalog releases, fabricated benchmark badges, or skipped-green gates.
- [ ] No external `.issues/` backlog records, coverage registers, ledgers, or generated reports included.

## Acceptance criteria

<!-- Copy or reference the ticket's acceptance criteria and record exact evidence or explicitly blocked prerequisites. -->

- [ ]

## Test evidence

<!-- Exact commands run (e.g. `python scripts/check-repository.py`, `pwsh -NoProfile -File scripts/check-powershell.ps1`) and observed output. -->

## Checklist

- [ ] All local links and heading fragments resolve cleanly (`python scripts/check-repository.py`).
- [ ] No secrets, tokens, personal data, or unredacted private host paths included.
- [ ] No `Co-authored-by` trailers in commits or PR description.
- [ ] Documentation affected by this change is updated in the same PR.
