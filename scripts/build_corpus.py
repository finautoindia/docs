#!/usr/bin/env python3
"""Build RAG corpus JSONL from markdown sources (mkdocs on_post_build hook + CLI)."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

BASE_URL = "https://finautoindia.github.io/docs/"
SKIP_H2 = {"Related links", "Related module docs"}
SOURCE_GLOBS = ("client/**/*.md", "configuration/**/*.md", "faq/**/*.md")


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm = yaml.safe_load(text[3:end]) or {}
    return fm, text[end + 3 :].lstrip("\n")


def slugify(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"[\s_]+", "-", s).strip("-")


def inline_image_alt(line: str) -> str:
    match = re.search(r"!\[([^\]]*)\]", line)
    if match and match.group(1).strip():
        return f"[Image: {match.group(1).strip()}]"
    return ""


def markdown_to_plain(section: str) -> str:
    lines: list[str] = []
    for raw in section.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("```"):
            continue
        if line.startswith("!!!"):
            line = re.sub(r"^!!!\s*\w+\s*", "", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\{[^}]+\}", "", line)
        alt = inline_image_alt(raw)
        if alt:
            lines.append(alt)
        elif line:
            lines.append(line)
    return "\n".join(lines).strip()


def split_h2_sections(body: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in body.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                sections.append((current_title, "\n".join(current_lines)))
            current_title = line[3:].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections.append((current_title, "\n".join(current_lines)))
    return sections


def docs_path_for_file(docs_dir: Path, md_path: Path) -> str:
    rel = md_path.relative_to(docs_dir).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    if rel.endswith("/index"):
        rel = rel[:-6]
    return rel + "/"


def build_records(docs_dir: Path) -> list[dict]:
    records: list[dict] = []
    for pattern in SOURCE_GLOBS:
        for md_path in sorted(docs_dir.glob(pattern)):
            if md_path.name == "index.md" and md_path.parent == docs_dir:
                continue
            text = md_path.read_text(encoding="utf-8")
            fm, body = parse_front_matter(text)
            page_title = fm.get("title") or md_path.stem.replace("-", " ").title()
            docs_path = docs_path_for_file(docs_dir, md_path)

            h1 = re.search(r"^# (.+)$", body, re.MULTILINE)
            if h1:
                page_title = h1.group(1).strip()

            for section_title, section_body in split_h2_sections(body):
                if section_title in SKIP_H2:
                    continue
                plain = markdown_to_plain(section_body)
                if not plain:
                    continue
                anchor = slugify(section_title)
                record = {
                    "url": f"{BASE_URL}{docs_path}#{anchor}",
                    "page_title": page_title,
                    "section_title": section_title,
                    "text": plain,
                }
                for key in ("controller", "function", "keywords", "symptoms", "client_version"):
                    if key in fm and fm[key]:
                        record[key] = fm[key]
                records.append(record)
    return records


def write_corpus(site_dir: Path, records: list[dict]) -> Path:
    out_dir = site_dir / "ai"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "corpus.jsonl"
    with out_path.open("w", encoding="utf-8") as fh:
        for row in records:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return out_path


def copy_llms_txt(docs_dir: Path, site_dir: Path) -> None:
    src = docs_dir / "llms.txt"
    if src.is_file():
        shutil.copy2(src, site_dir / "llms.txt")


def build_corpus(docs_dir: Path, site_dir: Path) -> int:
    records = build_records(docs_dir)
    out_path = write_corpus(site_dir, records)
    copy_llms_txt(docs_dir, site_dir)
    print(f"OK: wrote {len(records)} corpus chunks to {out_path}")
    return len(records)


def on_post_build(config, **kwargs) -> None:
    docs_dir = Path(config.docs_dir)
    site_dir = Path(config.site_dir)
    build_corpus(docs_dir, site_dir)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    args = parser.parse_args()
    if not args.site_dir.is_dir():
        print(f"ERROR: site dir not found: {args.site_dir}", file=sys.stderr)
        return 1
    build_corpus(args.docs_dir, args.site_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
