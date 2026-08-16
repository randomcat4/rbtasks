# F3UNT1 — Affine temperature units: heating data to an exact energy conversion

## Frozen source claim

Compute Q=m c ΔT for the frozen Fahrenheit measurements, treating Δ°F as a temperature difference with scale 5/9 K and no absolute offset, then convert the frozen Pint Btu to joules exactly.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return exact `delta_degF`, `delta_K`, `heat_Btu`, `heat_J`, and kind `source_unit_cancellation` or `full_SI_chain`.
