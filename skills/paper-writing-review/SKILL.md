---
name: paper-writing-review
description: Use when drafting, revising, structuring, reviewing, polishing, or preparing academic manuscripts, proposals, related work, LaTeX papers, abstracts, introductions, methods, limitations, or submission-ready scholarly text.
license: MIT
---

# Paper Writing Review

Write and revise scholarly text from project evidence, not from free-floating
memory. Use this for papers, proposals, related work, abstracts, introductions,
methods, limitations, and internal writing review. Use
`rebuttal-revision-strategy` for reviewer response letters and rebuttal plans.

## Read First

- `references/repository-contract.md`
- `references/claim-audit.md`

## Inputs

Before writing, identify:

- target artifact: proposal, paper, related work, abstract, section draft, or slides
- venue or audience
- citation style or LaTeX template
- source corpus
- intended contribution
- claims that must be preserved or avoided

If any of source corpus, contribution, or claim support is missing, produce a
writing plan or evidence-gap list before drafting durable scholarly prose.

## Writing Rules

- Use `sota/`, `wiki/`, and `sources/` as evidence.
- Preserve citation keys, labels, equations, and references unless asked to edit them.
- Mark missing evidence instead of inventing citations.
- Keep limitations and scope explicit.
- Separate author claims from cited claims.
- For related work, synthesize themes instead of listing papers mechanically.
- Use hedging that matches evidence strength; do not upgrade "suggests" to
  "demonstrates" without direct support.
- Keep reviewer-facing artifacts honest: name limitations, failed runs, missing
  baselines, and unverified claims.

## Review Modes

- `structure`: argument flow, section order, contribution clarity.
- `method`: validity of research design, dataset, metric, and comparison.
- `evidence`: claim support and citation alignment.
- `style`: clarity, concision, academic tone.
- `submission`: format, figures, tables, bibliography, reproducibility statement.
- `latex-audit`: compile, bibliography, figure/table, label/reference, and
  venue-format checks for existing LaTeX projects.
- `related-work`: thematic synthesis, comparison, and gap derivation from the
  SOTA matrix.

## Manuscript Workflow

1. Read target venue or artifact requirements.
2. Load only relevant project evidence.
3. Make a section plan with claims and required sources.
4. Draft or revise section-by-section.
5. Run citation/claim audit on new or changed claims.
6. Produce unresolved evidence gaps and next checks.

For existing LaTeX/Typst manuscripts, default to diagnosis and comment-style
recommendations before source editing. Keep build fixes, bibliography changes,
and prose rewrites separate.

## Output

For major revisions, produce:

- summary of changes
- unresolved evidence gaps
- claim/citation audit notes
- suggested next checks
- changed files or sections, if edits were made
