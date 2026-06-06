---
name: document-conversion
description: Use when converting PDFs, DOCX, HTML, scanned papers, reports, proposals, tables, or figures into Markdown, text, extracted assets, or quality reports for an academic research repository.
license: MIT
---

# Document Conversion

Convert documents into useful reading copies without weakening provenance. The
native document remains the source of truth; Markdown is a derived convenience
layer for search, synthesis, and LLM reading.

## Read First

- `references/repository-contract.md`
- `references/document-conversion-policy.md`
- `references/pdf-markdown-policy.md`
- `references/source-ledger.md`

## Workflow

1. Identify document type, provenance, identifiers, language, and whether OCR is needed.
2. Preserve the native file under `sources/pdfs/`, `reports/`, or `data/raw/`.
3. Pick the least lossy converter available: Docling/Nutrient-style PDF tools,
   `pdftotext`, PyMuPDF, OCR, Pandoc, or a project-specific parser.
4. Save Markdown to `sources/markdown/<source_id>.md` when it is a research source.
5. When a source needs cover-to-cover reading, also save a linear reading copy
   under `sources/markdown-linear/<source_id>.md`: single-column, reading order,
   suitable for full sequential reading.
6. Save extracted figures/tables/assets under `sources/assets/<source_id>/`.
7. For SOTA core/supporting papers, record the linear reading copy path in
   `sota/reading-log.csv` or the matrix row.
8. Append a row to `sources/conversion-ledger.csv`.
9. Update `sources/source-ledger.csv` and `wiki/sources/<source_id>.md`.

## Quality Gate

Before using converted text as evidence, sample-check:

- title, authors, year, DOI/arXiv/PMID
- headings and section order
- tables, equations, captions, and footnotes
- page numbers for exact claims
- OCR errors in names, numbers, formulas, and citations

Mark the conversion as `good`, `usable-with-checks`, or `poor`. Exact quotes,
numbers, metrics, and equations must be verified against the native file.

## Do Not

- Delete or overwrite the native source.
- Treat OCR text as authoritative.
- Mix extracted assets from multiple documents without source-specific folders.
- Use a converted Markdown file for citation-sensitive evidence without a quality note.
