# H4CYC13 — Cyclic code polynomial-to-matrix duality

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- All polynomial and matrix coefficients are canonical integers 0,...,p-1 in GF(p); polynomial lists are ascending. Let g be the input generator and k=n-deg(g).
- check_polynomial is the exact ascending quotient h with g*h=x^n-1. generator_matrix row i is the length-n coefficient vector of x^i g for i=0,...,k-1.
- parity_check_matrix is the canonical RREF nullspace basis of generator_matrix: free columns increasing, one unit free coordinate, pivot coordinates determined by RREF. Its rows are orthogonal to every generator row modulo p.

### Required output fields

- `check_polynomial_ascending` — JSON type: array of integers; shape: [n-degree(g)+1]. quotient (x^n-1)/g in GF(p). Canonicalization: ascending canonical residues.
- `generator_matrix` — JSON type: array of integer arrays; shape: [k][n]. rows are coefficients of x^i g. Canonicalization: i increasing; residues 0..p-1.
- `parity_check_matrix` — JSON type: array of integer arrays; shape: [n-k][n]. canonical RREF nullspace basis of generator_matrix. Canonicalization: free columns increasing; residues 0..p-1.
- `generator_rank` — JSON type: integer; shape: scalar. exact GF(p) rank of generator_matrix. Canonicalization: must equal k.
- `parity_rank` — JSON type: integer; shape: scalar. exact GF(p) rank of parity matrix. Canonicalization: must equal n-k.
