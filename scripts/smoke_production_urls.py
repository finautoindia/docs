#!/usr/bin/env python3
"""Verify production GitHub Pages URLs for contextual help matrix (T090)."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request

BASE = "https://finautoindia.github.io/docs/"
PATHS = [
    "client/aging/report/",
    "client/import/tally/",
    "client/trial-balance/ledgers/",
    "configuration/service/",
    "client/company/index/",
]


def check_url(path: str) -> tuple[bool, int]:
    url = BASE + path
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return 200 <= resp.status < 400, resp.status
    except urllib.error.HTTPError as exc:
        return False, exc.code
    except Exception:
        return False, 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    errors = []
    print("| docs_path | HTTP | Pass |")
    print("|-----------|------|------|")
    for path in PATHS:
        ok, status = check_url(path)
        print(f"| {path} | {status} | {'yes' if ok else 'NO'} |")
        if not ok:
            errors.append(path)
    if errors:
        print(f"\nFAIL: {len(errors)} URLs not reachable", file=sys.stderr)
        return 1
    print(f"\nOK: all {len(PATHS)} production URLs reachable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
