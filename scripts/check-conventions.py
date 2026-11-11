#!/usr/bin/env python3
"""Check a proposed commit message or pull-request title without editing history."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys

TYPE = r"(?:feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)"
TITLE = re.compile(rf"^{TYPE}\([a-z0-9][a-z0-9-]*\): [^\s].* \[[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\]$")
COAUTHOR = re.compile(r"^\s*co-authored-by\s*:", re.IGNORECASE)


def validate_coauthor(text: str) -> list[str]:
    errors: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        if COAUTHOR.match(line):
            errors.append(f"line {number}: Co-authored-by trailers are not permitted")
    return errors


def validate(message: str) -> list[str]:
    errors: list[str] = []
    lines = message.splitlines()
    if not lines or not lines[0].strip():
        errors.append("message is empty; add a Conventional Commit subject")
    elif not TITLE.fullmatch(lines[0]):
        errors.append(
            "subject must match `type(scope): subject [TICKET-ID]` "
            "(type: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert; "
            "lowercase kebab-case scope required; ticket like [LIB-001] or [LIB-ROADMAP-001])"
        )
    errors.extend(validate_coauthor(message))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--message-file", type=Path, help="commit message file; only the first line is the subject")
    source.add_argument("--title", help="pull-request title")
    source.add_argument(
        "--coauthor-check-env",
        metavar="ENV_VAR",
        help="environment variable containing text (such as PR body or commit bodies) to scan for Co-authored-by trailers",
    )
    args = parser.parse_args()

    if args.coauthor_check_env is not None:
        if args.coauthor_check_env not in os.environ:
            parser.error(f"environment variable {args.coauthor_check_env} is not defined")
        text = os.environ[args.coauthor_check_env]
        errors = validate_coauthor(text)
        if errors:
            for error in errors:
                print(f"ERROR {error}", file=sys.stderr)
            return 1
        print(f"PASS: no Co-authored-by trailer found in {args.coauthor_check_env}.")
        return 0

    if args.title is not None:
        message = args.title
    else:
        try:
            message = args.message_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"ERROR cannot read commit message file {args.message_file}: {exc}", file=sys.stderr)
            return 2

    errors = validate(message)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print("Expected: type(scope): concise subject [TICKET-ID]", file=sys.stderr)
        return 1
    print("PASS: commit/PR convention is valid; no Co-authored-by trailer found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
