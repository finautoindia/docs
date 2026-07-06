---
title: Trade Receivables
client_version: "9.0"
controller: aging
function: receivables
keywords:
  - receivables
  - debtors
  - aging calculate
symptoms:
  - receivables aging empty
  - calculate fails
---

# Trade receivables

View outstanding customer balances by aging bucket and recalculate receivables for the selected period.

## Prerequisites

- [Aging vouchers](vouchers.md) imported for the financial year
- Company, FY, and period set in the company bar

## Steps

### Step 1: Open receivables grid

1. Go to **Aging → Trade Receivables**.
2. Review ledger-wise outstanding and day buckets (0–30, 31–60, etc.).

### Step 2: Calculate aging

1. Click **Calculate** to refresh receivables from voucher data for the current period.
2. Confirm rows appear before generating the [Aging report](report.md).

![Trade receivables grid with aging buckets and Calculate action](../../assets/images/aging/receivables-01.png)

## Related links

- [Trade payables](payables.md)
- [Aging vouchers](vouchers.md)
- [Aging report](report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Empty grid after Calculate | No voucher data | Import vouchers or enable Tally aging import |
| Totals mismatch Tally | Period mismatch | Align period in company bar with Tally period |
| Stale balances | Calculate not run | Run **Calculate** after new imports |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
