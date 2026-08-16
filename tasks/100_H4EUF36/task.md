# H4EUF36 — EUF congruence closure with a minimal UNSAT explanation

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- Terms form a ground DAG in input order. Assumption equalities merge first in assertion order; then repeatedly merge the lexicographically first unequal same-symbol term pair whose corresponding arguments are equivalent.
- Each merge record is either an assumption with its source ID or a congruence with ordered argument pairs. Representatives are the lexicographically smallest term IDs in each final class.
- The core is the smallest-cardinality, then lexicographically first equality-ID subset that violates a disequality. Removing each core equality must separate the recorded conflict terms.

### Required output fields

- `class_representatives` — JSON type: object term_id->term_id; shape: [term count]. lexicographically smallest member of each full closure class. Canonicalization: keys term ID order.
- `merge_proof_forest` — JSON type: array of merge objects; shape: [successful full merges]. assumption/congruence explanations. Canonicalization: canonical merge order.
- `conflicting_disequality` — JSON type: string; shape: scalar. canonical violated disequality ID. Canonicalization: smallest violated ID.
- `conflict_terms` — JSON type: array of strings; shape: [2]. endpoints of conflicting disequality. Canonicalization: left then right.
- `minimal_unsat_core_equalities` — JSON type: array of strings; shape: [core size]. canonical equality subset causing conflict. Canonicalization: input ID order.
- `core_merge_proof_forest` — JSON type: array of merge objects; shape: [successful core merges]. closure proof using only core assumptions. Canonicalization: canonical merge order.
- `deletion_separations` — JSON type: array of objects; shape: [core size]. representatives after deleting each core equality and conflict_removed flag. Canonicalization: core equality order.
