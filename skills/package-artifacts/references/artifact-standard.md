# Minimum Artifact Standard

Every submitted artifact bundle has:

- a one-command smoke test, or a clearly documented manual path
- environment capture (pyproject/requirements/Dockerfile) inside the bundle
- data access and provenance instructions, or the data itself when
  shareable
- expected outputs, and a comparison path against the paper's claims
- license and citation file
- expected runtime and hardware notes
- ethics and access constraints stated

Venue badges (ACM-style and equivalents):

- Available → archival deposit with an immutable identifier
- Functional → runs as documented; the smoke test passes
- Reusable → documented well enough to extend, not just rerun
- Reproduced → an independent run regenerates the paper's key results

Map each badge the venue offers to concrete evidence in the bundle README.
