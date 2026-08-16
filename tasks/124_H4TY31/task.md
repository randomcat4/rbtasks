# H4TY31 — Hindley–Milner principal typing with a canonical MGU

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic and symbolic comparisons are exact. Extra fields are rejected.

## Complete public contract

- Indices are zero-based. Lists, matrices and traces use the explicit order below.
- Rational scalars, where used, are reduced JSON strings `n` or `n/d` with positive denominator. Integer and symbolic fields use their stated JSON types.
- The submission contains exactly the required top-level and nested fields.

### Task-specific definitions

- Fresh variables are allocated by the preorder Algorithm-W convention stated in input. Primitive quantified variables are instantiated in listed order.
- At a lambda allocate one fresh variable for its parameter; at application infer function then argument, allocate a result variable, and unify function type with argument_type -> result_type; at let, generalize exactly the variables free in the value type but not the environment.
- Unification applies the current substitution, performs occurs checks, decomposes arrows and constructors left-to-right, and records every entered equation.

### Required output fields

- `principal_type` — JSON type: string; shape: scalar. fully substituted top-level type. Canonicalization: raw u-index convention.
- `principal_quantified` — JSON type: array of strings; shape: [free variables of principal type]. variables generalized at top level. Canonicalization: increasing u index.
- `node_types` — JSON type: array of objects; shape: [AST node count]. each {node_id,type} after final substitution. Canonicalization: node_id increasing.
- `let_schemes` — JSON type: array of objects; shape: [let node count]. each let generalization with node_id,name,quantified,type. Canonicalization: in inference order.
- `mgu_substitution` — JSON type: array of objects; shape: [bound fresh variables]. each {variable,type} after transitive closure. Canonicalization: increasing variable index.
- `unification_trace` — JSON type: array of objects; shape: [entered unify equations]. each {left,right} after current substitution. Canonicalization: recursive entry order.
- `ground_specializations` — JSON type: array of objects; shape: [2]. two ground instantiations of the principal quantified variables. Canonicalization: names all_int then all_bool.
