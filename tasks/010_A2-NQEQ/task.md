# A2-NQEQ — N-Queens representation equivalence

Submit one UTF-8 Lean file with the following exact public declaration. The
frozen judge compiles it in the LeanCSP environment and rejects new axioms,
`sorry`, `admit`, and unsafe declarations.

```lean

open CSP.L2S CSP.L2S.PB
namespace RouteBenchSubmission.A2NQEq

theorem result {n : Nat} (hn : 0 < n) :
    piEquivalent (nqueens_csp1D n) (nqueens_csp2D n) π

end RouteBenchSubmission.A2NQEq
```
