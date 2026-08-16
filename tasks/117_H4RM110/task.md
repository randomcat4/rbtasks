# H4RM110 — Nearest first-order Reed–Muller word by Walsh spectrum

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Coordinates x and masks a are integers 0..2^m-1; parity(a & x) is the GF(2) dot product of their m low-to-high bits.
- W[a]=sum_x (-1)^(received[x]+parity(a&x)), listed by increasing a. Choose a maximizing |W[a]|, breaking ties by smallest a; choose b=0 for W[a]>=0 and b=1 otherwise.
- The affine codeword is parity(a&x) XOR b in increasing x order, and distance=(2^m-|W[a]|)/2.

### Required output fields

- `walsh_spectrum` — JSON type: array of integers; shape: [2^m]. W[a] under the stated parity convention. Canonicalization: increasing mask a.
- `affine_linear_mask` — JSON type: integer; shape: scalar. tie-broken maximizer of |W[a]|. Canonicalization: smallest maximizing mask.
- `affine_constant` — JSON type: integer; shape: scalar. 0 if selected W is nonnegative, else 1. Canonicalization: must be 0 or 1.
- `nearest_codeword` — JSON type: array of integers; shape: [2^m]. parity(mask & x) XOR constant. Canonicalization: increasing x, binary entries.
- `hamming_distance` — JSON type: integer; shape: scalar. distance from received, also (2^m-|W|)/2. Canonicalization: exact nonnegative integer.
