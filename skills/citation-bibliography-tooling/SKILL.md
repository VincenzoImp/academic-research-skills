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
7. For manuscripts, compare in-text citations against bibliography entries and
   claim pages.

## Citation Key Rules

Prefer stable, readable keys:

- `smith2024platform`
- `arxiv240112345`
- `doi10-1145-short-topic`

Do not change citation keys in a paper without updating all references.

## Quality Gate

Flag:

- citation supports the wrong claim
- citation exists only in bibliography but not source ledger
- source ledger row has no identifier or provenance note
- preprint and published version are conflated
- citation count or venue rank is used as evidence without context
