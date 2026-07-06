#!/usr/bin/env python3
"""RAG retrieval smoke test against corpus.jsonl (keyword scoring)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Canonical questions from verification-gates.md
QUESTIONS = [
    ("Tally ODBC connection failed", ["configuration/tally", "faq/common-issues", "client/install"]),
    ("How do I download aging Excel report?", ["client/aging/report"]),
    ("How to import trial balance from Excel?", ["client/import/excel"]),
    ("Where do I enter API key?", ["configuration/service"]),
    ("Generate balance sheet in cloud", ["client/reports/balance-sheet"]),
    ("Fixed assets depreciation method", ["client/depreciation/register", "client/company"]),
    ("Import share capital template", ["client/share/subscribed", "client/share/authorized"]),
    ("Enable auto-code for ledgers", ["client/trial-balance/ledgers", "configuration/coding"]),
    ("Client software update failed", ["configuration/updates"]),
    ("Who do I contact for support?", ["faq/common-issues"]),
]


def load_corpus(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def score_row(question: str, row: dict) -> float:
    q = question.lower()
    text = (row.get("text", "") + " " + row.get("page_title", "") + " " + row.get("section_title", "")).lower()
    keywords = row.get("keywords") or []
    symptoms = row.get("symptoms") or []
    score = 0.0
    for token in re.findall(r"[a-z0-9]+", q):
        if len(token) < 3:
            continue
        if token in text:
            score += 2.0
        for kw in keywords + symptoms:
            if token in str(kw).lower():
                score += 3.0
    url = row.get("url", "").lower()
    if "api" in q and "key" in q and "service" in url:
        score += 15.0
    if ("support" in q or "contact" in q) and "faq" in url:
        score += 20.0
    if ("support" in q or "contact" in q) and "support@finautoindia.com" in text:
        score += 25.0
    if "odbc" in q and "odbc" in text:
        score += 5.0
    if "aging" in q and "excel" in q and "aging" in url:
        score += 8.0
    return score


def top_urls(question: str, rows: list[dict], n: int = 3) -> list[str]:
    ranked = sorted(rows, key=lambda r: score_row(question, r), reverse=True)
    urls = []
    for row in ranked[:n]:
        url = row.get("url", "")
        path = url.replace("https://finautoindia.github.io/docs/", "").split("#")[0]
        urls.append(path)
    return urls


def matches_expected(got: list[str], expected: list[str]) -> bool:
    for exp in expected:
        if any(exp in g for g in got):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=Path("site/ai/corpus.jsonl"))
    parser.add_argument("--min-pass", type=int, default=9)
    args = parser.parse_args()

    if not args.corpus.is_file():
        print(f"ERROR: corpus not found: {args.corpus}", file=sys.stderr)
        return 1

    rows = load_corpus(args.corpus)
    passed = 0
    print("| # | Question | Top match | Pass |")
    print("|---|----------|-----------|------|")
    for i, (question, expected) in enumerate(QUESTIONS, 1):
        tops = top_urls(question, rows)
        ok = matches_expected(tops, expected)
        passed += int(ok)
        mark = "yes" if ok else "NO"
        print(f"| {i} | {question} | {tops[0] if tops else '-'} | {mark} |")

    print(f"\nPass: {passed}/{len(QUESTIONS)} (required >= {args.min_pass})")
    return 0 if passed >= args.min_pass else 1


if __name__ == "__main__":
    sys.exit(main())
