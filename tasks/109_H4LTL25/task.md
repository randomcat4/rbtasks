# H4LTL25 — LTL response violation by a Büchi-style lasso

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- State identifiers are input integers. prefix starts at initial; prefix[-1]=loop_entry=cycle[0]. Consecutive prefix/cycle states follow input edges, and cycle[-1] has an edge back to cycle[0].
- The finite displayed path is prefix followed by cycle[1:] (do not duplicate the loop entry). It contains no state labelled bad, contains a request with no later grant, and the cycle contains no grant.
- monitor_trace aligns with the displayed path. At each state process grant first (clear pending), then req (set pending); emit exactly clear or pending.

### Required output fields

- `prefix` — JSON type: array of integers; shape: [at least 1]. initial-to-loop-entry path. Canonicalization: starts at input initial, follows edges.
- `cycle` — JSON type: array of integers; shape: [at least 1]. loop-entry path whose last state returns by one edge to first. Canonicalization: cycle[0]=loop_entry.
- `loop_entry` — JSON type: integer; shape: scalar. shared prefix end and cycle start. Canonicalization: prefix[-1]=cycle[0].
- `monitor_trace` — JSON type: array of strings; shape: [len(prefix)+len(cycle)-1]. pending-response monitor along prefix+cycle[1:]. Canonicalization: entries exactly clear or pending.
