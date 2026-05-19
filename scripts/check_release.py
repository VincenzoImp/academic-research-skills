#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    tag = sys.argv[1] if len(sys.argv) > 1 else ""
    errors: list[str] = []

    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        errors.append(f"release tag must match vX.Y.Z, got {tag or '<empty>'}")

    version = tag.removeprefix("v")
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = pyproject.get("project", {})

    if project.get("name") != "academic-research-skills":
        errors.append(f"unexpected project name {project.get('name')!r}")
    if project.get("version") != version:
        errors.append(f"pyproject.toml version {project.get('version')} does not match tag {tag}")

    if errors:
        print("Release check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: release {tag} matches package version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
