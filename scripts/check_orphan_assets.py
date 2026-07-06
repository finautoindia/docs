#!/usr/bin/env python3
"""Fail if assets under docs/assets/ are not referenced by any markdown file."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    args = parser.parse_args()
    assets_dir = args.docs_dir / "assets"
    if not assets_dir.is_dir():
        print("OK: no assets directory")
        return 0

    md_text = ""
    for md in args.docs_dir.rglob("*.md"):
        md_text += md.read_text(encoding="utf-8") + "\n"
    mkdocs_yml = args.docs_dir.parent / "mkdocs.yml"
    if mkdocs_yml.is_file():
        md_text += mkdocs_yml.read_text(encoding="utf-8") + "\n"

    orphans: list[str] = []
    for asset in assets_dir.rglob("*"):
        if not asset.is_file():
            continue
        if asset.name == ".gitkeep":
            continue
        rel = asset.relative_to(args.docs_dir).as_posix()
        if rel not in md_text and asset.name not in md_text:
            orphans.append(rel)

    if orphans:
        for path in sorted(orphans):
            print(f"ERROR: unreferenced asset: {path}", file=sys.stderr)
        return 1

    print("OK: all assets referenced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
