# F3DFT1 — Eight-point DFT: Gaussian integers to exact Q(sqrt2,i) bins

## Frozen source claim

Compute the frozen unnormalised forward eight-point DFT with kernel exp(-2πikn/8), returning every bin exactly in Q(√2,i).

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return eight `bins`, each `[a,b,c,d]` for a+b√2+i(c+d√2), and kind `direct_dft` or `radix2_fft`.
