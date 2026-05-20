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

- `references/repository-contract.md`
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

## Protocol Fields

Record these before screening begins:

- review type: systematic review, scoping review, rapid review, mapping review,
  or narrative review with reproducible search
- research questions and subquestions
- databases and interfaces, including API/MCP/manual search date
- full Boolean/query strings and filters
- inclusion criteria, exclusion criteria, and controlled exclusion reason labels
- deduplication fields and tie-break rules
- screening stages, reviewer count or agent/human roles, and disagreement rule
- extraction fields and quality/risk-of-bias rubric
- stopping rule for search expansion

If these fields are missing, produce a protocol draft first instead of running a
pretend systematic review.

## Screening Rules

- Separate title/abstract screening from full-text screening.
- Keep exclusion reasons short and controlled.
- Do not silently delete duplicates; count them.
- If the review is not systematic, label it narrative or scoping.
- Never invent a PRISMA count. Unknown counts stay unknown until the raw search
  export or screening file exists.
- Full-text unavailable is an exclusion or limitation reason, not a license to
  rely on abstract-only claims.
- For AI-assisted evidence synthesis, check whether PRISMA-trAIce or RAISE-style
  transparency notes are relevant and record AI tool use, prompts, model/version,
  human oversight, and validation method.

## Extraction And Synthesis

Extract each included source into `sota/literature-matrix.csv` with method,
population/dataset, intervention/system, comparator/baseline, metric/outcome,
key result, limitations, and reusable claims. Synthesis must group by themes,
methods, evidence quality, contradictions, and gaps. Do not force themes when
the paper set is too small or heterogeneous.

## Output Contract

At minimum, maintain:

- `sota/search-strategy.md`
- `sota/screening-decisions.csv`
- `sota/prisma-flow.md`
- `sota/literature-matrix.csv`
- `sota/synthesis.md`
- `sota/gaps.md`
- `wiki/log.md`
