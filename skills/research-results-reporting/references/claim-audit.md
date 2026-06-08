# Claim Audit Reference

Use claim audits before publishing, submitting, or relying on important synthesis.

## Claim Classes

- `bibliographic`: title, author, venue, year, DOI, arXiv ID.
- `descriptive`: what a source says or does.
- `methodological`: dataset, model, method, protocol, metric, sample.
- `comparative`: better/worse, earlier/later, larger/smaller, SOTA claims.
- `causal`: X causes Y, intervention effects, mechanisms.
- `interpretive`: implication, explanation, theoretical reading.
- `result`: numerical metric, p-value, benchmark, table, graph.

## Verdicts

- `supported`: direct evidence in cited source.
- `partially-supported`: source supports a narrower or weaker statement.
- `unsupported`: no located evidence.
- `contradicted`: located evidence conflicts with claim.
- `wrong-source`: claim may be true but citation does not support it.
- `needs-human`: requires domain judgment, paywalled source, or unavailable data.

## Rules

- A citation after a paragraph does not automatically support every sentence.
- Exact numbers need exact source locations or experiment artifacts.
- Comparative claims need comparison set, date, metric, and scope.
- Do not turn "no evidence found" into "false"; mark unsupported.
- If a claim depends on a PDF conversion, check the PDF or source metadata before finalizing.
