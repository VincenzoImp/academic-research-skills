# Bibliography Rules

## Citekeys

- format `<firstauthorlastname><year><topicword>`, lowercase ASCII:
  `qin2022quantifying`
- stable: never change a citekey without first grepping `\cite{` usages
  across `survey/`, `contributions/`, `papers/` and updating all of them

## Authoritative version

- precedence: peer-reviewed published version > latest arXiv revision >
  other preprint
- when both exist, the bib entry cites the published version; the arXiv id
  stays in `metadata.yaml` as an alias
- never conflate preprint and published versions when their content differs
  in a way that matters to a claim; digest the version actually read and
  note the other in metadata

## Cross-validation

- query every configured scholarly MCP: semantic-scholar, dblp, and openalex
  always; arxiv for arXiv records
- field disagreements resolve by precedence:
  dblp (CS venues/BibTeX) > semantic-scholar > openalex > arxiv
- the DOI is the canonical identifier used to reconcile records across
  sources
- note unresolved conflicts as a comment in `metadata.yaml`
- never fill any bibliographic field from model memory; every field traces
  to an MCP record

## Provenance — the `verified:` block (mandatory)

- `bib_source`: the MCP whose record produced the BibTeX fields
- `record`: URL or id of that record
- `citation_graph_source`: MCP used for cites/cited_by (normally
  semantic-scholar)
- `s2_id`: Semantic Scholar paper id
- `date`: lookup date, YYYY-MM-DD

## Whitelist

Non-paper entries (software, datasets, standards) go under the `WHITELIST`
marker in `references.bib`; they need no SOTA folder and no synthesis.
