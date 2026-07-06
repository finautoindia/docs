---
title: Share Buyback
client_version: "9.0"
controller: share
function: capital_buyback
keywords:
  - buyback
  - capital reduction
  - treasury
symptoms:
  - buyback not balanced
---

# Share buyback

Record share buyback transactions and reduce capital proportionately across shareholders.

## Prerequisites

- [Issued capital](issued.md) and [Shareholders](holders.md) up to date
- Buyback board resolution date and price

## Steps

### Step 1: Add buyback entry

1. Go to **Share → Buyback**.
2. Click **Add** and enter buyback date, shares cancelled, and amount.

![Share buyback entry grid](../../assets/images/share/buyback-01.png)

!!! warning "Double entry required"
    After buyback, withdraw proportionate capital from individual shareholders in [Transfer logs](transfer-logs.md) on the **same date** as the buyback. Both entries are required for correct holdings.

### Step 2: Post transfer logs

1. Open [Transfer logs](transfer-logs.md).
2. Record seller-side reductions matching the buyback allocation.

## Related links

- [Transfer logs](transfer-logs.md)
- [Holding report](holding-report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Holding report imbalanced | Missing transfer log | Add matching transfer on buyback date |
| Cannot buy back | Insufficient issued shares | Verify issued capital counts |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
