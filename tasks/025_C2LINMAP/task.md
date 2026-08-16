# C2LINMAP — Injectivity versus surjectivity in equal finite dimension

Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import Mathlib
namespace RouteBenchSubmission.C2LINMAP

theorem result
    {K : Type} [Field K] {U V : Type} [AddCommGroup U] [Module K U]
    [AddCommGroup V] [Module K V] [FiniteDimensional K U]
    [FiniteDimensional K V]
    (h : Module.finrank K U = Module.finrank K V) (f : U →ₗ[K] V) :
    Function.Injective f ↔ Function.Surjective f

end RouteBenchSubmission.C2LINMAP
```
