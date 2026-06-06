# Repository Contract

Use this contract when a skill needs to write or locate project artifacts.

## Core Folders

- `sources/`: curated immutable research sources and machine-readable metadata.
- `sources/pdfs/`: native PDFs, named with a stable slug or citation key.
- `sources/markdown/`: converted Markdown from PDFs, HTML, DOCX, or notes.
- `sources/bib/`: BibTeX, CSL JSON, RIS, or citation exports.
- `sources/bib/references.bib`: canonical project bibliography.
- `sources/bib/citation-audit.csv`: missing, duplicate, unsupported, stale, and unused citation checks.
- `sources/metadata/`: JSON records from arXiv, Semantic Scholar, OpenAlex, Crossref, PubMed, DBLP, Zotero, or manual entry.
- `sources/conversion-ledger.csv`: document conversion commands, quality notes, and derived artifact paths.
- `sota/`: search strategies, literature matrices, topic synthesis, gaps, and related-work notes.
- `sota/screening-decisions.csv`: screening and exclusion decisions for structured reviews.
- `sota/prisma-flow.md`: reproducible review counts and flow notes.
- `wiki/`: LLM-maintained persistent knowledge base.
- `docs/agent/`: active agent state, MCP setup, project workflows, and research program files.
- `docs/agent/project-quality.md`: Project Quality Contract for request intake,
  work zones, trusted outputs, hygiene gates, and badge readiness.
- `configs/agent-stack.yaml`: optional skill/MCP capability manifest for agentic onboarding.
- `configs/capabilities.yaml`: optional project-local active skill/MCP state, usually written by `create-academic-research`.
- `docs/agent/capability-profile.md`: active skill/MCP capability profile when available.
- `docs/agent/generated/`: non-secret generated MCP config snippets.
- `.env.example`: committed empty-value reference for optional local/API
  environment variables. Filled `.env` or `.env.local` files must stay out of git.
- `docs/venue/`: venue targeting, review expectations, deadlines, and paper fit.
- `docs/methodology/`: stable method documentation for humans.
- `docs/methodology/research-design.md`: research questions, hypotheses, scope, contribution, and evidence plan.
- `docs/methodology/evaluation-plan.md`: evaluation questions, baselines, datasets, metrics, and validation plan.
- `docs/methodology/threats-to-validity.md`: internal, external, construct, conclusion, and reproducibility threats.
- `docs/reproducibility/`: commands, environments, artifact policies, and result reproduction notes.
- `docs/ethics/data-governance.md`: privacy, consent, sensitivity, terms, licensing, retention, and sharing notes.
- `experiments/`: human-curated experiment records, registries, and plans.
- `experiments/campaigns/`: autonomous campaign plans, frontier ledgers, and
  bounded iteration summaries.
- `scripts/`: thin repeatable command entrypoints that call reusable code in `src/`.
- `notebooks/`: optional exploratory and narrative notebooks; reusable logic belongs in `src/`.
- `repro_outputs/`: trusted reproduction evidence for external repos or papers.
- `train_outputs/`: training run evidence when the research includes model training.
- `explore_outputs/`: exploratory runs, hypotheses, candidate changes, and caveated findings.
- `analysis_outputs/`: data analysis reports and audit outputs.
- `debug_outputs/`: diagnosis artifacts for failures that affect scientific meaning.
- `outputs/`: curated paper-facing figures, tables, models, and exportable derived assets.
- `reports/proposal/`: research proposals and related administrative documents.
- `reports/paper/`: manuscript source, LaTeX, compiled PDFs, and response letters.
- `reports/reviews/`: internal and external review analysis.
- `reports/rebuttal/`: reviewer concern maps, rebuttal drafts, and revision plans.
- `reports/slides/`: presentation material.
- `artifacts/`: artifact evaluation checklists and public release preparation.
- `artifacts/badge-evidence-ledger.csv`: evidence ledger for Artifacts
  Available, Artifacts Evaluated Functional/Reusable, and Results
  Reproduced/Replicated readiness.

## Project Quality Contract

Use this contract for every user request, not only maintenance tasks. The user
should guide research direction; agents should preserve internal order,
provenance, validation, and file hygiene.

### Request Intake

Classify each request before acting: idea/positioning, source/SOTA,
experiment/reproduction, analysis, paper/LaTeX, artifact, venue/review,
ethics/governance, MCP/skills, or maintenance. Route through the narrowest
skill and update every durable record touched by that workflow.

### Clean Work Zones

Keep work in the correct zone:

- raw evidence in `sources/`, `data/raw/`, or `data/external/`
- reading and synthesis in `sources/markdown-linear/`, `sota/`, and `wiki/`
- exploratory work in `explore_outputs/`
- diagnostics in `debug_outputs/`
- analyses in `analysis_outputs/`
- trusted reproductions in `repro_outputs/`
- curated paper-facing exports in `outputs/`
- manuscripts, LaTeX, reviews, rebuttals, and slides in `reports/`
- release and badge material in `artifacts/`

Do not mix exploratory, trusted, raw, and final outputs. Promote artifacts only
when provenance, command/procedure, inputs, validation, and limitations are
recorded.

### Trusted Outputs

An output is trusted only when it names inputs, command/procedure, environment
or dependency notes, expected output or validation criterion, linked claim or
research question, and known limitations.

### Project Hygiene Gate

Before finishing, update the relevant ledger, matrix, wiki page, checklist, or
paper file; keep raw sources immutable; keep reusable logic in `src/`; keep
scripts thin; keep secrets/caches/private data out of git; reconcile source IDs,
citation keys, run IDs, and claim IDs; append durable changes to `wiki/log.md`;
and run the smallest meaningful validation command.

### Badge Readiness

When work touches code, data, benchmarks, models, experiments, reproduction, or
release material, update `artifacts/badge-evidence-ledger.csv` and
`artifacts/artifact-checklist.md`. Track readiness for Artifacts Available,
Artifacts Evaluated Functional, Artifacts Evaluated Reusable, Results
Reproduced, and Results Replicated throughout the project.

## Wiki Files

- `wiki/index.md`: content index. Update when adding reusable pages.
- `wiki/log.md`: chronological append-only log. Update after ingestion, synthesis, audits, and experiments.
- `wiki/synthesis.md`: current high-level synthesis.
- `wiki/contradictions.md`: unresolved conflicts across sources, data, or runs.
- `wiki/open_questions.md`: unresolved research questions.
- `wiki/templates/`: reusable page structures for sources, claims, experiments, decisions, reviewer concerns, and research questions.
- `wiki/templates/source-page.md`: source summary and evidence record.
- `wiki/templates/claim-page.md`: claim support and safe wording record.
- `wiki/templates/experiment-page.md`: experiment interpretation page linked to the registry.
- `wiki/templates/decision-record.md`: durable research or engineering decision record.
- `wiki/templates/reviewer-concern.md`: review concern and response plan.
- `wiki/templates/research-question.md`: question scope, contribution link, and evidence plan.

## Optional Agent Stack Contract

If the repository includes `configs/agent-stack.yaml`, use it as the source of
truth for available skill bundles, onboarding presets, and MCP candidates. If
the repository also includes `configs/capabilities.yaml`, treat that file as the
active project-local selection. Use `docs/agent/capability-profile.md` to
understand what is active in the project. Generated MCP snippets may live under
`docs/agent/generated/`, but must never contain API keys, cookies, Overleaf
tokens, or browser session data.

In repositories created by `create-academic-research`, prefer the project-local
npm lifecycle scripts:

- `npm run doctor` for structural checks.
- `npm run update` for a dry-run managed-file refresh, and
  `npm run update -- --apply` to write those managed changes.
- `npm run skills:install -- --preset <preset>` for project-local skill
  installs.
- `npm run mcp:env -- <server>`, `npm run mcp:dotenv`,
  `npm run mcp:doctor -- --env-file .env.local`,
  `npm run mcp:smoke -- --env-file .env.local`, and
  `npm run mcp:probe -- <server>` for MCP setup and checks.

For one-off use outside a generated project, invoke the package explicitly:

```bash
npm exec --yes --package=create-academic-research@latest -- academic-research <command>
```

## Non-Template Repositories

When a target repository does not follow this contract, map outputs to the
closest existing durable records and document assumptions. Suggest creating
missing folders only when provenance, reproducibility, or evidence quality would
otherwise be weak.

## Write Rules

- Never silently rewrite raw sources.
- Keep scripts thin; move reusable scientific logic to `src/`.
- Prefer adding a new derived artifact to editing an old derived artifact without explanation.
- Every generated artifact should name its input sources or command.
- Claims must point to a source, dataset, experiment, or decision record.
- Exploratory results must be marked as exploratory and kept separate from trusted reproduction outputs.
