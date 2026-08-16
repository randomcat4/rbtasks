# F3MW01 — Mann-Whitney exact test: samples to a rank-label distribution

## Frozen source claim

For the frozen tie-free samples, compute U1 and SciPy's exact two-sided p-value by the exact null distribution of rank labels, including the observed tail boundary.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return integer `u1`, the complete exact integer `counts[0..nx*ny]`, reduced `p_value`, and evidence kind `rank_sum_dp` or `label_enumeration`.
