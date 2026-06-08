---
name: research-agenda
description: Use when converting SOTA gaps, survey claims, and evidence limits into prioritized research opportunities, contribution ideas, and publishability decisions.
license: MIT
---

# Research Agenda

Create a reviewed agenda of work worth doing. Do not treat every gap as a
contribution.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/research-positioning-policy.md`

## Workflow

1. Run `npm run workflow:agenda` when available.
2. Read `research_agenda/agenda-contract.md`, `sota/gaps.md`, `sota/sota-claim-ledger.csv`, and `survey/survey-claim-ledger.csv`.
3. Add candidate opportunities to `research_agenda/opportunity-ledger.csv`.
4. Evaluate novelty, feasibility, evidence, expected contribution, failure condition, risk, cost, publishability, and release constraints.
5. Write direction records in `research_agenda/directions/` only for opportunities that survive initial review.
6. Store final agenda synthesis in `research_agenda/final/`.

## Review Loop

Review each opportunity adversarially, fix weak framing or evidence gaps, and
re-review until the decision is accepted, rejected, or held with a clear
rationale.

## Handoff

Hand off accepted opportunities to `contribution-package` with linked SOTA and
survey claim IDs.
