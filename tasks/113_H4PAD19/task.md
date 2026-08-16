# H4PAD19 — Exact [10/10] Pade approximant of exp

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let n=numerator_degree, m=denominator_degree, a_k=1/k!, P=sum_(k=0)^n p_k x^k, Q=sum_(j=0)^m q_j x^j with q_0=1.
- Require coefficients of Q*exp-P to vanish through degree n+m. For k<=n, p_k=sum_(j=0)^min(k,m) q_j a_(k-j).
- first_residual_coefficient is coefficient n+m+1 of Q*exp-P. hankel_system_determinant is det([a_(n+i-j)]_(i,j=1..m)) and must be nonzero.

### Required output fields

- `P_ascending` — JSON type: array of rationals; shape: [n+1]. numerator coefficients p_0,...,p_n. Canonicalization: ascending powers.
- `Q_ascending` — JSON type: array of rationals; shape: [m+1]. denominator coefficients q_0,...,q_m. Canonicalization: ascending powers, q_0=1.
- `first_residual_coefficient` — JSON type: rational scalar; shape: scalar. coefficient x^(n+m+1) of Q*exp-P. Canonicalization: exact reduced rational.
- `hankel_system_determinant` — JSON type: rational scalar; shape: scalar. determinant of the specified m by m coefficient system. Canonicalization: exact and nonzero.
