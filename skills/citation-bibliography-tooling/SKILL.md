---
name: citation-bibliography-tooling
description: Use when normalizing BibTeX, RIS, CSL JSON, citation keys, DOI/arXiv/PMID metadata, references, unused citations, missing citations, or bibliography quality for papers and SOTA work.
license: MIT
---

# Citation Bibliography Tooling

Keep bibliographic data machine-checkable and aligned with claims. Citation
metadata is not evidence by itself, but it is the backbone for traceability.

## Read First

- `references/repository-contract.md`
- `references/citation-bibliography-policy.md`
- `references/source-ledger.md`
- `references/claim-audit.md`

## Workflow

1. Inventory existing BibTeX, RIS, CSL JSON, Zotero exports, LaTeX citations,
   Markdown citations, and source metadata.
2. Normalize identifiers: DOI, arXiv ID, PMID/PMCID, OpenAlex ID, Semantic
   Scholar paper ID, DBLP key, ISBN, URL.
3. Deduplicate records by identifier first, then title plus author/year.
4. Store canonical bibliography in `sources/bib/references.bib`.
5. Update `sources/bib/citation-audit.csv` with missing, duplicate, unused, and
   unsupported citations.
6. Sync `sources/source-ledger.csv` and `sota/literature-matrix.csv` with stable
   `source_id` values.
7. For SOTA survey work, enforce the BibTeX gate before writing:
   every cited source has a verified entry, source ledger row, matrix row, and
   stable citation key.
8. For manuscripts, compare in-text citations against bibliography entries and
   claim pages.

## Canonical Metadata Order

Prefer metadata from:

1. DOI or publisher landing page.
2. arXiv, PubMed/PMCID, or other canonical identifier page.
3. Crossref, OpenAlex, Semantic Scholar, DBLP, or Zotero imported from a verified
   identifier.
4. Google Scholar only as manual discovery/fallback, not as final metadata.

For every important citation, verify title, first author, year, venue, and
identifier. If only a search result or scraped page exists, mark the entry
`needs-human` or `manual-verification` in the audit file.

## Citation Key Rules

Prefer stable, readable keys:

- `smith2024topic`
- `arxiv240112345`
- `doi10-1145-short-topic`

Do not change citation keys in a paper without updating all references.

## BibTeX Lifecycle

- `validate`: every in-text key resolves, no duplicate keys, no missing required
  fields for the entry type.
- `dedupe`: merge preprint/published versions only when the relationship is
  verified; preserve both when they support different claims.
- `harvest`: add missing references only from located papers; never generate a
  plausible BibTeX entry from memory.
- `format`: normalize indentation, braces for protected terms, DOI/URL fields,
  and venue names without changing scientific meaning.
- `sync`: update `sources/source-ledger.csv` and any source or claim pages that
  reference changed keys.
- `survey-gate`: verify every citation in `reports/paper/sota-survey.tex`
  resolves to `sources/bib/references.bib` and a `sota/literature-matrix.csv`
  row before claim audit.

## Quality Gate

Flag:

- citation supports the wrong claim
- citation exists only in bibliography but not source ledger
- source ledger row has no identifier or provenance note
- preprint and published version are conflated
- citation count or venue rank is used as evidence without context
- citation metadata was verified but the cited claim was not checked
