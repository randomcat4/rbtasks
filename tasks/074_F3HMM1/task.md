# F3HMM1 — Hidden Markov model: observation narrative to exact forward likelihood

## Frozen source claim

For the frozen three-state, four-symbol HMM, compute exactly the likelihood of the nine-symbol observation sequence and the posterior probability that the final hidden state is state 2.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return exact `likelihood`, exact `posterior_final`, and either the full `forward` table with kind `forward_table` or final hidden-state weights with kind `path_partition`.
