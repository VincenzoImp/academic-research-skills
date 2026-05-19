---
name: research-project-router
description: Use when an academic research repository task could involve research design, sources, conversion, bibliography, SOTA, reviews, ethics, experiments, papers, reproduction, MCP tools, or project maintenance and the correct workflow is not obvious.
license: MIT
---

# Research Project Router

Use this skill first when a request spans more than one research workflow. The
goal is to route deliberately and preserve project state.

## Read First

- `references/repository-contract.md`
- `references/output-contracts.md`

## Routing Table

| User intent | Prefer skill |
|---|---|
| Turn ideas, gaps, hunches, and vague goals into research questions, contribution claims, scope, and evidence plans | `research-design-positioning` |
| Choose CS venue, track, audience, review criteria, or paper positioning | `cs-venue-strategy` |
| Add PDFs, papers, proposals, archives, datasets, or web pages | `source-ingestion` |
| Convert PDFs, scans, DOCX, tables, or figures to Markdown/assets | `document-conversion` |
| Normalize BibTeX, identifiers, citation keys, missing/unused citations | `citation-bibliography-tooling` |
| Find related work, build SOTA, compare papers, discover gaps | `sota-literature-review` |
| Run reproducible systematic/scoping review and PRISMA-style screening | `systematic-review-prisma` |
| Check citations, claims, numbers, evidence, bibliography | `citation-claim-audit` |
| Design/audit CS evaluation, baselines, metrics, ablations, validity | `cs-methodology-evaluation` |
| Review a manuscript/proposal as a severe peer reviewer | `adversarial-peer-review` |
| Draft, revise, polish, or review a paper/proposal | `paper-writing-review` |
| Respond to reviews, rebuttal, revision plan, camera-ready changes | `rebuttal-revision-strategy` |
| Prepare artifact evaluation, code/data release, reproducibility package | `artifact-open-science` |
| Migrate a bad repo, archive, or notebook pile into the project structure | `repo-migration` |
| Understand or reproduce an external research repo | `research-repo-reproduction` |
| Run experiments, benchmark ideas, maintain run ledger | `experiment-logbook` |
| Analyze datasets, statistics, tables, and figures | `research-data-analysis` |
| Build research dashboards or interactive demos | `research-ui-prototyping` |
| Assess human-subject, privacy, scraping, license, or sharing risk | `ethics-data-governance` |
| Fix folder structure, docs, wiki, agent instructions | `research-project-maintenance` |
| Onboard or audit the skill/MCP capability stack | `academic-mcp-tooling` then `research-project-maintenance` |
| Select, configure, smoke-test, and document arXiv, OpenAlex, Zotero, Overleaf, Scholar, and scholarly metadata MCP tools | `academic-mcp-tooling` |
| Review or improve the skill package itself | `skill-evaluation` |

## Default Procedure

1. Identify the research artifact being touched: source, claim, data, code, experiment, paper, or project structure.
2. Check whether the repository follows the contract. If not, adapt conservatively and note the gap.
3. Route to the narrowest skill that can complete the task.
4. If several workflows are required, order them as: design/position -> venue/frame -> ingest/convert -> synthesize/review -> evaluate/audit -> write -> rebuttal/artifact -> reproduce/experiment -> update project/wiki.
5. Update `wiki/log.md` or the appropriate output ledger when the task changes project knowledge.

## Do Not

- Treat chat history as the project record.
- Skip ingestion and write a SOTA directly from raw PDFs.
- Let exploratory experiment outputs overwrite trusted reproduction outputs.
- Make a claim stronger than the source, dataset, or run supports.
