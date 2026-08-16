# F3FIR1 — Polyphase resampling: upsample-filter-downsample to exact phase-zero output

## Frozen source claim

Apply the frozen FIR with up=3, down=2, constant-zero extension and decimation phase zero, using SciPy upfirdn output-length semantics.

All rationals use reduced `{"num": integer, "den": positive_integer}`. Index, boundary, orientation, normalization and degeneracy conventions are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return the full exact rational `output` and kind `polyphase_index` or `zero_insert_convolve`.
