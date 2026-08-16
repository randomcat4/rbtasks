# LCSP-05 — Exact Schur number S(3)=13

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S CSP.L2S.PB
namespace RouteBenchSubmission.LCSP05

theorem result :
    _root_.Schur.SchurColorable 13 3 ∧
      ¬ _root_.Schur.SchurColorable 14 3

end RouteBenchSubmission.LCSP05
```
