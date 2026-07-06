---
title: Transfer Logs
client_version: "9.0"
controller: share
function: transfer_logs
keywords:
  - share transfer
  - transmission
  - buyback adjustment
symptoms:
  - holding percentage wrong
---

# Transfer logs

Record share transfers, transmissions, and buyback-related holder adjustments across financial years.

## Prerequisites

- [Shareholders](holders.md) and [Issued capital](issued.md) configured
- Transfer deed dates and parties

## Steps

### Step 1: Open transfer logs

1. Go to **Share → Transfer Logs**.
2. Review historical transfers for the company.

![Share transfer logs grid](../../assets/images/share/transfer-logs-01.png)

### Step 2: Add transfer

1. Click **Add** and enter transfer date, seller, buyer, share class, and quantity.
2. For [Buyback](buyback.md), post seller reductions on the **same date** as the buyback entry.

### Step 3: Validate holdings

1. Open [Holding report](holding-report.md) as of FY end.
2. Confirm percentages sum to 100% for each share class.

## Related links

- [Buyback](buyback.md)
- [Holding report](holding-report.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Negative holding | Transfer quantity too high | Correct transfer shares |
| Buyback imbalance | Missing transfer log | Add proportional withdrawal on buyback date |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
