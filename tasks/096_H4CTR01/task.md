# H4CTR01 — Minimum-energy reachability with a dual Gramian certificate

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let n=len(target), h=horizon and b be the only column of B. Define the reachability matrix C_h=[A^(h-1)b, A^(h-2)b, ..., b] in input-time order and G=C_h C_h^T.
- The submitted control is the unique minimizer of sum_k u_k^2 subject to C_h u=target; the dual convention is G y=target and u=C_h^T y.
- The canonical nullspace basis is obtained from RREF(C_h): free columns increase, each basis vector has its own free coordinate 1, other free coordinates 0, and pivot coordinates from the RREF equations.

### Required output fields

- `control` — JSON type: array of rationals; shape: [horizon]. u in input-time order. Canonicalization: unique minimum-energy solution.
- `dual` — JSON type: array of rationals; shape: [state dimension]. y with G*y=target and u=C_h^T*y. Canonicalization: unique exact Gramian/KKT dual.
- `energy` — JSON type: rational scalar; shape: scalar. sum_k control[k]^2. Canonicalization: reduced exact rational.
- `terminal` — JSON type: array of rationals; shape: [state dimension]. C_h*control. Canonicalization: must equal input target.
- `nullspace_orthogonality` — JSON type: array of rationals; shape: [horizon-rank(C_h)]. dot products of control with canonical nullspace basis vectors. Canonicalization: basis/free-column order from task rules; every value is zero.
