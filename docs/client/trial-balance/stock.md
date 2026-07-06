---
title: Stock Items
client_version: "9.0"
controller: stock
function: index
keywords:
  - stock
  - inventory
  - trial balance
symptoms:
  - stock items missing
---

# Stock items

View and manage stock item balances for the selected company and financial year.

## Prerequisites

- Stock data imported via [Tally](../import/tally.md) or [Excel](../import/excel.md)

## Steps

### Step 1: Open stock grid

1. Go to **Trial Balance → Stock Items**.
2. Review quantities and values in the grid.

![Stock items grid with company bar and trial balance columns](../../assets/images/trial-balance/stock-index-01.png)

### Step 2: Edit or export

1. Use inline edit actions where enabled.
2. Export for Excel round-trip via [Import data templates](../import/import-data.md).

## Related links

- [Ledgers](../trial-balance/ledgers.md)
- [Import from Tally](../import/tally.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Empty stock list | Not imported for FY | Re-import with stock option ticked |
| Values mismatch Tally | FY period mismatch | Align Tally period with client FY |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
