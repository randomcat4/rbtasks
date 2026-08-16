# C2BUFFON — Buffon's needle probability

The exact target below names a frozen compile-time fixture. Its proof-bearing
implementation is not part of the common package.
Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import RouteBenchFixtures.C2BUFFON

open MeasureTheory (MeasureSpace IsProbabilityMeasure Measure pdf.IsUniform)
open ProbabilityTheory Real
open RouteBenchFixtures.C2BUFFON
namespace RouteBenchSubmission.C2BUFFON

theorem result
    {Ω : Type*} [MeasureSpace Ω]
    (d l : ℝ) (hd : 0 < d) (hl : 0 < l)
    (B : Ω → ℝ × ℝ) (hBₘ : Measurable B)
    (hB : pdf.IsUniform B ((Set.Icc (-d / 2) (d / 2)) ×ˢ (Set.Icc 0 π)) ℙ)
    (h : l ≤ d) : ℙ[RouteBenchFixtures.C2BUFFON.N l B] = (2 * l) * (d * π)⁻¹

end RouteBenchSubmission.C2BUFFON
```
