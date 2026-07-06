---
title: Authorized Capital
client_version: "9.0"
controller: share
function: capital_authorized
keywords:
  - authorized capital
  - share capital
  - face value
symptoms:
  - authorized capital mismatch
---

# Authorized capital

Maintain authorized share capital classes (type, face value, number of shares) for the company.

## Prerequisites

- Company selected in the top bar
- Share capital structure known from MCA filings

## Steps

### Step 1: Open authorized capital grid

1. Go to **Share → Authorized**.
2. Review existing authorized classes.

![Authorized capital grid with share classes](../../assets/images/share/authorized-01.png)

### Step 2: Add or edit classes

1. Click **Add** to create a share class with face value and authorized count.
2. Edit rows to correct face value or authorized shares before subscribed/issued entries.

## Related links

- [Issued capital](issued.md)
- [Subscribed capital](subscribed.md)
- [Shareholders](holders.md)
- [Holding report](holding-report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Cannot issue more than authorized | Authorized count too low | Increase authorized shares first |
| Duplicate share type | Class already exists | Edit existing row instead of adding |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
