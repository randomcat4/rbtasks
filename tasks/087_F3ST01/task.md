# F3ST01 — Sturm root counting: polynomial coefficients to closed-interval certificates

## Frozen source claim

For the frozen square-free integer polynomial, count its real roots in each frozen closed rational interval, including any root equal to a lower endpoint, and provide the exact Sturm sequence.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return exact rational-coefficient `sturm_sequence`, integer `counts`, and kind `sturm_certificate` or `factor_isolation`.
