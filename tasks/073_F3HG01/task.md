# F3HG01 — Fisher exact test: fixed margins to an exact two-sided tail

## Frozen source claim

For the frozen 2×2 table, compute SciPy's exact two-sided Fisher p-value: under the fixed-margin hypergeometric law, sum the probabilities of every support table whose probability is less than or equal to that of the observed table.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return `claim`, `observed_x`, the complete `selected_x`, all unnormalised support `weights`, their `common_denominator`, and evidence kind `ratio_recurrence` or `support_enumeration`.
