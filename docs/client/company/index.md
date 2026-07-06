---
title: Manage Company
client_version: "9.0"
controller: company
function: index
keywords:
  - company
  - branch
  - pan
  - depreciation method
  - financial year
symptoms:
  - income tax number not set
  - cannot create company
---

# Manage company

Create and maintain companies, assign CA profiles, set depreciation methods, and open branches, financial years, and export actions from the company grid.

## Prerequisites

- Service configuration completed ([Configuration → Service](../../configuration/service.md))
- User logged into FinAuto Client

## Steps

### Step 1: Open the company grid

1. Click **Company** in the main menu (or open **Company → Manage Companies**).
2. Review the **Manage Company** page header and company selector in the top bar.

### Step 2: Add a company

1. Click **Add** (or the add icon) in the grid toolbar.
2. Enter company details:
   - **Display name** and legal **company name**
   - **Income tax number (PAN)** — required for Tally import
   - **Depreciation method** (SLM or WDV)
   - **CA profile** (optional; create under [CA Profiles](../../configuration/caprofiles.md))
3. Save the record.

!!! warning "Deleting a company"
    Deleting a company removes **all data** (ledgers, stock, etc.) for **all financial years**. Confirm carefully before delete.

### Step 3: Select active company and FY

Use the **company** and **financial year** dropdowns in the top bar before importing or generating reports.

![Manage Company grid with themed navbar, company bar, and action links for Branches, FY, Export, Balance Sheet](../../assets/images/company/company-index-01.png)

*Screenshot: FinAuto Client v9.0 — Manage Company grid*

## Related links

- [Branches](branches.md)
- [Financial years](fyear.md)
- [Export](export.md)
- [Balance sheet](../reports/balance-sheet.md)
- [CA profiles](../../configuration/caprofiles.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Duplicate branch after Tally re-import | PAN or branch name changed | Keep PAN consistent; see note on unique branch + PAN on this page |
| PAN missing in Tally import | PAN not set in Tally | Set PAN under Tally **F11 → Features → More Details** |
| Cannot delete company | Active sessions or locked FY | Close other users; unlock FY if needed |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
