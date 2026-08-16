# H4GBR15 — Groebner basis with ideal-membership transport

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- A sparse term is {m:[e_x,e_y,e_z,e_w], c:rational}; exponents are nonnegative, duplicate monomials are forbidden, and canonical term order is descending lex with x>y>z>w.
- groebner_basis is an ordered polynomial list. basis_in_generators[i][j] is a coefficient polynomial q_(i,j) such that basis_i=sum_j q_(i,j)*input_generator_j. target_in_generators[j] similarly represents the target.
- leading_monomials[i] is the lex-leading exponent of basis_i. Every pair S-polynomial must reduce to zero by ordered first-applicable division by the submitted basis, and the target normal form must be zero.

### Required output fields

- `groebner_basis` — JSON type: array of sparse polynomials; shape: [basis size]. a lex Groebner basis for the input ideal. Canonicalization: polynomial terms descending lex.
- `basis_in_generators` — JSON type: 2D array of sparse polynomials; shape: [basis size][input generator count]. coefficient polynomials representing every basis element. Canonicalization: row i corresponds to basis i.
- `target_in_generators` — JSON type: array of sparse polynomials; shape: [input generator count]. coefficient polynomials representing target. Canonicalization: input-generator order.
- `leading_monomials` — JSON type: array of integer arrays; shape: [basis size][variable count]. leading exponent vector of each basis polynomial. Canonicalization: basis order; nonnegative exponents.
