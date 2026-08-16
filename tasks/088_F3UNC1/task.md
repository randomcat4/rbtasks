# F3UNC1 — Correlated uncertainty: measurement formulas to an exact covariance pushforward

## Frozen source claim

At the frozen rational nominal measurements, compute the exact first-order output covariance J Sigma J^T for the three frozen derived quantities, retaining the supplied x-y correlation.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return exact `nominal_outputs`, exact `jacobian`, exact `output_covariance`, and kind `dual_jacobian` or `pairwise_covariance`.
