# E3SQ88 — 奇数阶有限群中平方根存在且唯一

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3SQ88.result`：

```lean
theorem result {G : Type u} [Fintype G] [Group G]
    (hg : Odd (Fintype.card G)) : ∀ (x : G), ∃! (y : G), y ^ 2 = x := by
  ...
```

隐藏 source judge 会重新绑定上述完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque 声明、FATE-M 源模块、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
