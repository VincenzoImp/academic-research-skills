import json
from pathlib import Path
import re


def test_each_skill_has_skill_md() -> None:
    root = Path(__file__).resolve().parents[1]
    skill_dirs = sorted(path for path in (root / "skills").iterdir() if path.is_dir())
    assert skill_dirs
    assert all((path / "SKILL.md").exists() for path in skill_dirs)


def test_each_skill_has_spec_frontmatter() -> None:
    root = Path(__file__).resolve().parents[1]
    for skill_path in sorted((root / "skills").glob("*/SKILL.md")):
        text = skill_path.read_text(encoding="utf-8")
        match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
        assert match, f"{skill_path} missing frontmatter"
        frontmatter = match.group(1)
        fields = {
            line.split(":", 1)[0]: line.split(":", 1)[1].strip()
            for line in frontmatter.splitlines()
            if ":" in line and not line.startswith(" ")
        }
        name = fields.get("name")
        assert name == skill_path.parent.name
        assert re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", name)
        assert "--" not in name
        assert fields.get("license") == "MIT"


def test_shared_references_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    expected = {
        "repository-contract.md",
        "mcp-catalog.md",
        "source-ledger.md",
        "output-contracts.md",
        "claim-audit.md",
        "pdf-markdown-policy.md",
        "experiment-policy.md",
        "external-skill-recommendations.md",
        "citation-bibliography-policy.md",
        "document-conversion-policy.md",
        "ethics-data-governance.md",
        "repo-migration-policy.md",
        "systematic-review-policy.md",
        "skill-evaluation-policy.md",
        "artifact-open-science-policy.md",
        "cs-methodology-evaluation-policy.md",
        "peer-review-policy.md",
        "research-positioning-policy.md",
        "venue-strategy-policy.md",
    }
    present = {path.name for path in (root / "references").glob("*.md")}
    assert expected <= present


def test_research_lifecycle_skills_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    expected = {
        "academic-mcp-tooling",
        "adversarial-peer-review",
        "artifact-open-science",
        "citation-bibliography-tooling",
        "document-conversion",
        "ethics-data-governance",
        "cs-methodology-evaluation",
        "cs-venue-strategy",
        "repo-migration",
        "rebuttal-revision-strategy",
        "research-design-positioning",
        "skill-evaluation",
        "systematic-review-prisma",
    }
    present = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    assert expected <= present
    assert len(present) <= 23


def test_each_skill_has_openai_metadata() -> None:
    root = Path(__file__).resolve().parents[1]
    skill_dirs = sorted(path for path in (root / "skills").iterdir() if path.is_dir())
    assert skill_dirs
    assert all((path / "agents" / "openai.yaml").exists() for path in skill_dirs)


def test_skill_references_are_self_contained() -> None:
    root = Path(__file__).resolve().parents[1]
    for skill_path in sorted((root / "skills").glob("*/SKILL.md")):
        text = skill_path.read_text(encoding="utf-8")
        assert "../../references/" not in text
        references = set(re.findall(r"`(references/[^`]+)`", text))
        assert references, f"{skill_path} should reference at least one local reference file"
        for relative in references:
            local_reference = skill_path.parent / relative
            canonical_reference = root / relative
            assert local_reference.exists(), f"{skill_path} references missing {relative}"
            assert canonical_reference.exists(), f"canonical reference missing {relative}"
            assert local_reference.read_text(encoding="utf-8") == canonical_reference.read_text(
                encoding="utf-8"
            )


def test_openai_metadata_is_human_written() -> None:
    root = Path(__file__).resolve().parents[1]
    for metadata_path in sorted((root / "skills").glob("*/agents/openai.yaml")):
        text = metadata_path.read_text(encoding="utf-8")
        assert "display_name:" in text
        assert "short_description:" in text
        assert "default_prompt:" in text
        assert "Help with " not in text
        assert " tasks" not in text


def test_readme_skill_list_matches_installed_skills() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"^- `([a-z0-9-]+)`:", readme, flags=re.MULTILINE))
    present = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    assert listed == present


def test_router_references_current_skills() -> None:
    root = Path(__file__).resolve().parents[1]
    router = (root / "skills" / "research-project-router" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    present = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    mentioned = set(re.findall(r"`([a-z0-9-]+)`", router))
    assert present - {"research-project-router"} <= mentioned
    assert "research-ideation-positioning" not in router
    assert "research-question-design" not in router
    assert "mcp-literature-tooling" not in router
    assert "academic-mcp-bootstrap" not in router


def test_default_external_recommendations_do_not_overlap_research_native_skills() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "references" / "external-skill-recommendations.md").read_text(
        encoding="utf-8"
    )
    default_block = text.split("## Suggested Install Bundle", 1)[1].split(
        "Optional connector installs:", 1
    )[0]
    for overlapping_skill in (
        "paper-audit",
        "citation-management",
        "literature-review",
        "rebuttal-writing",
        "research-synthesis",
    ):
        assert overlapping_skill not in default_block


def test_package_is_ready_for_public_skills_registry() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    pyproject = (root / "pyproject.toml").read_text(encoding="utf-8")

    assert (root / "LICENSE").exists()
    assert (root / "SECURITY.md").exists()
    assert (root / ".github" / "workflows" / "validate.yml").exists()
    assert (root / ".github" / "workflows" / "release.yml").exists()
    assert (root / ".github" / "release.yml").exists()
    assert (root / ".github" / "dependabot.yml").exists()
    assert (root / "scripts" / "check_release.py").exists()
    assert (root / "scripts" / "smoke_install_skills.sh").exists()
    assert (root / "scripts" / "spec_validate_skills.sh").exists()
    assert (root / "evals" / "trigger-boundaries.json").exists()
    assert "https://skills.sh/b/VincenzoImp/academic-research-skills" in readme
    assert "npx -y skills add VincenzoImp/academic-research-skills --skill '*' --copy -y" in readme
    assert "npx -y skills add VincenzoImp/academic-research-skills --agent '*' --skill '*' --copy -y" in readme
    assert "bash scripts/spec_validate_skills.sh" in readme
    assert "bash scripts/smoke_install_skills.sh" in readme
    assert "--agent '*'" in readme
    assert "--agent codex claude-code cursor windsurf opencode" not in readme
    assert "Release" in readme
    for agent_name in ("Codex", "Claude Code", "Cursor", "Windsurf", "OpenCode"):
        assert agent_name in readme
    assert "/Users/vincenzo" not in readme
    assert "Private" not in readme
    assert "Private" not in pyproject


def test_project_contract_references_are_current() -> None:
    root = Path(__file__).resolve().parents[1]
    paths = [
        root / "README.md",
        *sorted((root / "references").glob("*.md")),
        *sorted((root / "skills").glob("*/SKILL.md")),
    ]
    text = "\n".join(path.read_text(encoding="utf-8") for path in paths)

    assert "create-academic-research" in text
    assert "configs/agent-stack.yaml" in text
    assert "configs/capabilities.yaml" in text
    assert "docs/agent/capability-profile.md" in text
    for stale in (
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
        assert stale not in text


def test_trigger_boundary_evals_cover_current_skills() -> None:
    root = Path(__file__).resolve().parents[1]
    present = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    data = json.loads((root / "evals" / "trigger-boundaries.json").read_text(encoding="utf-8"))
    records = data["skills"]
    listed = {record["skill"] for record in records}

    assert listed == present
    for record in records:
        assert record["should_trigger"]
        assert record["should_not_trigger"]
        assert len(record["should_trigger"]) >= 2
        assert len(record["should_not_trigger"]) >= 1


def test_skill_use_case_examples_cover_current_skills() -> None:
    root = Path(__file__).resolve().parents[1]
    present = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    examples = (root / "examples" / "skill-use-cases.md").read_text(encoding="utf-8")

    for skill in present:
        assert f"`{skill}`" in examples
    assert "Use Case" in examples
    assert "Near Miss" in examples
