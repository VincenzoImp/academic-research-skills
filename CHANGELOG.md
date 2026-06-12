# Changelog

## 0.2.0

Full from-scratch rewrite for the create-academic-research v0.2 scaffold.

- 8 skills replace the 32 of v0.1: digest-paper, explore-sota,
  write-survey, develop-contribution, write-paper, package-artifacts,
  manage-submission, adversarial-review.
- Skills are plain portable `SKILL.md` + per-skill `references/`; the
  per-skill agent yaml, shared reference syncing, Python packaging, evals,
  and examples are gone.
- Skills target the v0.2 scaffold structure (root `references.bib`,
  `sota/papers/<citekey>/`, `survey/coverage.md`, `contributions/<slug>/`,
  `papers/<slug>/`) and its `make check` rails.
- Scholarly MCPs are mandatory for SOTA work: digest-paper and explore-sota
  hard-stop when arxiv or semantic-scholar do not respond.

Migration: v0.1 skills assume the v0.1 scaffold and were removed, not
renamed. Projects on the v0.1 scaffold should stay on skills 0.1.x.

## 0.1.x

See git history.
