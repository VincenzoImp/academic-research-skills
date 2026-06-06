# Per-Source Synthesis Template

A theme-first SOTA still needs a uniform, inspectable record for each core or
supporting source. Use this template so deep readings stay comparable across the
whole review and so the thematic synthesis and survey can cite consistent
evidence. This is the sanctioned per-source format: it is structured,
evidence-bound, and feeds the synthesis, so it is not a laundry list.

## When To Use

- every `core` and `supporting` source after a full linear reading
- skip for `background` sources; an annotated-bibliography card is enough
- store as `sota/paper-syntheses/<source_id>.md` in standard
  `create-academic-research` projects; use `sota/<review>/paper-syntheses/`
  only when the project intentionally maintains multiple named reviews

## Required Header

```md
Source ID:
Citation key:
Source type:
Evidence status:        full linear reading | partial | abstract-only
Local PDF:
Local Markdown:
Linear reading copy:
Reading log row:
Identifiers:
```

## Required Sections

```md
## Why This Source Matters
## Linear Reading Notes
## Research Questions / Problem
## Data And Sample
## Methodology
## Methodological Assumptions
## Key Findings
## Limitations And Validity Threats
## Relevance To This Project
## Project-Specific Delta
## Possible Research Directions
## Citation Leads To Chase
## Claims We Can Safely Make
## Claims We Must Not Make
## Open Follow-Up Checks
```

## Rules

- write the synthesis only after a full linear reading of the full text, not the
  abstract
- the safe-claims and must-not-claim sections must reflect what the full text
  supports; abstract-only sources cannot fill them
- exact numbers, tables, and quotations must be checked against the native PDF
  before they enter the synthesis or survey
- keep interpretation separate from what the source states
- link each synthesis from the literature-matrix row for the same `source_id`
- `Linear Reading Notes` should record section-by-section observations, not a
  generic abstract summary
- `Citation Leads To Chase` should name backward references, forward-citation
  targets, datasets, benchmarks, authors, venues, or terms that may expand the
  graph
- `Project-Specific Delta` should state what this source leaves open for the
  current research idea and what would falsify that opportunity
