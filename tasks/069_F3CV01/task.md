# F3CV01 — Boundary convolution: reflect semantics to an exact separable image filter

## Frozen source claim

Convolve the frozen integer image with the frozen asymmetric separable 3×3 kernel using SciPy ndimage mode=reflect, origin=0, and true convolution indexing.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return the complete integer `output` and kind `direct_2d` or `separable_passes`; frozen nonempty rectangular input and odd kernel are required.
