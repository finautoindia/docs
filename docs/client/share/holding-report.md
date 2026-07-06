---
title: Share Holding Report
client_version: "9.0"
controller: share
function: share_holding_view
keywords:
  - shareholding
  - cumulative holding
  - holder fy
  - excel export
symptoms:
  - holding report empty
  - percentage incorrect
---

# Share holding report

View cumulative shareholding by shareholder as of the selected financial year end and export to Excel.

## Prerequisites

- [Authorized](authorized.md), [Issued](issued.md), [Subscribed](subscribed.md), and [Transfer logs](transfer-logs.md) up to date
- Company and FY selected in the top bar

## Steps

### Step 1: Open holding view

1. Go to **Share → Holding Report** (Share Holding View).
2. Review shareholder, share type, face value, percentage, capital, and share count columns.

![Share holding report grid with cumulative percentages](../../assets/images/share/holding-report-01.png)

The grid shows cumulative holdings with **Last Updated** action date per holder.

### Step 2: Export

1. Use the grid **Excel** export for audit working papers or MCA schedules.
2. For holder-wise FY drill-down, use the **Holder FY** view from the Share menu (same documentation applies).

### Step 3: Reconcile

1. Compare totals to [Subscribed capital](subscribed.md).
2. Fix gaps via [Transfer logs](transfer-logs.md) before finalizing [Balance sheet](../reports/balance-sheet.md).

## Related links

- [Shareholders](holders.md)
- [Transfer logs](transfer-logs.md)
- [Balance sheet](../reports/balance-sheet.md)

## Related controller

The **Holder FY** screen (`share` / `holder_fy`) shows year-specific holder movements; maintain data using the same share menus above.

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Empty grid | No share data for FY | Import subscribed capital |
| Percentages ≠ 100% | Missing transfers | Post transfers through FY end |
| Stale Last Updated | No recent transfer | Add transfer log with correct date |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
