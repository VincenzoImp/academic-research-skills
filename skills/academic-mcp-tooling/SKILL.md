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
4. If the repository was created with `create-academic-research`, inspect the
   current project state first with `npm run doctor`.
5. Document execution mode, finite install commands, hosted endpoints, setup
   commands, env vars, auth scopes, rate limits, risks, and workflows in
   `docs/agent/mcp-setup.md`.
6. Update `docs/agent/capability-profile.md` when active capability changes.
7. Mark each server as default, low-friction, credentialed, local-service,
   manual-setup, domain-specific, or fallback.
8. Smoke-test each configured server with one harmless query.
9. Save useful results to `sources/metadata/` or `sota/literature-matrix.csv`.
10. Record external IDs, query dates, and deduplication decisions.
11. Append setup or query changes to `wiki/log.md`.

## Selection Rules

- Use local PDFs and Zotero records selected by the researcher as the first
  evidence layer.
- Prefer arXiv/OpenAlex/Semantic Scholar/Crossref/PubMed metadata over general
  web search.
- In `create-academic-research` projects, keep `arxiv` as the default enabled
  MCP. Add `dblp` for computer science bibliography work, `pubmed` for
  biomedical work, and credentialed/local-service integrations only after their
  prerequisites are configured.
- Use `npm run mcp:env -- <server>` before enabling optional servers so
  required/recommended env vars, hosted endpoints, local prerequisites, and
  setup commands are visible without opening generated files.
- Use `npm run mcp:dotenv` to regenerate the committed `.env.example`
  reference. Filled secrets belong in `.env.local`, the shell, or the MCP
  client secret store, not in git.
- Use `npm run mcp:doctor -- --env-file .env.local` and
  `npm run mcp:smoke -- --env-file .env.local` when the user wants the CLI to
  read explicit local secrets for checks.
- Use `npm run mcp:probe -- <server>` only after static checks pass and only
  when intentionally starting the selected MCP server process.
- Use Google Scholar only as fallback discovery unless the user explicitly asks.
- For Zotero, prefer local-library tools that can access attachments and collections.
- For Overleaf, require clear token/project setup and default to read-only flows.
- Do not write literal placeholder secrets into generated MCP config. Record
  required env vars in `docs/agent/mcp-setup.md` and let the client environment
  or secret store provide them.
- Keep `.env.example` empty of real secrets and treat it as documentation, not
  runtime configuration. Do not assume agents automatically load `.env.local`.
- Disable Sci-Hub, questionable download, or browser-session features unless the
  user explicitly accepts the legal and institutional risk.
- Prefer MCP servers for live scholarly access and keep research-specific
  external skills as optional fallbacks. The project-native research workflow
  should remain in this package.
- Treat Exa/BGPT-style search services as useful optional retrieval layers when
  the user has credentials, but record pricing, coverage, and provenance limits.

## Smoke-Test Record

For each configured server, record:

- server name and install command
- execution mode and hosted endpoint when available
- client config location
- setup command when required
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
- Save raw metadata or query outputs before synthesis when they influence a
  literature matrix, citation decision, or claim audit.
