# Document Conversion Policy

Use this when a source must be converted into Markdown, text, extracted tables,
figures, or other derived artifacts.

## Destination Map

| Input | Native destination | Derived destination |
|---|---|---|
| paper PDF | `sources/pdfs/` | `sources/markdown/`, `sources/assets/` |
| proposal PDF/DOCX | `reports/proposal/` | `sources/markdown/` if used as evidence |
| web article | `sources/metadata/` or `sources/markdown/` | `wiki/sources/` |
| dataset documentation | `data/raw/` or `data/external/` | `docs/data_dictionary/`, `wiki/sources/` |
| scanned document | native folder | OCR Markdown plus quality report |

## Conversion Ledger

Append to `sources/conversion-ledger.csv`:

- `source_id`
- `input_path`
- `output_path`
- `tool`
- `command_or_config`
- `conversion_date`
- `quality`
- `checked_pages`
- `known_issues`

## Quality Labels

- `good`: structure, tables, and identifiers are usable after spot checks.
- `usable-with-checks`: narrative text is useful, exact evidence requires native checks.
- `poor`: use only for rough discovery; do not cite derived text.

## OCR Notes

OCR requires explicit quality notes. Names, numbers, formulas, references, and
table cells are the highest-risk fields.
