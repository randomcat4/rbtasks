# H4BCH09 — BCH decoding with locator, roots and divisibility

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- A GF(64) element is an integer 0..63 whose bit j is the coefficient of alpha^j. Addition is XOR; multiplication is binary-polynomial multiplication modulo primitive_polynomial, whose integer bits encode x^6+x+1 (0x43).
- Binary words and polynomials use ascending coefficient order: received[i] is the x^i coefficient. Let alpha be the residue class of x and s_j=r(alpha^j).
- For an increasing error set E, Lambda(z)=product_(i in E)(1+alpha^i z), coefficients ascending. Its Chien roots satisfy Lambda(alpha^(-i))=0. The corrected word must equal received with exactly E toggled and equal generator_polynomial_ascending times the ascending binary quotient.

### Required output fields

- `syndromes_s1_to_s6` — JSON type: array of integers; shape: [2*designed_t]. s_j=received(alpha^j), j=1,...,2t, in GF(64) encoding. Canonicalization: j increasing.
- `locator_polynomial_gf64_ascending` — JSON type: array of integers; shape: [error_count+1]. Lambda(z)=product(1+alpha^i z). Canonicalization: ascending powers; constant 1.
- `error_positions` — JSON type: array of integers; shape: [at most designed_t]. bit coordinates i whose Chien root is alpha^(-i). Canonicalization: strictly increasing, unique, 0<=i<n.
- `corrected_codeword` — JSON type: array of integers; shape: [n]. received with exactly error_positions toggled. Canonicalization: binary entries, ascending coefficient/position order.
- `generator_quotient` — JSON type: array of integers; shape: [n-degree(g)]. binary q with corrected=g*q. Canonicalization: ascending coefficients, no trailing zero.
