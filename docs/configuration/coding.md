---
title: Coding Rules
client_version: "9.0"
controller: settings
function: coding
keywords:
  - coding rules
  - metadata sync
  - schedule mapping
symptoms:
  - auto-code rules outdated
---

# Coding rules

Refresh classification and coding rules from the FinAuto server for auto-code and report mapping.

## Prerequisites

- Valid [service configuration](service.md)

## Steps

### Step 1: Open coding settings

1. Go to **Configuration → Coding**.
2. Review available sync options on the form.

![Coding rules configuration screen](../assets/images/configuration/coding-01.png)

### Step 2: Sync rules

1. Submit the form to pull the latest coding rules from the server.
2. Confirm success message.

!!! note "When to sync"
    Sync after server-side rule updates or when auto-code produces unexpected mappings.

## Related links

- [Service configuration](service.md)
- [Ledgers](../client/trial-balance/ledgers.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Sync fails | API key or network | Update service settings; retry |
| Rules unchanged | Already current | Contact support if mappings still wrong |

See also [Common issues](../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
