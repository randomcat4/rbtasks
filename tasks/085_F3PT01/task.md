# F3PT01 — Paired exact permutation: sign symmetry to a subset-sum law

## Frozen source claim

For the frozen paired differences, compute the exact two-sided paired permutation p-value for the absolute signed-sum statistic, including outcomes tied with the observed extremeness.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return `observed_statistic`, the complete signed-sum `distribution`, exact `p_value`, and kind `subset_sum_dp` or `sign_enumeration`.
