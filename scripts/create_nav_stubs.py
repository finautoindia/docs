#!/usr/bin/env python3
"""Create placeholder articles for nav targets that do not exist yet."""
from pathlib import Path

STUBS = {
    "docs/client/company/index.md": "Manage Companies",
    "docs/client/company/branches.md": "Branches",
    "docs/client/company/fyear.md": "Financial Years",
    "docs/client/company/export.md": "Export",
    "docs/client/import/excel.md": "Import from Excel",
    "docs/client/import/import-data.md": "Import Data Templates",
    "docs/client/import/other-formats.md": "Other Formats",
    "docs/client/import/tally.md": "Import from Tally",
    "docs/client/import/resolve-conflict.md": "Resolve Import Conflicts",
    "docs/client/trial-balance/ledgers.md": "Ledgers",
    "docs/client/trial-balance/stock.md": "Stock Items",
    "docs/client/aging/vouchers.md": "Aging Vouchers",
    "docs/client/aging/payables.md": "Trade Payables",
    "docs/client/aging/receivables.md": "Trade Receivables",
    "docs/client/aging/report.md": "Aging Report",
    "docs/client/depreciation/register.md": "Fixed Assets Register",
    "docs/client/depreciation/asset-shifts.md": "Asset Shifts",
    "docs/client/depreciation/chart.md": "Depreciation Chart",
    "docs/client/depreciation/by-asset.md": "Depreciation by Asset",
    "docs/client/share/authorized.md": "Authorised Capital",
    "docs/client/share/issued.md": "Issued Capital",
    "docs/client/share/buyback.md": "Buy Back Capital",
    "docs/client/share/holders.md": "Shareholders",
    "docs/client/share/subscribed.md": "Subscribed Capital",
    "docs/client/share/payments.md": "Capital Payments",
    "docs/client/share/transfer-logs.md": "Transfer Logs",
    "docs/client/share/holding-report.md": "Share Holding Report",
    "docs/client/reports/balance-sheet.md": "Balance Sheet",
    "docs/client/reports/customize.md": "Customize Reports",
    "docs/configuration/service.md": "Service Settings",
    "docs/configuration/coding.md": "Coding Rules",
    "docs/configuration/cache.md": "Cache Cleanup",
    "docs/configuration/tally.md": "Tally Settings",
}

TEMPLATE = """---
title: {title}
draft: true
---

# {title}

!!! note "Documentation in progress"
    This article is being rewritten for the current FinAuto Client UI.

## Troubleshooting

See [Common issues]({faq_link}) or contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
"""


def faq_link_for(rel: str) -> str:
    parts = Path(rel).parts
    depth = len(parts) - 2  # under docs/
    return "/".join([".."] * depth) + "/faq/common-issues.md"


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    for rel, title in STUBS.items():
        path = root / rel
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            TEMPLATE.format(title=title, faq_link=faq_link_for(rel)),
            encoding="utf-8",
        )
        print("created", rel)


if __name__ == "__main__":
    main()
