# F3KEP1 — Kepler state vector: exact energy, eccentricity and orbital invariants

## Frozen source claim

For the frozen two-body state with exact rational radius, compute specific energy, angular momentum, eccentricity vector/square, semi-major axis and semilatus rectum, and cross-check the vector definitions against vis-viva and scalar eccentricity identities.

All rationals use reduced `{"num": integer, "den": positive_integer}`. The coordinate order, gravitational parameter, radius convention, and energy/orbit sign conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return exact `specific_energy`, `angular_momentum`, `angular_momentum_squared`, `eccentricity_vector`, `eccentricity_squared`, `semi_major_axis`, `semilatus_rectum`, and kind `state_vector_invariants` or `orbital_scalar_identities`.
