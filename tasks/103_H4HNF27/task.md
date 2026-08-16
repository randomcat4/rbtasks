# H4HNF27 — Hermite form with lattice membership and modular nonmembership

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let A=basis_matrix and n=rows(A). U,H are n by n integer matrices with det(U)=+1 or -1 and U*A=H.
- H is upper triangular, H[i,i]>0, and for every i<j, 0<=H[i,j]<H[j,j].
- member_coefficients z is an integer vector with A*z=member_query. For modulus p>1, separator w is nonzero modulo p and w^T A=0 modulo p; residues are least nonnegative values w dot query mod p and must differ.

### Required output fields

- `unimodular_U` — JSON type: integer matrix; shape: [n][n]. U in U*A=H. Canonicalization: determinant +/-1.
- `hermite_H` — JSON type: integer matrix; shape: [n][n]. upper Hermite matrix under task convention. Canonicalization: positive diagonal and reduced upper entries.
- `lattice_index` — JSON type: integer; shape: scalar. absolute determinant of A. Canonicalization: positive exact integer.
- `member_coefficients` — JSON type: array of integers; shape: [n]. z with A*z=member_query. Canonicalization: input basis-column order.
- `separator_modulus` — JSON type: integer; shape: scalar. modulus p for separating homomorphism. Canonicalization: p>1.
- `separator_vector` — JSON type: array of integers; shape: [n]. w with w^T A=0 mod p and w nonzero mod p. Canonicalization: input coordinate order.
- `member_residue` — JSON type: integer; shape: scalar. least nonnegative w dot member_query mod p. Canonicalization: 0<=value<p.
- `nonmember_residue` — JSON type: integer; shape: scalar. least nonnegative w dot nonmember_query mod p. Canonicalization: 0<=value<p and differs from member_residue.
