# LCSP-04 — Mutilated-board representation equivalence

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S Bench
open CSP.L2S.MutilatedOrient
namespace RouteBenchSubmission.LCSP04

theorem result (k : ℕ) (hk : 2 ≤ k) :
    piEquivalent (gen_mutilated k) (gen_orient k) (piMap k)

end RouteBenchSubmission.LCSP04
```
