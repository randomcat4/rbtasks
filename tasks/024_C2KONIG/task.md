# C2KONIG — Königsberg graph parity obstruction

The exact target below names a frozen compile-time fixture. Its proof-bearing
implementation is not part of the common package.
Submit one UTF-8 Lean file with the following exact public declaration.

```lean
import RouteBenchFixtures.C2KONIG

open RouteBenchFixtures.C2KONIG
open RouteBenchFixtures.C2KONIG.Verts
namespace RouteBenchSubmission.C2KONIG

theorem result {u v : Verts} (p : graph.Walk u v) (h : p.IsEulerian) : False

end RouteBenchSubmission.C2KONIG
```
