---
name: citation-claim-audit
description: Use when verifying citations, bibliography, manuscript claims, source support, factual accuracy, numerical results, citation drift, or evidence provenance in academic work.
license: MIT
---

# Citation Claim Audit

Audit claims before they become paper text, README claims, or wiki synthesis.

## Read First

- `references/claim-audit.md`
- `references/output-contracts.md`

## Workflow

1. Extract atomic claims.
2. Classify each claim: bibliographic, descriptive, methodological, comparative, causal, interpretive, or result.
3. Locate cited evidence and, when needed, the raw PDF or experiment artifact.
4. Assign a verdict.
5. Record unsupported, contradicted, or over-broad claims.
6. Propose minimal edits that preserve the supported meaning.

## Audit Table

Use this structure in `analysis_outputs/claim-audit.md` or CSV:

| claim_id | claim | class | cited_source | evidence_path | verdict | fix |
|---|---|---|---|---|---|---|

## Verdict Discipline

- `supported`: exact or clearly entailed by evidence.
- `partially-supported`: true only in narrower scope.
- `unsupported`: no evidence found.
- `contradicted`: evidence conflicts.
- `wrong-source`: source does not support the claim.
- `needs-human`: inaccessible or needs domain judgment.

## Do Not

- Fabricate missing references.
- Treat citation count as truth.
- Trust PDF-to-Markdown for exact numbers without checking the source.
- Collapse "unsupported" into "false".
- Strengthen claims during editing.

