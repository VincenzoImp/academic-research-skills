---
name: academic-mcp-tooling
description: Use when selecting, installing, configuring, smoke-testing, documenting, or troubleshooting MCP servers for academic search, arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed, Zotero, Overleaf, Google Scholar, paper metadata, or scholarly source tooling.
license: MIT
---

# Academic MCP Tooling

Use MCP servers as source access infrastructure, not as final scholarly
authorities. Selection, setup, query discipline, and documentation belong in one
auditable workflow so literature access remains reproducible.

## Read First

- `references/mcp-catalog.md`
- `references/external-skill-recommendations.md`
- `references/source-ledger.md`
- `references/repository-contract.md`

If the target repo has `configs/agent-stack.yaml`, read it before selecting MCP
servers. If it has `docs/agent/capability-profile.md`, treat that as the active
capability state.

## Workflow

1. Identify needed source systems: arXiv, Semantic Scholar, OpenAlex, Crossref,
   PubMed, Zotero, Overleaf, DBLP metadata, or fallback search.
2. Prefer API-backed source-specific servers over scraping or vague all-in-one
   wrappers when accuracy matters.
3. Choose the smallest set of MCP servers that covers the project need.
4. If `academic-research` is available, inspect the current project state first:
   `academic-research doctor`.
5. Document install commands, env vars, auth scopes, rate limits, risks, and
   workflows in `docs/agent/mcp-setup.md`.
6. Update `docs/agent/capability-profile.md` when active capability changes.
7. Mark each server as generated-config, manual-setup, optional, or fallback.
8. Smoke-test each configured server with one harmless query.
9. Save useful results to `sources/metadata/` or `sota/literature-matrix.csv`.
10. Record external IDs, query dates, and deduplication decisions.
11. Append setup or query changes to `wiki/log.md`.

## Selection Rules

- Use local PDFs and Zotero records selected by the researcher as the first
  evidence layer.
- Prefer arXiv/OpenAlex/Semantic Scholar/Crossref/PubMed metadata over general
  web search.
- Use Google Scholar only as fallback discovery unless the user explicitly asks.
- For Zotero, prefer local-library tools that can access attachments and collections.
- For Overleaf, require clear token/project setup and default to read-only flows.
- Disable Sci-Hub, questionable download, or browser-session features unless the
  user explicitly accepts the legal and institutional risk.

## Smoke-Test Record

For each configured server, record:

- server name and install command
- client config location
- required environment variables
- query
- timestamp
- returned identifier or result count
- failure, fallback, and known limitation if unavailable
- active preset or manual rationale when using `configs/agent-stack.yaml`
- whether the client config was generated or requires manual setup

## Query Discipline

- Deduplicate by DOI, arXiv ID, PMID, title, and author/year.
- Do not rely on one database for final SOTA coverage unless the scope says so.
- Treat scraped results as discovery leads, not proof.
- Update `sources/source-ledger.csv` only when a source becomes evidence.
