# C2BALLOT — Ballot probability

The exact target below names a frozen compile-time fixture. Its proof-bearing
implementation is not part of the common package.
Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import RouteBenchFixtures.C2BALLOT

open Set ProbabilityTheory MeasureTheory
open scoped ENNReal
open RouteBenchFixtures.C2BALLOT
namespace RouteBenchSubmission.C2BALLOT

theorem result :
    ∀ q p, q < p →
      uniformOn (countedSequence p q) staysPositive = (p - q) / (p + q)

end RouteBenchSubmission.C2BALLOT
```
