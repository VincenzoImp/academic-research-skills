---
name: package-artifacts
description: Use when packaging the artifacts of a paper for submission — assembling everything promised in the manuscript plus the venue's badge and artifact-evaluation requirements.
license: MIT
---

# Package Artifacts

Assemble `papers/<slug>/artifacts/`: the self-contained bundle a reviewer
or artifact-evaluation committee receives.

## Read First

- `papers/<slug>/venue.md` — the venue's badge/artifact requirements
- `papers/<slug>/manuscript/main.tex` — what the paper promises
- `references/artifact-standard.md`

## Procedure

1. List what must ship: every artifact promised in the manuscript (data,
   code, models, scripts) plus everything the venue's badge requirements
   demand.
2. Stage by copying the relevant `contributions/<slug>/` folders into
   `artifacts/` — they are self-contained by construction. Never hand-edit
   the staged copies: fix problems at the source contribution and re-stage.
3. Add the bundle-level files: an artifact README (claims-to-artifact map,
   setup, smoke test, expected outputs and runtime), license, citation
   file, and a `MANIFEST.md` listing every file with its sha256 checksum.
4. Strip what must not ship: gitignored material, secrets, raw sensitive
   data, and — when the venue requires anonymization — identifying paths
   and names.
5. Verify standalone: the bundle works without the surrounding repo (no
   `../` references, bibliography resolved, environment declared inside).
6. Walk `references/artifact-standard.md` and the venue checklist item by
   item; record the mapping in the artifact README.

## Done When

- The bundle satisfies the venue requirements and the artifact standard,
  `MANIFEST.md` checksums are fresh, and a clean-room smoke test (fresh
  unzip elsewhere, follow only the bundle README) succeeds
