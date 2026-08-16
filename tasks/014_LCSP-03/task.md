# LCSP-03 — N-Queens representation equivalence

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S CSP.L2S.PB
namespace RouteBenchSubmission.LCSP03

theorem result {n : ℕ} (hn : 0 < n) :
    piEquivalent (nqueens_csp1D n) (nqueens_csp2D n) π

end RouteBenchSubmission.LCSP03
```
