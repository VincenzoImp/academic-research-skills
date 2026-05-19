# Repo Migration Policy

Use this when a messy academic repository or downloaded archive must be moved
into the research project structure.

Preserve provenance first. The target structure should follow the user's chosen
repository contract.

## Classification

| Class | Destination |
|---|---|
| proposal, paper draft, slides | `reports/` |
| PDFs, articles, bibliographies | `sources/` |
| empirical datasets | `data/raw/` or `data/external/` |
| reusable package code | `src/` |
| thin command wrappers | `scripts/` |
| exploratory notebooks | `notebooks/` |
| final figures/tables | `outputs/` |
| reproduction evidence | `repro_outputs/` |
| exploratory runs | `explore_outputs/` |
| failure diagnostics | `debug_outputs/` |

## Migration Ledger

For non-trivial migrations, create `docs/agent/repo-migration-playbook.md` or
append a section with:

- original path
- new path
- reason
- provenance note
- unresolved issue

## Order

1. Inventory.
2. Preserve raw sources and data.
3. Move documentation and reports.
4. Move code.
5. Move outputs.
6. Update ledgers and wiki.
7. Run checks.

Do not improve methods and migrate layout in the same untracked step.
