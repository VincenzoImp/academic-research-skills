# Academic Research Skills

[![Validate Skills](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Eight agent skills for the full academic research pipeline:
SOTA → survey → contributions → papers.

Designed for repositories created by
[`create-academic-research`](https://github.com/VincenzoImp/create-academic-research)
(paired with the 0.3.0 scaffold), whose directory structure and formats the
skills rely on: one root `references.bib`, `sota/papers/<citekey>/` folders,
`survey/coverage.md`, self-contained `contributions/<slug>/` folders, and
per-venue `papers/<slug>/` folders. The skills are portable `SKILL.md`
files and work with any Agent-Skills-compatible runtime.

## Install

Project-local copy (done automatically by the create-academic-research
wizard):

```bash
npx -y skills add VincenzoImp/academic-research-skills --skill '*' --copy -y
```

## The Skills

| Skill | Use it to |
|---|---|
| `digest-paper` | digest one paper: PDF + synthesis + bib entry + citation graph + index row, MCP-verified end to end |
| `explore-sota` | run the SOTA exploration loop: search, citation chasing, triage queue, digestion — autonomous or targeted |
| `write-survey` | write the full LaTeX survey from all syntheses, or diff-update it when the SOTA changes |
| `develop-contribution` | create or regularize a badge-compliant, self-contained contribution with its LaTeX report |
| `write-paper` | pick a venue, frame the story, and write the manuscript from the survey and contribution reports |
| `package-artifacts` | build the self-contained submission bundle meeting the venue's badge requirements |
| `manage-submission` | freeze submission rounds, map reviewer concerns, draft rebuttals, apply revisions, camera-ready |
| `adversarial-review` | review the survey, a contribution, or a paper as a severe but fair reviewer |

Each skill is a `SKILL.md` procedure with optional `references/` files carrying
the deeper conventions (bibliography rules, citation chasing, experiment/data/
ethics/reproduction conventions, venue fit, writing rules, and so on).

## Hard Rules Baked In

- A citation exists only if a scholarly MCP lookup produced it; SOTA skills
  stop when the scholarly sources are unavailable.
- Digestion is atomic: paper folder, synthesis, bib entry, citation graph,
  and index row land together or not at all.
- The survey's create mode reads every synthesis before writing a word.
- Archives of submitted papers are immutable.
- Reviewers (adversarial-review) report; they never edit the artifact.

## Validate

```bash
python3 scripts/validate_skills.py
```

## Release

Tag-driven: update `CHANGELOG.md`, tag `vX.Y.Z`, push the tag.
