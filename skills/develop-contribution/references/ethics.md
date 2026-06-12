# Ethics & Data Red Flags

Check before collecting, storing, or sharing data:

- personal identifiers in raw or derived files
- screenshots exposing users, handles, addresses, or private chats
- scraping behind login or against platform terms
- "publicly visible" is not automatically redistributable
- datasets shared without license or consent analysis
- model outputs that may reveal memorized sensitive data

Rules: raw sensitive data stays in gitignored local folders unless sharing
is approved; prefer aggregate or redacted outputs in reports; record every
de-identification transformation; re-check all of the above before any
artifact is packaged for release.
