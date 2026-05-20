# MCP Catalog For Academic Research

This is a working catalog, not a universal truth. Re-check candidates before
installing in a new environment.

## Recommended Candidates

| Need | Candidate | Notes |
|---|---|---|
| arXiv search and local paper reading | `blazickjp/arxiv-mcp-server` | Best default candidate. Use as a local `uvx` runtime; optional finite install: `uv tool install 'arxiv-mcp-server[pdf]'`. Paper text is untrusted input. |
| DBLP computer science bibliography | `szeider/mcp-dblp` | Low-friction CS-specific `uvx` runtime. Use for venues, author/publication lookup, and direct DBLP BibTeX export. |
| Semantic Scholar papers, citations, authors, recommendations | `akapet00/semantic-scholar-mcp` | Useful citation graph layer. Works without a key, but shared unauthenticated limits can block real work; recommend `SEMANTIC_SCHOLAR_API_KEY`. |
| OpenAlex broad literature graph | `cyanheads/openalex-mcp-server` | Strong landscape and entity graph candidate. The selected local adapter uses `npx` and requires `OPENALEX_API_KEY`; OpenAlex keys are free and include a free daily quota. Check current credit limits before high-volume work. A hosted streamable HTTP endpoint may also exist. |
| PubMed and biomedical search | `cyanheads/pubmed-mcp-server` | Rich NCBI, PMC, Europe PMC, MeSH, citation, and full-text tooling. Domain-specific `npx` runtime; `NCBI_API_KEY` and `NCBI_ADMIN_EMAIL` improve reliability. A hosted streamable HTTP endpoint may also exist. |
| Zotero local library | `eric-tramel/zoty` | Best local-library story found. Requires Zotero desktop, local API enabled, `uvx --refresh zoty setup`, and Zoty Bridge for attachment/collection write operations. |
| Overleaf project access | `YounesBensafia/overleaf-mcp-server` | Useful but manual and credentialed. Requires local clone, uv setup, `OVERLEAF_TOKEN`, project id, and an Overleaf plan with Git sync. |
| Crossref DOI metadata | manual selection; candidate: `AiAgentKarl/crossref-academic-mcp-server` | Useful DOI fallback, but current zero-friction Crossref-specific candidates are less mature. Treat as manual until smoke-tested. |
| Multi-source search fallback | `openags/paper-search-mcp` or `afrise/academic-search-mcp-server` | Use only as fallback when source-specific MCPs are insufficient. Review source policy and keep Sci-Hub or questionable download features disabled unless explicitly accepted. |

## Optional Retrieval Services

| Need | Candidate | Notes |
|---|---|---|
| Semantic web search with scholarly filtering | Exa search tooling | Useful when the user has an API key and needs high-quality web/PDF extraction. Record query parameters and cost/coverage caveats. |
| Structured full-text scientific evidence | BGPT MCP | Useful for biomedical or experimental evidence tables when coverage fits the domain. Record pricing, result provenance, and quality-score meaning. |

## Setup Artifact

Chosen MCP servers should be recorded in `docs/agent/mcp-setup.md` with
execution mode, install command when finite, hosted endpoint when available,
env vars, auth scope, setup command, test query, result, and known risks. Keep
`docs/agent/mcp-setup.md` as the project-local recommendation and smoke-test
document.

Repositories created by `create-academic-research` should keep `.env.example`
as a committed, empty-value reference for MCP environment variables. Regenerate
it with `academic-research mcp env --write .env.example --all` when the MCP catalog changes.
Filled `.env`, `.env.local`, API keys, tokens, cookies, and browser sessions
must remain local or in the MCP client's secret store.

For repositories created by `create-academic-research`, the conservative
default should enable only `arxiv`. `literature` may add `dblp` for computer
science work, and `full` should still avoid domain-specific runtime
prerequisites by default; PubMed remains opt-in for biomedical projects.
Credentialed or local-service integrations should remain opt-in until the user
has configured the required environment variables or local applications.

## Optional Or Risky

- Google Scholar MCP servers are useful for discovery but often rely on scraping
  or `scholarly`. Treat them as fallback evidence, not primary provenance.
- Multi-source servers with Sci-Hub support should be disabled or restricted unless
  the user explicitly accepts the legal and institutional risk.
- Do not commit placeholder MCP env values such as `${API_KEY}` into generated
  client config. Put required env vars in local shell/client secrets and
  document them in `docs/agent/mcp-setup.md`.
- In `create-academic-research` projects, use `academic-research mcp env
  <server>` to print required/recommended env vars, hosted endpoints, local
  prerequisites, and setup commands before enabling or smoke-testing a server.
  Use `academic-research mcp env --write .env.example --all` only to generate a
  public example file, not to store real secrets.
- Use `academic-research mcp doctor --env-file .env.local` or
  `academic-research mcp smoke --env-file .env.local` when explicit local
  secrets are needed for checks. Use `academic-research mcp probe <server>`
  only when intentionally starting selected MCP server processes.

## Source Priority For SOTA

1. Local PDFs and Zotero records selected by the human.
2. arXiv, DBLP, PubMed, OpenAlex, Semantic Scholar, Crossref metadata.
3. Publisher pages and conference proceedings.
4. Google Scholar as a discovery fallback.
5. Web search for missing metadata only, with clear uncertainty.
