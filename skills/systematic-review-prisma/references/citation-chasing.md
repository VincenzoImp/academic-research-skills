# Citation Chasing

Keyword search alone misses relevant work: grey literature, recent or
not-yet-indexed papers, titles without query keywords, and results below a
retrieval cutoff. Citation chasing recovers them, but unmanaged graph traversal
can also create an echo chamber. The goal is controlled expansion: follow the
evidence neighbourhood while forcing seed diversification, adjacent terminology,
and anti-echo-chamber checks.

Run citation chasing whenever the review must be reasonably complete or centered
on a specific project, not only for a quick scan.

## Seeds

Anchor expansion on project-specific seeds, not broad topic terms:

- core papers already selected or full-text read
- proposal or manuscript reference lists
- known seminal work named by the user
- the highest-relevance keyword hits
- recent frontier papers from reputable venues or preprint streams
- adjacent-community papers that use different terminology for the same problem

Use seed diversification: avoid starting only from one author group, one venue,
one benchmark, one citation cluster, or one survey. A focused review should have
at least project-specific, seminal, and frontier seeds when available.

## Backward Chasing

For each seed, extract its reference list and recover cited works as candidates:

- use the source PDF/Markdown bibliography, or OpenAlex `referenced_works`,
  Semantic Scholar references, or Crossref reference metadata
- save raw exports under `sources/metadata/` named `references-of-<source_id>-*`
- new candidates enter the same screening and deduplication pipeline as keyword
  hits

## Forward Chasing

For each seed, recover newer work that cites it:

- use OpenAlex cited-by, Semantic Scholar citations, or the citation-graph MCP
  servers in the project MCP catalog
- save raw exports named `cited-by-<source_id>-*`
- forward chasing is the main way to catch work published after a keyword pass

## Frontier Management

Treat each round as a frontier:

1. expand only the current seed set one hop at a time
2. deduplicate before screening
3. screen with the same inclusion/exclusion criteria as keyword results
4. promote only `core` or high-value `supporting` candidates to the next seed set
5. record the next frontier in `sota/citation-chasing-log.csv`

Do not recursively chase every found paper. Promotion is a deliberate decision
based on relevance, methodological fit, novelty of cluster, and full-text
availability.

## Anti-Echo-Chamber Checks

Run these checks before declaring saturation:

- add at least one adjacent keyword or venue query learned from full readings
- inspect a stratified sample of excluded near-misses, high-citation outliers,
  and recent low-citation results
- compare OpenAlex/Semantic Scholar citation graph results against at least one
  database or venue search
- check whether one author group, benchmark, dataset, or venue dominates the
  matrix
- search for contradiction terms such as failure, limitation, negative result,
  reproduction, replication, benchmark, or ablation when relevant

Graph centrality, PageRank-style scores, recommender rank, and citation counts
are discovery signals, not proof of relevance or quality.

## Iteration And Stopping

- expand one hop at a time; promote a new candidate to a seed only if it screens
  as core or supporting
- record each round in a citation-chasing log: seed, direction, found, new after
  dedup, and notes
- stop when a new hop yields mostly duplicates or out-of-scope records
  (saturation), not at a fixed count
- state the achieved hop depth and any seeds left unexpanded as a blind spot
- if the review budget ends before saturation, report the unexpanded frontier
  explicitly instead of claiming exhaustive coverage

## Discipline

- deduplicate new candidates by DOI, arXiv ID, PMID, OpenAlex ID, Semantic
  Scholar ID, DBLP key, title, and author/year before reading
- citation count is a discovery signal, not evidence of quality or relevance
- a candidate found through chasing still needs full-text support before any
  durable claim
- record databases, seeds, hop depth, and dates so the expansion is reproducible
