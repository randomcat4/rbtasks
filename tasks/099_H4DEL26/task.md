# H4DEL26 — Delaunay triangulation: empty circles meet lower lifting

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Point order is input order. For each index triple a<b<c, orient it CCW (swap b,c if needed). For q=p, write ax=a_x-q_x, ay=a_y-q_y and similarly b,c; incircle(a,b,c,q)=(ax^2+ay^2)(bx*cy-by*cx)-(bx^2+by^2)(ax*cy-ay*cx)+(cx^2+cy^2)(ax*by-ay*bx). A triple is a Delaunay face exactly when this is <0 for every other input point.
- Each triangle lists the resulting CCW vertex IDs. min_negative_incircle is the maximum (closest to zero) of those strictly negative values. lifted_plane=[A,B,C] satisfies x^2+y^2=A*x+B*y+C at its three vertices; minimum_lifted_slack is the minimum of x^2+y^2-A*x-B*y-C over nonvertices.
- Sort triangles lexicographically by their vertex-ID lists. convex_hull_ccw is the strict monotone-chain hull beginning at minimum (x,y,id). triangle_count is the list length.

### Required output fields

- `triangles` — JSON type: array of objects; shape: [Delaunay face count]. each {vertices:[3 IDs],min_negative_incircle:rational,lifted_plane:[A,B,C],minimum_lifted_slack:rational}. Canonicalization: triangles lexicographic by vertex list; vertices CCW.
- `convex_hull_ccw` — JSON type: array of strings; shape: [hull vertex count]. strict convex-hull IDs. Canonicalization: CCW from minimum (x,y,id).
- `triangle_count` — JSON type: integer; shape: scalar. number of triangle records. Canonicalization: must equal triangles length.
