# E3S2S08 — 两平方和的素因子赋值奇偶判别

## 提交契约

提交一个 UTF-8 Lean 文件，只允许 `import Mathlib`，并声明 `RouteBenchSubmission.E3S2S08.result`：

```lean
theorem result {n : ℕ} :
    (∃ x y : ℕ, n = x ^ 2 + y ^ 2) ↔
      ∀ q ∈ n.primeFactors, q % 4 = 3 → Even (padicValNat q n) := by
  ...
```

隐藏 source judge 会重新绑定完整类型、编译提交并审计最终公理集。禁止 `sorry`、`admit`、`unsafe`、自设公理/opaque、源定理标识符、`Lean.ofReduceBool` 与 `Lean.trustCompiler`。最终公理只允许 `propext`、`Classical.choice`、`Quot.sound`。
