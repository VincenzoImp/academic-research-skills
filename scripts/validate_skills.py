#!/usr/bin/env python3
"""Validate skills/<name>/SKILL.md structure and frontmatter (v0.2)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]
    name = meta.get("name", "")
    desc = meta.get("description", "")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name {name!r} != folder name")
    if not NAME_RE.fullmatch(name) or "--" in name:
        errors.append(f"{skill_dir.name}: invalid skill name {name!r}")
    if not desc.startswith("Use when "):
        errors.append(f"{skill_dir.name}: description must start with 'Use when '")
    if len(desc) > 500:
        errors.append(f"{skill_dir.name}: description over 500 characters")
    if meta.get("license") != "MIT":
        errors.append(f"{skill_dir.name}: license must be MIT")
    refs_dir = skill_dir / "references"
    mentioned = set(re.findall(r"references/([\w./-]+\.md)", text))
    on_disk = {p.name for p in refs_dir.glob("*.md")} if refs_dir.is_dir() else set()
    for missing in sorted(mentioned - on_disk):
        errors.append(
            f"{skill_dir.name}: SKILL.md mentions references/{missing} which does not exist"
        )
    for orphan in sorted(on_disk - mentioned):
        errors.append(f"{skill_dir.name}: references/{orphan} is never mentioned in SKILL.md")
    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("no skills/ directory yet: nothing to validate")
        return 0
    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    all_errors: list[str] = []
    for d in dirs:
        all_errors.extend(validate_skill(d))
    for e in all_errors:
        print(f"ERROR: {e}", file=sys.stderr)
    print(f"validated {len(dirs)} skills: {'FAIL' if all_errors else 'OK'}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
