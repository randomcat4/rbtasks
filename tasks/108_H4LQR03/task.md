# H4LQR03 — Finite-horizon exact LQR: Riccati recursion meets open-loop KKT

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let N=horizon, n=rows(A), m=columns(B), with x_(t+1)=A x_t+B u_t. The cost is sum_(t=0)^(N-1)(x_t^T Q x_t+u_t^T R u_t)+x_N^T Q_terminal x_N.
- Use P_N=Q_terminal, M_t=R+B^T P_(t+1) B, K_t=M_t^(-1) B^T P_(t+1) A, and P_t=Q+A^T P_(t+1)A-A^T P_(t+1)B M_t^(-1)B^T P_(t+1)A.
- Controls follow u_t=-K_t x_t; all time-indexed arrays are chronological.

### Required output fields

- `riccati_P` — JSON type: array of rational matrices; shape: [N+1][n][n]. P_0 through P_N from the stated Riccati recursion. Canonicalization: chronological, P_N=Q_terminal.
- `feedback_K` — JSON type: array of rational matrices; shape: [N][m][n]. K_t in u_t=-K_t*x_t. Canonicalization: chronological.
- `states` — JSON type: array of rational vectors; shape: [N+1][n]. x_0 through x_N under submitted feedback. Canonicalization: chronological, begins at input x0.
- `controls` — JSON type: array of rational vectors; shape: [N][m]. u_0 through u_(N-1). Canonicalization: chronological.
- `optimal_value` — JSON type: rational scalar; shape: scalar. full finite-horizon cost, equivalently x0^T P0 x0. Canonicalization: reduced exact rational.
