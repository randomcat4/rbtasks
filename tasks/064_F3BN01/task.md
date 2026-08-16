# F3BN01 — Bayesian network: conditional tables to an exact posterior

## Frozen source claim

For the frozen eight-node binary Bayesian network and evidence C=1,G=0, compute exactly P(H=1 | C=1,G=0) and the evidence probability.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return exact `posterior` and `evidence_probability`; either provide a canonical factor `trace` for a complete `elimination_order` with kind `variable_elimination`, or every evidence-consistent joint `row` with kind `joint_enumeration`.
