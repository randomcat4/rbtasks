# d3iso02 — WL 细化非同构证书：同度序列图对

## Frozen task

Use the exact instance in `input.json`. Solve the following objective:
WL 细化非同构证书：同度序列图对. Return one UTF-8 `submission.json` whose structure matches
`submission.schema.json`. The schema reveals field names and shapes, not the
answer values.

## Submission contract

All identifiers must refer to the frozen input. Integers and finite objects are
checked exactly; undeclared tolerance or heuristic acceptance is not allowed.
The independent certificate verifier and an algorithmically distinct independent cross-check
must both accept. Their implementations, controls, expected values, and logs
are not in the actor package.
