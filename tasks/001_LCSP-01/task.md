# LCSP-01 — Schur reversal is not a variable symmetry

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S
open Schur
namespace RouteBenchSubmission.LCSP01

theorem result :
    ¬ VariableSymmetry
      (schur_csp_triples 3 3 (schurTriples 3)) Fin.revPerm

end RouteBenchSubmission.LCSP01
```
