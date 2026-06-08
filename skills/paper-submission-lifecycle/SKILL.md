---
name: paper-submission-lifecycle
description: Use when managing cover letters, submission checklists, submitted version locks, venue-system notes, decisions, correspondence, review rounds, or camera-ready state.
license: MIT
---

# Paper Submission Lifecycle

Manage venue communication state without treating it as scientific evidence.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/venue-strategy-policy.md`

## Workflow

1. Run `npm run workflow:submission` when preparing a submission.
2. Read `paper_submissions/submission-ledger.csv`, submission manifest, cover letter, checklist, submitted-version lock, venue-system notes, manuscript ledger, release ledger, and venue checklist.
3. Record submitted file checksums, venue system fields, anonymity mode, correspondence, decisions, review rounds, camera-ready state, and archive status.
4. Ensure cover letters reference only evidence already present in the manuscript claim map and citation audit.

## Review Loop

Review submission files, cover letter, checklist, lock, claims, citations,
release package, and venue constraints. Fix and re-review until internally
consistent.

## Handoff

Hand off decisions and reviewer comments to `rebuttal-revision-strategy`. New
scientific work requested by reviewers goes through contribution, analysis,
citation, or artifact workflows.
