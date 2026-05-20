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
