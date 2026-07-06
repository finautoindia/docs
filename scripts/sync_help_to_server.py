#!/usr/bin/env python3
"""Upsert server finauto_help rows from docs/reference/help-urls.json."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import urljoin


def load_entries(map_path: Path) -> tuple[str, list[dict]]:
    data = json.loads(map_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return "https://finautoindia.github.io/docs/", data
    base_url = data.get("base_url", "https://finautoindia.github.io/docs/")
    return base_url, data.get("entries", [])


def resolve_url(base_url: str, docs_path: str) -> str:
    return urljoin(base_url.rstrip("/") + "/", docs_path.lstrip("/"))


def sql_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "''")


def build_upsert_sql(controller: str, function: str, url: str) -> list[str]:
    c = sql_escape(controller)
    f = sql_escape(function)
    u = sql_escape(url)
    update = (
        f"UPDATE finauto_help SET url = '{u}' "
        f"WHERE controller = '{c}' AND cfunction = '{f}';"
    )
    insert = (
        "INSERT INTO finauto_help (controller, cfunction, url) "
        f"SELECT '{c}', '{f}', '{u}' FROM DUAL "
        f"WHERE NOT EXISTS (SELECT 1 FROM finauto_help "
        f"WHERE controller = '{c}' AND cfunction = '{f}');"
    )
    return [update, insert]


def execute_mysql(host: str, user: str, password: str, database: str, port: int, statements: list[str]) -> None:
    try:
        import pymysql
    except ImportError as exc:
        raise SystemExit("pymysql required for --execute (pip install pymysql)") from exc

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        charset="utf8mb4",
    )
    try:
        with conn.cursor() as cur:
            for stmt in statements:
                cur.execute(stmt)
        conn.commit()
    finally:
        conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", type=Path, default=Path("docs/reference/help-urls.json"))
    parser.add_argument("--base-url", help="Override base_url from map file")
    parser.add_argument("--sql", action="store_true", help="Print MySQL upsert statements")
    parser.add_argument("--execute", action="store_true", help="Run upserts via pymysql (requires DB env vars)")
    parser.add_argument("--dry-run", action="store_true", help="With --execute, only print planned changes")
    args = parser.parse_args()

    if not args.map.is_file():
        print(f"ERROR: map not found: {args.map}", file=sys.stderr)
        return 1

    base_url, entries = load_entries(args.map)
    if args.base_url:
        base_url = args.base_url

    rows: list[tuple[str, str, str]] = []
    for entry in entries:
        if entry.get("in_scope_v1") is False:
            continue
        controller = entry.get("controller", "")
        function = entry.get("function", "")
        docs_path = entry.get("docs_path", "")
        if not controller or not function or not docs_path:
            print(f"ERROR: incomplete entry: {entry}", file=sys.stderr)
            return 1
        rows.append((controller, function, resolve_url(base_url, docs_path)))

    statements: list[str] = []
    for c, f, u in rows:
        statements.extend(build_upsert_sql(c, f, u))

    if args.sql or (not args.execute):
        print("-- finauto_help upserts from help-urls.json")
        for stmt in statements:
            print(stmt)
        print(f"-- total: {len(statements)} rows")

    if args.execute:
        if args.dry_run:
            print(f"DRY RUN: would upsert {len(rows)} rows", file=sys.stderr)
            return 0
        host = os.environ.get("FINAUTO_DB_HOST", "127.0.0.1")
        user = os.environ.get("FINAUTO_DB_USER")
        password = os.environ.get("FINAUTO_DB_PASSWORD", "")
        database = os.environ.get("FINAUTO_DB_NAME", "finauto")
        port = int(os.environ.get("FINAUTO_DB_PORT", "3306"))
        if not user:
            print("ERROR: set FINAUTO_DB_USER (and FINAUTO_DB_PASSWORD) for --execute", file=sys.stderr)
            return 1
        execute_mysql(host, user, password, database, port, statements)
        print(f"OK: upserted {len(rows)} finauto_help rows")

    if not args.sql and not args.execute:
        print("Hint: use --sql to print statements or --execute to apply", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
