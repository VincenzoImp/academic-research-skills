# Skill Evaluation Policy

Use this reference when creating or revising skills.

## Pressure Scenario Template

```text
User asks:
[realistic request]

Risk:
[what a generic agent may do wrong]

Expected behavior with skill:
[observable actions and artifacts]

Pass/fail evidence:
[files, commands, outputs, or reasoning checks]
```

## Academic Pressure Scenarios

- PDF conversion with bad OCR and tables.
- Paper claim unsupported by cited source.
- SOTA search using only Google Scholar.
- Messy repo where notebooks are the only execution path.
- Missing DOI and duplicate preprint/published records.
- Sensitive dataset proposed for git commit.
- MCP server unavailable or rate-limited.

## Validation Checklist

- `python3 scripts/validate_skills.py`
- `pytest -q`
- `npx -y skills add <repo> --list`
- frontmatter descriptions are trigger-focused
- references exist and avoid duplicated policy text
- skills write to known research project contract paths
