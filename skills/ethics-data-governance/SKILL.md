---
name: ethics-data-governance
description: Use when academic research involves human subjects, public web data, platform scraping, sensitive domains, privacy risk, dataset sharing, consent, IRB, licenses, or data retention.
license: MIT
---

# Ethics Data Governance

Handle ethics and data governance as part of the research record, not as a late
appendix. This is especially important for platform, community, security, health,
education, and other sensitive-domain research.

## Read First

- `references/ethics-data-governance.md`
- `references/repository-contract.md`

## Workflow

1. Identify data subjects, platforms, communities, institutions, and affected groups.
2. Classify sensitivity: public, restricted, personal, vulnerable, illegal,
   copyrighted, proprietary, or dual-use.
3. Record collection boundaries, access method, terms-of-service risk, consent,
   IRB or ethics-board status, and retention policy in `docs/ethics/data-governance.md`.
4. Keep raw sensitive data in ignored local folders unless sharing is approved.
5. Prefer aggregate, redacted, or synthetic outputs in reports.
6. Add risk notes to dataset pages and claim pages.
7. Re-check governance before publishing artifacts, code, or examples.

## Red Flags

- personal identifiers in raw or derived files
- screenshots that expose users, handles, addresses, chats, or illegal content
- scraping behind login or against platform restrictions
- model outputs that can reveal memorized sensitive data
- publishing datasets without license or consent analysis

## Do Not

- Treat "publicly visible" as automatically safe to redistribute.
- Put credentials, cookies, session exports, or scraped private content in git.
- De-identify by hand without recording the transformation.
