#!/usr/bin/env python3
"""Contextual help smoke matrix — validates built docs paths and optional server API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

MATRIX = [
    ("Aging - Report", "aging", "report", "client/aging/report/"),
    ("Import - From Tally", "tally", "import_data", "client/import/tally/"),
    ("Trial Balance - Ledgers", "ledger", "index", "client/trial-balance/ledgers/"),
    ("Configuration - Service", "settings", "service", "configuration/service/"),
    ("Company (grid)", "company", "index", "client/company/index/"),
]

BASE_URL = "https://finautoindia.github.io/docs/"


def site_has_path(site_dir: Path, docs_path: str) -> bool:
    rel = docs_path.strip("/").replace("/", os.sep)
    index_html = site_dir / rel / "index.html"
    flat_html = site_dir / f"{rel}.html"
    return index_html.is_file() or flat_html.is_file()


def fetch_help_api(api_base: str, help_id: str) -> tuple[int, str]:
    url = f"{api_base.rstrip('/')}/finauto/default/api/help/{help_id}.json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return resp.status, body.get("url", "")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:
        return 0, ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--map", type=Path, default=Path("docs/reference/help-urls.json"))
    parser.add_argument("--api-base", help="e.g. http://127.0.0.1:8000 — optional server help API test")
    args = parser.parse_args()

    entries = json.loads(args.map.read_text(encoding="utf-8"))
    if isinstance(entries, dict):
        entries = entries.get("entries", [])

    lookup = {(e["controller"], e["function"]): e["docs_path"] for e in entries}
    errors: list[str] = []
    rows: list[str] = []

    print("| Menu path | help id | Expected docs_path | Site | Map | API |")
    print("|-----------|---------|-------------------|------|-----|-----|")

    for label, controller, function, expected_path in MATRIX:
        help_id = f"{controller}-{function}"
        map_path = lookup.get((controller, function), "")
        site_ok = site_has_path(args.site_dir, expected_path)
        map_ok = map_path == expected_path
        api_ok = "n/a"
        if args.api_base:
            status, url = fetch_help_api(args.api_base, help_id)
            api_ok = "yes" if expected_path.rstrip("/") in url else f"no ({url or status})"

        if not site_ok:
            errors.append(f"Site missing: {expected_path}")
        if not map_ok:
            errors.append(f"Map mismatch for {help_id}: {map_path}")

        rows.append(
            f"| {label} | {help_id} | {expected_path} | "
            f"{'yes' if site_ok else 'NO'} | {'yes' if map_ok else 'NO'} | {api_ok} |"
        )

    for row in rows:
        print(row)

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"\nOK: help smoke matrix passed ({len(MATRIX)} screens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
