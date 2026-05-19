# Output Contracts

Use these contracts to avoid ambiguous "done" states.

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

## Ideation And Positioning

- `docs/methodology/research-design.md`: contribution claims and failure conditions.
- `wiki/templates/contribution-claim-page.md` derived pages when reusable.
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
- `sota/literature-matrix.csv`: structured paper table.
- `sota/synthesis.md`: current state of the art and gap analysis.
- `sota/gaps.md`: open opportunities and unresolved disagreements.
- `wiki/contradictions.md` updated when sources conflict.

## Claim Audit

- `analysis_outputs/claim-audit.md`: claim-by-claim results.
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
- reviewer concerns linked to claims, methods, venue strategy, or rebuttal plan.

## Rebuttal And Revision

- `reports/rebuttal/<round_id>.md`
- revised manuscript sections or planned changes linked to reviewer concerns.

## Artifact And Open Science

- `artifacts/artifact-checklist.md`
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
- Machine logs stay in `train_outputs/`, `explore_outputs/`, or `debug_outputs/`; curated exports move to `outputs/`.
- Trusted, exploratory, and failed runs are clearly separated.
