---
name: research-design-positioning
description: Use when developing academic research ideas, framing research questions, defining scope, novelty, contribution claims, hypotheses, operational definitions, evidence plans, or publishable positioning before SOTA, experiments, or writing.
license: MIT
---

# Research Design Positioning

Turn rough ideas, literature gaps, and hunches into researchable questions and
defensible contribution claims. Use this before experiments, SOTA synthesis, or
paper drafting when the project is not yet falsifiable and scoped.

## Read First

- `references/research-positioning-policy.md`
- `references/repository-contract.md`
- `references/output-contracts.md`

## Workflow

1. State the problem, target community, and why the field should care now.
2. Extract candidate gaps from `sota/gaps.md`, `sota/synthesis.md`, source pages,
   and venue expectations.
3. Draft candidate research questions and reject questions that cannot be
   answered with available sources, data, experiments, or defensible analysis.
4. Convert viable questions into contribution claims and identify the closest
   prior work for each claim.
5. Define constructs, variables, units of analysis, operational definitions, and
   scope boundaries.
6. State hypotheses or expected patterns when appropriate.
7. Define the minimum evidence needed: SOTA, dataset, experiment, qualitative
   coding, reproduction, benchmark, expert judgment, or artifact evaluation.
8. Mark claims as hypothesis, partial, supported, rejected, or out of scope.
9. Save the stable version in `docs/methodology/research-design.md`.
10. Add open issues to `wiki/open_questions.md` or `wiki/questions/`.

## Contribution Types

- empirical finding
- method, algorithm, model, or system
- dataset, benchmark, taxonomy, or measurement instrument
- reproduction, replication, or negative result
- theory, conceptual reframing, or design framework
- survey, mapping study, or structured literature synthesis

## Quality Gate

A research design is not ready for experiments or writing until it has:

- problem, audience, and venue fit
- research questions with scope and evidence path
- closest prior work and specific delta
- operational definitions for key constructs
- success criteria and failure condition
- minimum evidence needed for each claim
- threat that could invalidate the contribution

## Output

Prefer concise tables in `docs/methodology/research-design.md`:

- `rq_id`, `question`, `scope`, `evidence_needed`, `method`, `risk`, `status`
- `claim_id`, `claim`, `closest_prior_work`, `delta`, `evidence`, `failure_condition`, `status`
- `construct`, `definition`, `observable_proxy`, `limitations`

## Do Not

- Treat "no one has done X" as novelty without searching.
- Claim generality beyond the intended population, benchmark, domain, or source base.
- Start drafting the paper before identifying the strongest adjacent work.
- Let an interesting question survive if it has no evidence path.
