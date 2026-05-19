# CS Methodology Evaluation Policy

Use this reference for computer science evaluation plans and validity audits.

## Evaluation Plan Fields

- research question
- claim under test
- dataset or benchmark
- baselines
- metrics
- experimental unit
- split policy
- seeds and repetitions
- hardware and environment
- ablations
- statistical test or uncertainty estimate
- expected output
- failure condition

## Threat Categories

- internal validity: confounding, leakage, implementation bugs
- external validity: benchmark/domain generalization
- construct validity: metric does not measure the intended concept
- conclusion validity: insufficient statistical support or overclaiming
- reproducibility: missing configs, data, seeds, hardware, or commands

## CS-Specific Checks

- compare against strong and recent baselines
- report negative and boundary cases
- avoid test-set tuning
- include ablations tied to mechanism claims
- disclose compute and hyperparameter search
- separate exploratory and confirmatory runs
