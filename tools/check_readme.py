#!/usr/bin/env python3
"""Lint the profile README: balanced code fences, complete table rows, no placeholders.

Runs in CI on every push. No network access, so the result cannot flake.

Exit codes: 0 — clean; 2 — bad arguments; 4 — problems found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NOT_PLACEHOLDER = ("[YOUR", "TODO", "TBD", "Lorem ipsum")


def check(text: str) -> list[str]:
    problems: list[str] = []
    if text.count("```") % 2:
        problems.append("unbalanced code fences (odd number of ```)")
    for token in NOT_PLACEHOLDER:
        if token in text:
            problems.append(f"placeholder text left in README: {token}")

    rows = [line for line in text.splitlines() if line.startswith("| [")]
    if not rows:
        problems.append("no project rows found: every project must be a table row")
    for line in rows:
        cells = [cell for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3:
            problems.append(f"project row has {len(cells)} cells, expected 3: {line[:60]}")
        if "http" not in line:
            problems.append(f"project row without a link: {line[:60]}")

    if len(re.findall(r"^## ", text, re.M)) < 3:
        problems.append("expected at least three sections (cases, projects, stack)")
    return problems


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    path = Path(argv[0] if argv else "README.md")
    if not path.exists():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2
    problems = check(path.read_text(encoding="utf-8"))
    if problems:
        for problem in problems:
            print("FAIL:", problem)
        return 4
    print(f"OK: {path} — fences balanced, project rows complete, no placeholders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
