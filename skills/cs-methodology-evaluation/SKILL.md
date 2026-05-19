---
name: cs-methodology-evaluation
description: Use when designing or auditing computer science experiments, evaluation plans, baselines, metrics, ablations, datasets, statistical tests, benchmarks, validity threats, or reproducibility claims.
license: MIT
---

# CS Methodology Evaluation

Use this for CS research where the scientific claim depends on experiments,
benchmarks, data analysis, systems measurements, user studies, or software
engineering evidence.

## Read First

- `references/cs-methodology-evaluation-policy.md`
- `references/experiment-policy.md`
- `references/repository-contract.md`

## Workflow

1. Identify claim type and evidence type: algorithmic, empirical, systems,
   human-subject, dataset, benchmark, tool, reproduction, or negative result.
2. Define evaluation questions before running experiments.
3. Select baselines, datasets, metrics, splits, seeds, hardware, and budgets.
4. Add ablations and sensitivity checks that test the claimed mechanism.
5. Identify leakage, confounding, overfitting, selection bias, and benchmark mismatch.
6. Record the plan in `docs/methodology/evaluation-plan.md`.
7. Record threats in `docs/methodology/threats-to-validity.md`.
8. Connect runs to `experiments/registry.csv` and output folders.

## Minimum Evaluation Standard

- credible baseline or reason none exists
- metric justified by research question
- dataset provenance and split policy
- repeatability details: seed, config, environment, hardware
- negative cases or boundary conditions
- threats to internal, external, construct, and conclusion validity

## Do Not

- Tune on test data.
- Add baselines after seeing only favorable results without noting the timing.
- Present exploratory runs as confirmed evidence.
- Hide failed or ambiguous runs that affect the claim.
