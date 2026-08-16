# F3KM01 — Kaplan-Meier: censored records to an exact product-limit curve

## Frozen source claim

For the frozen event/censor records, compute every exact Kaplan-Meier survival step and cumulative Greenwood sum, with same-time censored subjects remaining at risk for events at that time.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return exact final `survival`, exact `greenwood_sum`, the complete `timeline`, and kind `event_table_recurrence` or `individual_risk_sets`.
