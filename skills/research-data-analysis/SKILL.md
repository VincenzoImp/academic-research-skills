---
name: research-data-analysis
description: Use when analyzing research datasets, cleaning tabular data, selecting statistical tests, producing result tables, creating publication figures, or moving notebook logic into reproducible code.
license: MIT
---

# Research Data Analysis

Analysis should be repeatable, inspectable, and connected to claims.

## Read First

- `references/repository-contract.md`
- `references/output-contracts.md`
- `references/workflow-stage-contracts.md`

## Workflow

1. Run `npm run workflow:analysis` when available.
2. Read the contribution-local `analysis.yaml`, blocker summary, data paths,
   figure catalog, stats appendix, and paper-export folder.
3. If required preflight fields are missing, write only the blocker summary.
4. Identify raw, interim, and processed data paths.
5. Read data dictionary and provenance notes.
6. Write reusable analysis logic in `src/`, not only notebooks.
7. Use scripts or CLI entrypoints for repeatable runs.
8. Put generated tables and figures in the analysis bundle or declared output paths.
9. Record important findings in the contribution report, claim map, or wiki pages.
10. Link paper claims to exact table, figure, or experiment artifacts.

## Statistical Discipline

- Match tests to design, distribution, sample size, and hypothesis.
- Report effect sizes and confidence intervals when relevant.
- Distinguish statistical significance from practical significance.
- Flag multiple comparisons, missing data, selection bias, and confounds.
- Do not treat exploratory analysis as confirmatory.

## Figure Discipline

- Use readable labels, units, captions, and colorblind-safe palettes.
- Avoid misleading axes and decorative chart types.
- Save source data for final figures when practical.
- For publication figures, record command and input dataset.

## Notebook Policy

Notebooks can explore and explain. If the logic becomes part of the result,
move it into `src/` and leave the notebook as a consumer.

## Project Quality

Keep raw, interim, processed, exploratory, analysis, and final paper-facing
outputs separated. Promote a table, figure, statistic, or model result only
when the input data, command or procedure, environment notes, validation check,
and linked claim or experiment are recorded. If an analysis supports an
artifact or reproducibility claim, add the evidence path and validation status
to `artifacts/badge-evidence-ledger.csv`.

## Review Loop And Handoff

Run, validate, review, fix, and re-review the analysis until method, data,
metric, interpretation, and clean-copy issues are resolved. Handoff reviewed
generated outputs to `research-results-reporting` and paper-facing assets to
`publication-figures-tables`.
