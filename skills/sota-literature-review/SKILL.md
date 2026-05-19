---
name: sota-literature-review
description: Use when building a state-of-the-art review, literature matrix, related work section, systematic search, paper comparison, gap analysis, or citation-backed synthesis.
license: MIT
---

# SOTA Literature Review

Build literature review artifacts that are reproducible, inspectable, and easy
to continue later.

## Read First

- `references/repository-contract.md`
- `references/source-ledger.md`
- `references/mcp-catalog.md`

## Search Strategy

Create or update `sota/search-strategy.md` with:

- research question
- inclusion and exclusion criteria
- databases queried
- query strings
- date range
- filters
- screening decisions
- known blind spots

Prefer API-backed sources: arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed,
DBLP metadata, and Zotero. Use Google Scholar as a discovery fallback, not the
primary evidence layer.

## Literature Matrix

Maintain `sota/literature-matrix.csv` with at least:

- source_id
- title
- authors
- year
- venue
- method
- dataset/sample
- task/problem
- key claim
- metric/result
- limitations
- relevance
- citation_count_or_signal
- identifiers

## Synthesis

Write synthesis in `sota/synthesis.md`, not only in chat. Separate:

- established findings
- contested claims
- methodological families
- dataset or benchmark differences
- missing baselines
- open gaps
- implications for this project

## Quality Rules

- No paper-by-paper laundry list unless the user explicitly asks for annotated bibliography.
- Claims need inline source IDs or wiki links.
- SOTA claims need date, benchmark, metric, and scope.
- Contradictions go to `wiki/contradictions.md`.
- Reusable findings should be linked from `wiki/index.md`.

