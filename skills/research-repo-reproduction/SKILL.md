---
name: research-repo-reproduction
description: Use when inspecting, cleaning, understanding, reproducing, or auditing academic research code repositories, especially when README commands, datasets, checkpoints, experiments, or paper claims need verification.
license: MIT
---

# Research Repo Reproduction

Reproduction means a faithful, documented attempt to run or inspect the research
artifact. It does not mean changing anything until the result looks good.

## Read First

- `references/repository-contract.md`
- `references/output-contracts.md`

## Trusted Reproduction Flow

1. Read README, configs, environment files, scripts, and docs.
2. Inventory documented commands.
3. Identify the smallest trustworthy target: smoke test, inference, evaluation, or training startup.
4. Record assumptions about data, weights, environment, and hardware.
5. Run only documented or clearly justified commands.
6. If patching is required, isolate patch notes from scientific contribution claims.
7. Write standardized evidence under `repro_outputs/`.

## Output Files

- `repro_outputs/SUMMARY.md`
- `repro_outputs/COMMANDS.md`
- `repro_outputs/LOG.md`
- `repro_outputs/PATCHES.md`
- `repro_outputs/status.json`

## Boundaries

- Do not silently change datasets, splits, metrics, checkpoints, or evaluation code.
- Do not convert a failed reproduction into an exploratory refactor without naming the transition.
- Do not claim SOTA or correctness from a smoke test.
- Keep trusted reproduction separate from `explore_outputs/`.

## Repository Cleanup

For bad academic repos, prioritize:

- package structure
- clear CLI/scripts
- configs
- environment lock or setup docs
- tests for structural invariants
- reproducibility commands
- data provenance
- paper/proposal placement
- wiki/source summaries

