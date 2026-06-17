---
name: digest-paper
description: Use when adding, ingesting, or digesting a single paper into the SOTA — from a title, DOI, arXiv id, URL, or PDF — producing its folder, synthesis, bib entry, citation graph, and index row.
license: MIT
---

# Digest Paper

Digest one paper end-to-end into `sota/papers/<citekey>/`. This is the
atomic unit of SOTA work: it either completes fully or it does not happen.
Never leave a partial digest.

## Read First

- `sota/README.md` — synthesis format and digestion rules (the scaffold owns the format)
- `references/bibliography-rules.md` — citekeys, version resolution, cross-validation

## MCP Preflight (hard gate)

Before anything else, probe the scholarly MCP servers with one trivial query
each (e.g., search a known title). The gate is by capability, never by API
key — a missing key only throttles, it never blocks:

- **Required:** `arxiv` (full text) must respond, AND at least one
  bibliographic source — `semantic-scholar`, `dblp`, or `openalex` — must
  respond.
- If those required capabilities are unavailable: STOP, report which servers
  failed, and ask the user to fix the MCP setup.
- If a reachable source is down but the gate is met, proceed and note the
  reduced cross-check in the synthesis.

Never fall back to model memory, web search, or scraping. A citation exists
only if an MCP lookup produced it.

## Procedure

1. Resolve identity: from the given title/DOI/arXiv/PDF, find the paper via
   semantic-scholar (and dblp for CS work). Ask the user only if the match
   is genuinely ambiguous.
2. Resolve the most authoritative version: published venue > latest arXiv
   revision > other preprint, per `references/bibliography-rules.md`.
   Record both DOI and arXiv id when both exist.
3. Choose the citekey (`<firstauthor><year><topicword>`, lowercase) and
   check it is unused: not in `references.bib`, no
   `sota/papers/<citekey>/` folder.
4. Create `sota/papers/<citekey>/` and download the full-text PDF as
   `paper.pdf` (arxiv MCP for arXiv papers; otherwise the open-access URL
   from the MCP metadata). If no legal full text is found, stop, remove the
   folder, and record the candidate in `sota/queue.md` with decision
   `unresolvable-via-mcp`. Abstract-only digestion is forbidden.
5. Read the full paper — the PDF, cover to cover, not the abstract.
6. Write `synthesis.md` following the exact section order in
   `sota/README.md`. Verify every exact number and quotation against the
   PDF.
7. Write the BibTeX entry into the SOTA section of `references.bib`, built
   from MCP-sourced fields cross-checked per
   `references/bibliography-rules.md`. Never write a field from memory.
8. Fetch citations via semantic-scholar: outgoing references and incoming
   citations. Select the relevant ones, not all. Write `metadata.yaml` with
   every field from the schema in `sota/README.md`, including the mandatory
   `verified:` block. Use citekeys for papers already in the SOTA, external
   ids otherwise.
9. Append the row to `sota/index.md` with status `digested`.
10. Add in-scope leads from `cites`/`cited_by` and the synthesis "Citation
    leads" section to `sota/queue.md` as `pending`, with provenance.
11. Run `make check` from the project root and fix anything it reports.

## Rules

- All-or-nothing: if any step cannot complete, revert the partial folder
  and record the paper in `queue.md` instead.
- One paper = one folder = one bib entry = one index row (1:1:1).
- While digesting, the only edit allowed in other papers' folders is
  upgrading an external id to a citekey in their `cites`/`cited_by` lists.

## Done When

- `sota/papers/<citekey>/` has `paper.pdf`, `synthesis.md`, `metadata.yaml`
- `references.bib` and `sota/index.md` each gained exactly one entry
- `make check` passes
