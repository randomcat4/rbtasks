# F3WLS1 — Weighted least squares: inverse-variance prose to exact normal equations

## Frozen source claim

Fit the frozen three-parameter linear model by weighted least squares, interpreting the supplied weights as inverse variances, and return exact coefficients, residuals, weighted SSE and inverse weighted Gram matrix.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return `gram`, `rhs`, `beta`, `residuals`, exact `weighted_sse`, `gram_inverse`, and kind `normal_equations` or `cramer_kkt`.
