---
title: Import Data Templates
client_version: "9.0"
controller: excel
function: import_data
keywords:
  - excel templates
  - ledgers export
  - stock export
  - round trip
symptoms:
  - template columns invalid
---

# Import data templates

Export module-specific Excel templates from their screens, edit offline, and re-import through **Import → Import Data**.

## Prerequisites

- Source data already in the client for the module you are exporting
- Company and FY selected

## Steps

### Step 1: Export from module

1. Open the target module (for example **Trial Balance → Ledgers**).
2. Use the grid **Export** action to download the template workbook.

![Import Data screen with module template upload](../../assets/images/import/import-data-01.png)

### Step 2: Import revised file

1. Go to **Import → Import Data** (or the **Import Data** entry under Import).
2. Select the module type matching your file.
3. Upload the updated workbook and submit.

!!! warning "Data overwrite"
    Import replaces existing module data for the scope defined in the template. Back up exports before bulk changes.

## Related links

- [Import from Excel](excel.md)
- [Ledgers](../trial-balance/ledgers.md)
- [Stock items](../trial-balance/stock.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Column errors | Edited headers removed | Do not change header row names |
| Partial import | Wrong module selected | Match template type to import form |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
