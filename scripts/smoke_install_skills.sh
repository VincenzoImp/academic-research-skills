#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="${1:-$ROOT}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/home" "$TMP/project"

(
  cd "$TMP/project"
  HOME="$TMP/home" npx -y skills add "$SOURCE" --skill '*' --copy -y >/dev/null
)

expected_count="$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
installed_roots=()
while IFS= read -r installed_root; do
  installed_roots+=("$installed_root")
done < <(find "$TMP/project" -mindepth 1 -maxdepth 4 -type d -name skills | sort)

if [[ "${#installed_roots[@]}" == "0" ]]; then
  echo "ERROR: no project-local skill directories were installed" >&2
  exit 1
fi

for installed_dir in "${installed_roots[@]}"; do
  actual_count="$(find "$installed_dir" -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')"
  if [[ "$actual_count" != "$expected_count" ]]; then
    echo "ERROR: expected $expected_count installed skills in $installed_dir, found $actual_count" >&2
    exit 1
  fi

  while IFS= read -r skill_md; do
    skill_dir="$(dirname "$skill_md")"
    test -f "$skill_dir/agents/openai.yaml"

    while IFS= read -r reference; do
      [[ -z "$reference" ]] && continue
      if [[ ! -f "$skill_dir/$reference" ]]; then
        echo "ERROR: $(basename "$skill_dir") missing installed reference $reference" >&2
        exit 1
      fi
    done < <(grep -Eo 'references/[A-Za-z0-9._/-]+' "$skill_md" | sort -u || true)
  done < <(find "$installed_dir" -mindepth 2 -maxdepth 2 -name SKILL.md | sort)
done

echo "OK: smoke installed $expected_count skills into ${#installed_roots[@]} project-local loader(s)"
