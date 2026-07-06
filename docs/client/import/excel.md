---
title: Import Excel
client_version: "9.0"
controller: excel
function: import_excel
keywords:
  - excel import
  - trial balance
  - workbook
  - fy data
symptoms:
  - excel import failed
  - locked financial year skipped
---

# Import from Excel

Upload FY workbook data (ledgers, stock, fixed assets, share capital, vouchers) or a full company export package for the selected company and financial year.

## Prerequisites

- Company and financial year selected
- Excel templates exported from the relevant modules or sample files from your cloud dashboard

## Steps

### Step 1: Open Excel import

1. Go to **Import → From Excel**.
2. Review **FY data import** and **Company package import** cards.

### Step 2: Import FY workbook

1. Under **FY data import**, confirm company and FY in the context selector.
2. Choose the Excel file exported from ledgers, stock, or other modules.
3. Submit the form and wait for validation messages.

!!! note "Locked financial years"
    If a financial year is **locked** for a company, import for that FY is skipped.

### Step 3: Import company package (optional)

Use **Company package import** for zip or Excel exports containing company setup and branch data.

![Import Excel page with FY data import and company package cards](../../assets/images/import/import-excel-01.png)

*Screenshot: FinAuto Client v9.0 — Import → From Excel*

## Related links

- [Import data templates](import-data.md)
- [Ledgers](../trial-balance/ledgers.md)
- [Manage company](../company/index.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Import skipped for FY | FY locked | Unlock FY or choose another year |
| Validation errors listed | Template mismatch | Re-export template from the same module version |
| Empty data after import | Wrong company/FY selected | Check top bar selectors |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
