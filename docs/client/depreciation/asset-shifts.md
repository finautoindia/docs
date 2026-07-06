---
title: Asset Shifts
client_version: "9.0"
controller: depreciation
function: asset_shifts
keywords:
  - asset shift
  - transfer
  - location change
symptoms:
  - shift not reflected
---

# Asset shifts

Record transfers of fixed assets between locations or categories within the same company.

## Prerequisites

- Assets exist in [Fixed asset register](register.md)
- Financial year unlocked if edits are required ([Financial years](../company/fyear.md))

## Steps

### Step 1: Open asset shifts

1. Go to **Fixed Assets → Asset Shifts**.
2. Review existing shift entries.

![Asset shifts grid with company bar](../../assets/images/depreciation/asset-shifts-01.png)

### Step 2: Add a shift

1. Click **Add** and select the asset.
2. Enter shift date, from/to location or category, and supporting voucher reference.
3. Save and verify the register reflects the change.

## Related links

- [Fixed asset register](register.md)
- [Depreciation chart](chart.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Asset not in list | Not in register | Import asset in Register first |
| Cannot save | FY locked | Unlock FY on company FY screen |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
