# E3GRP02 — 有限群的两个正规互补子群给出直积分解

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3GRP02.result`：

```lean
theorem result {G : Type*} [Group G] [Fintype G] (H K : Subgroup G)
    [H.Normal] [K.Normal] (h : Disjoint H K)
    (hcard : Nat.card G = Nat.card H * Nat.card K) : Nonempty (G ≃* H × K) := by
  ...
```

隐藏 source judge 会重新绑定完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque、源定理标识符、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
