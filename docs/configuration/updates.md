---
title: Software Updates
client_version: "9.0"
controller: default
function: update
keywords:
  - update
  - upgrade
  - client version
symptoms:
  - update failed
  - client out of date
---

# Software updates

Download and install the latest FinAuto Client when a new version is available.

## Prerequisites

- FinAuto Client installed
- Internet access to FinAuto cloud services

## Steps

### Step 1: Open updates

1. Go to **Configuration → Updates**.
2. If a new version is available, the page shows a notification.

![Software updates screen with download action](../assets/images/configuration/updates-01.png)

### Step 2: Download and install

1. Click **Update** when prompted.
2. Run the downloaded `.exe` installer.
3. Relaunch the client and verify the version in the title bar or about dialog.

!!! warning "Save work before updating"
    Close imports and reports in progress. Complete or cancel long-running tasks before installing an update.

## Related links

- [Installation](../client/install.md)
- [Service configuration](service.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Update download fails | Network or proxy | Retry; check firewall |
| Client still shows old version | Installer not run | Re-run downloaded installer |

See also [Common issues](../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
