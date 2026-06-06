---
name: research-project-maintenance
description: Use when creating, repairing, refactoring, validating, or documenting an academic research repository structure, including wiki, sources, SOTA, outputs, agent docs, tests, and reproducibility folders.
license: MIT
---

# Research Project Maintenance

Keep the repository usable as both software project and scholarly record.

## Read First

- `references/repository-contract.md`
- `references/output-contracts.md`
- `references/external-skill-recommendations.md`

## Maintenance Tasks

- create missing research folders
- update `AGENTS.md`
- update README layout
- update `configs/agent-stack.yaml`
- update `configs/capabilities.yaml`
- update `docs/agent/` workflow and capability records
- update `docs/agent/capability-profile.md`
- update `docs/agent/mcp-setup.md`
- update `docs/agent/project-quality.md`
- update wiki templates
- update `artifacts/badge-evidence-ledger.csv`
- add structural tests
- separate raw sources from derived outputs
- move notebook logic into `src/`
- add reproducibility commands
- keep maintenance changes scoped to the repository contract the user selected

## Structure Check

Validate at least:

- source and SOTA directories exist
- wiki index/log exist
- data policy is documented
- output directories are separated by trust level
- experiments have registry and record templates
- the Project Quality Contract is present and matches the repository layout
- badge evidence has an append-only ledger when the project targets artifact review
- MCP and skill recommendations are documented
- agent onboarding and capability profile are documented when the repo supports them
- generated or large files are ignored appropriately

## Project Quality Gate

Maintenance is responsible for keeping the project easy to continue after many
agent turns. Before finishing, confirm that new files live in the right work
zone, trusted outputs have provenance and validation, scratch or debug material
is not mixed with final outputs, and badge-related evidence is linked from
`artifacts/badge-evidence-ledger.csv` and `artifacts/artifact-checklist.md`.

## Do Not

- Flatten the repo into notebooks.
- Hide important workflow rules inside chat history.
- Put secrets, raw sensitive datasets, or model weights in git.
- Move user data without preserving provenance.
