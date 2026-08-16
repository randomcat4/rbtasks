# F3MSH1 — Closed triangle mesh: oriented faces to exact volume and centroid

## Frozen source claim

For the frozen closed, nondegenerate, outward-oriented triangular prism mesh, compute exact signed volume and volume centroid; every undirected edge must occur exactly twice and total signed volume must be positive.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return exact `signed_volume`, exact `centroid`, and kind `oriented_origin_tetrahedra` or `interior_absolute_tetrahedra`.
