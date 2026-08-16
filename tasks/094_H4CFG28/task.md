# H4CFG28 — CFG parse counting with a canonical parse tree

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- Spans are zero-based half-open [i,j). Let count(A,i,j) be the number of ordered parse trees: terminal rules initialize length-one spans and binary rules sum count(B,i,k)*count(C,k,j) over increasing split k and input binary-rule order.
- cyk_nonzero_entries contains all and only positive cells, sorted by (i,j,nonterminal); no zero cells are emitted.
- A leaf tree has exactly nonterminal, span, terminal. An internal tree has exactly nonterminal, span, split, left, right. Canonical choice minimizes (split,left_nonterminal,right_nonterminal,canonical left JSON,canonical right JSON), recursively; JSON comparison uses lexicographic serialization with object keys sorted.

### Required output fields

- `cyk_nonzero_entries` — JSON type: array of objects; shape: [all positive CYK cells]. each {i:int,j:int,nonterminal:string,count:int}. Canonicalization: sorted by i,j,nonterminal; spans half-open; count>0.
- `parse_count` — JSON type: integer; shape: scalar. count(start,0,word length). Canonicalization: exact nonnegative integer.
- `canonical_parse_tree` — JSON type: recursive object; shape: one complete tree. leaf/internal schema and tie-break from task rules. Canonicalization: canonical recursive minimum.
- `topdown_parse_count` — JSON type: integer; shape: scalar. same count from memoized top-down recurrence. Canonicalization: must equal parse_count.
