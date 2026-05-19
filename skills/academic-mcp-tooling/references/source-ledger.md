# Source Ledger

Maintain `sources/source-ledger.csv` for every source that becomes part of the
project evidence base.

## Required Columns

- `source_id`: stable slug, usually `author-year-short-title` or external ID.
- `type`: paper, preprint, report, dataset, proposal, web, code, interview, note.
- `title`
- `authors`
- `year`
- `venue`
- `identifiers`: DOI, arXiv, PMID, OpenAlex, S2, DBLP, Zotero key.
- `raw_path`: local immutable source path.
- `derived_path`: Markdown, JSON, or extracted text path.
- `bib_path`: BibTeX/RIS/CSL path if available.
- `status`: queued, ingested, summarized, audited, superseded, rejected.
- `relevance`: seed, core, supporting, background, excluded.
- `evidence_level`: primary, secondary, tertiary, unknown.
- `quality_notes`
- `added_on`
- `last_checked`

## Status Rules

- `queued`: source exists but has not been read.
- `ingested`: source has a source page and ledger row.
- `summarized`: source summary has claims, methods, limitations, and citations.
- `audited`: bibliographic metadata and important claims were checked.
- `superseded`: a newer or better source replaces this one; keep the record.
- `rejected`: inspected and excluded; record why.
