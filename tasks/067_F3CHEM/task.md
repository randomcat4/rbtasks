# F3CHEM — Redox stoichiometry: species formulas and charge to a primitive integer balance

## Frozen source claim

Balance the frozen acidic permanganate/iron redox reaction as the unique primitive positive integer coefficient vector conserving every listed element and net electric charge.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return reactant-then-product `coefficients`, one zero `balance` per element plus charge, and kind `integer_nullspace` or `bounded_enumeration`.
