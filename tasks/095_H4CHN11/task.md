# H4CHN11 — Channel degradation with strict data-processing witness

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Rows are input symbols and columns are output symbols. A garbling T has shape columns(W) by columns(V), nonnegative rational entries, every row summing to 1, and W*T=V.
- For rows i<j, TV_W=1/2 sum_y |W[i,y]-W[j,y]| and similarly for V. Select the pair maximizing TV_W-TV_V, breaking ties by smaller i then smaller j.
- Positive sets list, in increasing column order, exactly those columns where row i is strictly larger than row j; the selected witness must have TV_W>TV_V.

### Required output fields

- `garbling_matrix` — JSON type: rational matrix; shape: [columns(W)][columns(V)]. row-stochastic T with W*T=V. Canonicalization: row-major, nonnegative, each row sum 1.
- `witness_row_pair` — JSON type: array of integers; shape: [2]. tie-broken pair [i,j] witnessing strict TV contraction. Canonicalization: i<j, max gap then smallest pair.
- `W_positive_set` — JSON type: array of integers; shape: [variable]. columns y with W[i,y]>W[j,y]. Canonicalization: strictly increasing.
- `V_positive_set` — JSON type: array of integers; shape: [variable]. columns y with V[i,y]>V[j,y]. Canonicalization: strictly increasing.
- `tv_W` — JSON type: rational scalar; shape: scalar. half L1 distance between selected W rows. Canonicalization: exact rational.
- `tv_V` — JSON type: rational scalar; shape: scalar. half L1 distance between selected V rows. Canonicalization: exact rational, strictly smaller than tv_W.
