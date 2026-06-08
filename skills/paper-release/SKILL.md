---
name: paper-release
description: Use when creating paper-specific release manifests, source maps, locks, checksums, metadata, staged artifacts, or badge-ready public packages.
license: MIT
---

# Paper Release

Build release packages from canonical project paths without creating stale
copies.

## Read First

- `references/repository-contract.md`
- `references/workflow-stage-contracts.md`
- `references/artifact-open-science-policy.md`

## Workflow

1. Run `npm run workflow:release` when available.
2. Read `paper_releases/release-ledger.csv`, `release.yaml`, `source-map.csv`, release-plan lock, checksums, metadata, frame decision, and included contribution paths.
3. Stage files from canonical sources. Do not hand-edit staged release files as evidence.
4. Generate or update checksums, metadata, smoke tests, reviews, and archive state.

## Review Loop

Review source maps, checksums, metadata, smoke tests, anonymization mode, badge
profiles, and stale files. Regenerate and re-review until clean.

## Handoff

Hand off release packages to submission, artifact evaluation, or public archive
only after release review passes.
