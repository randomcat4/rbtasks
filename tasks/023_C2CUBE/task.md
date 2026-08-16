# C2CUBE — Nonexistence of a finite unequal cube tiling

The exact target below names a frozen compile-time fixture. Its proof-bearing
implementation is not part of the common package.
Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import RouteBenchFixtures.C2CUBE

open Real Set Function Fin
open RouteBenchFixtures.C2CUBE.«82»
open RouteBenchFixtures.C2CUBE.«82».Cube
namespace RouteBenchSubmission.C2CUBE

theorem result :
    ∀ {n : ℕ}, n ≥ 3 →
    ∀ {s : Set (Cube n)}, s.Finite →
    s.Nontrivial → s.PairwiseDisjoint Cube.toSet →
    ⋃ c ∈ s, Cube.toSet c = unitCube.toSet →
    InjOn Cube.w s → False

end RouteBenchSubmission.C2CUBE
```
