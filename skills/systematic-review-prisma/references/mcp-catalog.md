# MCP Catalog For Academic Research

This is a working catalog, not a universal truth. Re-check candidates before
installing in a new environment.

## Recommended Candidates

| Need | Candidate | Notes |
|---|---|---|
| arXiv search and local paper reading | `blazickjp/arxiv-mcp-server` | Strongest arXiv candidate found. Supports search, download, read, local storage, semantic search, citation graph, alerts, and prompts. |
| Semantic Scholar papers, citations, authors, recommendations | `akapet00/semantic-scholar-mcp` or the `semanticscholar-skill` package | Prefer API-backed access over web scraping. Use an API key for sustained work. |
| OpenAlex broad literature graph | `cyanheads/openalex-mcp-server` | Good for works, authors, institutions, topics, filters, and trends. |
| Crossref DOI metadata | choose and verify a maintained local server | Useful DOI fallback; prefer manual setup until a stable zero-friction candidate is chosen. |
| PubMed and biomedical search | `cyanheads/pubmed-mcp-server` | Rich NCBI tooling, MeSH, related articles, citations, PMC full text. |
| Zotero local library | `eric-tramel/zoty` | Better local-library story than simple API-only wrappers. Supports search, passages, collections, BibTeX, and adding papers. |
| Overleaf project access | `YounesBensafia/overleaf-mcp-server` | Syncs LaTeX through Git and exposes read/write tools. Requires project token setup. |
| Multi-source search fallback | `afrise/academic-search-mcp-server` | Simple Semantic Scholar + Crossref wrapper. Good backup, not full SOTA infrastructure. |

## Setup Artifact

Chosen MCP servers should be recorded in `docs/agent/mcp-setup.md` with install
command, env vars, auth scope, test query, result, and known risks. Keep
`docs/agent/mcp-setup.md` as the project-local recommendation and smoke-test
document.

## Optional Or Risky

- Google Scholar MCP servers are useful for discovery but often rely on scraping
  or `scholarly`. Treat them as fallback evidence, not primary provenance.
- Multi-source servers with Sci-Hub support should be disabled or restricted unless
  the user explicitly accepts the legal and institutional risk.
- DBLP-specific MCP candidates were weak in the current scan. Prefer OpenAlex or
  Semantic Scholar external IDs until a better DBLP MCP appears.

## Source Priority For SOTA

1. Local PDFs and Zotero records selected by the human.
2. arXiv, PubMed, OpenAlex, Semantic Scholar, Crossref, DBLP metadata.
3. Publisher pages and conference proceedings.
4. Google Scholar as a discovery fallback.
5. Web search for missing metadata only, with clear uncertainty.
