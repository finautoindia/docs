---
title: Common Issues
client_version: "9.0"
keywords:
  - faq
  - troubleshooting
  - tally odbc
  - api key
symptoms:
  - tally connection error
  - invalid api key
  - income tax number not set
---

# Frequently asked questions

Symptom-indexed troubleshooting for FinAuto Client. Search this page or use the site search bar.

## Escalation template

Contact support when:

- Steps in the module article and FAQ do not resolve the issue
- You see data loss, license, or security concerns
- Cloud generation fails repeatedly after cache cleanup and re-import

**Contact:** [support@finautoindia.com](mailto:support@finautoindia.com)

!!! warning "Do not send secrets"
    Do not email or chat API keys, passwords, or PAN numbers. Configure API keys only inside **Configuration → Service** in the client.

---

## Tally connection error (port 9000)

**Symptom:** `Tally Connection Error: Ensure that Tally is running ODBC server on port: 9000`

**Cause:** Tally not running, ODBC disabled, or `tcodes.tcp` plugin missing.

**Resolution:**

1. Open Tally and enable ODBC on port **9000** ([Installation](../client/install.md)).
2. Verify plugin under **Help → F4: Add-Ons**.
3. Confirm [Tally configuration](../configuration/tally.md).

---

## Invalid API key / service login

**Symptom:** `Finauto username and/or password is not valid`

**Cause:** Expired or regenerated API key.

**Resolution:**

1. Generate a new key at [finautoindia.com/user/login](https://www.finautoindia.com/user/login).
2. **Configuration → Service** → paste key → **Update**.

---

## Income tax number not set

**Symptom:** Error referencing income tax / PAN during Tally import.

**Cause:** PAN not configured in Tally company.

**Resolution:** Tally **F11 → Features → More Details** → set PAN.

---

## Unclassified ledgers on balance sheet

**Symptom:** Balance sheet generation lists unclassified ledgers.

**Resolution:** Code ledgers in [Ledgers](../client/trial-balance/ledgers.md) or Tally; run auto-code.

---

## Balance sheet denomination (lakhs / millions)

After Excel export, open **MASTER SHEET** → cell **Convert To** (F1/F2) to scale figures.

---

## Auto-code and carry code

- **Auto-code:** Enabled via service metadata; sync rules under [Coding](../configuration/coding.md).
- **Carry code:** Applies prior-year codes when ledger names match; requires prior FY classified.

---

## Aging vouchers missing

Ensure **Import data for aging** was selected in Tally import or import vouchers via Excel templates.

---

## Aging report download fails

**Symptom:** Generate Aging Report button errors or Excel is empty.

**Cause:** Vouchers not imported, Calculate not run, or wrong FY/period.

**Resolution:**

1. Import vouchers with **Import data for aging** enabled ([Tally import](../client/import/tally.md)).
2. Run **Calculate** on [Trade receivables](../client/aging/receivables.md) and [Trade payables](../client/aging/payables.md).
3. Open [Aging report](../client/aging/report.md) and generate again for the selected period.

---

## Client update failed

**Symptom:** **Configuration → Updates** reports download or install failure.

**Resolution:**

1. Confirm internet access and service connection ([Service](../configuration/service.md)).
2. Retry update from [Updates](../configuration/updates.md).
3. Reinstall client from cloud dashboard if the installer is corrupt ([Installation](../client/install.md)).

---

## Related module docs

- [Import from Tally](../client/import/tally.md)
- [Aging report](../client/aging/report.md)
- [Service configuration](../configuration/service.md)

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
