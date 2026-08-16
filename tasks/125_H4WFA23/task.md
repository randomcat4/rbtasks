# H4WFA23 — Weighted-automata equivalence by invariant reachable space

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- An automaton value on word w is alpha^T M_w beta. Build block D_a=diag(M_A,a,M_B,a), start s=(alpha_A,-alpha_B), and output o=(beta_A,beta_B).
- reachable_difference_basis is the unique nonzero-row RREF basis of the least row space containing s and closed under v -> D_a^T v for symbols in input alphabet order.
- For each symbol, transition_closure_coordinates gives one coordinate row per basis row, satisfying coordinates*B=D_a^T basis_row. output_pairings[i]=basis_row_i dot o and must all be zero.

### Required output fields

- `reachable_difference_basis` — JSON type: rational matrix; shape: [r][dA+dB]. canonical RREF basis of least transition-closed difference space. Canonicalization: nonzero RREF rows in pivot order.
- `transition_closure_coordinates` — JSON type: object mapping each alphabet symbol to rational matrix; shape: each symbol -> [r][r]. row i gives coordinates of D_symbol^T*basis_i. Canonicalization: keys exactly input alphabet; basis order.
- `output_pairings` — JSON type: array of rationals; shape: [r]. basis_i dot (beta_A,beta_B). Canonicalization: basis order; every entry zero.
- `reachable_rank` — JSON type: integer; shape: scalar. number r of basis rows. Canonicalization: must equal matrix row count.
