# H4SOC30 — Exact SOCP optimum with KKT and dual-norm certificate

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let d=M_diagonal, R=radius, y_i=d_i*x_i, and minimize c dot x subject to sum_i y_i^2<=R^2. All vectors have length len(d).
- At the nonzero boundary, multiplier mu uses stationarity c_i+mu*d_i*y_i/R=0 and mu>=0. stationarity_residual lists these left sides.
- dual_vector is M^(-T)c, i.e. c_i/d_i. Certify primal feasibility, complementary slackness, exact stationarity, and the support equality objective_value=-radius*sqrt(dual_norm_square); all submitted squares remain derived fields.

### Required output fields

- `primal_x` — JSON type: array of rationals; shape: [len(M_diagonal)]. candidate minimizer x. Canonicalization: input coordinate order.
- `transformed_y` — JSON type: array of rationals; shape: [len(M_diagonal)]. y_i=M_diagonal[i]*x_i. Canonicalization: input coordinate order.
- `norm_square` — JSON type: rational scalar; shape: scalar. sum_i y_i^2. Canonicalization: derive exactly as sum_i transformed_y[i]^2; enforce norm_square<=radius^2 and KKT complementarity.
- `objective_value` — JSON type: rational scalar; shape: scalar. objective_c dot x. Canonicalization: exact optimal value.
- `kkt_multiplier` — JSON type: rational scalar; shape: scalar. mu in stated boundary stationarity. Canonicalization: nonnegative.
- `stationarity_residual` — JSON type: array of rationals; shape: [len(M_diagonal)]. c_i+mu*d_i*y_i/radius. Canonicalization: all entries exact zero.
- `dual_vector` — JSON type: array of rationals; shape: [len(M_diagonal)]. M^(-T)c, coordinate c_i/d_i. Canonicalization: input coordinate order.
- `dual_norm_square` — JSON type: rational scalar; shape: scalar. sum_i dual_vector[i]^2. Canonicalization: derive exactly as sum_i dual_vector[i]^2.
