---
name: artifact-open-science
description: Use when preparing academic artifacts, reproducibility packages, artifact evaluation submissions, open science materials, code/data release, model cards, dataset cards, or replication bundles.
license: MIT
---

# Artifact Open Science

Prepare research artifacts that reviewers and future researchers can actually
run, inspect, and cite. Use this for artifact evaluation, reproducibility
badges, camera-ready packages, and public release.

## Read First

- `references/artifact-open-science-policy.md`
- `references/repository-contract.md`
- `references/ethics-data-governance.md`

## Workflow

1. Identify artifact type: code, dataset, benchmark, model, UI, pipeline,
   reproduction package, or supplementary material.
2. Define what claims the artifact supports.
3. Create or update `artifacts/artifact-checklist.md`.
4. Ensure install/run instructions are fresh, minimal, and tested.
5. Separate public release files from private data, credentials, caches, and large local outputs.
6. Add license, citation, expected runtime, hardware, seed/config, and known limitations.
7. Link artifact claims to `experiments/`, `repro_outputs/`, `sources/`, and `wiki/`.

## Minimum Artifact Standard

- one-command smoke test or clear manual path
- environment file or dependency list
- data access/provenance instructions
- expected outputs
- result comparison against paper claims
- ethical and license constraints

## Do Not

- Release sensitive or license-restricted data without governance notes.
- Ship a notebook-only artifact when a script/CLI is expected.
- Claim reproducibility if only exploratory outputs are available.
