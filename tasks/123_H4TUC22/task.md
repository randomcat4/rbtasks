# H4TUC22 — Exact Tucker decomposition and multilinear ranks

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- If tensor has shape I by J by K and target ranks are (r1,r2,r3), factors have shapes I*r1, J*r2, K*r3 and core has shape r1*r2*r3.
- Reconstruction is T[i][j][k]=sum_(a,b,c) A[i,a]B[j,b]C[k,c]core[a,b,c].
- Mode-0 unfolding rows i and columns (j,k) with j outer; mode-1 rows j and columns (i,k); mode-2 rows k and columns (i,j). Ranks and zero-based RREF pivot columns are listed in mode order 0,1,2.

### Required output fields

- `factor_A` — JSON type: rational matrix; shape: [I][r1]. mode-0 Tucker factor. Canonicalization: row-major.
- `factor_B` — JSON type: rational matrix; shape: [J][r2]. mode-1 Tucker factor. Canonicalization: row-major.
- `factor_C` — JSON type: rational matrix; shape: [K][r3]. mode-2 Tucker factor. Canonicalization: row-major.
- `core` — JSON type: 3D rational array; shape: [r1][r2][r3]. Tucker core indexed [a][b][c]. Canonicalization: literal index order.
- `unfolding_ranks` — JSON type: array of integers; shape: [3]. exact ranks of mode 0,1,2 unfoldings. Canonicalization: mode order 0,1,2.
- `unfolding_pivots` — JSON type: array of integer arrays; shape: [3][rank per mode]. zero-based RREF pivot columns of each unfolding. Canonicalization: mode order; each list strictly increasing.
