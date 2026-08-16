# F3KF01 — Kalman filter: linear-Gaussian measurements to an exact rational posterior

## Frozen source claim

Execute the frozen two-dimensional, three-measurement Kalman model in predict-then-update order and return every exact rational predicted/updated mean and covariance, using the full Joseph covariance update.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return `final_mean`, `final_covariance`, the complete exact `trajectory`, and evidence kind `joseph_form` or `gaussian_conditioning`.
