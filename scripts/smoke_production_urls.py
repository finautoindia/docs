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
    "client/company/",
]


def check_url(path: str) -> tuple[bool, int]:
    candidates = [path]
    if path.endswith("/index/"):
        candidates.insert(0, path.replace("/index/", "/"))
    last_status = 0
    for candidate in candidates:
        url = BASE + candidate
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=15) as resp:
                if 200 <= resp.status < 400:
                    return True, resp.status
        except urllib.error.HTTPError as exc:
            last_status = exc.code
        except Exception:
            last_status = 0
    return False, last_status


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
