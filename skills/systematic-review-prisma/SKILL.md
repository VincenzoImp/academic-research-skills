---
name: systematic-review-prisma
description: Use when planning, running, auditing, or documenting systematic reviews, scoping reviews, PRISMA-style flows, screening decisions, inclusion criteria, exclusion criteria, or reproducible literature searches.
license: MIT
---

# Systematic Review PRISMA

Use this skill when the literature review needs reproducibility beyond a normal
narrative SOTA. The goal is inspectable search and screening, not bureaucratic
formatting.

## Read First

- `references/systematic-review-policy.md`
- `references/source-ledger.md`
- `references/mcp-catalog.md`

## Workflow

1. Define research questions, review type, inclusion/exclusion criteria, and date
   range before broad searching.
2. Record databases and exact query strings in `sota/search-strategy.md`.
3. Export raw search results to `sources/metadata/`.
4. Deduplicate by DOI, arXiv ID, PMID, title, and author/year.
5. Record screening decisions in `sota/screening-decisions.csv`.
6. Update counts and reasons in `sota/prisma-flow.md`.
7. Promote included works to `sources/source-ledger.csv` and
   `sota/literature-matrix.csv`.
8. Write synthesis in `sota/synthesis.md` and gaps in `sota/gaps.md`.

## Screening Rules

- Separate title/abstract screening from full-text screening.
- Keep exclusion reasons short and controlled.
- Do not silently delete duplicates; count them.
- If the review is not systematic, label it narrative or scoping.

## Output Contract

At minimum, maintain:

- `sota/search-strategy.md`
- `sota/screening-decisions.csv`
- `sota/prisma-flow.md`
- `sota/literature-matrix.csv`
- `wiki/log.md`
