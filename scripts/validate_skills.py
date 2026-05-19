#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata


def _validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    skill_name = path.parent.name

    try:
        metadata = _parse_frontmatter(text)
    except ValueError as exc:
        return [f"{path}: {exc}"]

    name = metadata.get("name")
    description = metadata.get("description")
    license_name = metadata.get("license")

    if name != skill_name:
        errors.append(f"{path}: frontmatter name {name!r} must match folder {skill_name!r}")
    if not name or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", name):
        errors.append(
            f"{path}: name must be 1-64 lowercase letters, numbers, and hyphens "
            "without leading or trailing hyphens"
        )
    elif "--" in name:
        errors.append(f"{path}: name must not contain consecutive hyphens")
    if not description:
        errors.append(f"{path}: missing description")
    elif not description.startswith("Use when "):
        errors.append(f"{path}: description should start with 'Use when '")
    elif len(description) > 500:
        errors.append(f"{path}: description should stay under 500 characters")
    if license_name != "MIT":
        errors.append(f"{path}: license must be MIT")

    if "../../references/" in text:
        errors.append(f"{path}: skill references must be local to the skill folder")

    for match in re.finditer(r"`(references/[^`]+)`", text):
        relative = match.group(1)
        ref = (path.parent / relative).resolve()
        if not ref.exists():
            errors.append(f"{path}: referenced file does not exist: {relative}")
            continue
        canonical = ROOT / relative
        if canonical.exists() and ref.read_text(encoding="utf-8") != canonical.read_text(encoding="utf-8"):
            errors.append(f"{path}: local reference differs from canonical {relative}")

    return errors


def _validate_openai_metadata(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "agents" / "openai.yaml"
    if not path.exists():
        return [f"{skill_dir}: missing agents/openai.yaml"]

    text = path.read_text(encoding="utf-8")
    for field in ("display_name:", "short_description:", "default_prompt:"):
        if field not in text:
            errors.append(f"{path}: missing {field.rstrip(':')}")
    if re.search(r' short_description:\s*"Help with .* tasks"', text):
        errors.append(f"{path}: short_description is generic")
    if "Cs " in text or "Sota " in text or "Prisma" in text:
        errors.append(f"{path}: acronym capitalization needs review")
    return errors


def _readme_skill_list() -> set[str]:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    return set(re.findall(r"^- `([a-z0-9-]+)`:", readme, flags=re.MULTILINE))


def _validate_package_contract(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    combined_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            ROOT / "README.md",
            *sorted((ROOT / "references").glob("*.md")),
            *sorted((ROOT / "skills").glob("*/SKILL.md")),
            *sorted((ROOT / "skills").glob("*/agents/openai.yaml")),
        ]
        if path.exists()
    )
    for stale_path in (
        "academic-research-template",
        "academic-research-starter",
        "research-template-maintenance",
        "docs/template",
        "../../references",
        "docs/agent/onboarding.md",
        "docs/agent/skills-and-mcp.md",
        "docs/project-profiles.md",
        "src/research_template",
        "path/to",
        "/Users/vincenzo",
        "still private",
        "repository is still private",
    ):
        if stale_path in combined_text:
            errors.append(f"package text contains stale or local path: {stale_path!r}")

    listed = _readme_skill_list()
    if listed != skill_names:
        errors.append(
            "README skill list does not match skills/: "
            f"missing_in_readme={sorted(skill_names - listed)}, "
            f"stale_in_readme={sorted(listed - skill_names)}"
        )

    router_path = SKILLS_DIR / "research-project-router" / "SKILL.md"
    if router_path.exists():
        router = router_path.read_text(encoding="utf-8")
        mentioned = set(re.findall(r"`([a-z0-9-]+)`", router))
        missing = sorted((skill_names - {"research-project-router"}) - mentioned)
        if missing:
            errors.append(f"{router_path}: router does not mention skills: {missing}")
        for stale in (
            "research-ideation-positioning",
            "research-question-design",
            "mcp-literature-tooling",
            "academic-mcp-bootstrap",
        ):
            if stale in router:
                errors.append(f"{router_path}: stale skill reference {stale!r}")

    recommendations_path = ROOT / "references" / "external-skill-recommendations.md"
    if recommendations_path.exists():
        recommendations = recommendations_path.read_text(encoding="utf-8")
        try:
            default_block = recommendations.split("## Suggested Install Bundle", 1)[1].split(
                "Optional connector installs:", 1
            )[0]
        except IndexError:
            errors.append(f"{recommendations_path}: missing default install bundle section")
        else:
            for overlap in (
                "paper-audit",
                "citation-management",
                "literature-review",
                "rebuttal-writing",
                "research-synthesis",
            ):
                if overlap in default_block:
                    errors.append(
                        f"{recommendations_path}: default install bundle includes overlapping skill {overlap!r}"
                    )

    return errors


def _validate_automation_files() -> list[str]:
    errors: list[str] = []
    for relative in (
        ".github/workflows/validate.yml",
        ".github/workflows/release.yml",
        ".github/release.yml",
        ".github/dependabot.yml",
        "scripts/check_release.py",
    ):
        if not (ROOT / relative).exists():
            errors.append(f"missing release/automation file: {relative}")

    release_workflow = ROOT / ".github" / "workflows" / "release.yml"
    if release_workflow.exists():
        text = release_workflow.read_text(encoding="utf-8")
        for required in (
            "github.event.repository.private == false",
            "--generate-notes",
            "bash scripts/smoke_install_skills.sh VincenzoImp/academic-research-skills",
        ):
            if required not in text:
                errors.append(f"{release_workflow}: missing required release guard/action {required!r}")

    smoke_install = ROOT / "scripts" / "smoke_install_skills.sh"
    if smoke_install.exists():
        text = smoke_install.read_text(encoding="utf-8")
        for required in (
            'SOURCE="${1:-$ROOT}"',
            'npx -y skills add "$SOURCE" --skill \'*\' --copy -y',
        ):
            if required not in text:
                errors.append(f"{smoke_install}: missing required smoke install action {required!r}")

    return errors


def main() -> int:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("ERROR: no skills found", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen: set[str] = set()
    for skill_file in skill_files:
        name = skill_file.parent.name
        if name in seen:
            errors.append(f"duplicate skill folder: {name}")
        seen.add(name)
        errors.extend(_validate_skill(skill_file))
        errors.extend(_validate_openai_metadata(skill_file.parent))

    errors.extend(_validate_package_contract(seen))
    errors.extend(_validate_automation_files())

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(skill_files)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
