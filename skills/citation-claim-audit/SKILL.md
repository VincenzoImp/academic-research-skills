---
name: citation-claim-audit
description: Use when verifying citations, bibliography, manuscript claims, source support, factual accuracy, numerical results, citation drift, or evidence provenance in academic work.
license: MIT
---

# Citation Claim Audit

Audit claims before they become paper text, README claims, or wiki synthesis.

## Read First

- `references/repository-contract.md`
- `references/claim-audit.md`
- `references/output-contracts.md`

## Workflow

1. Extract atomic claims.
2. Classify each claim: bibliographic, descriptive, methodological, comparative, causal, interpretive, or result.
3. Locate cited evidence and, when needed, the raw PDF or experiment artifact.
4. Check the exact support span: page, section, table, figure, equation, commit,
   run ID, dataset row, or source note.
5. Assign a verdict.
6. Record unsupported, contradicted, stale, or over-broad claims.
7. Propose minimal edits that preserve the supported meaning.

## Claim Scope

Audit all numerical, factual, comparative, causal, novelty, SOTA, and
methodology claims. For long documents, sample only when the user accepts the
sampling plan; final manuscript checks should cover every acceptance-critical
claim.

For `reports/paper/sota-survey.tex`, audit every durable survey claim that
summarizes the field, compares methods, states novelty, reports metrics, or
derives implications for the current research idea. Do not sample final SOTA
survey claims unless the user explicitly accepts a sampled audit.

## Audit Table

Use this structure in `analysis_outputs/claim-audit.md` or CSV:

| claim_id | claim | class | cited_source | evidence_path | support_span | verdict | fix |
|---|---|---|---|---|---|---|---|

## Verdict Discipline

- `supported`: exact or clearly entailed by evidence.
- `partially-supported`: true only in narrower scope.
- `unsupported`: no evidence found.
- `contradicted`: evidence conflicts.
- `wrong-source`: source does not support the claim.
- `needs-human`: inaccessible or needs domain judgment.
- `stale`: source was superseded or the result changed after the cited evidence.

## Fix Discipline

Prefer the smallest safe change:

- add missing citation only when the source was verified
- weaken wording to match source scope
- split one broad claim into narrower supported claims
- move speculation to limitations/future work
- remove the claim when support is absent
- add an experiment or analysis task when the claim belongs to project data

## Do Not

- Fabricate missing references.
- Treat citation count as truth.
- Trust PDF-to-Markdown for exact numbers without checking the source.
- Collapse "unsupported" into "false".
- Strengthen claims during editing.
- Accept a bibliography match as proof that the cited passage supports the claim.
