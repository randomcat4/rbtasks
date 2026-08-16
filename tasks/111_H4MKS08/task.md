# H4MKS08 — Minkowski sum with vertex-decomposition witnesses

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Canonicalize P and Q independently to strict CCW convex hulls with collinear interior points removed, beginning at minimum (x,y). Canonical summand indices refer to these hull arrays, not original input positions.
- Form every canonical vertex sum. The output is the strict CCW hull of these sums beginning at minimum (x,y).
- For each output vertex choose the lexicographically smallest pair (p_vertex,q_vertex) that sums to it. Doubled area is the positive shoelace value.

### Required output fields

- `vertices_ccw` — JSON type: array of objects; shape: [sum hull vertex count]. each {point:[x,y], p_vertex:i, q_vertex:j} with P[i]+Q[j]=point. Canonicalization: CCW from minimum point; lexicographically least witness pair.
- `doubled_area` — JSON type: rational scalar; shape: scalar. positive shoelace doubled area. Canonicalization: exact positive value.
- `vertex_count` — JSON type: integer; shape: scalar. number of vertices_ccw entries. Canonicalization: must equal array length.
