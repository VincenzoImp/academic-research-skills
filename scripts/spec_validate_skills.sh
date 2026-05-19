#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

while IFS= read -r skill_dir; do
  npx -y skills-ref validate "$skill_dir" >/dev/null
done < <(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | sort)

echo "OK: Agent Skills spec validation passed"
