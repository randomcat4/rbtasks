# C03AREA — Area of a disc

Submit one UTF-8 Lean file defining the disc and the exact theorem below.

```lean
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.InverseDeriv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral

open Set Real MeasureTheory intervalIntegral
open scoped Real NNReal
namespace RouteBenchSubmission.C03AREA

def disc (r : ℝ) :=
  {p : ℝ × ℝ | p.1 ^ 2 + p.2 ^ 2 < r ^ 2}

theorem result (r : ℝ≥0) :
    volume (disc r) = NNReal.pi * r ^ 2

end RouteBenchSubmission.C03AREA
```
