# F3P401 — Four-momentum conservation: visible particles to an exact missing invariant mass

## Frozen source claim

Under metric (+,-,-,-), subtract the two frozen visible four-momenta from the initial four-momentum and compute exact invariant mass-squared for the initial, both visible and missing momenta.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return exact `missing`, four exact `mass_squared` values, and kind `component_conservation` or `minkowski_invariants`; negative-energy or nonconserving submissions are rejected.
