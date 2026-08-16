# Design

ReturnBench tasks follow one common route:

`source mathematical object -> explicit representation transform -> checkable certificate -> source conclusion`

The benchmark favors exact witnesses, proof terms, primal/dual pairs, recurrences, residual bounds,
complete search traces and independently replayable certificates. Tasks that merely rename a library
theorem, change constants, or collapse to a one-line wrapper are excluded from the 150-task release.

Release quality and Pilot eligibility are separate axes. Public release means the statement,
provenance, license boundary and certificate contract passed review. Pilot eligibility additionally
requires hidden one-arm packaging and a fresh private evaluation instance.
