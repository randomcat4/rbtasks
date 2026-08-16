# E3POL46 — 低次数多项式由足够多的根值唯一确定

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3POL46.result`：

```lean
theorem result {R : Type*} [CommRing R] [IsDomain R] {n : ℕ} (a b : R[X])
    (ha : degree a < n) (hb : degree b < n)
    (hc : Multiset.card (roots (a - b)) = n) : a = b := by
  ...
```

隐藏 source judge 会重新绑定上述完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque 声明、FATE-M 源模块、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
