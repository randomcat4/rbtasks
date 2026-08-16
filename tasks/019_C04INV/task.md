# C04INV — Left and right inverses coincide

Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import Mathlib
namespace RouteBenchSubmission.C04INV

theorem result {R : Type*} [Ring R] {x y z : R} (hx : x ≠ 0)
    (hy : x * y = 1) (hz : z * x = 1) : y = z

end RouteBenchSubmission.C04INV
```
