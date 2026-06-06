# Systematic Review Policy

Use this when a review needs explicit, reproducible search and screening.

## Review Types

- `narrative`: useful synthesis, not exhaustive.
- `scoping`: broad map of a field, transparent but often less restrictive.
- `systematic`: pre-defined search, screening, inclusion/exclusion, and counts.
- `mapping`: structured categorization of a literature space.

Label the review type before presenting results.

## Controlled Exclusion Reasons

Use short reasons in `sota/screening-decisions.csv`:

- `out-of-scope`
- `wrong-population`
- `wrong-method`
- `wrong-outcome`
- `not-peer-reviewed`
- `duplicate`
- `no-full-text`
- `not-english`
- `superseded`
- `low-relevance`
- `quality-concern`

## Search Completeness

Keyword and database search is the first pass, not the whole search. For
systematic and scoping reviews, also run citation chasing (backward references
and forward citations) from seeds and included works, and record the achieved hop
depth. Report keyword databases, citation-graph sources, and search dates
together. Follow the citation-chasing procedure for backward and forward
expansion.

## Full-Text Of Included Works

`no-full-text` is an exclusion reason at screening. For a work that passes
screening but whose legal full text is not yet retrieved, mark it
`full-text-pending` as a tracked limitation rather than dropping it silently or
relying on its abstract for durable claims.

## Minimum Artifacts

- `sota/search-strategy.md`
- `sources/metadata/` raw exports, including citation-chasing exports
- `sota/screening-decisions.csv`
- `sota/prisma-flow.md`
- `sota/literature-matrix.csv`
- `sota/citation-chasing-log.csv`
- `sota/reading-log.csv`
- `sota/synthesis.md`

## Evidence Rule

Counts and conclusions must name the search date and database scope. Do not use
"no studies exist" unless the search strategy actually supports that scope.
