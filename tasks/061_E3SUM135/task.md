# E3SUM135 — 前 n 个立方和的精确四次多项式公式

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3SUM135.result`：

```lean
theorem result (n : ℕ) :
    ((∑ i ∈ Finset.range (n + 1), i ^ 3) : ℚ) =
    ((n : ℚ) ^ 4 / 4) + ((n : ℚ) ^ 3 / 2) + ((n : ℚ) ^ 2 / 4) := by
  ...
```

隐藏 source judge 会重新绑定上述完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque 声明、FATE-M 源模块、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
