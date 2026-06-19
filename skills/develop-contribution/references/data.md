# Data & Input Dependencies

Where a contribution's data lives, and how to handle data that flows between
contributions. Optional — use it only when a contribution has shared/large data
or consumes another contribution's output.

## Where data lives (two axes)

Decide by sharing scope and by tracked-vs-gitignored, not by size alone:

- **Private + small + curated + non-sensitive** (a hand-made input file, the
  contribution's own result tables/figures) → committed **inside** the
  contribution (`contributions/<slug>/…`).
- **Large OR regenerable OR governed/sensitive** → **gitignored**. For
  data-heavy projects, keep it in one root `data/` organized by a subfolder per
  **owning** contribution: `data/<slug>/` with tiers `raw/` (immutable source),
  `interim/` (regenerable intermediates), `processed/` (consumable datasets).
  One root = one place to gitignore, back up, and find; per-contribution
  subfolders = clear ownership.
- **Sensitive data** (account ids, raw PII) never enters the tracked tree — see
  `ethics.md`.

## Inter-contribution data dependencies

A contribution's input is often another contribution's output, or data
generated and archived by another contribution. When so:

- **Declare** the dependency in this contribution's README: name the producer
  contribution and the dataset it consumes.
- **Read it in place** at the producer's location (`data/<producer>/…`) —
  **never copy** it into your own folder. One dataset, one physical home.
- Record the lineage under the README "data provenance" badge item (which
  contribution and which output produced this input).

## Single source of truth for paths

Map each logical dataset to its one physical location in a single module or
config (e.g. a `paths` module), not as literals scattered across scripts — so
the producing contribution can change the layout in one place without breaking
its consumers.

Rules: a contribution stays self-contained at the interface — it declares what
it reads and never imports another contribution's *code*; data it consumes is
read from the producer's declared location, never duplicated.
