# E3COM92 — 多项式整除对线性组合封闭

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3COM92.result`：

```lean
theorem result {R : Type*} [CommRing R] (p f g : R[X]) (pdvd : p ∣ f ∧ p ∣ g) :
    ∀ u v : R[X], p ∣ f * u + g * v := by
  ...
```

隐藏 source judge 会重新绑定上述完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque 声明、FATE-M 源模块、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
