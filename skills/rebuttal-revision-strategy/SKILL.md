---
name: rebuttal-revision-strategy
description: Use when responding to academic reviewers, planning revisions, writing rebuttals, mapping reviewer concerns, deciding concede/defend/reframe actions, or preparing camera-ready changes.
license: MIT
---

# Rebuttal Revision Strategy

Use this after receiving reviews or internal adversarial review. The goal is to
respond precisely, respectfully, and strategically without overstating evidence.

## Read First

- `references/repository-contract.md`
- `references/peer-review-policy.md`
- `references/research-positioning-policy.md`
- `references/workflow-stage-contracts.md`

## Workflow

1. Run `npm run workflow:response` when available.
2. Work inside `paper_submissions/templates/review-rounds/<round>/` or the
   submission-specific review-round folder.
3. Split every review into atomic concerns.
4. Record concerns in `concern-map.csv`.
5. Classify each concern: misunderstanding, valid limitation, missing evidence,
   writing issue, incorrect claim, scope mismatch, or unfixable weakness.
6. Decide action: concede, clarify, add evidence, reframe, defend, or defer.
7. Route reviewer-requested new scientific work through `linked-work.csv` into
   contribution, analysis, citation, or artifact workflows.
8. Track promised manuscript edits in `manuscript-change-map.csv`.
9. Draft response with direct answer first, then evidence, then promised change.
10. Avoid new claims that cannot be added to the paper or artifact.
11. Update manuscript, validity notes, and claim records only after linked work
    passes its own review gate.

## Response Pattern

Use this structure:

1. thank and acknowledge
2. answer the exact concern
3. cite evidence or planned change
4. state manuscript location to change
5. avoid argumentative tone

## Do Not

- Ignore a reviewer concern because it seems unfair.
- Promise experiments that cannot be completed before the deadline.
- Defend a claim that the evidence does not support.
- Write a response that cannot be mirrored in the revised paper.

## Review Loop And Handoff

For each concern: map, classify, link work, revise, verify evidence, draft
response, review, fix, and re-review. Handoff only response packages whose
concern map, linked-work map, manuscript-change map, and response text agree.
