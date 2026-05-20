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

## Retrieval Protocol

1. Decompose the topic into 2-4 search concepts and synonyms before querying.
2. Run source-specific searches instead of one vague web search.
3. Use short, high-signal queries for arXiv and technical indexes; put field,
   date, and venue constraints in filters when the tool supports them.
4. Search both recent work and known seminal work. Do not let citation count
   alone define importance.
5. Capture raw metadata under `sources/metadata/` before synthesis.
6. Deduplicate by DOI, arXiv ID, PMID, OpenAlex ID, Semantic Scholar ID, title,
   and author/year.
7. Rank candidates by relevance, methodological fit, recency, venue/source
   authority, and citation/context signals. Record why core papers were chosen.
8. If coverage is weak, state the gap and next database/query to try instead of
   padding the review with marginal sources.

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

Also maintain `sota/gaps.md` when the review affects project direction. A gap is
not valid unless it names the evidence base, nearest prior work, why existing
methods fail or leave space, and what evidence would close the gap.

## Output Modes

- `search-plan`: query strategy, sources, filters, and expected blind spots.
- `annotated-bibliography`: source cards without broad claims.
- `matrix`: structured cross-paper comparison.
- `synthesis`: theme-first SOTA narrative with claim support.
- `related-work`: manuscript-ready draft after claims pass citation audit.
- `gap-map`: defensible opportunities and failure conditions for this project.

## Quality Rules

- No paper-by-paper laundry list unless the user explicitly asks for annotated bibliography.
- Claims need inline source IDs or wiki links.
- SOTA claims need date, benchmark, metric, and scope.
- Contradictions go to `wiki/contradictions.md`.
- Reusable findings should be linked from `wiki/index.md`.
- For each durable claim, record source IDs and allowed wording; do not promote
  abstract-only or unverified webpage summaries into paper text.
- Surface disagreements and negative results instead of smoothing them away.
