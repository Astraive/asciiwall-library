#!/usr/bin/env python3
"""Read-only standard-library checks for Astraive/asciiwall-library.

Runs standalone on a fresh clone with zero sibling-repository imports and zero
dependency on external ../.issues planning files.
"""
from __future__ import annotations

from collections import Counter
import html
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "__pycache__", "target"}
FORBIDDEN_FILES = {
    "publication-ledger.json",
    "publication-ledger.lock",
    "backlog-audit.json",
    "backlog-creation-ledger.json",
    "backlog-dependency-graph.md",
    "backlog-inventory.md",
    "backlog-requirement-traceability.md",
    "issue.json",
}
ART_INPUT_DIRS = ("wallpapers", "collections", "catalog", "packages")
ART_EXTENSIONS = {".asciiwall", ".ascii-clip"}
REQUIRED_PIPELINE_PREREQS = (
    ("schemas/engine-schema-lock.json", "LIB-002 / PKG-001 (pinned engine packer & schema digests)"),
    ("scripts/resolve-assets.py", "LIB-004 (digest-pinned asset lock verification)"),
    ("scripts/check-attribution.py", "LLEG-002 (per-asset rights & attribution ledger validator)"),
    ("scripts/build-library.py", "LIB-003 / CLI-001 / PKG-010 (pinned engine package build & validate)"),
    ("scripts/validate-catalog.py", "CAT-002 (bounded static catalog semantic validation)"),
)
LF_REQUIRED_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".ps1", ".sh"}
LF_REQUIRED_NAMES = {".editorconfig", ".gitattributes", ".gitignore", "CODEOWNERS", "pre-commit", "commit-msg"}

LINK = re.compile(r"(?<!!)\[[^\]\n]*(?:\][^\]\n]*)?\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
KEBAB_MD = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
USES_LINE = re.compile(r"^\s*(?:-\s*)?uses\s*:\s*([^\s#]+)")
SHA_PIN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*@[0-9a-f]{40}$")
UNSAFE_EXPR = re.compile(
    r"\$\{\{\s*github\.(?:event\.(?:pull_request\.(?:title|body)|issue\.(?:title|body)|comment\.body|commits\[\d+\]\.message)|head_ref)\s*\}\}"
)
EXTERNAL_ISSUES_URL = re.compile(
    r"https?://github\.com/Astraive/asciiwall(?:-library)?/(?:blob|tree)/[^/\s)]+/\.issues(?:/|$)",
    re.IGNORECASE,
)


def unfenced(text: str) -> str:
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            lines.append("")
        elif match:
            fence = match[1]
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def headings(text: str) -> list[tuple[int, str, int]]:
    lines = unfenced(text).splitlines()
    result: list[tuple[int, str, int]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if match:
            result.append((len(match[1]), match[2], index))
        elif index and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) and lines[index - 1].strip():
            result.append((1 if "=" in line else 2, lines[index - 1].strip(), index - 1))
    return result


def anchors(text: str) -> set[str]:
    counts: Counter[str] = Counter()
    found: set[str] = set()
    for _, heading, _ in headings(text):
        normalized = html.unescape(re.sub(r"<[^>]+>", "", heading)).lower().replace(" ", "-")
        base = re.sub(r"[^\w\-]", "", normalized)
        suffix = "" if not counts[base] else f"-{counts[base]}"
        found.add(base + suffix)
        counts[base] += 1
    return found


def no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def repository_files() -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []
    for directory, dirs, names in os.walk(ROOT, followlinks=False):
        current = Path(directory)
        for name in dirs:
            path = current / name
            relative = path.relative_to(ROOT).as_posix()
            if name == ".issues":
                errors.append(f"{relative}: external backlog directory must stay outside the repository")
            elif path.is_symlink() and name not in EXCLUDED_DIRS:
                errors.append(f"{relative}: symlinked repository directories are not allowed")
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS and name != ".issues" and not (current / name).is_symlink())
        for name in sorted(names):
            path = current / name
            relative = path.relative_to(ROOT).as_posix()
            if name in FORBIDDEN_FILES:
                errors.append(f"{relative}: forbidden external backlog artifact; keep it outside the repository")
            if path.is_symlink():
                errors.append(f"{relative}: symlinked repository files are not checked or allowed")
                continue
            if path.is_file():
                files.append(path)
    return files, errors


def check_text_encoding_and_lf(path: Path, relative: str, errors: list[str]) -> str | None:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        errors.append(f"{relative}: cannot read file ({exc})")
        return None
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append(f"{relative}: UTF-8 BOM is disallowed; use UTF-8 without BOM")
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        errors.append(f"{relative}: invalid UTF-8 ({exc})")
        return None
    if path.suffix.lower() in LF_REQUIRED_SUFFIXES or path.name in LF_REQUIRED_NAMES or ".githooks" in path.relative_to(ROOT).parts:
        if b"\r\n" in raw:
            errors.append(f"{relative}: CRLF line endings found; repository policy requires LF")
    return text


def without_inline_code(text: str) -> str:
    """Mask CommonMark backtick spans without changing link offsets or newlines."""
    runs = list(re.finditer(r"`+", text))
    masked = list(text)
    index = 0
    while index < len(runs):
        opening = runs[index]
        start, width = opening.start(), len(opening[0])
        previous = start - 1
        while previous >= 0 and text[previous] == "\\":
            previous -= 1
        if (start - previous - 1) % 2:
            start += 1
            width -= 1
        if width:
            closing = next(
                (candidate for candidate in range(index + 1, len(runs))
                 if len(runs[candidate][0]) == width),
                None,
            )
            if closing is not None:
                for position in range(start, runs[closing].end()):
                    if masked[position] != "\n":
                        masked[position] = " "
                index = closing + 1
                continue
        index += 1
    return "".join(masked)


def check_markdown(path: Path, relative: str, text: str, errors: list[str]) -> None:
    rel_parts = path.relative_to(ROOT).parts
    if rel_parts[0] == "docs":
        for part in rel_parts[1:-1]:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", part):
                errors.append(f"{relative}: docs subdirectory {part!r} must be lowercase kebab-case")
        if not KEBAB_MD.fullmatch(path.name):
            errors.append(f"{relative}: docs Markdown filename must be lowercase kebab-case")

    lines = text.splitlines()
    fence: tuple[str, int] | None = None
    for line in lines:
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is None:
            if match:
                fence = (match[1][0], len(match[1]))
        elif match and match[1][0] == fence[0] and len(match[1]) >= fence[1] and not match[2].strip():
            fence = None
    if fence is not None:
        errors.append(f"{relative}:{len(lines)}: unclosed Markdown code fence")

    body = without_inline_code(unfenced(text))
    if EXTERNAL_ISSUES_URL.search(body):
        errors.append(f"{relative}: links to external .issues as a GitHub URL; .issues stays outside Git")

    source_anchors = anchors(text)
    for link in LINK.finditer(body):
        raw_target = link.group(1).strip().strip("<>")
        parsed = urlsplit(raw_target)
        if parsed.scheme or parsed.netloc or raw_target.startswith("//"):
            continue
        if not parsed.path and not parsed.fragment:
            continue
        target_text = unquote(parsed.path)
        target = (path.parent / target_text).resolve() if target_text else path.resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{relative}: local link escapes repository: {raw_target}")
            continue
        if not target.exists() or not target.is_file():
            errors.append(f"{relative}: local link target does not exist: {raw_target}")
            continue
        if parsed.fragment:
            if target.suffix.lower() != ".md":
                errors.append(f"{relative}: fragment links are supported only for Markdown targets: {raw_target}")
                continue
            try:
                target_content = target.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{target.relative_to(ROOT).as_posix()}: cannot read UTF-8 Markdown ({exc})")
                continue
            target_anchors = source_anchors if target == path.resolve() else anchors(target_content)
            if unquote(parsed.fragment) not in target_anchors:
                errors.append(f"{relative}: fragment #{parsed.fragment} not found in {target.relative_to(ROOT).as_posix()}")


def check_yaml_and_workflow(relative: str, text: str, errors: list[str]) -> None:
    for line_no, line in enumerate(text.splitlines(), 1):
        if "\t" in line:
            errors.append(f"{relative}:{line_no}: YAML files must use spaces, not tabs")
    if not relative.startswith(".github/workflows/"):
        return

    stripped_lines = [line.split("#", 1)[0] for line in text.splitlines()]
    uncommented = "\n".join(stripped_lines)
    if re.search(r"(?m)^\s*pull_request_target\s*:", uncommented):
        errors.append(f"{relative}: pull_request_target is forbidden for untrusted library PR workflows")
    if not re.search(r"(?m)^\s*permissions\s*:", uncommented):
        errors.append(f"{relative}: workflow must declare least-privilege permissions")
    if re.search(r"(?m)^\s*permissions\s*:\s*write-all\b", uncommented):
        errors.append(f"{relative}: write-all workflow permissions are forbidden")
    for forbidden_perm in ("contents", "packages", "id-token", "actions", "deployments", "issues", "pull-requests"):
        if re.search(rf"(?m)^\s*{forbidden_perm}\s*:\s*write\b", uncommented):
            errors.append(f"{relative}: {forbidden_perm}: write is not permitted in unprivileged CI workflows")
    if not re.search(r"(?m)^\s*timeout-minutes\s*:", uncommented):
        errors.append(f"{relative}: workflow jobs must define timeout-minutes")

    in_run = False
    run_indent = 0
    for line_no, line in enumerate(stripped_lines, 1):
        if in_run:
            if line.strip() and (len(line) - len(line.lstrip(" "))) <= run_indent:
                in_run = False
            elif UNSAFE_EXPR.search(line):
                errors.append(f"{relative}:{line_no}: pass untrusted GitHub event fields via env:, never inline in run:")
                continue
            else:
                continue
        uses_match = USES_LINE.match(line)
        if uses_match:
            action_ref = uses_match.group(1).strip().strip("\"'")
            if not action_ref.startswith("./") and not SHA_PIN.fullmatch(action_ref):
                errors.append(f"{relative}:{line_no}: action {action_ref!r} must be pinned to a 40-hex commit SHA")
        run_match = re.match(r"^(\s*)(?:-\s+)?run\s*:(.*)$", line)
        if run_match:
            inline = run_match.group(2).strip()
            if inline in ("|", "|-", "|+", ">", ">-", ">+"):
                in_run = True
                run_indent = len(run_match.group(1)) + (2 if re.match(r"^\s*-\s+run\b", line) else 0)
            elif UNSAFE_EXPR.search(inline):
                errors.append(f"{relative}:{line_no}: pass untrusted GitHub event fields via env:, never inline in run:")


def check_art_gate_fail_closed(files: list[Path], errors: list[str]) -> None:
    art_inputs: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT)
        if rel.parts[0] in ART_INPUT_DIRS or path.suffix.lower() in ART_EXTENSIONS:
            art_inputs.append(rel.as_posix())
    if not art_inputs:
        return

    missing = [
        f"{rel_path} ({ticket_desc})"
        for rel_path, ticket_desc in REQUIRED_PIPELINE_PREREQS
        if not (ROOT / rel_path).is_file()
    ]

    sample = ", ".join(art_inputs[:5])
    suffix = f" (+{len(art_inputs) - 5} more)" if len(art_inputs) > 5 else ""
    details = "; ".join(missing) if missing else "prerequisite-shaped files exist, but this foundation does not execute approved artifact validators"
    errors.append(
        f"art/package/catalog input(s) present [{sample}{suffix}] cannot be accepted before the L1 pipeline is implemented and invoked (fail-closed): "
        f"{details}. File presence alone is not verification."
    )


def main() -> int:
    files, errors = repository_files()
    markdown_files: list[Path] = []
    json_files: list[Path] = []
    yaml_files: list[Path] = []

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        suffix = path.suffix.lower()
        is_text = (
            suffix in LF_REQUIRED_SUFFIXES
            or path.name in LF_REQUIRED_NAMES
            or ".githooks" in path.relative_to(ROOT).parts
        )
        if not is_text:
            continue
        text = check_text_encoding_and_lf(path, relative, errors)
        if text is None:
            continue
        if suffix == ".md":
            markdown_files.append(path)
            check_markdown(path, relative, text, errors)
        elif suffix == ".json":
            json_files.append(path)
            try:
                json.loads(text, object_pairs_hook=no_duplicate_keys)
            except (json.JSONDecodeError, ValueError) as exc:
                errors.append(f"{relative}: invalid strict UTF-8 JSON ({exc})")
        elif suffix in {".yml", ".yaml"}:
            yaml_files.append(path)
            check_yaml_and_workflow(relative, text, errors)

    check_art_gate_fail_closed(files, errors)

    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print(f"FAIL: repository checks found {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"PASS: checked {len(markdown_files)} Markdown, {len(yaml_files)} YAML, and {len(json_files)} JSON file(s); "
        "no external backlog artifacts or unvalidated art inputs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
