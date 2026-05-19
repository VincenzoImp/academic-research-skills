# Citation Bibliography Policy

Use this when bibliography records, source ledgers, manuscripts, and claims must
agree.

## Canonical Files

- `sources/bib/references.bib`: canonical project bibliography.
- `sources/bib/citation-audit.csv`: audit ledger for missing, duplicate, unused,
  unsupported, or stale citations.
- `sources/source-ledger.csv`: evidence ledger linking source IDs to files and metadata.
- `sources/metadata/`: raw API metadata from Crossref, OpenAlex, Semantic
  Scholar, arXiv, PubMed, DBLP, Zotero, or publisher pages.

## Audit Columns

`citation_key,status,issue,source_id,claim_or_location,expected_fix,checked_on`

Recommended statuses:

- `ok`
- `missing-bib`
- `missing-source-ledger`
- `unused`
- `duplicate`
- `wrong-support`
- `stale-version`
- `needs-human`

## Identifier Priority

Use DOI when available, then arXiv ID, PMID/PMCID, OpenAlex ID, Semantic Scholar
ID, DBLP key, ISBN, stable publisher URL, or archived URL.

## Versioning

Do not conflate preprints and published papers. Link them in metadata and decide
which version supports each claim.
