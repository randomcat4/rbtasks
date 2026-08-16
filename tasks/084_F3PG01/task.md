# F3PG01 — Polygon with a hole: oriented rings to exact area and centroid

## Frozen source claim

For the frozen simple polygon with a clockwise hole, compute exact area and centroid using signed ring orientation; reject zero-area, self-intersecting or nonpositive-total-area inputs.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return `signed_ring_areas`, exact positive `area`, exact `centroid`, and kind `shoelace_moments` or `signed_triangle_fan`.
