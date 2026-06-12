---
name: write-survey
description: Use when writing the project survey from the digested SOTA or updating it after the SOTA changed — grouping design, gaps and research directions, and coverage maintenance.
license: MIT
---

# Write Survey

Produce or maintain `survey/survey.tex`: the single, complete, detailed
reading reference for the whole SOTA. After reading the survey, nobody
should need to reopen syntheses or PDFs for the large majority of questions.

## Read First

- `survey/README.md` — the survey contract
- `sota/index.md` — what the SOTA currently contains
- `survey/coverage.md` — what the survey currently integrates
- `references/survey-content.md` — content checklist and style

## Mode Selection

- `survey/coverage.md` lists no citekeys → **create mode**.
- Otherwise → **update mode**. The user can force a full rewrite, which is
  create mode.

## Create Mode

1. **Hard gate: read every synthesis.** List all `digested` citekeys from
   `sota/index.md`, read every `sota/papers/<citekey>/synthesis.md`, and
   confirm the count matches before writing a single word of survey prose.
2. Design the grouping from what was read: themes, concepts, methodologies
   — whatever organization fits this SOTA best. Write the outline as LaTeX
   section comments first.
3. Write section by section: per group, discuss each paper's contributions
   and notable aspects in depth, compare approaches, name tensions and
   contradictions. Respect each synthesis's "Safe claims / do-not-claim"
   section. Cite with `\cite{<citekey>}` only; every key resolves in the
   root `references.bib`.
4. Write the mandatory final content section, **Gaps and Research
   Directions**, grounded in the full picture per
   `references/survey-content.md`.
5. Fill `survey/coverage.md` with every integrated citekey.
6. Build (`make survey`) and validate (`make check`). Fix all errors.

## Update Mode

1. Diff: `to_add` = digested keys in `sota/index.md` missing from
   `coverage.md`; `to_remove` = covered keys now `excluded` or gone.
2. Read the syntheses of `to_add` and the survey sections they belong to.
3. Integrate additions into the right groups — extend or restructure a
   group when the new papers change its internal logic; never just append.
4. Excise removals: delete their discussion, repair comparisons and
   transitions that referenced them, re-check the gaps section.
5. Update `coverage.md`, rebuild, run `make check`.

## Rules

- Every statement about a paper is supported by its synthesis (or its PDF
  when more depth is needed) — never by model memory.
- The survey is self-contained: detailed enough to replace re-reading the
  SOTA for most purposes. No length limit; completeness wins.
- Never edit `references.bib` from this skill: a missing entry means the
  SOTA work is incomplete — stop and report.

## Done When

- `coverage.md` equals the set of digested citekeys (or the user-approved
  subset), `survey.pdf` is rebuilt, `make check` passes
