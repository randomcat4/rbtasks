# H4TRS32 — Terminating rewrite system with complete critical-pair joins

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- A rewrite step chooses a rule and a zero-based substring position. The termination measure is lexicographic (word length, inversion count under alphabet_order).
- Enumerate every nonempty proper suffix/prefix overlap of ordered rule pairs. Each critical record contains the two one-step branches and complete leftmost-position/lowest-rule join traces.
- The independent normal form reference for test words is the alphabet-sorted word with duplicates removed.

### Required output fields

- `termination_certificate` — JSON type: array of objects; shape: [rule count]. rule_id,length_drop,inversion_drop. Canonicalization: rule order.
- `critical_pairs` — JSON type: array of objects; shape: [all proper overlaps]. ordered-rule overlap, branches, join traces and common normal form. Canonicalization: left_rule,right_rule,overlap_length,word order.
- `test_normalizations` — JSON type: array of objects; shape: [test word count]. deterministic rewrite trace and independent sorted-unique reference. Canonicalization: input test order.
- `critical_pair_count` — JSON type: integer; shape: scalar. number of critical-pair records. Canonicalization: equals list length.
