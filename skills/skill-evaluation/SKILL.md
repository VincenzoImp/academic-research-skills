---
name: skill-evaluation
description: Use when testing, reviewing, pressure-testing, refining, packaging, or validating agent skills for academic research workflows before installing or relying on them.
license: MIT
---

# Skill Evaluation

Evaluate skills as operational procedures. A good research skill changes future
agent behavior on realistic tasks and leaves inspectable artifacts.

## Read First

- `references/skill-evaluation-policy.md`
- `references/external-skill-recommendations.md`

## Workflow

1. Define the failure mode the skill should prevent.
2. Write pressure scenarios using real academic tasks: bad PDFs, missing DOI,
   unsupported claim, messy repo, ambiguous SOTA, unreliable notebook, or MCP outage.
3. Run or reason through the baseline behavior without assuming the skill helps.
4. Revise the skill frontmatter so it triggers on the right user intents.
5. Keep `SKILL.md` lean; move detailed policies to `references/`.
6. Validate local structure with `python3 scripts/validate_skills.py`.
7. Install-list the package with `npx -y skills add <repo> --list`.
8. Record recommended external skills separately from custom internal skills.

## Review Criteria

- trigger description starts with `Use when`
- no workflow summary in frontmatter
- references exist and are loaded only when needed
- outputs map to the research project contract
- citations and evidence rules are explicit
- skill does not duplicate a stronger external skill without a reason

## Do Not

- Create one giant "research agent" skill.
- Hide fragile procedures in prose when a script or test can check them.
- Copy external skills blindly without adapting output paths and repository contracts.
