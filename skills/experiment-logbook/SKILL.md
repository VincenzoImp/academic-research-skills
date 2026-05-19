---
name: experiment-logbook
description: Use when planning, running, comparing, or recording computational experiments, benchmarks, ablations, autonomous research loops, overnight runs, training runs, or exploratory variants.
license: MIT
---

# Experiment Logbook

Use this skill to keep experiments scientifically interpretable. The experiment
record is part of the research output.

## Read First

- `references/experiment-policy.md`
- `references/output-contracts.md`

## Before Running

Record:

- hypothesis
- editable scope
- frozen evaluation harness
- metric and direction
- data version
- time or compute budget
- command
- expected output
- stop condition

## Run Record

Update `experiments/registry.csv` and create `experiments/<run_id>.md` for
non-trivial runs.

Minimum fields:

- run_id
- git commit
- command
- config
- seed
- dataset
- metric
- result
- runtime
- status
- notes

## Autonomous Loop Rules

- Establish a baseline first.
- Keep a machine-readable ledger.
- Commit candidate changes before each run when code changes matter.
- Keep only improvements if that is the agreed policy; otherwise record all variants.
- Never alter the metric, data split, or evaluation harness silently.
- Stop for human approval if the change alters scientific meaning.

## Output Separation

- `train_outputs/`: trusted training evidence.
- `explore_outputs/`: exploratory variants and caveated ideas.
- `analysis_outputs/`: result analysis and figures.
- `debug_outputs/`: failure diagnosis.

