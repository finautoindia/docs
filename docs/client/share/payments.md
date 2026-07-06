---
title: Share Capital Payments
client_version: "9.0"
controller: share
function: capital_payments
keywords:
  - share payments
  - calls
  - allotment money
symptoms:
  - paid up mismatch
---

# Share capital payments

Track amounts received from shareholders against subscribed capital (calls, allotments, refunds).

## Prerequisites

- [Subscribed capital](subscribed.md) entries exist

## Steps

### Step 1: Open payments grid

1. Go to **Share → Payments**.
2. Review payment dates and amounts per shareholder.

![Share capital payments grid](../../assets/images/share/payments-01.png)

### Step 2: Record payments

1. Click **Add** and link to shareholder and share class.
2. Enter receipt date, amount, and reference (bank/cheque).
3. Reconcile paid-up capital in [Holding report](holding-report.md).

## Related links

- [Subscribed capital](subscribed.md)
- [Transfer logs](transfer-logs.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Over-payment warning | Exceeds subscribed | Adjust subscribed amount or payment |
| Holding capital wrong | Payments not entered | Add payment rows for the FY |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
