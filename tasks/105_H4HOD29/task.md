# H4HOD29 — Six-dimensional Hodge star with exact wedge pairing

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- A form map key i,j,k means coefficient of e^i wedge e^j wedge e^k, with 0<=i<j<k<6. Orientation e^0 wedge ... wedge e^5 is positive.
- For diagonal metric g, let rho=sqrt(product_i g_i). For ordered I and increasing complement J, star(e^I)=sign(I concatenated J)*rho/(product_(i in I)g_i)*e^J.
- Maps contain exactly the nonzero coefficients in increasing key order. alpha_wedge_star_scalar is the coefficient of the positive volume form in alpha wedge star(alpha). The second star satisfies star(star(alpha))=(-1)^(degree*(dimension-degree))*alpha.

### Required output fields

- `star_alpha` — JSON type: object from index triples to rationals; shape: nonzero complement triples. coefficients of Hodge star(alpha). Canonicalization: keys increasing i,j,k; exactly nonzero terms.
- `alpha_wedge_star_scalar` — JSON type: rational scalar; shape: scalar. positive-volume coefficient of alpha wedge star(alpha). Canonicalization: exact reduced rational.
- `star_star_alpha` — JSON type: object from index triples to rationals; shape: same support as alpha. coefficients of star(star(alpha)). Canonicalization: keys increasing; equals star_square_sign times alpha.
- `star_square_sign` — JSON type: integer; shape: scalar. sign in star^2=(-1)^(k(n-k)). Canonicalization: evaluate (-1)^(degree*(dimension-degree)) from the public input.
