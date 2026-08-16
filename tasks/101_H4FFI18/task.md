# H4FFI18 — GF(2) factorization with Rabin irreducibility certificates

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- All GF(2) polynomials are ascending bit lists with coefficients 0 or 1, no trailing zero, and monic. Factors are sorted by (degree, coefficient list). Their product must equal the input polynomial.
- For a factor q of degree d, prime_divisors is the increasing list of distinct primes dividing d; frobenius_full is the canonical remainder x^(2^d) mod q; gcd_checks[r-index] is the monic ascending gcd(x^(2^(d/r))-x,q).
- Rabin irreducibility requires frobenius_full=x and every gcd_check=1. Certificate entries align one-to-one with the sorted factors.

### Required output fields

- `irreducible_factors_ascending` — JSON type: array of binary-polynomial arrays; shape: [factor count]. monic irreducible GF(2) factors whose product is input. Canonicalization: sorted by degree then coefficient list.
- `rabin_certificates` — JSON type: array of objects; shape: [factor count]. each {degree,prime_divisors,frobenius_full,gcd_checks}. Canonicalization: aligned with factors; primes increasing, gcd checks aligned.
