---
name: manage-submission
description: Use when submitting a paper, recording decisions and reviews, drafting rebuttals and response letters, applying revisions, or preparing the camera-ready version.
license: MIT
---

# Manage Submission

Operate the lifecycle of `papers/<slug>/` around its venue events. The
current version always lives in `manuscript/`; every submitted version is
frozen forever in `archive/`.

## Read First

- `papers/README.md` — the lifecycle contract
- `papers/<slug>/correspondence/` — current review state
- `references/concern-map.md`

## Events

**Submit.** Verify `make paper P=<slug>` and `make check` pass and the
artifacts bundle is current. Freeze: copy `manuscript/` (with its PDF) and
`artifacts/` into `archive/r<N>/` exactly as submitted. Archives are
immutable from that moment.

**Decision received.** Save the decision letter and the reviews verbatim in
`correspondence/`. Summarize the outcome for the user.

**Rebuttal.** Build the concern map per `references/concern-map.md`. Draft
the response in `correspondence/`: per concern — direct answer, evidence,
and the exact manuscript change it commits to. Get user approval before
anything is sent.

**Revision.** Apply the promised changes to `manuscript/`, tracking which
concern each change answers (concern ids in a change log in
`correspondence/`). New scientific work requested by reviewers goes through
develop-contribution first, never directly into prose. Rebuild, re-check,
then Submit again as the next round.

**Camera-ready.** Apply final venue requirements (de-anonymization, format,
DOI links), then freeze `archive/camera-ready/`.

## Rules

- Never edit anything inside `archive/`.
- A response letter only promises changes that can actually land in the
  revision before the deadline.
- Reviews are private input: they stay inside `correspondence/` and are
  never quoted in public artifacts.

## Done When

- The event is fully recorded — archive frozen and/or correspondence
  updated — the manuscript state is consistent, and `make check` passes
