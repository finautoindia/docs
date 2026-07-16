#!/usr/bin/env python3
"""Validate help-urls.json against built MkDocs site and in-scope controller actions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# In-scope v1 controller actions (excludes external DB per FR-H04)
IN_SCOPE_ACTIONS = {
    ("company", "index"),
    ("company", "branches"),
    ("company", "fyear"),
    ("company", "export"),
    ("import", "index"),
    ("excel", "import_excel"),
    ("excel", "import_data"),
    ("other", "import_excel"),
    ("tally", "import_data"),
    ("tally", "resolve_conflict"),
    ("ledger", "index"),
    ("stock", "index"),
    ("aging", "index"),
    ("aging", "vouchers"),
    ("aging", "payables"),
    ("aging", "receivables"),
    ("aging", "report"),
    ("depreciation", "index"),
    ("depreciation", "fixed_assets"),
    ("depreciation", "asset_shifts"),
    ("depreciation", "depreciation"),
    ("depreciation", "by_asset"),
    ("share", "index"),
    ("share", "capital_authorized"),
    ("share", "capital_issued"),
    ("share", "capital_buyback"),
    ("share", "holders"),
    ("share", "capital_subscribed"),
    ("share", "capital_payments"),
    ("share", "transfer_logs"),
    ("share", "share_holding_view"),
    ("share", "holder_fy"),
    ("reports", "index"),
    ("reports", "customize"),
    ("balance_sheet", "index"),
    ("default", "index"),
    ("default", "update"),
    ("ca", "profile"),
    ("settings", "service"),
    ("settings", "coding"),
    ("settings", "cache"),
    ("settings", "tally"),
}


def load_map(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    return data.get("entries", [])


def site_has_path(site_dir: Path, docs_path: str) -> bool:
    parts = [p for p in docs_path.strip("/").split("/") if p]
    index_html = site_dir.joinpath(*parts, "index.html")
    flat_html = site_dir.joinpath(*parts[:-1], f"{parts[-1]}.html") if parts else site_dir
    return index_html.is_file() or flat_html.is_file()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", type=Path, default=Path("docs/reference/help-urls.json"))
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--partial", action="store_true", help="Validate only entries present in map")
    mode.add_argument("--strict", action="store_true", help="Require all in-scope actions mapped with live paths")
    args = parser.parse_args()
    strict = args.strict or not args.partial

    entries = load_map(args.map)
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()

    for row in entries:
        if row.get("in_scope_v1") is False:
            continue
        controller = row.get("controller", "")
        function = row.get("function", "")
        key = (controller, function)
        if key in seen:
            errors.append(f"Duplicate help map entry: {controller}-{function}")
        seen.add(key)
        docs_path = row.get("docs_path", "")
        if not docs_path:
            errors.append(f"Missing docs_path for {controller}-{function}")
            continue
        if not site_has_path(args.site_dir, docs_path):
            errors.append(f"Built site missing path for {controller}-{function}: {docs_path}")

    if strict:
        for key in IN_SCOPE_ACTIONS:
            if key not in seen:
                errors.append(f"Missing in-scope help map entry: {key[0]}-{key[1]}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(seen)} help map entries ({'strict' if strict else 'partial'} mode)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
