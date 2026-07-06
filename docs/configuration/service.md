---
title: Service Configuration
client_version: "9.0"
controller: settings
function: service
keywords:
  - api key
  - service
  - cloud sync
  - metadata
  - auto-code
symptoms:
  - finauto username and password is not valid
  - auto-code not working
---

# Service configuration

Connect the FinAuto Client to your cloud account and refresh server metadata used for auto-coding, balance sheet rules, and report generation.

## Prerequisites

- FinAuto Client installed and running
- Active FinAuto cloud subscription
- API key generated from [finautoindia.com/user/login](https://www.finautoindia.com/user/login)

## Steps

### Step 1: Open service settings

1. In the client menu, go to **Configuration → Service**.
2. Review the page header **Service Configuration** and the subtitle about metadata updates.

### Step 2: Enter domain and API key

1. Enter your **domain** (as provided by FinAuto support or your account setup).
2. Paste the **API key** from your cloud dashboard.

!!! warning "Protect your API key"
    Do not share API keys in email, chat, or screenshots. Regenerate the key from the cloud portal if it is exposed.

### Step 3: Update metadata

1. Click **Update**.
2. Wait for the client to refresh code maps, feature flags, and sync rules from the server.
3. Confirm the success message **Service Configurations Updated**.

![Service Configuration form showing Domain, API Key fields and Update button](../assets/images/configuration/service-settings-01.png)

*Screenshot: FinAuto Client v9.0 — Configuration → Service with FinAuto Demo company selected*

## Related links

- [Installation](../client/install.md)
- [Coding rules](coding.md)
- [Software updates](updates.md)
- [Tally configuration](tally.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| "Username and/or password is not valid" | Expired or replaced API key | Generate a new key in the cloud portal; click **Update** here |
| Auto-code or reports misbehave after upgrade | Stale metadata | Click **Update** on this page to refresh rules |
| Update shows connection errors | Network or domain mismatch | Verify internet access and domain value with support |

See also [Common issues](../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
