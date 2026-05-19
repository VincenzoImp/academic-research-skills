# Experiment Policy

Use this policy for computational experiments, including autonomous or overnight
loops.

## Required Boundary

Before a run campaign, record:

- research question or hypothesis
- editable files or modules
- non-editable files or frozen evaluation harness
- metric and direction
- time budget
- compute constraints
- allowed dependencies
- stopping condition
- output directory

## Run Ledger

Every run should record:

- run ID
- git commit
- command
- config
- seed
- dataset version
- metric result
- runtime
- resource usage if relevant
- status: trusted, exploratory, failed, discarded
- short description

## Autonomous Loop Rule

Autonomous loops must not silently change the benchmark, dataset split, metric,
or evaluation harness. If those need to change, stop and ask for a new research
decision.
