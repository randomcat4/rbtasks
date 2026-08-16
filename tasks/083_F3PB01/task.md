# F3PB01 — Poisson-binomial tail: heterogeneous Bernoulli trials to a generating polynomial

## Frozen source claim

For the frozen independent Bernoulli trials with heterogeneous rational success probabilities, compute exactly the probability that at least eight trials succeed and certify the full Poisson-binomial mass function.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return the exact tail as `claim`, the complete exact `pmf[0..n]`, and evidence kind `polynomial_dp` or `outcome_enumeration`.
