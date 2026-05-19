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
6. Extract claims, methods, datasets, limitations, and open questions.
7. Update `wiki/index.md`, `wiki/log.md`, and any affected concept, claim, method, or question pages.

## Source ID

Prefer stable slugs:

- `smith-2024-topic`
- `arxiv-2401-12345`
- `doi-10-1145-short-topic`
- `proposal-telegram-marketplace-2026`

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
- `wiki/sources/<source_id>.md`
- `wiki/index.md`
- `wiki/log.md`
