---
title: Financial Years
client_version: "9.0"
controller: company
function: fyear
keywords:
  - financial year
  - fy lock
  - export fy
symptoms:
  - cannot edit locked fy
  - fy missing
---

# Financial years

View financial years linked to a company, lock completed periods to prevent edits, and export selected FY packages.

## Prerequisites

- Company selected in the top bar
- Data imported for the FY you want to lock or export

## Steps

### Step 1: Open FY management

1. Go to **Company → Manage Companies**.
2. Click **Manage FY data** (<i class="bi bi-calendar-check"></i>) on the company row.

![Financial years grid with lock and export actions](../../assets/images/company/fyear-01.png)

### Step 2: Lock or unlock a year

1. Review the FY grid (years sync from imported data and master FY list).
2. Click **Lock** on a row to prevent further edits for that company-year.
3. Click **Unlock** to allow edits again.

!!! warning "Locking a financial year"
    Locked FY data cannot be changed in grids until unlocked. Lock only after you have verified imports and adjustments.

### Step 3: Export selected FY

1. Select one or more FY rows using the checkboxes.
2. Choose **Export Selected FY** from the grid action bar.
3. Wait for the download to complete.

## Related links

- [Manage company](index.md)
- [Export company data](export.md)
- [Import from Tally](../import/tally.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| FY not listed | No data imported for that year | Import Tally or Excel data for the FY |
| Cannot edit grids | FY is locked | Unlock from this screen if changes are required |
| Export produces empty file | No rows selected | Select at least one FY before export |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
