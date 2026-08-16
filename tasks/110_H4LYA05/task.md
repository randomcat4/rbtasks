# H4LYA05 — Exact discrete Lyapunov equation with an LDL positivity witness

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let n=rows(A). P is the unique symmetric exact solution of P-A^T P A=Q.
- LDL uses a unit lower-triangular L and diagonal vector D in increasing pivot order, with no symmetric pivoting: P=L diag(D)L^T.
- Leading principal minors are determinants of P[0:k,0:k] for k=1,...,n.

### Required output fields

- `P` — JSON type: rational matrix; shape: [n][n]. unique symmetric P with P-A^T P A=Q. Canonicalization: row-major exact matrix.
- `LDL_L` — JSON type: rational matrix; shape: [n][n]. unit lower-triangular L from unpivoted LDL. Canonicalization: diagonal 1, entries above diagonal 0.
- `LDL_D` — JSON type: array of rationals; shape: [n]. diagonal pivots D with P=L diag(D)L^T. Canonicalization: in pivot order, all positive.
- `leading_principal_minors` — JSON type: array of rationals; shape: [n]. determinants of leading k by k blocks. Canonicalization: k=1,...,n order.
