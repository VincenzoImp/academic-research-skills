# Artifact Open Science Policy

Use this reference for artifact evaluation, reproducibility packages, and public
research releases.

## Artifact Types

- code
- dataset
- benchmark
- model
- UI/demo
- reproduction package
- supplementary material

## Checklist Fields

- artifact name
- supported claims
- license
- citation
- install command
- smoke test
- full reproduction command
- expected runtime
- hardware requirements
- data access
- expected outputs
- known limitations
- ethics/license constraints

## ACM Artifact Review Badging

Use the ACM artifact review and badging policy as the default badge vocabulary
when a venue follows ACM-style artifact review.

- **Artifacts Available**: artifact is placed in a publicly accessible archival
  repository with a stable identifier and license or access terms.
- **Artifacts Evaluated: Functional**: artifact is documented, complete enough
  for the stated purpose, installs/runs, and has evidence that basic operation
  was checked.
- **Artifacts Evaluated: Reusable**: artifact goes beyond functional by being
  documented, structured, and packaged so others can reuse or adapt it.
- **Results Reproduced**: the paper's main results are obtained in an
  independent review using the author's artifacts.
- **Results Replicated**: the paper's main results are independently obtained
  with artifacts or implementations not supplied by the authors.

Badge work should start during SOTA and methodology planning, not only after a
paper is accepted. When a literature gap motivates code, data, benchmark,
model, or reproduction work, record the artifact implication and expected badge
path in `artifacts/artifact-checklist.md`.

## Release Rule

Public artifacts must exclude credentials, private data, caches, and local-only
paths. Sensitive datasets need an access policy, not accidental inclusion.
