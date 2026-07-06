#!/usr/bin/env python3
"""Fail if legacy inline colors or emoji appear in markdown headings."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LEGACY_COLORS = ("#0073e6", "#e67e22", "#0073E6", "#E67E22")
EMOJI_IN_HEADING = re.compile(
    r"^#{1,6}\s*[^\w\s<].*",
    re.MULTILINE,
)
# Rough emoji / symbol prefix in headings (non-ASCII or common emoji blocks)
EMOJI_PREFIX = re.compile(
    r"^#{1,6}\s*[\U0001F300-\U0001FAFF\U00002600-\U000027BF]",
    re.MULTILINE,
)


def scan_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    for color in LEGACY_COLORS:
        if color.lower() in text.lower():
            issues.append(f"{path}: contains legacy color {color}")
    for match in EMOJI_PREFIX.finditer(text):
        line = text[: match.start()].count("\n") + 1
        issues.append(f"{path}:{line}: heading uses emoji (use Bootstrap Icons instead)")
    if "<h2 style=" in text or "<h3 style=" in text:
        issues.append(f"{path}: contains inline-styled HTML headings")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    args = parser.parse_args()
    errors: list[str] = []
    for md in sorted(args.docs_dir.rglob("*.md")):
        errors.extend(scan_file(md))
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print(f"OK: no legacy styles in {args.docs_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
