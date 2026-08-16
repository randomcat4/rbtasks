# LCSP-22 — Langford L(2,2) is unsatisfiable

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S CSP.L2S.PB
namespace RouteBenchSubmission.LCSP22

theorem result : ¬ (langford_2n_csp 2).isSatisfiableInt

end RouteBenchSubmission.LCSP22
```
