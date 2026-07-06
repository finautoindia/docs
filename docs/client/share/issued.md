---
title: Issued Capital
client_version: "9.0"
controller: share
function: capital_issued
keywords:
  - issued shares
  - allotment
symptoms:
  - issued exceeds authorized
---

# Issued capital

Record shares issued to shareholders up to authorized limits.

## Prerequisites

- [Authorized capital](authorized.md) configured
- Allotment dates and counts from board resolutions

## Steps

### Step 1: Open issued capital

1. Go to **Share → Issued**.
2. Review issued classes and counts.

![Issued capital grid](../../assets/images/share/issued-01.png)

### Step 2: Add issuance

1. Click **Add** and link to authorized class.
2. Enter issue date, number of shares, and consideration details.
3. Update [Subscribed capital](subscribed.md) and [Payments](payments.md) as needed.

## Related links

- [Authorized capital](authorized.md)
- [Transfer logs](transfer-logs.md)
- [Holding report](holding-report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Validation on share count | Exceeds authorized | Increase authorized capital |
| Holding % wrong | Missing transfer log | Post transfers in [Transfer logs](transfer-logs.md) |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
