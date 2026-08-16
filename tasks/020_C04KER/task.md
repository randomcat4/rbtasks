# C04KER — Kernel membership is invariant under swapping two factors

Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import Mathlib
namespace RouteBenchSubmission.C04KER

theorem result {G G' : Type*} [Group G] [Group G'] (f : G →* G') {a b : G} :
    (a * b ∈ f.ker) ↔ (b * a ∈ f.ker)

end RouteBenchSubmission.C04KER
```
