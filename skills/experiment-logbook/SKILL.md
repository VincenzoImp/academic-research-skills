---
name: experiment-logbook
description: Use when planning, running, comparing, or recording computational experiments, benchmarks, ablations, autonomous research loops, overnight runs, training runs, or exploratory variants.
license: MIT
---

# Experiment Logbook

Use this skill to keep experiments scientifically interpretable. The experiment
record is part of the research output.

## Read First

- `references/repository-contract.md`
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

For overnight or fully autonomous campaigns, create
`experiments/campaigns/<campaign_id>.md` from the scaffold campaign template and
maintain `experiments/campaigns/frontier-results.tsv` or a campaign-specific
copy. The campaign must define:

- mutability envelope: editable files, read-only files, allowed dependencies,
  and forbidden changes
- frozen harness: dataset split, evaluation command, metric direction, resource
  measure, and fixed time or compute budget
- baseline run before any candidate change
- frontier policy: `keep`, `discard`, and `crash` statuses with a clear rule for
  advancing or reverting candidates
- stop conditions and the events that require human approval

Use a frontier plot when it helps interpretation: discarded candidates as
background points, kept candidates as the running best, and labels only for
changes that materially explain the frontier.

## Output Separation

- `train_outputs/`: trusted training evidence.
- `explore_outputs/`: exploratory variants and caveated ideas.
- `analysis_outputs/`: result analysis and figures.
- `debug_outputs/`: failure diagnosis.

## Project Quality And Badge Readiness

Experiments that support a claim, figure, table, artifact, or reproducibility
statement must remain traceable from `experiments/registry.csv` to the run
record, command, inputs, outputs, and validation result. Keep exploratory runs
in `explore_outputs/`; promote only trusted evidence to `train_outputs/`,
`repro_outputs/`, or `outputs/`. When a run supports artifact availability,
functionality, reusability, reproduction, or replication, update
`artifacts/badge-evidence-ledger.csv`.
