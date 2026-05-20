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
4. Check the paper against nearest prior work and target venue expectations.
5. Attack novelty, significance, correctness, methodology, clarity, ethics, and reproducibility.
6. Separate fatal flaws, major weaknesses, minor issues, and presentation issues.
7. Produce reviewer-style scores only when the user asks or the venue requires them.
8. Save reusable findings in `reports/reviews/` or `wiki/templates/reviewer-concern-page.md` derived pages.

## Review Lanes

Use multiple lanes even when writing one consolidated review:

- editor lane: venue fit, contribution threshold, audience, desk-reject risks
- methodology lane: design, datasets, baselines, metrics, statistics, ablations
- domain lane: related work, terminology, prior art, missing comparisons
- adversarial lane: strongest counterargument, overclaiming, alternative explanations
- reproducibility/ethics lane: code/data access, artifact quality, privacy, licenses, dual use

If the user asks for a simulated panel, keep findings from lanes separate before
synthesis so the final decision cannot invent or duplicate reviewer concerns.

## Review Standard

Every major criticism should include:

- exact claim or section
- why it matters
- evidence from paper/source/run
- what would fix or weaken the concern
- severity: fatal, major, moderate, minor
- confidence and what would change the judgment

## Do Not

- Be performatively harsh without evidence.
- Suggest impossible experiments without labeling them as optional.
- Let writing polish hide methodological weakness.
- Accept citation volume as proof of related-work coverage.
- Edit the manuscript while acting as reviewer; produce a report and revision roadmap.
- Let an adversarial finding disappear during synthesis. If it is wrong, explain why.

## Output Contract

For deep reviews, write:

- `reports/reviews/<review-id>.md`
- executive summary and recommendation
- strengths with evidence
- weaknesses grouped by severity
- methodology/reproducibility assessment
- missing related work and gap-positioning issues
- questions for authors
- prioritized revision roadmap
