# F3BSP1 — Repeated-knot B-spline: exact value and right derivative

## Frozen source claim

Evaluate the frozen quadratic B-spline and its first right derivative exactly at the repeated interior knot x=1, using the frozen half-open interval convention.

All rationals use reduced `{"num": integer, "den": positive_integer}`. The knot vector, coefficient data, half-open basis convention, and right-sided derivative convention are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return reduced rational `value`, `first_derivative_right`, and kind `cox_de_boor_basis` or `local_de_boor_derivative`.
