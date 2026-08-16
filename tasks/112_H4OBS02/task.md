# H4OBS02 — Observability quotient with an invariant-kernel certificate

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let n be the state dimension. Stack O=[C; CA; ...; CA^(n-1)] with rows in increasing power order. RREF uses left-to-right pivots and exact rational arithmetic.
- The annihilator is the least positive degree d for which a monic p(z)=sum_{j=0}^d c_j z^j satisfies C p(A)=0; degrees are tried in increasing order and c_d=1.
- The canonical nullspace basis of O uses increasing free columns, one unit free coordinate per vector, and RREF-determined pivot coordinates.

### Required output fields

- `rank` — JSON type: integer; shape: scalar. rank of stacked observability matrix O. Canonicalization: exact RREF rank.
- `rref_pivots` — JSON type: array of integers; shape: [rank]. zero-based pivot columns of RREF(O). Canonicalization: strictly increasing.
- `kernel_basis` — JSON type: array of rational arrays; shape: [(n-rank) by n]. canonical basis of ker(O). Canonicalization: in increasing free-column order.
- `annihilator_coefficients_ascending` — JSON type: array of rationals; shape: [d+1]. coefficients c_0,...,c_d of least-degree monic p with C*p(A)=0. Canonicalization: ascending powers, last entry 1.
- `indistinguishable_delta` — JSON type: array of rationals; shape: [n]. first canonical kernel vector. Canonicalization: exactly kernel_basis[0].
