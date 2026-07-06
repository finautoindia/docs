---
title: Resolve Import Conflicts
client_version: "9.0"
controller: tally
function: resolve_conflict
keywords:
  - branch conflict
  - tally import
  - duplicate branch
symptoms:
  - branch conflict on import
---

# Resolve import conflicts

Resolve branch naming conflicts when Tally import detects duplicate or ambiguous branch mappings.

## Prerequisites

- A Tally import that reported branch conflicts
- Access to **Import → Resolve Conflicts** (shown when conflicts exist)

## Steps

### Step 1: Open conflict resolution

1. After import, follow the link or menu to **Resolve Conflicts**.
2. Review the list of conflicting branches.

![Resolve conflicts screen listing branch mapping options](../../assets/images/import/resolve-conflict-01.png)

### Step 2: Map branches

1. For each conflict, choose the correct FinAuto branch or create a mapping.
2. Save resolutions and re-run import if prompted.

## Related links

- [Import from Tally](tally.md)
- [Branches](../company/branches.md)

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Conflicts repeat | PAN changed between imports | Align PAN on HQ and branches |
| New branch created unexpectedly | Branch renamed in Tally | Map to existing branch manually |

See also [Common issues](../../faq/common-issues.md).

**Need more help?** Contact [support@finautoindia.com](mailto:support@finautoindia.com). Do not share API keys or PAN in email.
