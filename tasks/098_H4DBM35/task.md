# H4DBM35 — Timed-automata DBM closure through guards, reset and elapse

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- DBM[i][j] bounds clock_i-clock_j. null is infinity; [c,true] is strict and tighter than [c,false] at equal c. Bound addition adds constants and ORs strictness.
- Canonical closure is all-pairs shortest paths in the bound semiring. Guard intersects bounds then closes; reset copies reference-clock row and column for the reset clock; time elapse removes each real clock upper bound to the reference then closes.
- Every finite final entry has a clock-index path realizing its bound. The rational valuation sets reference clock to zero and must satisfy strict and non-strict entries literally.

### Required output fields

- `stage_dbms` — JSON type: array of objects; shape: [initial plus operation count]. stage name and canonical DBM after each operation. Canonicalization: operation order.
- `final_canonical_dbm` — JSON type: matrix of bounds; shape: [clock count]^2. closed DBM at last stage. Canonicalization: row i,column j.
- `final_shortest_paths` — JSON type: array of objects; shape: [finite DBM entries]. i,j and clock-index path realizing the entry. Canonicalization: row-major finite-entry order.
- `valuation_witness` — JSON type: array of rationals; shape: [clock count]. one valuation satisfying final zone with reference zero. Canonicalization: clock order.
- `diagonal_bounds` — JSON type: array of bounds; shape: [clock count]. final diagonal entries. Canonicalization: clock order.
