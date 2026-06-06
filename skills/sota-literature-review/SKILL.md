---
name: sota-literature-review
description: Use when building a state-of-the-art review, literature matrix, related work section, systematic search, paper comparison, gap analysis, or citation-backed synthesis.
license: MIT
---

# SOTA Literature Review

Build literature review artifacts that are reproducible, inspectable, and easy
to continue later. This skill is the orchestrator for autonomous SOTA work:
from a rough idea, a seed paper, a few references, or a query, it should drive
source discovery, citation-graph expansion, full-text acquisition, linear
reading, per-source synthesis, bibliography hygiene, claim audit, and survey
production.

## Read First

- `references/repository-contract.md`
- `references/source-ledger.md`
- `references/mcp-catalog.md`
- `references/citation-chasing.md`
- `references/per-source-synthesis-template.md`
- `references/survey-production.md`

## Review Scale

Before searching, declare the intended weight of the review and record it in
`sota/search-strategy.md`.

| Scale | Typical Use | Target Included Papers | Core Full Reads | Citation Chasing |
|---|---|---:|---:|---|
| `quick-scan` | orient an idea or proposal | 8-15 | 3-5 | seeds plus one high-yield hop |
| `focused-sota` | defensible related work and gap map | 20-40 | 8-15 | backward and forward until local saturation |
| `full-survey` | survey paper or major SOTA chapter | 50+ | 20+ | iterative frontier expansion with saturation evidence |

The target count is a planning budget, not a quality target. Stop because the
recorded search frontier reaches saturation or because the declared budget is
exhausted and blind spots are documented; do not pad with weak papers.

## Autonomous Workflow

1. Frame the review objective, research idea, contribution hypothesis, and
   inclusion/exclusion criteria. If the idea is underspecified, use
   `research-design-positioning` first.
2. Run `npm run workflow:literature` in `create-academic-research` projects
   when available; otherwise inspect MCP capability state with
   `academic-mcp-tooling`.
3. Build the initial seed set from user references, proposal citations, local
   PDFs, known seminal papers, and high-relevance API hits.
4. Create search concepts, synonyms, adjacent terms, exclusion terms, and
   negative-control queries. Record them in `sota/search-strategy.md`.
5. Run source-specific search across the active stack, saving raw metadata under
   `sources/metadata/`.
6. Expand through citation chasing. Record every round in
   `sota/citation-chasing-log.csv`.
7. Deduplicate and screen candidates into `sota/screening-decisions.csv`.
8. Promote included works into `sources/source-ledger.csv` and
   `sota/literature-matrix.csv`.
9. For every `core` or `supporting` source, acquire full text through
   `source-ingestion` and `document-conversion`, store a linear reading copy in
   `sources/markdown-linear/`, and update `sota/reading-log.csv`.
10. Read core/supporting sources linearly before writing source claims. Store
    per-paper syntheses in `sota/paper-syntheses/` using
    `references/per-source-synthesis-template.md`.
11. Normalize and verify bibliography entries in `sources/bib/references.bib`
    with `citation-bibliography-tooling`.
12. Write theme-first synthesis in `sota/synthesis.md`, gap analysis in
    `sota/gaps.md`, and when requested a LaTeX survey draft at
    `reports/paper/sota-survey.tex` using `references/survey-production.md`.
13. Run `citation-claim-audit` before promoting claims into manuscript prose.
14. When the research idea involves code/data/evaluation artifacts, connect
    gaps and evidence plans to ACM artifact badge readiness through
    `artifact-open-science`.

Keep the Project Quality Contract active across the loop: search metadata,
reading copies, syntheses, bibliography, LaTeX drafts, and artifact evidence
belong in separate durable zones, and only audited full-text evidence should be
promoted into trusted SOTA or manuscript claims.

## Search Strategy

Create or update `sota/search-strategy.md` with:

- research question
- review scale and paper budget
- seed set
- search concepts, synonyms, adjacent terms, and exclusion terms
- inclusion and exclusion criteria
- databases queried
- query strings
- date range
- filters
- screening decisions
- citation-chasing depth and saturation notes
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
5. Expand beyond keyword hits with citation chasing: follow references (backward)
   and citing papers (forward) from core seeds and proposal references. See
   `references/citation-chasing.md`. Skipping this step is the main cause of
   missed relevant work.
6. Capture raw metadata under `sources/metadata/` before synthesis.
7. Deduplicate by DOI, arXiv ID, PMID, OpenAlex ID, Semantic Scholar ID, title,
   and author/year.
8. Rank candidates by relevance, methodological fit, recency, venue/source
   authority, and citation/context signals. Record why core papers were chosen.
9. If coverage is weak, state the gap and next database, query, or seed to try
   instead of padding the review with marginal sources.
10. Re-run search with new concepts learned from full readings when the matrix
    reveals missing terminology, benchmarks, venues, or method families.

## Anti-Echo-Chamber Rules

- Maintain at least three seed types when possible: project-specific, seminal,
  and recent frontier.
- Search adjacent communities and alternative terminology, not only papers that
  cite the same seed.
- Include negative or contrastive queries that can disconfirm the initial idea.
- Sample excluded near-misses and high-citation outliers to check whether the
  screening rule is too narrow.
- Do not let one author group, venue, benchmark, or citation cluster dominate
  without recording why.
- Treat citation count, PageRank-style centrality, recommendations, and graph
  proximity as discovery signals only. Evidence still requires full text.

## Full-Text Policy

For every `core` and `supporting` source, acquire the full text, not just the
abstract:

- store the native PDF and a converted reading copy via `source-ingestion` and
  `document-conversion`
- read the full text linearly before writing its synthesis
- record progress in `sota/reading-log.csv`
- if no legal full text is found, mark it as a tracked limitation on the source
  and matrix row, not a silent drop; abstract-only records cannot carry durable
  claims

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
- full_text_status
- reading_status
- synthesis_path
- bib_key
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
- `per-source-synthesis`: uniform deep record per core/supporting source using
  `references/per-source-synthesis-template.md`.
- `related-work`: manuscript-ready draft after claims pass citation audit.
- `survey`: full survey narrative plus research agenda using
  `references/survey-production.md`.
- `gap-map`: defensible opportunities and failure conditions for this project.

## Completion Gates

A serious SOTA task is not complete until:

- search scale, seeds, queries, and blind spots are recorded
- citation chasing has a logged stopping rule in `sota/citation-chasing-log.csv`
- core/supporting papers have full-text status and reading status
- each core/supporting paper has a `sota/paper-syntheses/` record
- cited papers appear in `sources/bib/references.bib`
- survey or related-work claims pass `citation-claim-audit`
- ACM artifact implications are recorded when the SOTA motivates code, data,
  benchmark, model, reproduction, or evaluation artifacts

## Quality Rules

- No unstructured paper-by-paper laundry list. For core/supporting sources use
  the structured per-source synthesis template; reserve plain cards for the
  annotated-bibliography mode.
- Claims need inline source IDs or wiki links.
- SOTA claims need date, benchmark, metric, and scope.
- Contradictions go to `wiki/contradictions.md`.
- Reusable findings should be linked from `wiki/index.md`.
- For each durable claim, record source IDs and allowed wording; do not promote
  abstract-only or unverified webpage summaries into paper text.
- Surface disagreements and negative results instead of smoothing them away.
