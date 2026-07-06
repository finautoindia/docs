---
title: Export Company Data
client_version: "9.0"
controller: company
function: export
keywords:
  - export
  - backup
  - company package
symptoms:
  - export download slow
  - export failed
---

# Export company data

Download a full company data package (all financial years) for backup, migration, or support handoff.

## Prerequisites

- Company exists with imported data
- Stable network connection (large entities may take several minutes)

## Steps

### Step 1: Start export

1. Go to **Company → Manage Companies**.
2. Click **Export Company Data** (<i class="bi bi-download"></i>) on the company row.
3. Wait on the page until the browser download starts.

![Export company data action on Manage Company grid](../../assets/images/company/export-01.png)

!!! note "Export duration"
    Depending on entity count and data volume, export may take noticeable time. Do not close the client until the file downloads.

### Step 2: Store the package

1. Save the downloaded archive in a secure location.
2. Use FY-specific export from [Financial years](fyear.md) when you only need selected years.

## Related links

- [Manage company](index.md)
- [Financial years](fyear.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Download never starts | Session timeout or server error | Retry; check service connection in [Service settings](../../configuration/service.md) |
| Very slow export | Large multi-year dataset | Expected; wait or export selected FY only |
| Invalid company error | Stale bookmark | Open export from the company grid again |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
