# H4HPI07 — Half-plane intersection with Farkas redundancy certificates

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Constraint index means zero-based position in input.constraints; every inequality is a*x+b*y<=c.
- Vertices are feasible pairwise line intersections, reduced to the strict CCW convex hull beginning at minimum (x,y); each vertex lists every tight input constraint in increasing order.
- Active constraints are the sorted union of vertex-tight indices. For each inactive t in increasing order, choose first a single parallel active constraint with identical normal and no larger bound, otherwise the lexicographically first active pair whose nonnegative combination reproduces t normal and has weighted bound <=c_t.

### Required output fields

- `vertices_ccw` — JSON type: array of objects; shape: [polygon vertex count]. each {point:[x,y], active_constraints:[indices]}. Canonicalization: strict CCW from minimum point; active indices increasing.
- `active_constraints` — JSON type: array of integers; shape: [number active]. union of all tight input-constraint indices. Canonicalization: strictly increasing.
- `redundancy_certificates` — JSON type: array of objects; shape: [number inactive]. each {constraint:t, combination:[{constraint:i,multiplier:lambda}]} satisfying the conic identity. Canonicalization: inactive t increasing; deterministic single/pair choice in task rules.
- `doubled_area` — JSON type: rational scalar; shape: scalar. positive shoelace doubled area of the intersection polygon. Canonicalization: exact positive value.
