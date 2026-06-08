---
name: paper-framing
description: Use when selecting a venue-aware paper frame, argument map, evidence map, contribution set, release plan, outline, or frame decision.
license: MIT
---

# Paper Framing

Choose what paper should exist from reviewed contributions before writing it.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/venue-strategy-policy.md`

## Workflow

1. Run `npm run workflow:frame` when available.
2. Read `paper_frames/frame-ledger.csv`, frame contract, selected contributions, argument map, evidence map, venue fit, badge fit, compliance fit, release plan, outline, and prior reviews.
3. Compare possible framings by venue, track, audience, contribution coherence, evidence strength, badge targets, and release implications.
4. Record accepted, rejected, or held decisions in `paper_frames/templates/decision.md` or the frame-specific decision file.

## Review Loop

Review each candidate frame for novelty, fit, evidence, contribution load,
release feasibility, badge feasibility, and narrative risk. Iterate until the
decision is defensible.

## Handoff

Hand off accepted frames to `paper-release` and `paper-writing-review`.
