# Academic Research Skills

[![skills.sh](https://skills.sh/b/VincenzoImp/academic-research-skills)](https://skills.sh/VincenzoImp/academic-research-skills)

Professional agent skill package for academic research repositories, especially
projects created by `create-academic-research`. The package is broadly useful
for academic research work and gives first-class support to computer science
research across AI/ML, systems, HCI, security, software engineering, databases,
theory, robotics, IR, PL, graphics, and adjacent interdisciplinary CS. It is
designed to be installed through the open skills ecosystem and to work across
Agent Skills compatible LLM coding agents.

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

## Skills

- `research-project-router`: choose the right workflow and preserve project state.
- `research-design-positioning`: frame research questions, contribution claims, scope, and evidence paths.
- `cs-venue-strategy`: select and position for computer science venues and tracks.
- `source-ingestion`: ingest papers, PDFs, proposals, datasets, and web sources.
- `document-conversion`: convert PDFs, DOCX, scanned papers, tables, and figures with quality notes.
- `citation-bibliography-tooling`: normalize BibTeX, citation keys, identifiers, and bibliography audits.
- `sota-literature-review`: build and maintain state-of-the-art reviews.
- `systematic-review-prisma`: run reproducible searches, screening, and PRISMA-style review artifacts.
- `citation-claim-audit`: verify claims, citations, evidence, and provenance.
- `cs-methodology-evaluation`: design and audit CS experiments, baselines, metrics, and validity.
- `adversarial-peer-review`: review papers like a severe but fair top-venue reviewer.
- `paper-writing-review`: draft, revise, and review manuscripts without fabricating evidence.
- `rebuttal-revision-strategy`: map reviewer concerns and write precise rebuttals/revisions.
- `artifact-open-science`: prepare reproducibility packages and artifact evaluation material.
- `repo-migration`: move messy academic repos and archives into the standard project structure.
- `research-repo-reproduction`: audit and reproduce research code repositories.
- `experiment-logbook`: run and record bounded computational experiments.
- `research-data-analysis`: analyze data and produce publication-quality tables and figures.
- `research-ui-prototyping`: build research dashboards and paper-supporting interfaces.
- `ethics-data-governance`: document human-subject, platform, privacy, license, and sharing risks.
- `research-project-maintenance`: keep project folders, docs, wiki, and outputs coherent.
- `academic-mcp-tooling`: select, configure, smoke-test, and document MCP servers for scholarly search.
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
python3.11 scripts/check_release.py v0.1.2
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
skill. It is a seed set for future trigger testing and a lightweight guard
against description drift.

## Release

Releases are tag-driven. Update `pyproject.toml`, commit the change, create
`vX.Y.Z`, and push the tag:

```bash
git tag -a v0.1.2 -m "v0.1.2"
git push origin main v0.1.2
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
