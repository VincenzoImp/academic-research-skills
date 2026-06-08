---
name: survey-synthesis
description: Use when turning reviewed SOTA claims into survey sections, survey outlines, thematic syntheses, methodology comparisons, gap maps, or survey claim ledgers.
license: MIT
---

# Survey Synthesis

Build surveys from reviewed SOTA claims, not from free-form memory.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/output-contracts.md`
- `references/claim-audit.md`

## Workflow

1. Run `npm run workflow:survey` when available.
2. Read `survey/survey-contract.md`, `survey/outline.md`, and `sota/sota-claim-ledger.csv`.
3. Plan sections before drafting. Name the SOTA claim IDs, source IDs, and role of each section.
4. Draft one section at a time in `survey/drafts/`.
5. Update `survey/survey-claim-ledger.csv` with claim text, evidence strength, limitations, contradictions, review status, and downstream status.
6. Move only reviewed clean sections into `survey/final/`.

## Review Loop

For each section: plan, draft, audit claims, review adversarially, fix, and
re-review. Continue until there are no unsupported claims, missing caveats,
stale citations, or section-order problems.

## Handoff

Hand off reviewed survey claims and final sections to `research-agenda`. Do not
create agenda opportunities directly inside survey prose.
