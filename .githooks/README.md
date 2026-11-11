# Opt-In Local Git Hooks

This directory contains lightweight, read-only local Git hooks for `Astraive/asciiwall-library`:

- `pre-commit` — runs `python scripts/check-repository.py` and `pwsh -NoProfile -File scripts/check-powershell.ps1`.
- `commit-msg` — runs `python scripts/check-conventions.py --message-file <path>` to enforce Conventional Commits with a stable ticket ID (`type(scope): subject [TICKET-ID]`) and reject `Co-authored-by:` trailers case-insensitively.

## Guarantees

- **Opt-in only:** hooks are never installed automatically or silently on clone.
- **Repository-local only:** `.githooks/install.ps1` configures only `git config --local core.hooksPath .githooks`.
- **No identity tampering:** never modifies global Git configuration, `user.name`, `user.email`, or signing settings; contributors retain their own commit identity.
- **No silent rewriting or autofix:** hooks reject invalid content with actionable diagnostics instead of editing commit messages, staging files, or rewriting history.

## Prerequisites

- **Git** (with Git Bash / `sh` on Windows)
- **Python 3.12+** (`python3` or `python` on `PATH`)
- **PowerShell 7** (`pwsh` on `PATH`)

## Installation

Run from the repository root:

```powershell
pwsh -NoProfile -File .githooks/install.ps1
```

Or configure manually without PowerShell:

```sh
git config --local core.hooksPath .githooks
```

On Linux or macOS, ensure both hook scripts have executable permissions (`chmod +x .githooks/pre-commit .githooks/commit-msg`) if not already set in your checkout.

## Inspect or Uninstall

Check current local hook configuration:

```powershell
pwsh -NoProfile -File .githooks/install.ps1 -Status
```

Remove `.githooks` from local configuration:

```powershell
pwsh -NoProfile -File .githooks/install.ps1 -Uninstall
```

For full commit, PR, and repository verification rules, see [CONTRIBUTING.md](../CONTRIBUTING.md), [docs/development-plan.md](../docs/development-plan.md), and [docs/quality-requirements.md](../docs/quality-requirements.md).
