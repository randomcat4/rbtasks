# LCSP-02 — Vertex and one-hot graph colouring equivalence

Submit one UTF-8 Lean file with the following exact public declaration.

```lean

open CSP.L2S CSP.L2S.PB
namespace RouteBenchSubmission.LCSP02

theorem result (vertices colors : ℕ) (hcolors : 0 < colors)
    (edges : List (Fin vertices × Fin vertices)) :
    piEquivalent
      (graph_coloring_vertex vertices colors edges)
      (graph_coloring_matrix vertices colors edges)
      (@π vertices colors)

end RouteBenchSubmission.LCSP02
```
