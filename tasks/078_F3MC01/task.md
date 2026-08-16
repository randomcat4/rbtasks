# F3MC01 — Markov temporal event: workflow prose to a product-state automaton

## Frozen source claim

Under the frozen rational five-state Markov transition matrix, compute exactly the probability that during times 1 through 8 the chain visits success exactly twice and never visits failure.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return exact `claim`, its exact partition `event_by_final_state`, and evidence kind `product_automaton` or `path_partition`.
