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

## Workflow

1. Identify raw, interim, and processed data paths.
2. Read data dictionary and provenance notes.
3. Write reusable analysis logic in `src/`, not only notebooks.
4. Use scripts or CLI entrypoints for repeatable runs.
5. Put generated tables in `outputs/tables/` and figures in `outputs/figures/`.
6. Record important findings in `wiki/claims/` or `wiki/experiments/`.
7. Link paper claims to exact table, figure, or experiment artifacts.

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

