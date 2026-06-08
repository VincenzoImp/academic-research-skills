# Output Contracts

Use these contracts to avoid ambiguous "done" states.

Use this file with the Project Quality Contract in
`references/repository-contract.md`. A generated file is not automatically a
trusted output; it must stay in the correct work zone until provenance,
procedure, validation, limitations, and linked claims are recorded.

## Trust Levels

- `explore_outputs/`: exploratory variants, early hypotheses, and caveated runs.
- `debug_outputs/`: diagnosis artifacts for failures, data issues, or scientific bugs.
- `analysis_outputs/`: analysis reports, audits, intermediate tables, and draft figures.
- `repro_outputs/`: trusted reproduction evidence for external or internal results.
- `train_outputs/`: trusted training run evidence when model training is part of the research.
- `outputs/`: curated paper-facing figures, tables, models, and exportable derived assets.

## Promotion Rules

Do not promote an output into `outputs/`, `repro_outputs/`, `train_outputs/`,
`reports/`, or `artifacts/` until it names:

- input sources, datasets, or run records
- command, script, notebook, or manual procedure
- environment or dependency notes
- expected output or validation criterion
- linked claim, research question, experiment, source, or artifact checklist row
- known limitations

If any item is missing, keep the material in `explore_outputs/`,
`analysis_outputs/`, or `debug_outputs/` and record the gap in the relevant
wiki page, ledger, or checklist.

## Source Ingestion

- `sources/source-ledger.csv` updated.
- Raw source stored under `sources/pdfs/`, `sources/metadata/`, `data/raw/`, or `reports/`.
- Markdown extraction stored under `sources/markdown/` when useful.
- `sources/conversion-ledger.csv` updated when conversion happens.
- `sources/bib/references.bib` updated when a citation record is used.
- `wiki/sources/<source_id>.md` created or updated.
- `wiki/index.md` and `wiki/log.md` updated.

## Agent Capability Onboarding

- `configs/agent-stack.yaml` used when present for presets and MCP candidates.
- `configs/capabilities.yaml` used when present for active project-local selections.
- `docs/agent/mcp-setup.md` updated with project-local MCP recommendations, actual setup, and smoke tests.
- `docs/agent/capability-profile.md` updated when active skills/MCPs change.
- `docs/agent/generated/<agent>-mcp.json` written only with non-secret config.
- `wiki/log.md` updated with onboarding or capability changes.

## Research Design

- `docs/methodology/research-design.md`: questions, contribution, scope, evidence plan.
- `wiki/open_questions.md` or `wiki/questions/<question_id>.md` updated.
- `wiki/templates/research-question.md` used when creating durable question pages.

## Ideation And Positioning

- `docs/methodology/research-design.md`: contribution claims and failure conditions.
- `wiki/templates/claim-page.md` used when contribution claims become reusable wiki pages.
- `sota/gaps.md` updated when the idea changes the gap map.

## Venue Strategy

- `docs/venue/venue-strategy.md`: target venues, fit, risks, and required changes.
- affected paper/research design updated for venue-specific expectations.

## Document Conversion

- Native source preserved.
- Derived Markdown stored under `sources/markdown/` when useful.
- Extracted assets stored under `sources/assets/<source_id>/` when useful.
- `sources/conversion-ledger.csv` updated with tool and quality.

## Bibliography

- `sources/bib/references.bib`: canonical bibliography.
- `sources/bib/citation-audit.csv`: missing, duplicate, unused, stale, unsupported citation checks.
- `sources/source-ledger.csv` aligned with citation keys and identifiers.

## SOTA Review

- `sota/search-strategy.md`: query strings, sources, filters, inclusion criteria.
- `sota/screening-decisions.csv`: screening decisions for structured reviews.
- `sota/prisma-flow.md`: counts for systematic/scoping reviews.
- `sota/citation-chasing-log.csv`: backward/forward citation expansion rounds, promoted seeds, and stopping rule.
- `sota/reading-log.csv`: full-text linear reading status for core/supporting sources.
- `sota/literature-matrix.csv`: structured paper table.
- `sota/paper-syntheses/`: per-source syntheses for core/supporting papers.
- `sota/synthesis.md`: current state of the art and gap analysis.
- `sota/gaps.md`: open opportunities and unresolved disagreements.
- `reports/paper/sota-survey.tex`: LaTeX survey or SOTA chapter when the requested output is survey-scale.
- `wiki/contradictions.md` updated when sources conflict.

## Claim Audit

- `analysis_outputs/claim-audit.md`: claim-by-claim results.
- `wiki/templates/claim-page.md` used for durable claim records.
- `sources/bib/citation-audit.csv`: citation-level issues when bibliography is involved.
- Manuscript or wiki pages updated only after the audit verdict is clear.

## Data Analysis

- `analysis_outputs/`: analysis reports, notebooks-to-code transition notes, and audit outputs.
- `outputs/figures/`: curated final figures used in papers, slides, or reports.
- `outputs/tables/`: curated final tables used in papers, slides, or reports.
- `outputs/models/`: curated lightweight model artifacts or references to external model storage.
- `wiki/claims/` or `wiki/experiments/` updated when an analysis changes the evidence base.

## CS Methodology Evaluation

- `docs/methodology/evaluation-plan.md`
- `docs/methodology/threats-to-validity.md`
- `experiments/registry.csv` entries linked to claims and outputs.

## Peer Review

- `reports/reviews/<review_id>.md`
- `wiki/templates/reviewer-concern.md` used for reusable acceptance-critical concerns.
- reviewer concerns linked to claims, methods, venue strategy, or rebuttal plan.

## Rebuttal And Revision

- `reports/rebuttal/<round_id>.md`
- revised manuscript sections or planned changes linked to reviewer concerns.

## Artifact And Open Science

- `artifacts/artifact-checklist.md`
- `artifacts/badge-evidence-ledger.csv`: badge target, evidence path, linked claim/result, procedure, validation status.
- release notes, license, citation, data access, and smoke-test command.

## Ethics And Governance

- `docs/ethics/data-governance.md`: sensitivity, retention, sharing, and publication policy.
- Dataset/source pages updated with relevant constraints.

## Reproduction

- `repro_outputs/SUMMARY.md`
- `repro_outputs/COMMANDS.md`
- `repro_outputs/LOG.md`
- `repro_outputs/PATCHES.md`
- `repro_outputs/status.json`

## Experiments

- `experiments/registry.csv` updated.
- `experiments/<run_id>.md` created for human-readable context.
- `experiments/campaigns/<campaign_id>.md` created for autonomous or overnight experiment campaigns.
- `experiments/campaigns/frontier-results.tsv` or a campaign-specific frontier ledger updated for `keep`, `discard`, and `crash` decisions.
- `wiki/templates/experiment-page.md` used when a run changes project knowledge or claims.
- Machine logs stay in `train_outputs/`, `explore_outputs/`, or `debug_outputs/`; curated exports move to `outputs/`.
- Trusted, exploratory, and failed runs are clearly separated.
