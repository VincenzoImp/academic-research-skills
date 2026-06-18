# Changelog

## 0.2.1

- MCP Preflight (digest-paper, explore-sota) is now a capability gate, never
  an API-key gate. SOTA work starts when `arxiv` (full text) and at least one
  bibliographic source (`semantic-scholar`, `dblp`, or `openalex`) respond. A
  missing key only throttles; a reachable source being down degrades the
  cross-check rather than stopping. Previously the gate hard-required `arxiv`
  + `semantic-scholar`, so a transient `semantic-scholar` issue blocked all
  SOTA work. Pairs with create-academic-research 0.2.1.
- `digest-paper` full-text retrieval (step 4) is now a fallback pipeline,
  most-authoritative/legal first: arxiv → publisher/DOI open-access →
  Unpaywall → green-OA repositories → Sci-Hub (opt-in, last resort, via
  paper-search). The PDF is only the reading copy — the citation and
  authoritative version always come from the scholarly MCPs (reconciled by
  DOI); the source URL is recorded in `pdf_source`. Stops as
  `unresolvable-via-mcp` only when every source fails.

## 0.2.0

Full from-scratch rewrite for the create-academic-research v0.2 scaffold.

- 8 skills replace the 32 of v0.1: digest-paper, explore-sota,
  write-survey, develop-contribution, write-paper, package-artifacts,
  manage-submission, adversarial-review.
- Skills are plain portable `SKILL.md` + per-skill `references/`; the
  per-skill agent yaml, shared reference syncing, Python packaging, evals,
  and examples are gone.
- Skills target the v0.2 scaffold structure (root `references.bib`,
  `sota/papers/<citekey>/`, `survey/coverage.md`, `contributions/<slug>/`,
  `papers/<slug>/`) and its `make check` rails.
- Scholarly MCPs are mandatory for SOTA work: digest-paper and explore-sota
  hard-stop when arxiv or semantic-scholar do not respond.

Migration: v0.1 skills assume the v0.1 scaffold and were removed, not
renamed. Projects on the v0.1 scaffold should stay on skills 0.1.x.

## 0.1.x

See git history.
