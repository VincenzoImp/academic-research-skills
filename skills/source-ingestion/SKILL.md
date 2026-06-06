---
name: source-ingestion
description: Use when adding, reading, registering, or organizing research sources such as PDFs, arXiv papers, Zotero items, proposals, datasets, reports, archives, web pages, BibTeX, or source metadata.
license: MIT
---

# Source Ingestion

Ingest sources so future analysis compounds instead of rediscovering the same
document. The native source remains immutable; derived Markdown and wiki pages
are working artifacts.

## Read First

- `references/repository-contract.md`
- `references/source-ledger.md`
- `references/pdf-markdown-policy.md`

## Workflow

1. Identify source type, provenance, identifiers, and destination.
2. Store immutable originals under `sources/`, `data/raw/`, `data/external/`, or `reports/`.
3. If conversion is needed, hand off the conversion procedure to
   `document-conversion`; keep this workflow responsible for provenance and
   repository registration.
4. Add or update `sources/source-ledger.csv`.
5. Create or update `wiki/sources/<source_id>.md`.
6. For core/supporting sources, read the full text linearly end to end before
   summarizing, and record reading progress (source, range, status) in a reading
   log so deep reading is auditable and resumable. In `create-academic-research`
   projects, use `sota/reading-log.csv`.
7. Extract claims, methods, datasets, limitations, and open questions.
8. Update `wiki/index.md`, `wiki/log.md`, and any affected concept, claim, method, or question pages.

Preserve Project Quality during ingestion: raw sources stay immutable,
abstract-only records stay out of durable claim support, and derived reading
copies, SOTA syntheses, wiki pages, and bibliography entries are updated in
their own work zones instead of being mixed into ad hoc notes.

## Full-Text And Reading

- Prefer acquiring the full-text PDF for every source that will support a claim;
  abstract-only ingestion can seed a to-read queue but not durable evidence.
- Save a linear reading copy under `sources/markdown-linear/<source_id>.md` when
  the source needs cover-to-cover reading; keep the layout Markdown for tables
  and figures.
- For core/supporting sources, produce a structured per-source synthesis after
  reading, using the per-source synthesis template defined in the
  `sota-literature-review` skill, and store it under `sota/paper-syntheses/`
  unless the project has a more specific review folder.

## Evidence Record

For reusable sources, add an evidence record to the source page:

```md
Evidence ID:
Source type: full paper | preprint | dataset | experiment artifact | project note | abstract-only | webpage placeholder
Supports:
Contradicts:
Method / dataset / metric:
Limitation:
Project relevance:
Claim strength: speculative | observed | supported | strong
Allowed wording:
Forbidden stronger wording:
```

Abstract-only notes and webpage placeholders can update coverage or a to-read
queue, but they cannot support durable `wiki/`, SOTA, manuscript, or rebuttal
claims until stronger evidence is ingested.

## Source ID

Prefer stable slugs:

- `smith-2024-topic`
- `arxiv-2401-12345`
- `doi-10-1145-short-topic`
- `proposal-short-topic-2026`

## Conversion Handoff

- Preserve the native PDF.
- Save derived Markdown under `sources/markdown/<source_id>.md` only after the
  conversion workflow records quality and command details.
- Verify exact claims, tables, equations, and quotes against the native file.
- If extraction quality is poor, mark it and avoid using the Markdown for exact evidence.

## Output Contract

The task is not complete until these are updated when applicable:

- source file path
- derived Markdown path
- metadata or BibTeX path
- `sources/source-ledger.csv`
- `sota/reading-log.csv` for core/supporting full-text reads
- `sota/paper-syntheses/<source_id>.md` for SOTA core/supporting sources
- `wiki/sources/<source_id>.md`
- `wiki/index.md`
- `wiki/log.md`

## Wiki Maintenance

Keep synthesis separate from source notes. Source pages summarize the source;
topic, method, claim, gap, and contradiction pages belong elsewhere in `wiki/`
and must link back to supporting source pages. Append `wiki/log.md` with the
date, source ID, created/updated pages, and unresolved follow-up checks.
