# External Skill Recommendations

These are useful external installs for agents working in academic research
projects. Keep the boundary clear: this package owns academic judgment and
research workflow. External skills should supply complementary tools, file
handling, UI craft, coding discipline, or API connectors.

## Default Complementary Skills

- Superpowers: planning, debugging, TDD, verification, worktrees, and code-review discipline.
- frontend-design: polished research dashboards, visual artifacts, and frontend UI.
- webapp-testing: Playwright verification for dashboards and local apps.
- docling: document parsing and PDF-to-Markdown workflows.
- Anthropic document skills: `pdf`, `docx`, `xlsx`, and `pptx` for native document handling.
- MCP builder: when a missing scholarly connector needs a local MCP server.
- skill-creator: for revising this package safely.

## Optional Connectors

- `semanticscholar-skill`: API-backed Semantic Scholar search and citation traversal
  when no MCP server is configured.
- `openalex-database`: OpenAlex client workflows and query helpers when no MCP
  server is configured.
- Zotero paper reader skills when the user keeps a local Zotero library and no
  Zotero MCP is available.
- Google Scholar skills only as fallback discovery, not primary provenance.

## Optional Mechanical Specialists

- `latex-paper-en`: LaTeX compilation, formatting, figure/table checks, and
  venue template mechanics. Do not use it as the primary research-writing policy.
- Paper reproduction skill bundles only when reproducing external code, models,
  and training runs. Keep our `research-repo-reproduction` skill as the project
  governance layer.

## Avoid As Default With This Package

- `paper-audit`, generic literature-review, generic rebuttal-writing, and generic
  citation-management skills overlap with this package's research-native review,
  SOTA, rebuttal, and citation workflows. Study them as references if useful, but
  do not recommend them as default installs beside this package.

## Suggested Install Bundle

When a project was created with `create-academic-research`, prefer:

```bash
npx academic-research skills install --preset default
```

Manual project-local install commands:

```bash
npx -y skills add VincenzoImp/academic-research-skills --skill '*' --copy -y
npx -y skills add obra/superpowers --skill '*' --copy -y
npx -y skills add anthropics/skills --skill frontend-design webapp-testing skill-creator mcp-builder pdf docx xlsx pptx --copy -y
npx -y skills add existential-birds/beagle --skill docling --copy -y
```

Optional connector installs:

```bash
npx -y skills add davila7/claude-code-templates --skill openalex-database --copy -y
npx -y skills add agents365-ai/365-skills --skill semanticscholar-skill --copy -y
npx -y skills add fuzhiyu/researchprojecttemplate --skill zotero-paper-reader --copy -y
```

Optional mechanical specialists:

```bash
npx -y skills add bahayonghang/academic-writing-skills --skill latex-paper-en --copy -y
npx -y skills add lllllllama/ai-paper-reproduction-skill --skill ai-research-reproduction repo-intake-and-plan env-and-assets-bootstrap minimal-run-and-audit paper-context-resolver analyze-project safe-debug run-train explore-run explore-code --copy -y
```

## Local Customization

When adapting Superpowers-style skills, point generated design/spec/plan files
to `docs/agent/`, `docs/superpowers/`, or the project-specific folder documented
in `AGENTS.md`.
