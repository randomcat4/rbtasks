# F3BH01 — Benjamini-Hochberg: multiple-testing prose to exact step-up decisions

## Frozen source claim

Apply SciPy's Benjamini-Hochberg false-discovery-control semantics to the frozen rational p-values: return every exact adjusted p-value in original order and the original indices rejected at alpha=1/20.

The exact public input is `input.json`. Every rational must be returned as a reduced `{"num": integer, "den": positive_integer}`; floating-point approximations and tolerance-based equality are rejected.

## Submission contract

Return `order`, the sorted raw factors `raw_sorted`, exact `adjusted` values, `rejected_indices`, and evidence kind `reverse_cummin` or `threshold_scan`.
