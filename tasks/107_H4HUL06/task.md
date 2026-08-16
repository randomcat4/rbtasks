# H4HUL06 — Convex hull with edge-support and exact area certificates

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- orient(a,b,p)=(b_x-a_x)(p_y-a_y)-(b_y-a_y)(p_x-a_x).
- The hull is strict CCW, removes collinear interior boundary points, and begins at the minimum input point under (x,y,id).
- Each support entry is aligned with one cyclic directed hull edge and reports min_p orient(edge_start,edge_end,p). Doubled area is the positive shoelace sum.

### Required output fields

- `hull_ids_ccw` — JSON type: array of strings; shape: [hull vertex count]. IDs of strict convex-hull vertices. Canonicalization: CCW from minimum (x,y,id).
- `doubled_area` — JSON type: rational scalar; shape: scalar. positive shoelace doubled area. Canonicalization: exact positive value.
- `edge_support` — JSON type: array of objects; shape: [hull vertex count]. each {edge:[start_id,end_id], minimum_oriented_area:rational}. Canonicalization: aligned with cyclic hull edges; edge order equals hull order.
