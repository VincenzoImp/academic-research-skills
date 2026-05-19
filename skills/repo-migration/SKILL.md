---
name: repo-migration
description: Use when migrating messy academic research repositories, downloaded archives, proposal folders, ad hoc notebooks, scripts, datasets, or paper assets into the standard research project structure.
license: MIT
---

# Repo Migration

Migrate bad research repos without losing provenance. The first pass should make
the repository understandable before trying to improve scientific quality.

## Read First

- `references/repository-contract.md`
- `references/repo-migration-policy.md`
- `references/output-contracts.md`

## Workflow

1. Snapshot current state with `git status --short` and a file inventory.
2. Classify files as sources, data, code, notebooks, outputs, reports, configs,
   credentials, generated caches, or unknown.
3. Move immutable research sources into `sources/`, `reports/`, or `data/raw/`.
4. Move repeatable code into `src/` and thin entrypoints into `scripts/`.
5. Keep notebooks in `notebooks/` only when they are exploratory or narrative.
6. Separate trusted, exploratory, training, analysis, and debug outputs.
7. Add source ledger rows and wiki pages for important papers, proposals, and datasets.
8. Record unresolved questions in `wiki/open_questions.md` instead of guessing.
9. Run repository structure checks and tests.

## Preserve

- original filenames in ledger notes when renaming
- archive paths and extraction paths
- proposal versions
- command history if present
- data provenance and access constraints

## Do Not

- Rewrite scientific logic while doing structural migration unless required to
  keep tests runnable.
- Delete suspicious files without user approval.
- Promote notebook-only results to final claims without reproduction.
