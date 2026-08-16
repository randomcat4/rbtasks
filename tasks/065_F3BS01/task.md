# F3BS01 — Exact bootstrap: empirical observations to a multinomial resampling law

## Frozen source claim

Draw seven observations with replacement from the frozen seven-observation empirical sample, retaining duplicate observations as separate empirical atoms; compute exactly the distribution of the resample sum and its tail at 42.

The exact public input is `input.json`. All rationals must be reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance equality are rejected.

## Submission contract

Return the complete integer `distribution`, `total_resamples`, exact `tail_probability`, and kind `multinomial_compositions` or `ordered_resamples`.
