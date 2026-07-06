---
title: Tally Configuration
client_version: "9.0"
controller: settings
function: tally
keywords:
  - tally path
  - odbc
  - port 9000
  - code list
symptoms:
  - tally connection error port 9000
---

# Tally configuration

Set Tally install location, ODBC port, and optional ledger group codes for balance sheet generation.

## Prerequisites

- Tally installed on the same machine or reachable via ODBC
- [Installation](../client/install.md) steps for plugin and ODBC completed

## Steps

### Step 1: Open Tally settings

1. Go to **Configuration → Tally**.
2. Review **Tally Configuration** page header.

### Step 2: Set path and port

1. Enter **Tally install location** (for example `C:\Program Files\TallyPrime`).
2. Set **ODBC port** to **9000** (Tally default).
3. Click **Save**.

### Step 3: Code list (optional)

Download the **code list** template from this page to assign optional group codes in Tally.

![Tally ODBC configuration in Tally Help settings](../assets/images/configuration/install-tally-odbc-01.png)

*Screenshot: Tally ODBC — enable Client/Server mode Both on port 9000*

## Related links

- [Installation](../client/install.md)
- [Import from Tally](../client/import/tally.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Port 9000 connection error | ODBC disabled | Enable in Tally connectivity settings; restart Tally |
| Wrong Tally path | Multiple Tally versions | Point to active TallyPrime folder |

See also [Common issues](../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
