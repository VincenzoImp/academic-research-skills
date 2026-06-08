---
name: contribution-package
description: Use when creating or maintaining contribution packages, claim maps, badge plans, reports, paper exports, or component bundles from reviewed agenda opportunities.
license: MIT
---

# Contribution Package

Turn an accepted research opportunity into an organized contribution package.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/output-contracts.md`

## Workflow

1. Run `npm run workflow:contribution` when available.
2. Read `research_agenda/opportunity-ledger.csv` and `contributions/contribution-ledger.csv`.
3. Create or update `contributions/<contribution_id>/contribution.yaml`.
4. Maintain claim maps, badge plans, component inputs, generated outputs, report, paper export, reviews, and archive.
5. Link source IDs, SOTA claim IDs, survey claim IDs, analysis IDs, experiment IDs, artifacts, tables, figures, and compliance profiles.

## Review Loop

Build the contribution slice by slice. After each slice, check evidence,
outputs, claims, limitations, badge readiness, and clean-copy status. Repeat
until no blocking issue remains.

## Handoff

Hand off strict analyses to `research-data-analysis`, paper-facing assets to
`publication-figures-tables`, and reviewed reports to paper framing.
