#!/usr/bin/env python3
"""Validate site/ai/corpus.jsonl for metadata, PII, and escalation content."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PAN_RE = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")
GSTIN_RE = re.compile(r"\b[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9A-Z]Z[0-9A-Z]\b")
API_KEY_RE = re.compile(r"api[_-]?key\s*[:=]\s*\S+", re.I)

IN_SCOPE_WITH_CONTROLLER = 36  # help-urls.json in-scope actions


def load_rows(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=Path("site/ai/corpus.jsonl"))
    parser.add_argument("--min-chunks", type=int, default=80)
    args = parser.parse_args()

    if not args.corpus.is_file():
        print(f"ERROR: corpus not found: {args.corpus}", file=sys.stderr)
        return 1

    rows = load_rows(args.corpus)
    errors: list[str] = []

    if len(rows) < args.min_chunks:
        errors.append(f"Row count {len(rows)} < minimum {args.min_chunks}")

    controller_rows = [r for r in rows if r.get("controller")]
    for row in controller_rows:
        if not row.get("function"):
            errors.append(f"Missing function for controller chunk: {row.get('url')}")

    for row in rows:
        text = row.get("text", "")
        if PAN_RE.search(text):
            errors.append(f"Possible PAN in corpus: {row.get('url')}")
        if GSTIN_RE.search(text):
            errors.append(f"Possible GSTIN in corpus: {row.get('url')}")
        if API_KEY_RE.search(text):
            errors.append(f"Possible API key pattern in corpus: {row.get('url')}")

    faq_rows = [r for r in rows if "/faq/" in r.get("url", "")]
    escalation_ok = any(
        "support@finautoindia.com" in r.get("text", "")
        and "do not" in r.get("text", "").lower()
        for r in faq_rows
    )
    if not escalation_ok:
        errors.append("FAQ corpus missing escalation email + credential warning")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(
        f"OK: validated {len(rows)} corpus rows "
        f"({len(controller_rows)} with controller metadata)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
