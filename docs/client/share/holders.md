---
title: Shareholders
client_version: "9.0"
controller: share
function: holders
keywords:
  - shareholders
  - holder category
  - promoter
symptoms:
  - holder category missing
---

# Shareholders

Maintain the shareholder master list and assign holder categories (promoter, holding company, public, etc.).

## Prerequisites

- Company selected
- Shareholder list from statutory registers or import template

## Steps

### Step 1: Open holder list

1. Go to **Share → Shareholders**.
2. Review shareholder IDs, names, and categories.

![Shareholders grid with holder categories](../../assets/images/share/holders-01.png)

### Step 2: Add or categorize holders

1. Click **Add** for new shareholders or edit existing rows.
2. Set **holder type** (category) for each shareholder — required for correct disclosure in [Holding report](holding-report.md).

### Step 3: Import via Excel (optional)

1. Download the share capital Excel template from [Subscribed capital](subscribed.md).
2. Import holders and capital data, then return here to verify categories.

## Related links

- [Subscribed capital](subscribed.md)
- [Transfer logs](transfer-logs.md)
- [Holding report](holding-report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Holder missing after import | Template row skipped | Re-import with valid shareholder ID |
| Wrong disclosure bucket | Category not set | Edit holder type on this grid |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
