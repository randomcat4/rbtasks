# C03HERON — Heron's formula

Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import Mathlib

open Real EuclideanGeometry
open scoped Real EuclideanGeometry
namespace RouteBenchSubmission.C03HERON

local notation "√" => Real.sqrt
variable {V : Type*} {P : Type*} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]

theorem result {p₁ p₂ p₃ : P} (h1 : p₁ ≠ p₂) (h2 : p₃ ≠ p₂) :
    let a := dist p₁ p₂
    let b := dist p₃ p₂
    let c := dist p₁ p₃
    let s := (a + b + c) / 2
    1 / 2 * a * b * sin (∠ p₁ p₂ p₃) =
      √ (s * (s - a) * (s - b) * (s - c))

end RouteBenchSubmission.C03HERON
```
