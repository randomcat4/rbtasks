# H4TEN20 — Tensor-network contraction across two parenthesizations

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- All indices i,j,k,l,m,n range 0..d-1 with d inferred from B. Nested arrays follow the literal index order named below.
- AB_over_k[i][j][l]=sum_k A[i][j][k]B[k][l]. CD_over_n[l][m][i]=sum_n C[l][m][n]D[n][i].
- Y[j][m]=sum_(i,l) AB_over_k[i][j][l] CD_over_n[l][m][i], which must also equal the direct four-index contraction in input.index_equation.

### Required output fields

- `AB_over_k` — JSON type: 3D rational array; shape: [d][d][d] indexed [i][j][l]. sum_k A[i,j,k]B[k,l]. Canonicalization: literal index order i,j,l.
- `CD_over_n` — JSON type: 3D rational array; shape: [d][d][d] indexed [l][m][i]. sum_n C[l,m,n]D[n,i]. Canonicalization: literal index order l,m,i.
- `Y` — JSON type: rational matrix; shape: [d][d] indexed [j][m]. contraction of the two intermediates and direct Einstein network. Canonicalization: literal index order j,m.
