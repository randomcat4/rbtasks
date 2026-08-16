# F3DIM1 — Buckingham-style dimensional analysis: physical quantities to canonical Pi groups

## Frozen source claim

Using the frozen M/L/T dimensions, find the two uniquely anchored primitive dimensionless monomials: one with exponent F=1,mu=0 and one with F=0,mu=1.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return the two exponent vectors as `groups` in frozen variable order and kind `dimension_nullspace` or `bounded_monomial_search`.
