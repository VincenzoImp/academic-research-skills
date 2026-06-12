# Reproducing External Work

A reproduction contribution faithfully runs someone else's artifact; it
does not improve anything until the reproduction outcome is recorded.

1. Read the external repo's README, configs, environment files.
2. Inventory the documented commands.
3. Pick the smallest trustworthy target first: smoke test → inference →
   evaluation → training.
4. Record assumptions (data, weights, hardware) in the contribution README.
5. Run only documented or clearly justified commands.
6. Patches needed to make it run go in a separate `PATCHES.md` and are
   never mixed with this project's contribution claims.
7. Record the outcome honestly: reproduced / partial / failed, with logs.

A failed reproduction never silently becomes an exploratory refactor, and a
smoke test never supports a correctness or SOTA claim.
