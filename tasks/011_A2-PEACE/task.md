# A2-PEACE — Peaceable armies unsatisfiability

Submit one UTF-8 Lean file with the following exact public declaration. The
frozen LeanCSP environment supplies the model and certificate-checking API.

```lean

open CSP.L2S CSP.L2S.PB
open CSP.L2S.PB.PeaceableArmies
namespace RouteBenchSubmission.A2Peace

theorem result : Not peaceableArmies.isSatisfiableInt

end RouteBenchSubmission.A2Peace
```
