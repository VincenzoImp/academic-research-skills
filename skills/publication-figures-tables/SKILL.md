---
name: publication-figures-tables
description: Use when preparing, auditing, exporting, captioning, or checking publication-facing figures, tables, table fragments, source data, and asset maps.
license: MIT
---

# Publication Figures Tables

Prepare paper-facing figures and tables from canonical generated outputs.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/output-contracts.md`

## Workflow

1. Run `npm run workflow:analysis` or `npm run workflow:manuscript` depending on context.
2. Read analysis output paths, `figure-catalog.md`, `stats-appendix.md`, paper export folders, and `reports/paper/templates/asset-map.csv`.
3. Produce or audit figures, table fragments, captions, source-data links, export formats, and accessibility/readability checks.
4. Keep data paths and checksums traceable.

## Review Loop

Check every figure and table for source data, stale values, readability,
caption accuracy, statistical interpretation, and venue constraints. Fix and
re-review until clean.

## Handoff

Hand off only asset-map rows, figure/table files, captions, and source-data
links that match canonical analysis outputs.
