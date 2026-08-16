# H4AIF34 — Abstract interpretation by a least interval fixed point

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- An abstract state is null for bottom or a map from every variable to [lower,upper]. Bounds use integers in the finite range plus strings -inf,+inf; arithmetic outside the range rounds outward to infinity.
- Round zero maps every node to bottom. Each next synchronous round injects initial_state at entry and joins every incoming edge image. Include the first repeated snapshot, which certifies a fixed point.
- The submitted fixed point must also equal an independent chaotic-worklist result, include every final edge image, and imply the public safety query.

### Required output fields

- `kleene_rounds` — JSON type: array of node-state maps; shape: [iterations through first repeat]. complete synchronous Kleene sequence. Canonicalization: round order.
- `least_fixpoint` — JSON type: object node->state; shape: [node count]. last repeated synchronous snapshot. Canonicalization: string node IDs increasing.
- `worklist_fixpoint` — JSON type: object node->state; shape: [node count]. independent chaotic-worklist result. Canonicalization: same representation.
- `edge_images` — JSON type: array of objects; shape: [edge count]. each final transfer image. Canonicalization: input edge order.
- `safety_certificate` — JSON type: object; shape: scalar. node,variable,abstract_interval,required_upper_bound,proved. Canonicalization: must derive from least_fixpoint and public query.
