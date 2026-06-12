# Experiment Log & Autonomous Campaigns

## Per-run record

Keep a run log in the contribution folder (e.g. `runs.md`) for every run
that supports a claim:

hypothesis | command | git commit | seed | config | data version | metric |
result | runtime | status | notes

## Autonomous campaigns (long unattended sessions)

Declare in the run log header before starting:

- mutability envelope: which files may change; which are frozen
- frozen harness: dataset split, evaluation command, metric and direction,
  budget (time or run count)
- baseline: run and record it before any variant
- frontier policy: keep / discard / crash, with the rule for advancing or
  reverting candidates
- stop conditions, and which events require human approval

Never silently change the metric, the split, or the evaluation harness. Any
change that alters scientific meaning stops the campaign for approval.
