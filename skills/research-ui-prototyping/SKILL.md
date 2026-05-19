---
name: research-ui-prototyping
description: Use when building research dashboards, annotation tools, data browsers, paper-supporting demos, SOTA explorers, experiment viewers, or frontend interfaces for academic projects.
license: MIT
---

# Research UI Prototyping

Research UIs are working tools, not landing pages. Favor dense, inspectable,
task-focused interfaces that expose evidence and uncertainty.

## Read First

- `references/repository-contract.md`
- `references/output-contracts.md`

## When To Use

- dashboard for experiment metrics
- source or paper browser
- annotation or coding interface
- SOTA matrix explorer
- reproducibility report viewer
- demo for a method or dataset

## Design Rules

- Start with the core workflow, not a hero section.
- Show identifiers, provenance, filters, and export controls.
- Make uncertainty and missing evidence visible.
- Prefer tables, facets, timelines, charts, and diff views over marketing cards.
- Keep visual style restrained and domain-appropriate.
- Use the existing `frontend-design` skill when available for polish and UI craft.
- Verify with screenshots and interaction checks before claiming completion.

## Data Rules

- Do not hardcode research results into the UI unless it is a static report.
- Keep data loading paths documented.
- Export tables/figures back to `outputs/` when they support the paper.

## Output

Record UI purpose, run command, and data dependencies in `docs/agent/` or
`docs/reproducibility/commands.md`.
