---
title: Branches
client_version: "9.0"
controller: company
function: branches
keywords:
  - branches
  - headquarters
  - pan
  - multi-entity
symptoms:
  - no applicable branch found
  - branch link missing
---

# Branches

Link branch companies to a headquarters entity so consolidated reporting and balance sheet generation treat them as one income-tax group.

## Prerequisites

- Headquarters company created on [Manage company](index.md) with **location type** set to headquarters
- Branch companies share the same **income tax number (PAN)** as the headquarters
- Branch records exist as separate companies in the grid

## Steps

### Step 1: Open branch management

1. Go to **Company → Manage Companies**.
2. On the headquarters row, click the **Manage Branches** icon (<i class="bi bi-diagram-3"></i>).
3. Confirm the page header shows **Branches** for the selected headquarters.

![Manage Company grid with Manage Branches action on headquarters row](../../assets/images/company/company-branches-01.png)

### Step 2: Add branches

1. Click **Add** in the branches grid.
2. Select a branch company from the autocomplete list (only companies with matching PAN and non-headquarters location type appear).
3. Save the link.

### Step 3: Export branch data

1. Use **Export** on the company grid when you need a full company package.
2. Generate consolidated statements from [Balance sheet](../reports/balance-sheet.md) after branch data is imported for the same financial year.

## Related links

- [Manage company](index.md)
- [Financial years](fyear.md)
- [Export company data](export.md)
- [Balance sheet](../reports/balance-sheet.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| "Could not find any applicable branch" | PAN mismatch or no branch companies | Ensure branch companies use the same PAN as HQ and are not marked headquarters |
| Manage Branches icon missing | Row is not headquarters | Only headquarters location type shows the branches action |
| Consolidated BS incomplete | Branch FY data not imported | Import each branch for the same FY before generating |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
