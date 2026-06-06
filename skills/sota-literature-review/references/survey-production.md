# Survey Production

Turn a collected SOTA into a survey-style narrative plus a defensible research
agenda. Run this after sources are ingested, full-text read, and synthesized, not
from raw search results.

## Inputs

- `sota/literature-matrix.csv`: complete structured rows
- per-source syntheses for core and supporting sources
- `sota/synthesis.md` themes and `sota/gaps.md`
- `sources/bib/references.bib`: canonical bibliography

## Pipeline

1. Confirm coverage: keyword search plus citation chasing reached saturation and
   the matrix has no unreviewed core or supporting rows.
2. Cluster sources into methodological and thematic families from the matrix.
3. Write the thematic synthesis: established findings, contested claims, method
   families, dataset or benchmark differences, missing baselines, contradictions.
4. Run the BibTeX gate: every cited source has a canonical entry in
   `sources/bib/references.bib`, a stable citation key, identifiers, and an
   aligned source-ledger and matrix row.
5. Draft the LaTeX survey narrative section by section in
   `reports/paper/sota-survey.tex`, citing BibTeX keys, source IDs, or wiki
   claim pages, not free-floating memory. Hand prose work to
   `paper-writing-review`.
6. Derive the research agenda: open gaps, candidate directions, methodologies,
   artifact implications, and feasibility, each tied to evidence and a failure
   condition. Hand framing to `research-design-positioning`.
7. Run `citation-claim-audit` on every durable survey claim before it is final.

## BibTeX Gate

Before any survey or related-work draft is called usable:

- every cited key resolves in `sources/bib/references.bib`
- each bibliography entry has verified title, authors, year, venue, and stable
  identifier when available
- preprint and published versions are reconciled or intentionally kept separate
- every bibliography entry used in the survey maps to `source_id`
- `sources/bib/citation-audit.csv` records duplicates, missing identifiers,
  unsupported citations, and manual-verification needs

## LaTeX Structure

Use `reports/paper/sota-survey.tex` for a survey or survey-like SOTA chapter:

- search protocol and review scale
- methodological families
- datasets, benchmarks, metrics, and baselines
- established findings and contested claims
- limitations and validity threats in the evidence base
- implications for the current research idea
- research agenda with evidence, nearest prior work, method, risk, and status

## Output

- `reports/paper/sota-survey.tex` survey draft with sections, related work, and directions
- `sota/synthesis.md` and `sota/gaps.md` updated
- `sources/bib/references.bib` and `sources/bib/citation-audit.csv` complete and
  aligned with cited `source_id` values
- a directions table: direction, evidence, nearest prior work, method, risk,
  status

## Rules

- every cited paper in the survey must have a bibliography entry and a matrix row
- do not promote abstract-only or unaudited claims into the survey narrative
- report search and chasing scope, databases, dates, and blind spots; do not
  claim exhaustive coverage beyond the recorded protocol
- keep the bibliography best-effort canonical: verified identifiers, no fabricated
  entries, preprint and published versions reconciled
- the research agenda must be grounded in the current project's idea, not a
  generic future-work list
