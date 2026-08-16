# H4SSS33 — Shamir reconstruction with a coalition-privacy polynomial witness

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- All arithmetic is in GF(prime), represented by integers 0,...,prime-1. Polynomial coefficients are ascending.
- Each reconstruction subset uses the listed share order; Lagrange coefficients are evaluated at zero and a Vandermonde solve independently recovers the degree-bounded polynomial.
- For the privacy coalition, a nonzero multiple of the monic polynomial vanishing on coalition x-coordinates transforms one degree-bounded polynomial into another with identical coalition evaluations and a distinct constant term.

### Required output fields

- `reconstructed_polynomial_ascending` — JSON type: array of integers; shape: [threshold]. degree-bounded polynomial from Vandermonde reconstruction. Canonicalization: GF residues, ascending.
- `reconstruction_certificates` — JSON type: array of objects; shape: [subset count]. share IDs, Lagrange-at-zero coefficients and reconstructed secret. Canonicalization: input subset order.
- `reconstructed_secret` — JSON type: integer; shape: scalar. constant coefficient recovered independently by every subset. Canonicalization: GF residue.
- `all_share_residuals` — JSON type: array of objects; shape: [share count]. evaluation minus public share value modulo prime. Canonicalization: input share order.
- `privacy_vanishing_polynomial_ascending` — JSON type: array of integers; shape: [coalition size+1]. monic product of x minus coalition coordinates. Canonicalization: ascending.
- `privacy_polynomials_ascending` — JSON type: array of polynomial arrays; shape: [2][threshold]. two degree-bounded polynomials with identical coalition observations. Canonicalization: base then affine shift.
- `privacy_secrets` — JSON type: array of integers; shape: [2]. constant terms of privacy polynomials. Canonicalization: same order as polynomials.
- `privacy_coalition_evaluations` — JSON type: array of arrays; shape: [2][coalition size]. evaluations of both polynomials on coalition x-values. Canonicalization: coalition order.
- `privacy_difference_multiple` — JSON type: integer; shape: scalar. nonzero gamma with f1-f0=gamma*q. Canonicalization: canonical GF residue.
