---
title: Software Overview
client_version: "9.0"
keywords:
  - overview
  - modules
  - finauto client
symptoms: []
---

<div class="fa-docs-page-header" markdown="1">

# FinAuto Client at a glance

Desktop app for CAs and finance teams: import trial balances, maintain registers, and produce Schedule III–ready statements. Every screen has a **Help** link that opens the matching topic in this site.

</div>

## How the app is organised

The top menu in FinAuto Client matches the tabs in this documentation:

| Menu | What you do there |
|------|-------------------|
| **Company** | Create companies, branches, financial years, export data |
| **Import** | Load trial balance, stock, assets, and vouchers from Excel or Tally |
| **Trial Balance** | Edit ledgers and stock after import |
| **Aging** | Trade receivables / payables and Excel aging reports |
| **Fixed Assets** | Register, shifts, depreciation schedules |
| **Share** | Authorised / issued capital, holders, transfers |
| **Reports** | Balance sheet and custom report layouts |
| **Configuration** | Service API key, Tally ODBC, coding rules, updates |

## Recommended first-day path

1. [Install](install.md) the client and connect [Service](../configuration/service.md).
2. [Create a company](company/index.md) with PAN and depreciation method.
3. [Import from Excel](import/excel.md) or [from Tally](import/tally.md).
4. Review [Ledgers](trial-balance/ledgers.md) and run [Balance sheet](reports/balance-sheet.md).

## Cloud vs local

- **Cloud mode** (Configuration → Service): faster report generation and remote support when enabled.
- **Local mode**: all data stays on your PC; suitable for air-gapped or offline work.

![FinAuto Client main window](../assets/images/company/company-index-01.png)

## Troubleshooting

See [Common issues](../faq/common-issues.md) or email [support@finautoindia.com](mailto:support@finautoindia.com). Never send API keys or PAN in email.
