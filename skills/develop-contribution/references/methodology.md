# Methodology Standard (CS evaluation)

Minimum for any evaluation that supports a claim:

- a credible baseline, or a stated reason none exists
- a metric justified by the research question
- dataset provenance and split policy recorded
- repeatability: seed, config, environment, hardware noted
- negative cases or boundary conditions exercised
- threats to validity: internal, external, construct, conclusion

Never: tune on test data; add baselines after seeing favorable results
without noting the timing; present exploratory runs as confirmed evidence;
hide failed or ambiguous runs that affect the claim.

## Statistics

- match the test to design, distribution, sample size, hypothesis
- report effect sizes and confidence intervals when relevant
- distinguish statistical from practical significance
- flag multiple comparisons, missing data, selection bias, confounds
- exploratory analysis is never confirmatory

## Figures and tables

- readable labels, units, captions; colorblind-safe palettes
- no misleading axes or decorative chart types
- save the source data and the generating command for every final figure
