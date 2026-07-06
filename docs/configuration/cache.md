---
title: Cache Cleanup
client_version: "9.0"
controller: settings
function: cache
keywords:
  - cache
  - cleanup
  - balance sheet temp
symptoms:
  - stale report output
---

# Cache cleanup

Clear local cache and temporary balance sheet files to resolve stale report output or free disk space.

## Prerequisites

- No balance sheet generation in progress

## Steps

### Step 1: Open cleanup

1. Go to **Configuration → Cleanup** (cache).
2. Click **CleanUp**.

![Cache cleanup screen with CleanUp button](../assets/images/configuration/cache-01.png)

!!! warning "Destructive cleanup"
    Cleanup removes cached report files. Regenerate reports after cleanup if needed.

### Step 2: Verify

Wait for **Success!** message and retry report generation.

## Related links

- [Balance sheet](../client/reports/balance-sheet.md)
- [Software updates](updates.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Cleanup errors | Files locked | Close open Excel exports; retry |
| Reports still wrong | Data issue not cache | Re-import trial balance; check ledger codes |

See also [Common issues](../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
