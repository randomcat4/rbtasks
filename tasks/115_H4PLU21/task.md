# H4PLU21 — Pluecker coordinates to an RREF two-plane

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Input plucker key i,j means p_ij for 0<=i<j<n, with p_01=1. The canonical chart basis is row0=[1,0,-p_12,...,-p_1,n-1] and row1=[0,1,p_02,...,p_0,n-1].
- For every quadruple i<j<k<l in lexicographic order, residual=p_ij p_kl-p_ik p_jl+p_il p_jk.
- The skew matrix has K_ij=p_ij, K_ji=-p_ij, K_ii=0; skew_matrix_rank is its exact rational rank.

### Required output fields

- `rref_basis` — JSON type: rational matrix; shape: [2][dimension]. canonical p01=1 chart basis from task rule. Canonicalization: two rows exactly in stated order.
- `plucker_relation_residuals` — JSON type: array of objects; shape: [choose(dimension,4)]. each {indices:[i,j,k,l],value:rational}. Canonicalization: quadruples lexicographic; value is stated Pluecker residual.
- `skew_matrix_rank` — JSON type: integer; shape: scalar. exact rank of skew matrix built from p_ij. Canonicalization: nonnegative exact rank.
