---
name: badge-compliance-profiles
description: Use when selecting, auditing, or updating artifact badges, open-science badges, TOP-style transparency checks, release profiles, or venue compliance evidence.
license: MIT
---

# Badge Compliance Profiles

Map claims of openness, reproducibility, release, and reporting to explicit
evidence.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/artifact-open-science-policy.md`

## Workflow

1. Inspect `compliance/profiles.yaml` and `artifacts/badge-evidence-ledger.csv`.
2. Use the relevant workflow preflight: contribution, analysis, frame, release, manuscript, or submission.
3. Record profile applicability, evidence paths, missing evidence, blocking gaps, reviewer, checked date, and status.
4. Keep venue checklist, release manifest, submission package, and badge evidence consistent.

## Review Loop

Review each badge or compliance target for actual evidence, not intent. Fix
missing artifacts, metadata, commands, licenses, anonymization, or reproducible
instructions and re-review.

## Handoff

Hand off only badge claims that have concrete evidence rows and no blocking
gaps.
