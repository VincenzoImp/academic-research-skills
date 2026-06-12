---
name: develop-contribution
description: Use when creating a new contribution (analysis, experiment, dataset, software, reproduction) or regularizing a draft folder into badge compliance with its LaTeX report.
license: MIT
---

# Develop Contribution

Create or regularize one `contributions/<slug>/` folder: badge-general
compliant, self-contained, with a `report/report.tex` detailed enough that
paper writing never needs to re-read the code.

## Read First

- `contributions/README.md` — the badge-general contract
- `survey/survey.pdf`, gaps section — when positioning a new contribution
- `references/methodology.md` — evaluation, statistics, figure discipline
- `references/experiments.md` — run logs and autonomous campaigns
- `references/reproduction.md` — reproducing external work
- `references/ethics.md` — data red flags

## Before Building (both modes)

Fill the Positioning section of the contribution README:

- the claim this contribution will support
- the delta vs the nearest prior work (cite survey/SOTA citekeys)
- the evidence plan: what will be measured or collected, and how
- the falsifiability condition: what outcome would refute the claim

If the claim has no evidence path, stop and discuss with the user.

## Create Mode

1. Copy `contributions/_template/` to `contributions/<slug>/` (kebab-case
   slug).
2. Python code? Write the contribution's own `pyproject.toml` (name,
   requires-python, dependencies), add `"contributions/<slug>"` to
   `[tool.uv.workspace] members` in the root `pyproject.toml`, run
   `uv sync` from the root. Genuinely conflicting dependencies → move the
   path to `exclude`, create a local venv, document it in the README.
3. Develop inside the folder — free-form structure (`src/`, `data/`,
   `figures/`, `outputs/`, notebooks). Follow `references/methodology.md`
   for any evaluation; keep a run log per `references/experiments.md` for
   every run that supports a claim, including autonomous campaigns. For
   reproductions of external work, follow `references/reproduction.md`.
4. Fill the README badge checklist truthfully — every checked box has
   evidence inside the folder. Check data against `references/ethics.md`.
5. Write `report/report.tex`: motivation, positioning vs the SOTA (cite the
   root `.bib`), method, setup, results with figures/tables, limitations.
   Build it: `make contribution C=<slug>`.
6. Run `make check`.

## Regularize Mode

1. Inventory the draft folder: what exists, what it claims, what is missing
   against the badge checklist.
2. Reorganize in place — keep provenance (note original filenames when
   renaming), capture the environment, verify the run path works
   end-to-end, record data provenance and ethics flags.
3. Continue with Create Mode steps 4–6.

## Rules

- Self-contained: no imports from other contributions; tooling worth
  sharing becomes its own contribution referenced in the README.
- Exploratory results never masquerade as confirmed evidence — label them.
- Negative results are results: report them in report.tex.

## Done When

- Badge checklist fully and truthfully checked, `report.pdf` built,
  workspace coherent, `make check` passes
