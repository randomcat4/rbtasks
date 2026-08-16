# H4HNK04 — Minimal realization from Markov parameters and Hankel rank

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Let h_k=C A^k B, using the scalar entry because B has one column and C one row.
- The recurrence is the shortest monic list [c_0,...,c_(d-1),1] such that h_(k+d)+sum_(j=0)^(d-1)c_j h_(k+j)=0 for every available k; try d=1,2,... in order.
- The s by s Hankel matrix is H[i,j]=h_(i+j). The ordinary generating denominator is 1+c_(d-1)z+...+c_0 z^d; its numerator contains the first d coefficients of denominator times the series.

### Required output fields

- `markov_parameters` — JSON type: array of rationals; shape: [markov_parameter_count]. h_k=C*A^k*B for k increasing from 0. Canonicalization: chronological k order.
- `minimal_recurrence_ascending` — JSON type: array of rationals; shape: [d+1]. shortest monic recurrence coefficients. Canonicalization: ascending shift; final coefficient 1.
- `hankel_rank` — JSON type: integer; shape: scalar. exact rank of H[i,j]=h_(i+j). Canonicalization: exact RREF rank.
- `hankel_rref_pivots` — JSON type: array of integers; shape: [hankel_rank]. zero-based pivot columns of the requested Hankel matrix. Canonicalization: strictly increasing.
- `generating_denominator_ascending` — JSON type: array of rationals; shape: [d+1]. ordinary generating denominator 1+c_(d-1)z+...+c_0z^d. Canonicalization: ascending powers, constant 1.
- `generating_numerator_ascending` — JSON type: array of rationals; shape: [d]. first d convolution coefficients denominator times sum h_k z^k. Canonicalization: ascending powers.
