# Academic Research Skills

[![skills.sh](https://skills.sh/b/VincenzoImp/academic-research-skills)](https://skills.sh/VincenzoImp/academic-research-skills)
[![Validate Skills](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/validate.yml)
[![Release Skills](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/release.yml/badge.svg)](https://github.com/VincenzoImp/academic-research-skills/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Professional agent skill package for academic research: autonomous SOTA and
survey workflows, source ingestion, citation hygiene, claim auditing, paper
writing, peer review, rebuttal strategy, reproducibility, MCP tooling, and
project maintenance.

The skills are broadly useful for academic work and give first-class support to
computer science research across AI/ML, systems, HCI, security, software
engineering, databases, theory, robotics, IR, PL, graphics, and adjacent
interdisciplinary CS. They are designed for the open skills ecosystem and for
Agent Skills compatible LLM coding agents.

The package works standalone, but it is strongest inside repositories created
by [`create-academic-research`](https://github.com/VincenzoImp/create-academic-research),
where the skills can rely on source ledgers, SOTA files, experiment records,
MCP setup docs, and a durable wiki/log structure.

The package is intentionally modular. It does not try to be one giant
"research agent"; it gives agents separate procedures for literature search,
research design, source ingestion, document conversion, bibliography hygiene,
SOTA synthesis, PRISMA-style review, citation auditing, paper writing,
repository migration and reproduction, experiments, data analysis, UI
prototyping, ethics, MCP setup, and project maintenance. The package keeps
research-native judgment inside this repo; generic tooling such as PDF engines,
frontend design, Office formats, MCP servers, and general coding workflows
remain external dependencies.

Research-specific external skills are treated as references or explicit
project-local opt-ins, not default companions. The default stack should not
install competing academic-paper, literature-review, citation, or peer-review
policies beside this package; those concepts are consolidated here.

## What It Covers

| Research Area | Skills |
|---|---|
| Project Routing | `research-project-router`, `research-project-maintenance`, `repo-migration` |
| Literature And Sources | `source-ingestion`, `document-conversion`, `sota-literature-review`, `systematic-review-prisma`, `survey-synthesis` |
| Citations And Evidence | `citation-bibliography-tooling`, `citation-claim-audit`, `academic-mcp-tooling` |
| Research Design | `research-design-positioning`, `research-agenda`, `contribution-package`, `cs-methodology-evaluation`, `ethics-data-governance` |
| Writing And Review | `paper-framing`, `paper-writing-review`, `adversarial-peer-review`, `paper-submission-lifecycle`, `rebuttal-revision-strategy`, `cs-venue-strategy` |
| Artifacts And Execution | `experiment-logbook`, `research-data-analysis`, `research-results-reporting`, `publication-figures-tables`, `research-repo-reproduction`, `paper-release`, `artifact-open-science`, `badge-compliance-profiles`, `research-ui-prototyping` |
| Skill Quality | `skill-evaluation` |

## Skills

- `research-project-router`: choose the right workflow and preserve project state.
- `research-design-positioning`: frame research questions, contribution claims, scope, and evidence paths.
- `cs-venue-strategy`: select and position for computer science venues and tracks.
- `source-ingestion`: ingest papers, PDFs, proposals, datasets, and web sources.
- `document-conversion`: convert PDFs, DOCX, scanned papers, tables, and figures with quality notes.
- `citation-bibliography-tooling`: normalize BibTeX, citation keys, identifiers, and bibliography audits.
- `sota-literature-review`: build full SOTA reviews from ideas, seeds, or papers with citation chasing, full-text reading, BibTeX gates, survey LaTeX, and gap maps.
- `systematic-review-prisma`: run reproducible searches, screening, and PRISMA-style review artifacts.
- `survey-synthesis`: turn reviewed SOTA claims into survey sections, survey claim ledgers, gaps, and final survey artifacts.
- `citation-claim-audit`: verify claims, citations, evidence, and provenance.
- `cs-methodology-evaluation`: design and audit CS experiments, baselines, metrics, and validity.
- `adversarial-peer-review`: review papers like a severe but fair top-venue reviewer.
- `research-agenda`: prioritize SOTA gaps and survey claims into feasible, publishable research opportunities.
- `contribution-package`: create contribution packages with manifests, claim maps, badge plans, outputs, reports, reviews, and paper exports.
- `research-results-reporting`: write analysis and contribution reports from generated outputs without duplicating numeric truth.
- `publication-figures-tables`: prepare publication-facing figures, tables, captions, source data, and asset maps.
- `paper-framing`: select accepted paper frames from contributions, evidence, venue fit, badge fit, and release implications.
- `paper-writing-review`: draft, revise, and review manuscripts without fabricating evidence.
- `paper-release`: create paper-specific release manifests, source maps, locks, checksums, metadata, reviews, and staged artifacts.
- `paper-submission-lifecycle`: manage cover letters, submission checklists, submitted locks, decisions, review rounds, and camera-ready state.
- `rebuttal-revision-strategy`: map reviewer concerns and write precise rebuttals/revisions.
- `artifact-open-science`: prepare reproducibility packages and ACM-style artifact badge material.
- `badge-compliance-profiles`: audit badge, open-science, transparency, release, and venue compliance evidence.
- `repo-migration`: move messy academic repos and archives into the standard project structure.
- `research-repo-reproduction`: audit and reproduce research code repositories.
- `experiment-logbook`: run and record bounded experiments and autonomous campaign frontiers.
- `research-data-analysis`: analyze data and produce publication-quality tables and figures.
- `research-ui-prototyping`: build research dashboards and paper-supporting interfaces.
- `ethics-data-governance`: document human-subject, platform, privacy, license, and sharing risks.
- `research-project-maintenance`: keep project folders, docs, wiki, and outputs coherent.
- `academic-mcp-tooling`: select, configure, smoke-test, and document MCP servers and literature workflow stacks for scholarly search.
- `skill-evaluation`: pressure-test and refine academic research skills.

## Install

Install the full package for the current project and detected local agent:

```bash
npx -y skills add VincenzoImp/academic-research-skills --skill '*' --copy -y
```

Install the full package into every supported project-local loader only when
you intentionally want the same skills available to multiple local agents:

```bash
npx -y skills add VincenzoImp/academic-research-skills --agent '*' --skill '*' --copy -y
```

Install one skill into every supported project-local loader:

```bash
npx -y skills add VincenzoImp/academic-research-skills --agent '*' --skill source-ingestion --copy -y
```

Use an explicit `--agent <name>` only when you know the target loader you want
to configure.

Use `npx -y skills add VincenzoImp/academic-research-skills --list` to inspect
the package before installing or recommending a subset.

## Agent Compatibility

This package follows the Agent Skills directory convention: each skill is a
folder with `SKILL.md`, optional `references/`, optional `scripts/`, and
OpenAI-facing metadata in `agents/openai.yaml`.

Compatibility is with agent runtimes and skill loaders, not with every raw model
API by itself. A model only benefits from these skills when its client loads the
`SKILL.md` instructions, installs them through the `skills` CLI, or lets the user
paste/import the relevant skill text into context. Stronger tool-using coding
agents will follow the workflows more reliably than small or instruction-weak
models.

Known compatible loaders include:

- Codex
- Claude Code
- Cursor
- Windsurf
- OpenCode
- GitHub Copilot compatible loaders
- other agents supported by the `skills` CLI

The skills are written to avoid agent-specific assumptions. Project-specific
state belongs in the research repository, especially `AGENTS.md`, `docs/agent/`,
`sources/`, `sota/`, `experiments/`, and `wiki/`.

## Validate

```bash
python3.11 scripts/check_release.py vX.Y.Z
python3.11 scripts/sync_skill_references.py --check
python3.11 scripts/validate_skills.py
bash scripts/spec_validate_skills.sh
python3.11 -m pytest -q
python3.11 -m ruff check scripts tests
npx -y skills add . --list
bash scripts/smoke_install_skills.sh
```

`smoke_install_skills.sh` installs the package into a temporary project and
checks that every installed skill keeps its local `references/` files.

`spec_validate_skills.sh` runs the public Agent Skills reference validator over
each skill directory.

`evals/trigger-boundaries.json` records positive and near-miss prompts for every
skill. `examples/skill-use-cases.md` gives a compact human-readable boundary
table. Together they are a seed set for future trigger testing and a lightweight
guard against description drift.

## Release

Releases are tag-driven. Update `pyproject.toml`, commit the change, create
`vX.Y.Z`, and push the tag:

```bash
git tag -a vX.Y.Z -m "vX.Y.Z"
git push origin main vX.Y.Z
```

Once the GitHub repository is public, the release workflow validates the tag
against the package version, runs the full skill validation suite, smoke-tests
local installation, smoke-tests public installation through the `skills` CLI,
and creates a GitHub Release with generated notes. If a tag was pushed while
the repository was private, make the repository public and run the
`Release Skills` workflow manually with the existing tag.

## Design Notes

The package works best in repositories created by `create-academic-research`.
In those projects, skills should treat `configs/capabilities.yaml`,
`docs/agent/capability-profile.md`, `docs/agent/generated/`, and
`docs/agent/mcp-setup.md` as project-local capability state. Outside that
structure, skills should inspect the target repository, use the closest
available durable records, and propose creating missing folders only when the
task needs them.

The package intentionally uses a moderate number of skills. Separate skills
mark real workflow boundaries: source ingestion, SOTA, systematic review,
bibliography, claim audit, methodology, writing, peer review, rebuttal,
reproduction, experiments, data analysis, ethics, MCP tooling, and maintenance.
Do not split these further unless a workflow needs different triggers, different
artifacts, or different safety rules.
