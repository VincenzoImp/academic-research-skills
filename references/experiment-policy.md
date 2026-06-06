# Experiment Policy

Use this policy for computational experiments, including autonomous or overnight
loops.

## Required Boundary

Before a run campaign, record:

- research question or hypothesis
- Mutability Envelope: editable files or modules, read-only files or modules,
  allowed dependencies, and forbidden changes
- Frozen Harness: non-editable evaluation code, dataset split, metric direction,
  resource measure, and fixed time or compute budget
- metric and direction
- time budget
- compute constraints
- allowed dependencies
- stopping condition
- output directory
- baseline run

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
- status: trusted, exploratory, failed, discarded, keep, discard, crash
- short description

## Frontier Ledger

For autonomous or overnight campaigns, keep a tab-separated frontier ledger such
as `experiments/campaigns/frontier-results.tsv` with a compact row per
candidate. The minimum columns are:

```tsv
run_id	git_commit	metric_value	resource_value	status	description
```

Use `keep, discard, crash` as campaign statuses when the campaign advances a
single frontier. A candidate can be kept only when it improves the agreed metric
or meaningfully simplifies the system without degrading the metric. The baseline
run must be recorded before the first candidate.

## Autonomous Loop Rule

Autonomous loops must not silently change the benchmark, dataset split, metric,
or evaluation harness. If those need to change, stop and ask for a new research
decision.
