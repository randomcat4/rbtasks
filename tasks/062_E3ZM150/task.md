# E3ZM150 — 整数循环子群包含等价于反向整除

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3ZM150.result`：

```lean
theorem result (m n : ℤ) :
    (AddSubgroup.zmultiples m : Set ℤ) ≤ AddSubgroup.zmultiples n ↔ n ∣ m := by
  ...
```

隐藏 source judge 会重新绑定上述完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque 声明、FATE-M 源模块、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
