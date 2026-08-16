# H4PET24 — Petri reachability plus invariant-separated decoy

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Places and transitions use zero-based input order. A transition t is enabled when marking>=pre[t] componentwise and fires to marking-pre[t]+post[t].
- firing_sequence must reach target; firing_counts has one entry per transition and exactly counts the sequence.
- place_invariant y has one integer per place and satisfies y^T(post-pre)=0 for every transition. Report its dot products with initial, target and decoy; initial=target and differs from decoy.

### Required output fields

- `firing_sequence` — JSON type: array of integers; shape: [variable]. enabled transition indices taking initial to target. Canonicalization: chronological, zero-based.
- `firing_counts` — JSON type: array of integers; shape: [transition count]. exact occurrence count of each transition. Canonicalization: input transition order.
- `place_invariant` — JSON type: array of integers; shape: [place count]. y with y^T(post-pre)=0. Canonicalization: input place order.
- `initial_invariant` — JSON type: integer; shape: scalar. y dot initial. Canonicalization: exact integer.
- `target_invariant` — JSON type: integer; shape: scalar. y dot target. Canonicalization: must equal initial_invariant.
- `decoy_invariant` — JSON type: integer; shape: scalar. y dot decoy. Canonicalization: must differ from initial_invariant.
