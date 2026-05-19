# PDF To Markdown Policy

Keep native PDFs and derived Markdown. Markdown is for search and synthesis; the
PDF remains the source of truth.

## Recommended Flow

1. Save the native PDF under `sources/pdfs/`.
2. Save bibliographic metadata under `sources/metadata/`.
3. Convert to Markdown under `sources/markdown/`.
4. Record conversion tool, command, date, and warnings in the source page.
5. Use Markdown for first-pass reading; check the PDF for quotes, equations, tables, and exact claims.

## Tool Order

1. Native text PDF: use `pdftotext`, `pymupdf`, or similar fast extraction.
2. Complex paper with tables/layout: use Docling.
3. Scanned or image-heavy source: use OCR and mark confidence.
4. MinerU or hosted converters: useful, but record external dependency and security/API risk.

## Warnings

- Converted Markdown can reorder columns, captions, footnotes, and tables.
- Do not cite a converted chunk as evidence without preserving the source path.
- For mathematical notation, verify against the PDF.
- For tables, save extracted CSV/JSON separately when values matter.
