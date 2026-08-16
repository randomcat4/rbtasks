# H4RES16 — Resultant determinant with a Bezout elimination witness

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Input and output univariate polynomials use ascending coefficients. If deg(f)=m and deg(g)=n, the Sylvester matrix has n shifted rows of descending f coefficients followed by m shifted rows of descending g coefficients.
- resultant and sylvester_determinant are the same exact rational integer det(Sylvester(f,g)).
- Bezout lists a,b satisfy a(x)f(x)+b(x)g(x)=resultant as an exact coefficient identity; trailing zeros are omitted.

### Required output fields

- `resultant` — JSON type: rational scalar; shape: scalar. determinant of the stated Sylvester matrix. Canonicalization: exact value.
- `bezout_a_ascending` — JSON type: array of rationals; shape: [variable]. a coefficients in a*f+b*g=resultant. Canonicalization: ascending, trailing zeros omitted.
- `bezout_b_ascending` — JSON type: array of rationals; shape: [variable]. b coefficients in a*f+b*g=resultant. Canonicalization: ascending, trailing zeros omitted.
- `sylvester_determinant` — JSON type: rational scalar; shape: scalar. independently named determinant of Sylvester(f,g). Canonicalization: must equal resultant.
