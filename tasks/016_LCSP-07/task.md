# LCSP-07 — Sudoku representation equivalence

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S LatinSquare Sudoku
namespace RouteBenchSubmission.LCSP07

theorem result (b : ℕ) (h_b : 0 < b) :
    piEquivalent (sudoku_csp b) (sudoku_matrix b) (@sudoku_π b)

end RouteBenchSubmission.LCSP07
```
