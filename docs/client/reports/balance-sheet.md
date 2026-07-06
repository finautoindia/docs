---
title: Balance Sheet
client_version: "9.0"
controller: balance_sheet
function: index
keywords:
  - balance sheet
  - schedule iii
  - cloud generation
  - excel export
symptoms:
  - balance sheet generation failed
  - unclassified ledgers
---

# Balance sheet

Generate Schedule III–ready balance sheets for the selected company and period, locally or via cloud processing.

## Prerequisites

- Trial balance imported and [ledgers coded](../trial-balance/ledgers.md)
- Service configuration valid ([Service settings](../../configuration/service.md))
- Company CA profile assigned if required for salutation

## Steps

### Step 1: Open balance sheet

1. From **Company** grid links or **Reports → Balance Sheet**, open the balance sheet screen.
2. Select period (annual, quarterly, or half-yearly if enabled).

### Step 2: Generate

1. Choose **local** or **cloud** generation if prompted (cloud recommended for large files — see service metadata).
2. Click generate and wait for completion.
3. Download or open the Excel output.

!!! warning "Unclassified ledgers"
    Generation fails if ledgers with balances lack codes. Fix codes in [Ledgers](../trial-balance/ledgers.md) or Tally before retrying.

![Balance sheet generation screen with company bar and generate action](../../assets/images/reports/balance-sheet-01.png)

*Screenshot: FinAuto Client v9.0 — Balance sheet generation*

## Related links

- [Ledgers](../trial-balance/ledgers.md)
- [Manage company](../company/index.md)
- [Customize reports](customize.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Unclassified ledger error | Missing codes | Auto-code or assign codes |
| Cloud generation slow | Large dataset | Expected; use cloud mode for support visibility |
| Rounding / denomination | Excel MASTER SHEET | Use **Convert To** dropdown in exported MASTER SHEET (see FAQ) |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
