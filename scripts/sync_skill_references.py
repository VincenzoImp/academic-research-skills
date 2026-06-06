#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REFERENCE_PATTERN = re.compile(r"`(references/[^`]+)`")


def referenced_files(skill_md: Path) -> set[str]:
    text = skill_md.read_text(encoding="utf-8")
    return set(REFERENCE_PATTERN.findall(text))


def sync_references(*, apply: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    changed: list[str] = []

    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill_dir = skill_md.parent
        for relative in sorted(referenced_files(skill_md)):
            canonical = ROOT / relative
            local = skill_dir / relative

            if not canonical.exists():
                errors.append(f"{skill_md}: canonical reference missing: {relative}")
                continue

            canonical_text = canonical.read_text(encoding="utf-8")
            local_text = local.read_text(encoding="utf-8") if local.exists() else None
            if local_text == canonical_text:
                continue

            changed.append(str(local.relative_to(ROOT)))
            if apply:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_text(canonical_text, encoding="utf-8")

    return errors, changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Synchronize local skill references from canonical references/ files."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check for drift without writing files")
    mode.add_argument("--apply", action="store_true", help="copy canonical references into skill folders")
    args = parser.parse_args()

    errors, changed = sync_references(apply=args.apply)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if changed and not args.apply:
        print("Reference copies are out of sync:")
        for path in changed:
            print(f"- {path}")
        print("Run: python3.11 scripts/sync_skill_references.py --apply")
        return 1

    if args.apply:
        print(f"OK: synchronized {len(changed)} reference copies")
    else:
        print("OK: skill reference copies are synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
