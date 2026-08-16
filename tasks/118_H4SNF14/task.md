# H4SNF14 — Smith normal form with determinantal-divisor audit

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- For n=rows(matrix), U,D,V are n by n integer matrices, det(U),det(V) in {+1,-1}, and U*matrix*V=D.
- D is diagonal; nonzero diagonal entries are positive, precede zeros, and each divides the next nonzero entry.
- determinantal_divisors[k-1] is the nonnegative gcd of absolute values of all k by k minors of the input, for k=1,...,rank(D), in increasing k.

### Required output fields

- `U` — JSON type: integer matrix; shape: [n][n]. left unimodular transform. Canonicalization: determinant +/-1.
- `D` — JSON type: integer matrix; shape: [n][n]. canonical Smith diagonal in U*A*V=D. Canonicalization: positive divisibility chain then zeros.
- `V` — JSON type: integer matrix; shape: [n][n]. right unimodular transform. Canonicalization: determinant +/-1.
- `determinantal_divisors` — JSON type: array of integers; shape: [rank(D)]. gcds of all k-minors for increasing k. Canonicalization: nonnegative, k=1,...,rank.
