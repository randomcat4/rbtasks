# A2-MUTIL — Mutilated chessboard unsatisfiability

Submit one UTF-8 Lean file with the following exact public declaration. The
frozen LeanCSP environment supplies the model and certificate-checking API.

```lean

open CSP.L2S CSP.L2S.PB
open CSP.L2S.PB.MutilatedChessboard
namespace RouteBenchSubmission.A2Mutil

theorem result : Not mutilatedChessboard.isSatisfiableInt

end RouteBenchSubmission.A2Mutil
```
