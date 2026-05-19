---
name: adversarial-peer-review
description: Use when reviewing academic papers, proposals, experiments, claims, related work, novelty, methodology, or manuscripts as a severe but fair peer reviewer before submission.
license: MIT
---

# Adversarial Peer Review

Review as a serious top-venue reviewer: skeptical, specific, evidence-based, and
fair. The goal is to find the objections that would block acceptance before
external reviewers do.

## Read First

- `references/peer-review-policy.md`
- `references/claim-audit.md`
- `references/cs-methodology-evaluation-policy.md`

## Workflow

1. Identify target venue or assumed review culture.
2. Read the paper/proposal/manuscript claim-first: abstract, introduction,
   contributions, experiments, related work, conclusion.
3. List acceptance-critical claims and what evidence supports each.
4. Attack novelty, significance, correctness, methodology, clarity, ethics, and reproducibility.
5. Separate fatal flaws, major weaknesses, minor issues, and presentation issues.
6. Produce reviewer-style scores only when the user asks or the venue requires them.
7. Save reusable findings in `reports/reviews/` or `wiki/templates/reviewer-concern-page.md` derived pages.

## Review Standard

Every major criticism should include:

- exact claim or section
- why it matters
- evidence from paper/source/run
- what would fix or weaken the concern

## Do Not

- Be performatively harsh without evidence.
- Suggest impossible experiments without labeling them as optional.
- Let writing polish hide methodological weakness.
- Accept citation volume as proof of related-work coverage.
