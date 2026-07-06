---
title: Trade Payables
client_version: "9.0"
controller: aging
function: payables
keywords:
  - payables
  - creditors
  - aging calculate
symptoms:
  - payables aging empty
---

# Trade payables

View outstanding supplier balances by aging bucket and recalculate payables for the selected period.

## Prerequisites

- [Aging vouchers](vouchers.md) imported for the financial year
- Company, FY, and period set in the company bar

## Steps

### Step 1: Open payables grid

1. Go to **Aging → Trade Payables**.
2. Review ledger-wise outstanding and duration buckets.

![Trade payables grid with aging buckets and Calculate action](../../assets/images/aging/payables-01.png)

### Step 2: Calculate aging

1. Click **Calculate** to refresh payables from voucher data.
2. Export combined aging via [Aging report](report.md) after receivables and payables are both calculated.

## Related links

- [Trade receivables](receivables.md)
- [Aging vouchers](vouchers.md)
- [Aging report](report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Empty grid | Missing vouchers | Import voucher data first |
| Report missing payables sheet | No payables rows for period | Verify supplier vouchers exist for FY/period |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
