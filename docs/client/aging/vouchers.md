---
title: Aging Vouchers
client_version: "9.0"
controller: aging
function: vouchers
keywords:
  - vouchers
  - aging import
  - excel template
symptoms:
  - vouchers not imported
  - aging empty
---

# Aging vouchers

Import or review voucher lines used to compute trade receivables and payables aging buckets.

## Prerequisites

- Company and financial year selected
- For Tally users: [Import from Tally](../import/tally.md) with **Import Data for Aging** checked
- For non-Tally users: Excel template from this screen

## Steps

### Step 1: Open vouchers grid

1. Go to **Aging → Vouchers**.
2. Review existing voucher rows for the selected company and FY.

![Aging Vouchers grid with company bar and voucher import options](../../assets/images/aging/vouchers-01.png)

### Step 2: Import voucher data

**Tally users:** Vouchers import automatically with Tally data when aging import is enabled.

**Excel users:**

1. Scroll to the template section at the bottom of the page.
2. Download the voucher Excel template.
3. Fill required voucher details (ledger, amounts, dates).
4. Upload via **Import from Excel** and follow on-screen validation.

### Step 3: Refresh aging

1. Open [Trade receivables](receivables.md) and [Trade payables](payables.md).
2. Click **Calculate** for the current period.
3. Generate the [Aging report](report.md).

## Related links

- [Aging report](report.md)
- [Import from Tally](../import/tally.md)
- [Import data templates](../import/import-data.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| No vouchers after Tally import | Aging option not ticked | Re-import with **Import Data for Aging** enabled |
| Excel import rejected | Template version mismatch | Re-download template from this page |
| Aging buckets wrong | Prior FY outstanding | Import prior-year vouchers |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
