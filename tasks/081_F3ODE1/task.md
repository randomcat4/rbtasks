# F3ODE1 — Validated decay ODE: exact Taylor remainder to an outward interval

## Frozen source claim

For y′=-(3/5)y, y(0)=2, enclose y(1) in a rational interval of width at most 10^-12 using outward rounding, and certify the alternating-series truncation.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return integer `terms`, reduced rational `lower` and `upper`, and kind `alternating_taylor` or `decimal_envelope_crosscheck`; the judge also requires an independent outward 80-digit Decimal envelope to lie inside.
