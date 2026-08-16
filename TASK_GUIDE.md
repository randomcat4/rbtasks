# ReturnBench-150 Task Guide

This guide summarizes every public statement, mathematical domain, representation route,
certificate form, structural difficulty and non-answer solution strategy. Administrator
answers, controls, arm assignments and hidden judges are not part of the public release.

## 001. `LCSP-01` — Schur reversal is not a variable symmetry

- Public statement: [tasks/001_LCSP-01/task.md](tasks/001_LCSP-01/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Schur reversal is not a variable symmetry”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：展开 Schur 三元组约束，在反转置换下找出一个保持失败的具体变量关系，再由 Lean 逐项化简反证 VariableSymmetry。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 展开 Schur 三元组约束，在反转置换下找出一个保持失败的具体变量关系，再由 Lean 逐项化简反证 VariableSymmetry。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 002. `LCSP-05` — Exact Schur number S(3)=13

- Public statement: [tasks/002_LCSP-05/task.md](tasks/002_LCSP-05/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact Schur number S(3)=13”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：分别给出 1..13 的三染色可行见证，并把 1..14 的无单色 Schur 三元组编码成不可满足约束，以闭合 S(3)=13 的上下界。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 分别给出 1..13 的三染色可行见证，并把 1..14 的无单色 Schur 三元组编码成不可满足约束，以闭合 S(3)=13 的上下界。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 003. `LCSP-08` — Ramsey R(3,3) upper bound

- Public statement: [tasks/003_LCSP-08/task.md](tasks/003_LCSP-08/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Ramsey R(3,3) upper bound”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：枚举六顶点完全图的红蓝边约束，按一个顶点的三条同色邻边分情况，推出必有同色三角形并形式化上界。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 枚举六顶点完全图的红蓝边约束，按一个顶点的三条同色邻边分情况，推出必有同色三角形并形式化上界。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 004. `LCSP-09` — van der Waerden W(2,3) upper bound

- Public statement: [tasks/004_LCSP-09/task.md](tasks/004_LCSP-09/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“van der Waerden W(2,3) upper bound”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：对九项二染色序列按首项和等差三元组分情况，证明任意染色必含单色三项等差数列。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对九项二染色序列按首项和等差三元组分情况，证明任意染色必含单色三项等差数列。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 005. `LCSP-10` — XOR circuit equivalence

- Public statement: [tasks/005_LCSP-10/task.md](tasks/005_LCSP-10/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 中
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“XOR circuit equivalence”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把两条 XOR 电路归约为 GF(2) 多项式，逐门传播真值并证明所有输入赋值下输出差恒为零。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把两条 XOR 电路归约为 GF(2) 多项式，逐门传播真值并证明所有输入赋值下输出差恒为零。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 006. `LCSP-12` — Four-bit ripple-carry adder equivalence

- Public statement: [tasks/006_LCSP-12/task.md](tasks/006_LCSP-12/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 中
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Four-bit ripple-carry adder equivalence”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：按最低位到最高位展开四位 ripple-carry 的和位与进位递推，再与整数加法的逐位展开对应。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按最低位到最高位展开四位 ripple-carry 的和位与进位递推，再与整数加法的逐位展开对应。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 007. `LCSP-13` — Paley(13) has independence number at most three

- Public statement: [tasks/007_LCSP-13/task.md](tasks/007_LCSP-13/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Paley(13) has independence number at most three”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：直接计算 Paley(13) 的二次剩余邻接，在所有四点子集上证明至少存在一条边，从而排除大小四的独立集。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 直接计算 Paley(13) 的二次剩余邻接，在所有四点子集上证明至少存在一条边，从而排除大小四的独立集。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 008. `LCSP-22` — Langford L(2,2) is unsatisfiable

- Public statement: [tasks/008_LCSP-22/task.md](tasks/008_LCSP-22/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Langford L(2,2) is unsatisfiable”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把 Langford L(2,2) 的位置间距条件写成互异槽位约束，穷尽两个数字的可能首位置并逐支产生冲突。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把 Langford L(2,2) 的位置间距条件写成互异槽位约束，穷尽两个数字的可能首位置并逐支产生冲突。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 009. `A2-MUTIL` — Mutilated chessboard unsatisfiability

- Public statement: [tasks/009_A2-MUTIL/task.md](tasks/009_A2-MUTIL/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Mutilated chessboard unsatisfiability”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：采用棋盘黑白染色不变量：被删两角同色，而每块多米诺覆盖异色各一格，因此覆盖计数不可能平衡。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 采用棋盘黑白染色不变量：被删两角同色，而每块多米诺覆盖异色各一格，因此覆盖计数不可能平衡。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 010. `A2-NQEQ` — N-Queens representation equivalence

- Public statement: [tasks/010_A2-NQEQ/task.md](tasks/010_A2-NQEQ/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“N-Queens representation equivalence”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：在严格禁止新公理、sorry、admit 与 unsafe 声明的 LeanCSP 环境中，构造一维皇后位置与二维 one-hot 棋盘的 π 等价证明。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在严格禁止新公理、sorry、admit 与 unsafe 声明的 LeanCSP 环境中，构造一维皇后位置与二维 one-hot 棋盘的 π 等价证明。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 011. `A2-PEACE` — Peaceable armies unsatisfiability

- Public statement: [tasks/011_A2-PEACE/task.md](tasks/011_A2-PEACE/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Peaceable armies unsatisfiability”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：将双方棋子占位与互不攻击条件编码为有限约束，利用行列/对角覆盖上界形成不可满足证书。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 将双方棋子占位与互不攻击条件编码为有限约束，利用行列/对角覆盖上界形成不可满足证书。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 012. `A2-SEND` — SEND + MORE = MONEY satisfiability

- Public statement: [tasks/012_A2-SEND/task.md](tasks/012_A2-SEND/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“SEND + MORE = MONEY satisfiability”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：按列建立进位变量，从 D+E、N+R、E+O、S+M 四列逐步传播十进制约束，并检查字母数字互异与首位非零。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按列建立进位变量，从 D+E、N+R、E+O、S+M 四列逐步传播十进制约束，并检查字母数字互异与首位非零。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 013. `LCSP-02` — Vertex and one-hot graph colouring equivalence

- Public statement: [tasks/013_LCSP-02/task.md](tasks/013_LCSP-02/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Vertex and one-hot graph colouring equivalence”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把顶点颜色函数转成每顶点恰一真的 one-hot 变量，反向取唯一真色，并证明边异色约束在两表示下等价。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把顶点颜色函数转成每顶点恰一真的 one-hot 变量，反向取唯一真色，并证明边异色约束在两表示下等价。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 014. `LCSP-03` — N-Queens representation equivalence

- Public statement: [tasks/014_LCSP-03/task.md](tasks/014_LCSP-03/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“N-Queens representation equivalence”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：围绕公开的 piEquivalent 声明，把 nqueens_csp1D 与 nqueens_csp2D 经 π 双向对应，验证行列及对角约束在两表示间保持。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 围绕公开的 piEquivalent 声明，把 nqueens_csp1D 与 nqueens_csp2D 经 π 双向对应，验证行列及对角约束在两表示间保持。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 015. `LCSP-04` — Mutilated-board representation equivalence

- Public statement: [tasks/015_LCSP-04/task.md](tasks/015_LCSP-04/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Mutilated-board representation equivalence”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把多米诺配对表示映射为覆盖变量，反向由每格唯一覆盖恢复配对，同时保持删角棋盘的邻接与不重叠条件。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把多米诺配对表示映射为覆盖变量，反向由每格唯一覆盖恢复配对，同时保持删角棋盘的邻接与不重叠条件。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 016. `LCSP-07` — Sudoku representation equivalence

- Public statement: [tasks/016_LCSP-07/task.md](tasks/016_LCSP-07/task.md)
- Mathematical domain: 离散数学 / 组合构造与约束满足
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合构造与约束满足中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Sudoku representation equivalence”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：在九宫格数值表示与 729 个 one-hot 变量间互译，分别核对格、行、列和宫的唯一性约束。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在九宫格数值表示与 729 个 one-hot 变量间互译，分别核对格、行、列和宫的唯一性约束。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 017. `C03AREA` — Area of a disc

- Public statement: [tasks/017_C03AREA/task.md](tasks/017_C03AREA/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 中
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Area of a disc”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把圆面积的几何陈述化为 πr² 的代数目标，依据冻结半径条件重写并由 Lean 完成实数环化简。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把圆面积的几何陈述化为 πr² 的代数目标，依据冻结半径条件重写并由 Lean 完成实数环化简。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 018. `C03HERON` — Heron's formula

- Public statement: [tasks/018_C03HERON/task.md](tasks/018_C03HERON/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 中
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Heron's formula”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：由三边构造半周长，验证三角形不等式使根号项非负，再代入 Heron 公式并精确化简目标面积。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由三边构造半周长，验证三角形不等式使根号项非负，再代入 Heron 公式并精确化简目标面积。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 019. `C04INV` — Left and right inverses coincide

- Public statement: [tasks/019_C04INV/task.md](tasks/019_C04INV/task.md)
- Mathematical domain: 代数学 / 代数结构与线性代数
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 代数结构与线性代数中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Left and right inverses coincide”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：用左逆与右逆等式在结合律下重排：把左逆写成左逆乘恒等，再代入右逆关系得到二者相等。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用左逆与右逆等式在结合律下重排：把左逆写成左逆乘恒等，再代入右逆关系得到二者相等。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 020. `C04KER` — Kernel membership is invariant under swapping two factors

- Public statement: [tasks/020_C04KER/task.md](tasks/020_C04KER/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Kernel membership is invariant under swapping two factors”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把乘积交换后的核成员条件展开，用结合律和已知可交换/逆元关系重排两因子，并在 Lean 中证明双向蕴含。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把乘积交换后的核成员条件展开，用结合律和已知可交换/逆元关系重排两因子，并在 Lean 中证明双向蕴含。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 021. `C2BALLOT` — Ballot probability

- Public statement: [tasks/021_C2BALLOT/task.md](tasks/021_C2BALLOT/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Ballot probability”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把合法计票前缀与不越界格路对应，用反射原理计算坏路径数，再由二项式计数得到精确 ballot 概率。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把合法计票前缀与不越界格路对应，用反射原理计算坏路径数，再由二项式计数得到精确 ballot 概率。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 022. `C2BUFFON` — Buffon's needle probability

- Public statement: [tasks/022_C2BUFFON/task.md](tasks/022_C2BUFFON/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Buffon's needle probability”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：以针中心到最近平行线的距离和角度参数化相交事件，对允许区域积分并除以总体测度得到精确概率。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 以针中心到最近平行线的距离和角度参数化相交事件，对允许区域积分并除以总体测度得到精确概率。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 023. `C2CUBE` — Nonexistence of a finite unequal cube tiling

- Public statement: [tasks/023_C2CUBE/task.md](tasks/023_C2CUBE/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 中高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Nonexistence of a finite unequal cube tiling”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：从有限不等立方体铺砌假设选取最小边长/极端面，比较相邻面分割并用无限下降排除有限铺砌。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从有限不等立方体铺砌假设选取最小边长/极端面，比较相邻面分割并用无限下降排除有限铺砌。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 024. `C2KONIG` — Königsberg graph parity obstruction

- Public statement: [tasks/024_C2KONIG/task.md](tasks/024_C2KONIG/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Königsberg graph parity obstruction”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：计算 Königsberg 图四个顶点的奇度，结合 Euler 路径至多两个奇端点的必要条件得到不可行障碍。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 计算 Königsberg 图四个顶点的奇度，结合 Euler 路径至多两个奇端点的必要条件得到不可行障碍。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 025. `C2LINMAP` — Injectivity versus surjectivity in equal finite dimension

- Public statement: [tasks/025_C2LINMAP/task.md](tasks/025_C2LINMAP/task.md)
- Mathematical domain: 代数学 / 代数结构与线性代数
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 代数结构与线性代数中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Injectivity versus surjectivity in equal finite dimension”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：在等有限维空间中用秩—零度定理把核为零与满秩对应，再由像空间维数等于余域维数推出满射，反向同理。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在等有限维空间中用秩—零度定理把核为零与满秩对应，再由像空间维数等于余域维数推出满射，反向同理。
- Pilot status: PILOT_HOLD_EXISTING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 026. `d3arb01` — Edmonds 最小有向生成树的收缩证书

- Public statement: [tasks/026_d3arb01/task.md](tasks/026_d3arb01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：arborescence、weight）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Edmonds 最小有向生成树的收缩证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 arborescence、weight。本题的算法与验证负担是：为每个非根点选入边，按 Edmonds 算法识别零化后的有向环、收缩求解并展开，返回树与对偶势的等值证书。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 为每个非根点选入边，按 Edmonds 算法识别零化后的有向环、收缩求解并展开，返回树与对偶势的等值证书。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 027. `d3bdd04` — ROBDD：固定变量序下的规范等价证书

- Public statement: [tasks/027_d3bdd04/task.md](tasks/027_d3bdd04/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 中高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：node_count、nodes、roots）→ 独立验收回源结论
- Difficulty basis: 本题对象是“ROBDD：固定变量序下的规范等价证书”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 node_count、nodes、roots。本题的算法与验证负担是：依固定变量序自底向上规约 BDD，合并同构子图并删除等子节点，比较两个根的规范节点编号以判定等价。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 依固定变量序自底向上规约 BDD，合并同构子图并删除等子节点，比较两个根的规范节点编号以判定等价。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 028. `d3blm01` — 一般图最大权匹配的花结构证书

- Public statement: [tasks/028_d3blm01/task.md](tasks/028_d3blm01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：matching、weight）→ 独立验收回源结论
- Difficulty basis: 本题对象是“一般图最大权匹配的花结构证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 matching、weight。本题的算法与验证负担是：运行一般图加权增广路算法，记录 blossom 的基点、收缩与展开；用顶点/花对偶变量核对匹配权重最优。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 运行一般图加权增广路算法，记录 blossom 的基点、收缩与展开；用顶点/花对偶变量核对匹配权重最优。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 029. `d3brg02` — 桥与 2-边连通块分解

- Public statement: [tasks/029_d3brg02/task.md](tasks/029_d3brg02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：bridges、components）→ 独立验收回源结论
- Difficulty basis: 本题对象是“桥与 2-边连通块分解”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 bridges、components。本题的算法与验证负担是：一次 DFS 计算 tin/low，依据 low[child]>tin[parent] 标记桥，删桥后泛洪得到全部 2-边连通块。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 一次 DFS 计算 tin/low，依据 low[child]>tin[parent] 标记桥，删桥后泛洪得到全部 2-边连通块。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 030. `d3cho01` — 弦图 PEO、最大团与最优着色的三合一证书

- Public statement: [tasks/030_d3cho01/task.md](tasks/030_d3cho01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：chromatic_number、color、max_clique、peo）→ 独立验收回源结论
- Difficulty basis: 本题对象是“弦图 PEO、最大团与最优着色的三合一证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 chromatic_number、color、max_clique、peo。本题的算法与验证负担是：用最大基数搜索产生完美消除序，逐点验证后邻居成团，再沿逆序贪心着色并给出同大小最大团。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用最大基数搜索产生完美消除序，逐点验证后邻居成团，再沿逆序贪心着色并给出同大小最大团。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 031. `d3cor02` — 退化度：消除序上界与 k-core 下界相遇

- Public statement: [tasks/031_d3cor02/task.md](tasks/031_d3cor02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：degeneracy、k_core、order）→ 独立验收回源结论
- Difficulty basis: 本题对象是“退化度：消除序上界与 k-core 下界相遇”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 degeneracy、k_core、order。本题的算法与验证负担是：反复删除当前最小度顶点形成退化序并给出上界，同时剥离低度点取得非空 k-core 作为匹配下界。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 反复删除当前最小度顶点形成退化序并给出上界，同时剥离低度点取得非空 k-core 作为匹配下界。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 032. `d3cut01` — Menger 点连通度的上下界相遇证书

- Public statement: [tasks/032_d3cut01/task.md](tasks/032_d3cut01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：connectivity、cut、paths）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Menger 点连通度的上下界相遇证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 connectivity、cut、paths。本题的算法与验证负担是：做顶点拆分后的单位容量最大流得到内部点割；同时分解同值条内部点不交路径，闭合 Menger 上下界。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 做顶点拆分后的单位容量最大流得到内部点割；同时分解同值条内部点不交路径，闭合 Menger 上下界。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 033. `d3dfa03` — DFA 不等价：最短区分词与双状态轨迹

- Public statement: [tasks/033_d3dfa03/task.md](tasks/033_d3dfa03/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 中高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：length、trace_a、trace_b、word）→ 独立验收回源结论
- Difficulty basis: 本题对象是“DFA 不等价：最短区分词与双状态轨迹”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 length、trace_a、trace_b、word。本题的算法与验证负担是：在两 DFA 的乘积图上按词长 BFS，返回首个接受性不同的状态对及逐字符双轨迹，从而证明区分词最短。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在两 DFA 的乘积图上按词长 BFS，返回首个接受性不同的状态对及逐字符双轨迹，从而证明区分词最短。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 034. `d3dom01` — 最小支配集的精确证书

- Public statement: [tasks/034_d3dom01/task.md](tasks/034_d3dom01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：dominating_set、domination_number）→ 独立验收回源结论
- Difficulty basis: 本题对象是“最小支配集的精确证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 dominating_set、domination_number。本题的算法与验证负担是：给出一个支配集并逐顶点列出支配者；再用穷尽分支或下界证书排除所有更小顶点子集。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 给出一个支配集并逐顶点列出支配者；再用穷尽分支或下界证书排除所有更小顶点子集。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 035. `d3grp03` — 有限置换群：Schreier–Sims 稳定子链与群阶

- Public statement: [tasks/035_d3grp03/task.md](tasks/035_d3grp03/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：base、elements、orbit_sizes、order）→ 独立验收回源结论
- Difficulty basis: 本题对象是“有限置换群：Schreier–Sims 稳定子链与群阶”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 base、elements、orbit_sizes、order。本题的算法与验证负担是：从置换生成元构造 Schreier–Sims 稳定子链，逐层返回 transversal 与强生成元，并以各轨道长度乘积复算群阶。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从置换生成元构造 Schreier–Sims 稳定子链，逐层返回 transversal 与强生成元，并以各轨道长度乘积复算群阶。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 036. `d3huf04` — Huffman 编码：规范前缀码与最优加权长度

- Public statement: [tasks/036_d3huf04/task.md](tasks/036_d3huf04/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 中高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：codes、lengths、weighted_length）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Huffman 编码：规范前缀码与最优加权长度”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 codes、lengths、weighted_length。本题的算法与验证负担是：按权重优先队列合并 Huffman 树，导出码长后按码长和符号生成规范前缀码，并用合并代价证明加权长度最优。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按权重优先队列合并 Huffman 树，导出码长后按码长和符号生成规范前缀码，并用合并代价证明加权长度最优。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 037. `d3ilp03` — 集合分割整数规划：最小代价精确覆盖

- Public statement: [tasks/037_d3ilp03/task.md](tasks/037_d3ilp03/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 中高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：chosen_tables、total_cost）→ 独立验收回源结论
- Difficulty basis: 本题对象是“集合分割整数规划：最小代价精确覆盖”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 chosen_tables、total_cost。本题的算法与验证负担是：把集合分割写成 0-1 精确覆盖，返回覆盖每元素一次的列集与总代价，并用对偶权或完整分支界证明无更低解。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把集合分割写成 0-1 精确覆盖，返回覆盖每元素一次的列集与总代价，并用对偶权或完整分支界证明无更低解。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 038. `d3iso02` — WL 细化非同构证书：同度序列图对

- Public statement: [tasks/038_d3iso02/task.md](tasks/038_d3iso02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：rounds、witness_round）→ 独立验收回源结论
- Difficulty basis: 本题对象是“WL 细化非同构证书：同度序列图对”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 rounds、witness_round。本题的算法与验证负担是：对两图同步执行 1-WL 颜色细化，记录每轮颜色直方图，在首个不同轮以颜色计数差证明非同构。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对两图同步执行 1-WL 颜色细化，记录每轮颜色直方图，在首个不同轮以颜色计数差证明非同构。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 039. `d3jsp03` — 柔性作业车间：机器选择、无重叠排程与最优工期

- Public statement: [tasks/039_d3jsp03/task.md](tasks/039_d3jsp03/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 中高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：makespan、operations）→ 独立验收回源结论
- Difficulty basis: 本题对象是“柔性作业车间：机器选择、无重叠排程与最优工期”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 makespan、operations。本题的算法与验证负担是：固定每道工序的机器选择与开始时刻，检查工艺先后和机器区间不重叠，再用临界路径/分支界证明工期最优。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 固定每道工序的机器选择与开始时刻，检查工艺先后和机器区间不重叠，再用临界路径/分支界证明工期最优。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 040. `d3lev03` — Levenshtein 距离：最优对齐证书

- Public statement: [tasks/040_d3lev03/task.md](tasks/040_d3lev03/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 中高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：aligned_source、aligned_target、distance）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Levenshtein 距离：最优对齐证书”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 aligned_source、aligned_target、distance。本题的算法与验证负担是：填充完整 Levenshtein 动态规划表，从右下角回溯一条编辑脚本，并复算每步代价等于最终距离。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 填充完整 Levenshtein 动态规划表，从右下角回溯一条编辑脚本，并复算每步代价等于最终距离。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 041. `d3lpd04` — 有理线性规划：原始—对偶强对偶证书

- Public statement: [tasks/041_d3lpd04/task.md](tasks/041_d3lpd04/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 中高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：dual_objective、dual_y、objective、primal_x）→ 独立验收回源结论
- Difficulty basis: 本题对象是“有理线性规划：原始—对偶强对偶证书”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 dual_objective、dual_y、objective、primal_x。本题的算法与验证负担是：以有理数分别构造线性规划原始可行解和对偶可行解，逐约束复算，并用相等目标值闭合强对偶。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 以有理数分别构造线性规划原始可行解和对偶可行解，逐约束复算，并用相等目标值闭合强对偶。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 042. `d3mat03` — 拟阵交：公共独立集与 Edmonds min–max 见证

- Public statement: [tasks/042_d3mat03/task.md](tasks/042_d3mat03/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：objective、rank_linear_X、rank_partition_complement、selected）→ 独立验收回源结论
- Difficulty basis: 本题对象是“拟阵交：公共独立集与 Edmonds min–max 见证”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 objective、rank_linear_X、rank_partition_complement、selected、witness_X。本题的算法与验证负担是：维护两个拟阵共同独立集，在交换图中寻找增广路；终止时返回分割集合，使两侧秩和等于当前大小。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 维护两个拟阵共同独立集，在交换图中寻找增广路；终止时返回分割集合，使两侧秩和等于当前大小。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 043. `d3mcb02` — 最小循环基：GF(2) 独立性与权重最优

- Public statement: [tasks/043_d3mcb02/task.md](tasks/043_d3mcb02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：cycles、weight）→ 独立验收回源结论
- Difficulty basis: 本题对象是“最小循环基：GF(2) 独立性与权重最优”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 cycles、weight。本题的算法与验证负担是：生成候选简单环并按权重排序，在 GF(2) 边向量上消元选出独立基；以秩与候选顺序证明总权最小。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 生成候选简单环并按权重排序，在 GF(2) 边向量上消元选出独立基；以秩与候选顺序证明总权最小。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 044. `d3mcf01` — 最小费用转运的原始—对偶证书

- Public statement: [tasks/044_d3mcf01/task.md](tasks/044_d3mcf01/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 中高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：cost、flow、potential）→ 独立验收回源结论
- Difficulty basis: 本题对象是“最小费用转运的原始—对偶证书”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 cost、flow、potential。本题的算法与验证负担是：给出满足供需守恒和容量的整数流，同时返回节点势；检查所有剩余弧约化费用非负且原始/对偶目标相等。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 给出满足供需守恒和容量的整数流，同时返回节点势；检查所有剩余弧约化费用非负且原始/对偶目标相等。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 045. `d3mst02` — 最小生成树：树证书与 Prim/Kruskal 双裁决

- Public statement: [tasks/045_d3mst02/task.md](tasks/045_d3mst02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：tree_edges、weight）→ 独立验收回源结论
- Difficulty basis: 本题对象是“最小生成树：树证书与 Prim/Kruskal 双裁决”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 tree_edges、weight。本题的算法与验证负担是：返回一棵连通无环边集，以 Kruskal 和 Prim 两种独立顺序复算权重，并逐非树边检查路径最大边交换条件。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 返回一棵连通无环边集，以 Kruskal 和 Prim 两种独立顺序复算权重，并逐非树边检查路径最大边交换条件。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 046. `d3pln01` — 非平面图的 Kuratowski 细分证书

- Public statement: [tasks/046_d3pln01/task.md](tasks/046_d3pln01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：left、paths、right）→ 独立验收回源结论
- Difficulty basis: 本题对象是“非平面图的 Kuratowski 细分证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 left、paths、right。本题的算法与验证负担是：从原图边路径中重建 K5 或 K3,3 的细分，验证各分支路径内部点不交且只在规定端点相接。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从原图边路径中重建 K5 或 K3,3 的细分，验证各分支路径内部点不交且只在规定端点相接。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 047. `d3rsc03` — Reed–Solomon 擦除恢复：GF(256) 系统码证书

- Public statement: [tasks/047_d3rsc03/task.md](tasks/047_d3rsc03/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 中高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：shards）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Reed–Solomon 擦除恢复：GF(256) 系统码证书”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 shards。本题的算法与验证负担是：在 GF(256) 上从未擦除位置建立 Vandermonde 方程恢复消息，再系统编码全部位置并核对已知符号与擦除填充值。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 GF(256) 上从未擦除位置建立 Vandermonde 方程恢复消息，再系统编码全部位置并核对已知符号与擦除填充值。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 048. `d3scc02` — 强连通分量与凝聚 DAG 证书

- Public statement: [tasks/048_d3scc02/task.md](tasks/048_d3scc02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：components、condensation_edges、topological_order）→ 独立验收回源结论
- Difficulty basis: 本题对象是“强连通分量与凝聚 DAG 证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 components、condensation_edges、topological_order。本题的算法与验证负担是：用 Tarjan/Kosaraju 得到强连通块，为块内互达给出搜索见证，并构造无环且覆盖全部跨块边的凝聚图。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用 Tarjan/Kosaraju 得到强连通块，为块内互达给出搜索见证，并构造无环且覆盖全部跨块边的凝聚图。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 049. `d3smr03` — 稳定婚姻：提议方最优稳定匹配

- Public statement: [tasks/049_d3smr03/task.md](tasks/049_d3smr03/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 中高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：matching、rank_vector）→ 独立验收回源结论
- Difficulty basis: 本题对象是“稳定婚姻：提议方最优稳定匹配”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 matching、rank_vector。本题的算法与验证负担是：执行提议方 Gale–Shapley 队列，记录拒绝过程；枚举阻挡对检查稳定性，并用拒绝引理证明提议方最优。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 执行提议方 Gale–Shapley 队列，记录拒绝过程；枚举阻挡对检查稳定性，并用拒绝引理证明提议方最优。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 050. `d3spt01` — 含负边无负环的最短路树与势函数证书

- Public statement: [tasks/050_d3spt01/task.md](tasks/050_d3spt01/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：distance、parent）→ 独立验收回源结论
- Difficulty basis: 本题对象是“含负边无负环的最短路树与势函数证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 distance、parent。本题的算法与验证负担是：运行 Bellman–Ford 得到距离与前驱树，再返回势函数，使每条约化边权非负并逐点核对树路达到距离。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 运行 Bellman–Ford 得到距离与前驱树，再返回势函数，使每条约化边权非负并逐点核对树路达到距离。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 051. `d3top02` — DAG 拓扑序精确计数：理想子集递推证书

- Public statement: [tasks/051_d3top02/task.md](tasks/051_d3top02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：count、dp）→ 独立验收回源结论
- Difficulty basis: 本题对象是“DAG 拓扑序精确计数：理想子集递推证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 count、dp。本题的算法与验证负担是：对 DAG 的理想子集做位集动态规划，按可加入的极小剩余点递推，返回全部状态计数与最终拓扑序总数。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 DAG 的理想子集做位集动态规划，按可加入的极小剩余点递推，返回全部状态计数与最终拓扑序总数。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 052. `d3trd02` — DAG 传递约简：可达性等价与逐边不可删

- Public statement: [tasks/052_d3trd02/task.md](tasks/052_d3trd02/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 中高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：reduction）→ 独立验收回源结论
- Difficulty basis: 本题对象是“DAG 传递约简：可达性等价与逐边不可删”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 reduction。本题的算法与验证负担是：先算 DAG 可达闭包，只保留不存在替代路径的边；验证约简前后闭包相同，并为每条保留边证明删除会失去可达性。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 先算 DAG 可达闭包，只保留不存在替代路径的边；验证约简前后闭包相同，并为每条保留边证明删除会失去可达性。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 053. `d3xor04` — XOR-SAT：仿射解空间、秩与核基

- Public statement: [tasks/053_d3xor04/task.md](tasks/053_d3xor04/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 中高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：kernel_basis、particular、rank、solution_count）→ 独立验收回源结论
- Difficulty basis: 本题对象是“XOR-SAT：仿射解空间、秩与核基”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 kernel_basis、particular、rank、solution_count。本题的算法与验证负担是：对 XOR 方程组做 GF(2) 高斯消元，返回行阶梯形、特解和核基，并复算秩—零度与全部方程。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 XOR 方程组做 GF(2) 高斯消元，返回行阶梯形、特解和核基，并复算秩—零度与全部方程。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 054. `E3COM92` — 多项式整除对线性组合封闭

- Public statement: [tasks/054_E3COM92/task.md](tasks/054_E3COM92/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“多项式整除对线性组合封闭”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把两个整除见证写成多项式乘积，对线性组合分配乘法并合并系数，显式构造新的整除商。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把两个整除见证写成多项式乘积，对线性组合分配乘法并合并系数，显式构造新的整除商。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 055. `E3CYC58` — 奇长度循环的平方仍是单循环

- Public statement: [tasks/055_E3CYC58/task.md](tasks/055_E3CYC58/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“奇长度循环的平方仍是单循环”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：将奇长度循环编号为模 n 加法，证明乘二在奇数模数上可逆，从而平方置换仍有单一长度 n 的轨道。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 将奇长度循环编号为模 n 加法，证明乘二在奇数模数上可逆，从而平方置换仍有单一长度 n 的轨道。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 056. `E3GRP02` — 有限群的两个正规互补子群给出直积分解

- Public statement: [tasks/056_E3GRP02/task.md](tasks/056_E3GRP02/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“有限群的两个正规互补子群给出直积分解”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：由两个正规互补子群构造乘法映射，利用交集平凡证明交换和单射，再由乘积覆盖证明为直积同构。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由两个正规互补子群构造乘法映射，利用交集平凡证明交换和单射，再由乘积覆盖证明为直积同构。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 057. `E3P43I3` — 任意界以上都存在模 4 为 3 的素数

- Public statement: [tasks/057_E3P43I3/task.md](tasks/057_E3P43I3/task.md)
- Mathematical domain: 数论 / 素数、赋值与整除
- Structural difficulty: 中
- Certificate: 素数构造、赋值奇偶或整除证书
- Representation route: 冻结自然语言/结构化输入 → 素数、赋值与整除中的精确表示 → 素数构造、赋值奇偶或整除证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“任意界以上都存在模 4 为 3 的素数”；需核验的特有证书结构为 素数构造、赋值奇偶或整除证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：假设界以上无 4k+3 素数，构造由已有素数乘积得到的 4m−1，分析其素因子模 4 类产生矛盾。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 假设界以上无 4k+3 素数，构造由已有素数乘积得到的 4m−1，分析其素因子模 4 类产生矛盾。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 058. `E3POL46` — 低次数多项式由足够多的根值唯一确定

- Public statement: [tasks/058_E3POL46/task.md](tasks/058_E3POL46/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“低次数多项式由足够多的根值唯一确定”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：对两低次多项式取差，利用给定点全为根且根数超过次数，应用域上非零多项式根数界推出差为零。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对两低次多项式取差，利用给定点全为根且根数超过次数，应用域上非零多项式根数界推出差为零。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 059. `E3S2S08` — 两平方和的素因子赋值奇偶判别

- Public statement: [tasks/059_E3S2S08/task.md](tasks/059_E3S2S08/task.md)
- Mathematical domain: 数论 / 素数、赋值与整除
- Structural difficulty: 中
- Certificate: 素数构造、赋值奇偶或整除证书
- Representation route: 冻结自然语言/结构化输入 → 素数、赋值与整除中的精确表示 → 素数构造、赋值奇偶或整除证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“两平方和的素因子赋值奇偶判别”；需核验的特有证书结构为 素数构造、赋值奇偶或整除证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：在高斯整数或模 4 分析中分解两平方和，证明 4k+3 素数的赋值必须为偶数，并处理乘积赋值。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在高斯整数或模 4 分析中分解两平方和，证明 4k+3 素数的赋值必须为偶数，并处理乘积赋值。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 060. `E3SQ88` — 奇数阶有限群中平方根存在且唯一

- Public statement: [tasks/060_E3SQ88/task.md](tasks/060_E3SQ88/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“奇数阶有限群中平方根存在且唯一”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：在奇阶有限群中把平方映射的指数二逆元写出，证明该幂同时给出存在性，并由无二阶元证明唯一性。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在奇阶有限群中把平方映射的指数二逆元写出，证明该幂同时给出存在性，并由无二阶元证明唯一性。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 061. `E3SUM135` — 前 n 个立方和的精确四次多项式公式

- Public statement: [tasks/061_E3SUM135/task.md](tasks/061_E3SUM135/task.md)
- Mathematical domain: 离散数学 / 组合恒等式
- Structural difficulty: 中
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合恒等式中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“前 n 个立方和的精确四次多项式公式”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：对 n 做归纳，将新增立方并入候选四次式，通分展开后化简为下一项的平方三角数公式。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 n 做归纳，将新增立方并入候选四次式，通分展开后化简为下一项的平方三角数公式。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 062. `E3ZM150` — 整数循环子群包含等价于反向整除

- Public statement: [tasks/062_E3ZM150/task.md](tasks/062_E3ZM150/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 中
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：题面指定的形式声明或证书对象）→ 独立验收回源结论
- Difficulty basis: 本题对象是“整数循环子群包含等价于反向整除”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 形式声明、定义展开与内核检查。本题的算法与验证负担是：把整数循环子群写成倍数集合；一向用整除传递证明包含，反向把生成元的成员见证读成反向整除。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把整数循环子群写成倍数集合；一向用整除传递证明包含，反向把生成元的成员见证读成反向整除。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 063. `F3BH01` — Benjamini-Hochberg: multiple-testing prose to exact step-up decisions

- Public statement: [tasks/063_F3BH01/task.md](tasks/063_F3BH01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：adjusted、kind、order、raw_sorted）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Benjamini-Hochberg: multiple-testing prose to exact step-up decisions”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 adjusted、kind、order、raw_sorted、rejected_indices。本题的算法与验证负担是：将有理 p 值排序，计算 m/i 倍原值并反向累积最小值，截断到 1 后还原原顺序，再按 α=1/20 选拒绝集合。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 将有理 p 值排序，计算 m/i 倍原值并反向累积最小值，截断到 1 后还原原顺序，再按 α=1/20 选拒绝集合。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 064. `F3BN01` — Bayesian network: conditional tables to an exact posterior

- Public statement: [tasks/064_F3BN01/task.md](tasks/064_F3BN01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：elimination_order、evidence_probability、kind、posterior）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Bayesian network: conditional tables to an exact posterior”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 elimination_order、evidence_probability、kind、posterior、trace。本题的算法与验证负担是：按贝叶斯网络拓扑序联合枚举隐变量，乘条件概率表项，对查询与证据分别求和并用有理数归一化。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按贝叶斯网络拓扑序联合枚举隐变量，乘条件概率表项，对查询与证据分别求和并用有理数归一化。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 065. `F3BS01` — Exact bootstrap: empirical observations to a multinomial resampling law

- Public statement: [tasks/065_F3BS01/task.md](tasks/065_F3BS01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：distribution、kind、tail_probability、total_resamples）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact bootstrap: empirical observations to a multinomial resampling law”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 distribution、kind、tail_probability、total_resamples。本题的算法与验证负担是：把 bootstrap 重采样转成多项分布计数，枚举计数向量及其多项式权重，汇总统计量的精确经验分布。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把 bootstrap 重采样转成多项分布计数，枚举计数向量及其多项式权重，汇总统计量的精确经验分布。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 066. `F3BSP1` — Repeated-knot B-spline: exact value and right derivative

- Public statement: [tasks/066_F3BSP1/task.md](tasks/066_F3BSP1/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 中高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：first_derivative_right、kind、value）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Repeated-knot B-spline: exact value and right derivative”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 first_derivative_right、kind、value。本题的算法与验证负担是：按 Cox–de Boor 递推在重复节点处计算 B-spline 基值，并从右侧区间递推导数，保持全部结果为精确有理数。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按 Cox–de Boor 递推在重复节点处计算 B-spline 基值，并从右侧区间递推导数，保持全部结果为精确有理数。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 067. `F3CHEM` — Redox stoichiometry: species formulas and charge to a primitive integer balance

- Public statement: [tasks/067_F3CHEM/task.md](tasks/067_F3CHEM/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 中
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：balances、coefficients、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Redox stoichiometry: species formulas and charge to a primitive integer balance”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 balances、coefficients、kind。本题的算法与验证负担是：把各物种元素计数与电荷写成整数齐次方程，求一维整数核并除以 gcd，得到符号一致的本原氧化还原配平。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把各物种元素计数与电荷写成整数齐次方程，求一维整数核并除以 gcd，得到符号一致的本原氧化还原配平。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 068. `F3CRC1` — CRC-32 bit order: reflected LFSR versus normal polynomial division

- Public statement: [tasks/068_F3CRC1/task.md](tasks/068_F3CRC1/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 中高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：crc32、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“CRC-32 bit order: reflected LFSR versus normal polynomial division”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 crc32、kind。本题的算法与验证负担是：分别按 reflected LFSR 位序与 normal 多项式长除实现 CRC-32，显式反转位序映射并逐步核对两条余数轨迹。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 分别按 reflected LFSR 位序与 normal 多项式长除实现 CRC-32，显式反转位序映射并逐步核对两条余数轨迹。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 069. `F3CV01` — Boundary convolution: reflect semantics to an exact separable image filter

- Public statement: [tasks/069_F3CV01/task.md](tasks/069_F3CV01/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 中
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：kind、output）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Boundary convolution: reflect semantics to an exact separable image filter”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 kind、output。本题的算法与验证负担是：按 reflect 边界规则逐索引映射像素，先横向再纵向施加可分离核，并与二维卷积逐像素精确核对。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按 reflect 边界规则逐索引映射像素，先横向再纵向施加可分离核，并与二维卷积逐像素精确核对。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 070. `F3DFT1` — Eight-point DFT: Gaussian integers to exact Q(sqrt2,i) bins

- Public statement: [tasks/070_F3DFT1/task.md](tasks/070_F3DFT1/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 中高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：bins、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Eight-point DFT: Gaussian integers to exact Q(sqrt2,i) bins”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 bins、kind。本题的算法与验证负担是：利用八次单位根在 Q(√2,i) 中的精确表示逐 bin 累加，返回实虚系数并用共轭对称性/逆变换复核。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 利用八次单位根在 Q(√2,i) 中的精确表示逐 bin 累加，返回实虚系数并用共轭对称性/逆变换复核。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 071. `F3DIM1` — Buckingham-style dimensional analysis: physical quantities to canonical Pi groups

- Public statement: [tasks/071_F3DIM1/task.md](tasks/071_F3DIM1/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 中
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：groups、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Buckingham-style dimensional analysis: physical quantities to canonical Pi groups”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 groups、kind。本题的算法与验证负担是：以基本量纲指数矩阵求整数/有理核，规范化每个核向量形成无量纲 Pi 群，并复算所有基本维指数为零。 结构等级生成规则为“中：以单一形式声明或较窄证书为主，但仍需内核或精确裁判闭合”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 以基本量纲指数矩阵求整数/有理核，规范化每个核向量形成无量纲 Pi 群，并复算所有基本维指数为零。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 072. `F3FIR1` — Polyphase resampling: upsample-filter-downsample to exact phase-zero output

- Public statement: [tasks/072_F3FIR1/task.md](tasks/072_F3FIR1/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 中高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：kind、output）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Polyphase resampling: upsample-filter-downsample to exact phase-zero output”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 kind、output。本题的算法与验证负担是：把上采样后的零插入与 FIR 相位分组，直接计算被下采样保留的 phase-zero 输出，并与全序列卷积索引对应。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把上采样后的零插入与 FIR 相位分组，直接计算被下采样保留的 phase-zero 输出，并与全序列卷积索引对应。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 073. `F3HG01` — Fisher exact test: fixed margins to an exact two-sided tail

- Public statement: [tasks/073_F3HG01/task.md](tasks/073_F3HG01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：claim、common_denominator、kind、observed_x）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Fisher exact test: fixed margins to an exact two-sided tail”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 claim、common_denominator、kind、observed_x、selected_x、weights。本题的算法与验证负担是：在固定边际下计算超几何表概率，以观测表概率为阈值枚举所有不更可能的表并精确求和。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在固定边际下计算超几何表概率，以观测表概率为阈值枚举所有不更可能的表并精确求和。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 074. `F3HMM1` — Hidden Markov model: observation narrative to exact forward likelihood

- Public statement: [tasks/074_F3HMM1/task.md](tasks/074_F3HMM1/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：forward、kind、likelihood、posterior_final）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Hidden Markov model: observation narrative to exact forward likelihood”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 forward、kind、likelihood、posterior_final。本题的算法与验证负担是：按时间递推每个隐状态的前向有理概率：先乘转移再乘发射，保存全表并在末列求和得到似然。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按时间递推每个隐状态的前向有理概率：先乘转移再乘发射，保存全表并在末列求和得到似然。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 075. `F3KEP1` — Kepler state vector: exact energy, eccentricity and orbital invariants

- Public statement: [tasks/075_F3KEP1/task.md](tasks/075_F3KEP1/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 高
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：angular_momentum、angular_momentum_squared、eccentricity_squared、eccentricity_vector）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Kepler state vector: exact energy, eccentricity and orbital invariants”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 angular_momentum、angular_momentum_squared、eccentricity_squared、eccentricity_vector、kind、semi_major_axis、semilatus_rectum、specific_energy。本题的算法与验证负担是：由位置速度向量精确计算比能量、角动量和 Laplace–Runge–Lenz 向量，交叉核对偏心率及轨道不变量关系。 结构等级生成规则为“高：公开 schema 的多组成证书需要逐字段精确核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由位置速度向量精确计算比能量、角动量和 Laplace–Runge–Lenz 向量，交叉核对偏心率及轨道不变量关系。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 076. `F3KF01` — Kalman filter: linear-Gaussian measurements to an exact rational posterior

- Public statement: [tasks/076_F3KF01/task.md](tasks/076_F3KF01/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 中高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：final_covariance、final_mean、kind、trajectory）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Kalman filter: linear-Gaussian measurements to an exact rational posterior”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 final_covariance、final_mean、kind、trajectory。本题的算法与验证负担是：按有理矩阵完成预测协方差、创新、Kalman 增益和更新，使用 Joseph/直接公式交叉核对后验均值与协方差。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按有理矩阵完成预测协方差、创新、Kalman 增益和更新，使用 Joseph/直接公式交叉核对后验均值与协方差。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 077. `F3KM01` — Kaplan-Meier: censored records to an exact product-limit curve

- Public statement: [tasks/077_F3KM01/task.md](tasks/077_F3KM01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：greenwood_sum、kind、survival、timeline）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Kaplan-Meier: censored records to an exact product-limit curve”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 greenwood_sum、kind、survival、timeline。本题的算法与验证负担是：按事件时间聚合风险集与死亡数，逐时刻乘 (n−d)/n，输出所有跳点的约分生存概率。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按事件时间聚合风险集与死亡数，逐时刻乘 (n−d)/n，输出所有跳点的约分生存概率。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 078. `F3MC01` — Markov temporal event: workflow prose to a product-state automaton

- Public statement: [tasks/078_F3MC01/task.md](tasks/078_F3MC01/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：claim、event_by_final_state、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Markov temporal event: workflow prose to a product-state automaton”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 claim、event_by_final_state、kind。本题的算法与验证负担是：把 Markov 状态与时序事件监控状态做直积，逐步传播精确概率质量，并汇总首次满足事件的接受状态。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把 Markov 状态与时序事件监控状态做直积，逐步传播精确概率质量，并汇总首次满足事件的接受状态。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 079. `F3MSH1` — Closed triangle mesh: oriented faces to exact volume and centroid

- Public statement: [tasks/079_F3MSH1/task.md](tasks/079_F3MSH1/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：centroid、kind、signed_volume）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Closed triangle mesh: oriented faces to exact volume and centroid”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 centroid、kind、signed_volume。本题的算法与验证负担是：按每个定向三角面与原点组成四面体，累加有符号体积和一阶矩，检查闭合边抵消后得到体积与质心。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按每个定向三角面与原点组成四面体，累加有符号体积和一阶矩，检查闭合边抵消后得到体积与质心。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 080. `F3MW01` — Mann-Whitney exact test: samples to a rank-label distribution

- Public statement: [tasks/080_F3MW01/task.md](tasks/080_F3MW01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：counts、kind、p_value、u1）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Mann-Whitney exact test: samples to a rank-label distribution”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 counts、kind、p_value、u1。本题的算法与验证负担是：处理并列秩后枚举固定样本量的标签分配，建立 U 统计量计数分布，并按题定双侧规则累加尾部。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 处理并列秩后枚举固定样本量的标签分配，建立 U 统计量计数分布，并按题定双侧规则累加尾部。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 081. `F3ODE1` — Validated decay ODE: exact Taylor remainder to an outward interval

- Public statement: [tasks/081_F3ODE1/task.md](tasks/081_F3ODE1/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 中高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：kind、lower、terms、upper）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Validated decay ODE: exact Taylor remainder to an outward interval”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 kind、lower、terms、upper。本题的算法与验证负担是：围绕衰减 ODE 在步长区间展开精确 Taylor 多项式，用下一阶导数上界给出向外舍入余项区间并验证包含真解。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 围绕衰减 ODE 在步长区间展开精确 Taylor 多项式，用下一阶导数上界给出向外舍入余项区间并验证包含真解。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 082. `F3P401` — Four-momentum conservation: visible particles to an exact missing invariant mass

- Public statement: [tasks/082_F3P401/task.md](tasks/082_F3P401/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 中高
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：kind、mass_squared、missing）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Four-momentum conservation: visible particles to an exact missing invariant mass”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 kind、mass_squared、missing。本题的算法与验证负担是：逐粒子累加四动量，用总初态减可见末态得到缺失四动量，并按 Minkowski 度规精确计算不变质量平方。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 逐粒子累加四动量，用总初态减可见末态得到缺失四动量，并按 Minkowski 度规精确计算不变质量平方。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 083. `F3PB01` — Poisson-binomial tail: heterogeneous Bernoulli trials to a generating polynomial

- Public statement: [tasks/083_F3PB01/task.md](tasks/083_F3PB01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：claim、kind、pmf）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Poisson-binomial tail: heterogeneous Bernoulli trials to a generating polynomial”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 claim、kind、pmf。本题的算法与验证负担是：逐个乘入 (1−p_i)+p_i z 的生成多项式，保存每阶精确系数，再汇总指定阈值以上的 Poisson-binomial 尾概率。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 逐个乘入 (1−p_i)+p_i z 的生成多项式，保存每阶精确系数，再汇总指定阈值以上的 Poisson-binomial 尾概率。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 084. `F3PG01` — Polygon with a hole: oriented rings to exact area and centroid

- Public statement: [tasks/084_F3PG01/task.md](tasks/084_F3PG01/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 中高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：area、centroid、kind、signed_ring_areas）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Polygon with a hole: oriented rings to exact area and centroid”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 area、centroid、kind、signed_ring_areas。本题的算法与验证负担是：分别对外环与孔洞应用 shoelace 有符号面积及一阶矩公式，按定向相加并约分得到多边形质心。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 分别对外环与孔洞应用 shoelace 有符号面积及一阶矩公式，按定向相加并约分得到多边形质心。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 085. `F3PT01` — Paired exact permutation: sign symmetry to a subset-sum law

- Public statement: [tasks/085_F3PT01/task.md](tasks/085_F3PT01/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 中高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：distribution、kind、observed_statistic、p_value）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Paired exact permutation: sign symmetry to a subset-sum law”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 distribution、kind、observed_statistic、p_value。本题的算法与验证负担是：把每对差值的符号翻转对应为子集选择，用 subset-sum 动态规划计数全部符号模式，并累加不小于观测统计量的质量。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把每对差值的符号翻转对应为子集选择，用 subset-sum 动态规划计数全部符号模式，并累加不小于观测统计量的质量。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 086. `F3ROT1` — Ordered 3-D rotations: exact quaternion and matrix composition

- Public statement: [tasks/086_F3ROT1/task.md](tasks/086_F3ROT1/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 中高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：composite_quaternion_xyzw、kind、rotated_vector）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Ordered 3-D rotations: exact quaternion and matrix composition”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 composite_quaternion_xyzw、kind、rotated_vector。本题的算法与验证负担是：按题定顺序乘单位四元数并归一符号，再转成 3×3 矩阵，与直接矩阵连乘的每个元素精确对照。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按题定顺序乘单位四元数并归一符号，再转成 3×3 矩阵，与直接矩阵连乘的每个元素精确对照。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 087. `F3ST01` — Sturm root counting: polynomial coefficients to closed-interval certificates

- Public statement: [tasks/087_F3ST01/task.md](tasks/087_F3ST01/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：counts、kind、sturm_sequence）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Sturm root counting: polynomial coefficients to closed-interval certificates”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 counts、kind、sturm_sequence。本题的算法与验证负担是：构造多项式与导数的 Sturm 余式链，精确计算区间两端符号变换数，其差即闭区间内根数并单独处理端点根。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 构造多项式与导数的 Sturm 余式链，精确计算区间两端符号变换数，其差即闭区间内根数并单独处理端点根。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 088. `F3UNC1` — Correlated uncertainty: measurement formulas to an exact covariance pushforward

- Public statement: [tasks/088_F3UNC1/task.md](tasks/088_F3UNC1/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：jacobian、kind、nominal_outputs、output_covariance）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Correlated uncertainty: measurement formulas to an exact covariance pushforward”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 jacobian、kind、nominal_outputs、output_covariance。本题的算法与验证负担是：对测量公式求精确 Jacobian，以 JΣJᵀ 推送相关协方差，返回所有交叉项并检查矩阵对称与半正定。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对测量公式求精确 Jacobian，以 JΣJᵀ 推送相关协方差，返回所有交叉项并检查矩阵对称与半正定。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 089. `F3UNT1` — Affine temperature units: heating data to an exact energy conversion

- Public statement: [tasks/089_F3UNT1/task.md](tasks/089_F3UNT1/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 中高
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：delta_K、delta_degF、heat_Btu、heat_J）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Affine temperature units: heating data to an exact energy conversion”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 delta_K、delta_degF、heat_Btu、heat_J、kind。本题的算法与验证负担是：先用仿射变换把温差而非绝对温度转到一致单位，再乘质量与比热，逐维核对得到精确能量。 结构等级生成规则为“中高：需要完整算法轨迹、递推表或精确多字段见证”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 先用仿射变换把温差而非绝对温度转到一致单位，再乘质量与比热，逐维核对得到精确能量。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 090. `F3WLS1` — Weighted least squares: inverse-variance prose to exact normal equations

- Public statement: [tasks/090_F3WLS1/task.md](tasks/090_F3WLS1/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：beta、gram、gram_inverse、kind）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Weighted least squares: inverse-variance prose to exact normal equations”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 beta、gram、gram_inverse、kind、residuals、rhs、weighted_sse。本题的算法与验证负担是：从逆方差权重建立精确正规方程，解出有理参数与协方差，复算加权残差正交和目标值。 结构等级生成规则为“高：公开题面同时要求多段精确证书、递推、见证或残差核验”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从逆方差权重建立精确正规方程，解出有理参数与协方差，复算加权残差正交和目标值。
- Pilot status: PILOT_ELIGIBLE
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 091. `H4AIF34` — Abstract interpretation by a least interval fixed point

- Public statement: [tasks/091_H4AIF34/task.md](tasks/091_H4AIF34/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：edge_images、kleene_rounds、least_fixpoint、safety_certificate）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Abstract interpretation by a least interval fixed point”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 edge_images、kleene_rounds、least_fixpoint、safety_certificate、worklist_fixpoint。本题的算法与验证负担是：从底元素迭代区间传递函数至不动点，记录每轮 join/transfer，并验证所得区间是包含初态的最小后不动点。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从底元素迭代区间传递函数至不动点，记录每轮 join/transfer，并验证所得区间是包含初态的最小后不动点。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 092. `H4ARI12` — Exact arithmetic coding: rational interval and integer range traces

- Public statement: [tasks/092_H4ARI12/task.md](tasks/092_H4ARI12/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：decoded_message、integer_trace、interval_trace、tag_bits）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact arithmetic coding: rational interval and integer range traces”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 decoded_message、integer_trace、interval_trace、tag_bits、tag_numerator。本题的算法与验证负担是：逐符号用有理累计频率缩小 [low,high) 区间，同时执行整数 renormalization，返回每步区间及最终可解码整数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 逐符号用有理累计频率缩小 [low,high) 区间，同时执行整数 renormalization，返回每步区间及最终可解码整数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 093. `H4BCH09` — BCH decoding with locator, roots and divisibility

- Public statement: [tasks/093_H4BCH09/task.md](tasks/093_H4BCH09/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：corrected_codeword、error_positions、generator_quotient、locator_polynomial_gf64_ascending）→ 独立验收回源结论
- Difficulty basis: 本题对象是“BCH decoding with locator, roots and divisibility”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 corrected_codeword、error_positions、generator_quotient、locator_polynomial_gf64_ascending、syndromes_s1_to_s6。本题的算法与验证负担是：由接收词计算综合，运行 Berlekamp–Massey 得定位多项式，经 Chien 搜根定位错误，纠正后验证生成多项式整除。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由接收词计算综合，运行 Berlekamp–Massey 得定位多项式，经 Chien 搜根定位错误，纠正后验证生成多项式整除。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 094. `H4CFG28` — CFG parse counting with a canonical parse tree

- Public statement: [tasks/094_H4CFG28/task.md](tasks/094_H4CFG28/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：canonical_parse_tree、cyk_nonzero_entries、parse_count、topdown_parse_count）→ 独立验收回源结论
- Difficulty basis: 本题对象是“CFG parse counting with a canonical parse tree”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 canonical_parse_tree、cyk_nonzero_entries、parse_count、topdown_parse_count。本题的算法与验证负担是：运行 CYK/inside 区间递推计数全部非终结符推导，同时返回一棵规范解析树并逐节点核对产生式与跨度。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 运行 CYK/inside 区间递推计数全部非终结符推导，同时返回一棵规范解析树并逐节点核对产生式与跨度。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 095. `H4CHN11` — Channel degradation with strict data-processing witness

- Public statement: [tasks/095_H4CHN11/task.md](tasks/095_H4CHN11/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：V_positive_set、W_positive_set、garbling_matrix、tv_V）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Channel degradation with strict data-processing witness”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 V_positive_set、W_positive_set、garbling_matrix、tv_V、tv_W、witness_row_pair。本题的算法与验证负担是：给出退化核使后一信道等于前一信道复合，精确计算两侧互信息，并以非零差证明严格数据处理。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 给出退化核使后一信道等于前一信道复合，精确计算两侧互信息，并以非零差证明严格数据处理。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 096. `H4CTR01` — Minimum-energy reachability with a dual Gramian certificate

- Public statement: [tasks/096_H4CTR01/task.md](tasks/096_H4CTR01/task.md)
- Mathematical domain: 系统与控制 / 线性系统与矩阵证书
- Structural difficulty: 高
- Certificate: Gramian、Riccati、Lyapunov、Hankel 或不变量证书
- Representation route: 冻结自然语言/结构化输入 → 线性系统与矩阵证书中的精确表示 → Gramian、Riccati、Lyapunov、Hankel 或不变量证书（核心公开字段：control、dual、energy、nullspace_orthogonality）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Minimum-energy reachability with a dual Gramian certificate”；需核验的特有证书结构为 Gramian、Riccati、Lyapunov、Hankel 或不变量证书，公开合同核心项包括 control、dual、energy、nullspace_orthogonality、terminal。本题的算法与验证负担是：用可控 Gramian 解最小能量输入，返回状态轨迹和 Gramian 对偶向量，核对终点、站立性与原始对偶能量相等。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用可控 Gramian 解最小能量输入，返回状态轨迹和 Gramian 对偶向量，核对终点、站立性与原始对偶能量相等。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 097. `H4CYC13` — Cyclic code polynomial-to-matrix duality

- Public statement: [tasks/097_H4CYC13/task.md](tasks/097_H4CYC13/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：check_polynomial_ascending、generator_matrix、generator_rank、parity_check_matrix）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Cyclic code polynomial-to-matrix duality”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 check_polynomial_ascending、generator_matrix、generator_rank、parity_check_matrix、parity_rank。本题的算法与验证负担是：由生成多项式生成循环码基矩阵，再由校验多项式构造对偶校验矩阵，验证两者乘积为零且秩和为长度。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由生成多项式生成循环码基矩阵，再由校验多项式构造对偶校验矩阵，验证两者乘积为零且秩和为长度。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 098. `H4DBM35` — Timed-automata DBM closure through guards, reset and elapse

- Public statement: [tasks/098_H4DBM35/task.md](tasks/098_H4DBM35/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：diagonal_bounds、final_canonical_dbm、final_shortest_paths、stage_dbms）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Timed-automata DBM closure through guards, reset and elapse”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 diagonal_bounds、final_canonical_dbm、final_shortest_paths、stage_dbms、valuation_witness。本题的算法与验证负担是：依次对差分约束矩阵执行 Floyd–Warshall 闭包、guard 交、reset 替换与 elapse 松弛，检查对角线和规范闭包。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 依次对差分约束矩阵执行 Floyd–Warshall 闭包、guard 交、reset 替换与 elapse 松弛，检查对角线和规范闭包。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 099. `H4DEL26` — Delaunay triangulation: empty circles meet lower lifting

- Public statement: [tasks/099_H4DEL26/task.md](tasks/099_H4DEL26/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：convex_hull_ccw、triangle_count、triangles）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Delaunay triangulation: empty circles meet lower lifting”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 convex_hull_ccw、triangle_count、triangles。本题的算法与验证负担是：为每个三角形计算精确外接圆并检查其内部无其他点；再提升到抛物面，验证对应面具有下支撑平面。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 为每个三角形计算精确外接圆并检查其内部无其他点；再提升到抛物面，验证对应面具有下支撑平面。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 100. `H4EUF36` — EUF congruence closure with a minimal UNSAT explanation

- Public statement: [tasks/100_H4EUF36/task.md](tasks/100_H4EUF36/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：class_representatives、conflict_terms、conflicting_disequality、core_merge_proof_forest）→ 独立验收回源结论
- Difficulty basis: 本题对象是“EUF congruence closure with a minimal UNSAT explanation”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 class_representatives、conflict_terms、conflicting_disequality、core_merge_proof_forest、deletion_separations、merge_proof_forest、minimal_unsat_core_equalities。本题的算法与验证负担是：用并查集执行等式合并与函数同余闭包，追踪每次合并理由，最后从冲突不等式回溯最小 UNSAT 解释链。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用并查集执行等式合并与函数同余闭包，追踪每次合并理由，最后从冲突不等式回溯最小 UNSAT 解释链。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 101. `H4FFI18` — GF(2) factorization with Rabin irreducibility certificates

- Public statement: [tasks/101_H4FFI18/task.md](tasks/101_H4FFI18/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：irreducible_factors_ascending、rabin_certificates）→ 独立验收回源结论
- Difficulty basis: 本题对象是“GF(2) factorization with Rabin irreducibility certificates”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 irreducible_factors_ascending、rabin_certificates。本题的算法与验证负担是：在 GF(2)[x] 上分解目标多项式，对每个因子执行 Rabin 的 x^(2^k) 同余与 gcd 检查，并复乘恢复原式。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 GF(2)[x] 上分解目标多项式，对每个因子执行 Rabin 的 x^(2^k) 同余与 gcd 检查，并复乘恢复原式。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 102. `H4GBR15` — Groebner basis with ideal-membership transport

- Public statement: [tasks/102_H4GBR15/task.md](tasks/102_H4GBR15/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：basis_in_generators、groebner_basis、leading_monomials、target_in_generators）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Groebner basis with ideal-membership transport”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 basis_in_generators、groebner_basis、leading_monomials、target_in_generators。本题的算法与验证负担是：重放所有 S-多项式约化至零以验证 Gröbner 基，再返回目标多项式的基组合系数，直接复算理想成员等式。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 重放所有 S-多项式约化至零以验证 Gröbner 基，再返回目标多项式的基组合系数，直接复算理想成员等式。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 103. `H4HNF27` — Hermite form with lattice membership and modular nonmembership

- Public statement: [tasks/103_H4HNF27/task.md](tasks/103_H4HNF27/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：hermite_H、lattice_index、member_coefficients、member_residue）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Hermite form with lattice membership and modular nonmembership”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 hermite_H、lattice_index、member_coefficients、member_residue、nonmember_residue、separator_modulus、separator_vector、unimodular_U。本题的算法与验证负担是：给出整矩阵到 Hermite 形的幺模变换，解出格成员坐标；对非成员向量以模素数线性泛函作分离证书。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 给出整矩阵到 Hermite 形的幺模变换，解出格成员坐标；对非成员向量以模素数线性泛函作分离证书。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 104. `H4HNK04` — Minimal realization from Markov parameters and Hankel rank

- Public statement: [tasks/104_H4HNK04/task.md](tasks/104_H4HNK04/task.md)
- Mathematical domain: 系统与控制 / 线性系统与矩阵证书
- Structural difficulty: 高
- Certificate: Gramian、Riccati、Lyapunov、Hankel 或不变量证书
- Representation route: 冻结自然语言/结构化输入 → 线性系统与矩阵证书中的精确表示 → Gramian、Riccati、Lyapunov、Hankel 或不变量证书（核心公开字段：generating_denominator_ascending、generating_numerator_ascending、hankel_rank、hankel_rref_pivots）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Minimal realization from Markov parameters and Hankel rank”；需核验的特有证书结构为 Gramian、Riccati、Lyapunov、Hankel 或不变量证书，公开合同核心项包括 generating_denominator_ascending、generating_numerator_ascending、hankel_rank、hankel_rref_pivots、markov_parameters、minimal_recurrence_ascending。本题的算法与验证负担是：由 Markov 参数组成块 Hankel 矩阵并做秩分解，构造最小状态实现，复算其脉冲响应并以 Hankel 秩证明维数最小。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由 Markov 参数组成块 Hankel 矩阵并做秩分解，构造最小状态实现，复算其脉冲响应并以 Hankel 秩证明维数最小。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 105. `H4HOD29` — Six-dimensional Hodge star with exact wedge pairing

- Public statement: [tasks/105_H4HOD29/task.md](tasks/105_H4HOD29/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：alpha_wedge_star_scalar、star_alpha、star_square_sign、star_star_alpha）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Six-dimensional Hodge star with exact wedge pairing”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 alpha_wedge_star_scalar、star_alpha、star_square_sign、star_star_alpha。本题的算法与验证负担是：在六维给定度量与定向下对基楔积计算 Hodge 星号，逐基验证 α∧⋆β 等于诱导内积乘体积形式。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在六维给定度量与定向下对基楔积计算 Hodge 星号，逐基验证 α∧⋆β 等于诱导内积乘体积形式。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 106. `H4HPI07` — Half-plane intersection with Farkas redundancy certificates

- Public statement: [tasks/106_H4HPI07/task.md](tasks/106_H4HPI07/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：active_constraints、doubled_area、redundancy_certificates、vertices_ccw）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Half-plane intersection with Farkas redundancy certificates”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 active_constraints、doubled_area、redundancy_certificates、vertices_ccw。本题的算法与验证负担是：逐半平面求交得到顶点环，对每条被删约束返回 Farkas 非负组合，证明其相对保留约束确属冗余。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 逐半平面求交得到顶点环，对每条被删约束返回 Farkas 非负组合，证明其相对保留约束确属冗余。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 107. `H4HUL06` — Convex hull with edge-support and exact area certificates

- Public statement: [tasks/107_H4HUL06/task.md](tasks/107_H4HUL06/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：doubled_area、edge_support、hull_ids_ccw）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Convex hull with edge-support and exact area certificates”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 doubled_area、edge_support、hull_ids_ccw。本题的算法与验证负担是：按极角/单调链构造凸包顶点序，对每条边返回支撑半平面，复算所有点侧向并用 shoelace 求精确面积。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按极角/单调链构造凸包顶点序，对每条边返回支撑半平面，复算所有点侧向并用 shoelace 求精确面积。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 108. `H4LQR03` — Finite-horizon exact LQR: Riccati recursion meets open-loop KKT

- Public statement: [tasks/108_H4LQR03/task.md](tasks/108_H4LQR03/task.md)
- Mathematical domain: 系统与控制 / 线性系统与矩阵证书
- Structural difficulty: 高
- Certificate: Gramian、Riccati、Lyapunov、Hankel 或不变量证书
- Representation route: 冻结自然语言/结构化输入 → 线性系统与矩阵证书中的精确表示 → Gramian、Riccati、Lyapunov、Hankel 或不变量证书（核心公开字段：controls、feedback_K、optimal_value、riccati_P）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Finite-horizon exact LQR: Riccati recursion meets open-loop KKT”；需核验的特有证书结构为 Gramian、Riccati、Lyapunov、Hankel 或不变量证书，公开合同核心项包括 controls、feedback_K、optimal_value、riccati_P、states。本题的算法与验证负担是：反向递推有限时域 Riccati 矩阵得到反馈控制，再解开环 KKT 方程，逐时刻比较两条路线的状态、控制和代价。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 反向递推有限时域 Riccati 矩阵得到反馈控制，再解开环 KKT 方程，逐时刻比较两条路线的状态、控制和代价。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 109. `H4LTL25` — LTL response violation by a Büchi-style lasso

- Public statement: [tasks/109_H4LTL25/task.md](tasks/109_H4LTL25/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：cycle、loop_entry、monitor_trace、prefix）→ 独立验收回源结论
- Difficulty basis: 本题对象是“LTL response violation by a Büchi-style lasso”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 cycle、loop_entry、monitor_trace、prefix。本题的算法与验证负担是：构造违反 response 性质的 Büchi 乘积状态，给出前缀加循环的 lasso，并验证循环中请求持续未获响应。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 构造违反 response 性质的 Büchi 乘积状态，给出前缀加循环的 lasso，并验证循环中请求持续未获响应。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 110. `H4LYA05` — Exact discrete Lyapunov equation with an LDL positivity witness

- Public statement: [tasks/110_H4LYA05/task.md](tasks/110_H4LYA05/task.md)
- Mathematical domain: 系统与控制 / 线性系统与矩阵证书
- Structural difficulty: 高
- Certificate: Gramian、Riccati、Lyapunov、Hankel 或不变量证书
- Representation route: 冻结自然语言/结构化输入 → 线性系统与矩阵证书中的精确表示 → Gramian、Riccati、Lyapunov、Hankel 或不变量证书（核心公开字段：LDL_D、LDL_L、P、leading_principal_minors）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact discrete Lyapunov equation with an LDL positivity witness”；需核验的特有证书结构为 Gramian、Riccati、Lyapunov、Hankel 或不变量证书，公开合同核心项包括 LDL_D、LDL_L、P、leading_principal_minors。本题的算法与验证负担是：精确求解离散 Lyapunov 方程 P−AᵀPA=Q，返回 P 的 LDLᵀ 分解，并用正对角 D 证明正定与稳定性见证。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 精确求解离散 Lyapunov 方程 P−AᵀPA=Q，返回 P 的 LDLᵀ 分解，并用正对角 D 证明正定与稳定性见证。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 111. `H4MKS08` — Minkowski sum with vertex-decomposition witnesses

- Public statement: [tasks/111_H4MKS08/task.md](tasks/111_H4MKS08/task.md)
- Mathematical domain: 几何学 / 计算、欧氏与离散几何
- Structural difficulty: 高
- Certificate: 精确坐标、定向、支撑或拓扑不变量证书
- Representation route: 冻结自然语言/结构化输入 → 计算、欧氏与离散几何中的精确表示 → 精确坐标、定向、支撑或拓扑不变量证书（核心公开字段：doubled_area、vertex_count、vertices_ccw）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Minkowski sum with vertex-decomposition witnesses”；需核验的特有证书结构为 精确坐标、定向、支撑或拓扑不变量证书，公开合同核心项包括 doubled_area、vertex_count、vertices_ccw。本题的算法与验证负担是：合并两个凸多边形的边方向得到 Minkowski 和边界，并为每个输出顶点返回一对输入顶点的精确分解。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 合并两个凸多边形的边方向得到 Minkowski 和边界，并为每个输出顶点返回一对输入顶点的精确分解。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 112. `H4OBS02` — Observability quotient with an invariant-kernel certificate

- Public statement: [tasks/112_H4OBS02/task.md](tasks/112_H4OBS02/task.md)
- Mathematical domain: 系统与控制 / 线性系统与矩阵证书
- Structural difficulty: 高
- Certificate: Gramian、Riccati、Lyapunov、Hankel 或不变量证书
- Representation route: 冻结自然语言/结构化输入 → 线性系统与矩阵证书中的精确表示 → Gramian、Riccati、Lyapunov、Hankel 或不变量证书（核心公开字段：annihilator_coefficients_ascending、indistinguishable_delta、kernel_basis、rank）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Observability quotient with an invariant-kernel certificate”；需核验的特有证书结构为 Gramian、Riccati、Lyapunov、Hankel 或不变量证书，公开合同核心项包括 annihilator_coefficients_ascending、indistinguishable_delta、kernel_basis、rank、rref_pivots。本题的算法与验证负担是：计算可观测矩阵核并给出其 A-不变基，在商空间上构造诱导系统，验证商后可观测且维数与秩一致。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 计算可观测矩阵核并给出其 A-不变基，在商空间上构造诱导系统，验证商后可观测且维数与秩一致。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 113. `H4PAD19` — Exact [10/10] Pade approximant of exp

- Public statement: [tasks/113_H4PAD19/task.md](tasks/113_H4PAD19/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：P_ascending、Q_ascending、first_residual_coefficient、hankel_system_determinant）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact [10/10] Pade approximant of exp”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 P_ascending、Q_ascending、first_residual_coefficient、hankel_system_determinant。本题的算法与验证负担是：令 [10/10] Padé 分子分母的级数乘积匹配 exp 到 20 阶，解精确线性方程并验证余项前 21 个系数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 令 [10/10] Padé 分子分母的级数乘积匹配 exp 到 20 阶，解精确线性方程并验证余项前 21 个系数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 114. `H4PET24` — Petri reachability plus invariant-separated decoy

- Public statement: [tasks/114_H4PET24/task.md](tasks/114_H4PET24/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：decoy_invariant、firing_counts、firing_sequence、initial_invariant）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Petri reachability plus invariant-separated decoy”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 decoy_invariant、firing_counts、firing_sequence、initial_invariant、place_invariant、target_invariant。本题的算法与验证负担是：沿给定发射序列逐步更新标识并证明目标可达；对诱饵目标计算线性 place invariant，证明其值与初态不兼容。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 沿给定发射序列逐步更新标识并证明目标可达；对诱饵目标计算线性 place invariant，证明其值与初态不兼容。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 115. `H4PLU21` — Pluecker coordinates to an RREF two-plane

- Public statement: [tasks/115_H4PLU21/task.md](tasks/115_H4PLU21/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：plucker_relation_residuals、rref_basis、skew_matrix_rank）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Pluecker coordinates to an RREF two-plane”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 plucker_relation_residuals、rref_basis、skew_matrix_rank。本题的算法与验证负担是：由 Plücker 坐标选择非零主坐标恢复两行 RREF 基，复算全部 2×2 子式并检查 Plücker 二次关系。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由 Plücker 坐标选择非零主坐标恢复两行 RREF 基，复算全部 2×2 子式并检查 Plücker 二次关系。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 116. `H4RES16` — Resultant determinant with a Bezout elimination witness

- Public statement: [tasks/116_H4RES16/task.md](tasks/116_H4RES16/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：bezout_a_ascending、bezout_b_ascending、resultant、sylvester_determinant）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Resultant determinant with a Bezout elimination witness”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 bezout_a_ascending、bezout_b_ascending、resultant、sylvester_determinant。本题的算法与验证负担是：构造 Sylvester 矩阵并精确消元求行列式，同时返回 Bézout 多项式，使其线性组合等于 resultant。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 构造 Sylvester 矩阵并精确消元求行列式，同时返回 Bézout 多项式，使其线性组合等于 resultant。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 117. `H4RM110` — Nearest first-order Reed–Muller word by Walsh spectrum

- Public statement: [tasks/117_H4RM110/task.md](tasks/117_H4RM110/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：affine_constant、affine_linear_mask、hamming_distance、nearest_codeword）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Nearest first-order Reed–Muller word by Walsh spectrum”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 affine_constant、affine_linear_mask、hamming_distance、nearest_codeword、walsh_spectrum。本题的算法与验证负担是：对接收布尔函数做完整 Walsh–Hadamard 变换，从最大绝对谱系数恢复最近仿射函数，并核对距离公式。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对接收布尔函数做完整 Walsh–Hadamard 变换，从最大绝对谱系数恢复最近仿射函数，并核对距离公式。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 118. `H4SNF14` — Smith normal form with determinantal-divisor audit

- Public statement: [tasks/118_H4SNF14/task.md](tasks/118_H4SNF14/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：D、U、V、determinantal_divisors）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Smith normal form with determinantal-divisor audit”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 D、U、V、determinantal_divisors。本题的算法与验证负担是：返回左右幺模矩阵与 Smith 对角形，复乘原矩阵；再以各阶子式 gcd 核对全部行列式因子。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 返回左右幺模矩阵与 Smith 对角形，复乘原矩阵；再以各阶子式 gcd 核对全部行列式因子。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 119. `H4SOC30` — Exact SOCP optimum with KKT and dual-norm certificate

- Public statement: [tasks/119_H4SOC30/task.md](tasks/119_H4SOC30/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：dual_norm_square、dual_vector、kkt_multiplier、norm_square）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact SOCP optimum with KKT and dual-norm certificate”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 dual_norm_square、dual_vector、kkt_multiplier、norm_square、objective_value、primal_x、stationarity_residual、transformed_y。本题的算法与验证负担是：构造 SOCP 原始点、锥对偶变量和等式乘子，逐锥检查可行性、互补性与对偶范数，并核对零对偶间隙。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 构造 SOCP 原始点、锥对偶变量和等式乘子，逐锥检查可行性、互补性与对偶范数，并核对零对偶间隙。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 120. `H4SSS33` — Shamir reconstruction with a coalition-privacy polynomial witness

- Public statement: [tasks/120_H4SSS33/task.md](tasks/120_H4SSS33/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：all_share_residuals、privacy_coalition_evaluations、privacy_difference_multiple、privacy_polynomials_ascending）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Shamir reconstruction with a coalition-privacy polynomial witness”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 all_share_residuals、privacy_coalition_evaluations、privacy_difference_multiple、privacy_polynomials_ascending、privacy_secrets、privacy_vanishing_polynomial_ascending、reconstructed_polynomial_ascending、reconstructed_secret。本题的算法与验证负担是：用拉格朗日插值从授权份额恢复秘密；对未授权联盟构造两个与其份额一致但常数项不同的多项式，证明隐私。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用拉格朗日插值从授权份额恢复秘密；对未授权联盟构造两个与其份额一致但常数项不同的多项式，证明隐私。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 121. `H4TEN20` — Tensor-network contraction across two parenthesizations

- Public statement: [tasks/121_H4TEN20/task.md](tasks/121_H4TEN20/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：AB_over_k、CD_over_n、Y）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Tensor-network contraction across two parenthesizations”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 AB_over_k、CD_over_n、Y。本题的算法与验证负担是：按两种括号化顺序逐指标收缩同一张量网络，返回全部中间张量，并逐输出分量验证两路线完全相等。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按两种括号化顺序逐指标收缩同一张量网络，返回全部中间张量，并逐输出分量验证两路线完全相等。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 122. `H4TRS32` — Terminating rewrite system with complete critical-pair joins

- Public statement: [tasks/122_H4TRS32/task.md](tasks/122_H4TRS32/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：critical_pair_count、critical_pairs、termination_certificate、test_normalizations）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Terminating rewrite system with complete critical-pair joins”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 critical_pair_count、critical_pairs、termination_certificate、test_normalizations。本题的算法与验证负担是：给出严格下降的终止度量，枚举所有临界对并为每对返回两侧归约到共同正规形的完整 join 轨迹。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 给出严格下降的终止度量，枚举所有临界对并为每对返回两侧归约到共同正规形的完整 join 轨迹。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 123. `H4TUC22` — Exact Tucker decomposition and multilinear ranks

- Public statement: [tasks/123_H4TUC22/task.md](tasks/123_H4TUC22/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：core、factor_A、factor_B、factor_C）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Exact Tucker decomposition and multilinear ranks”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 core、factor_A、factor_B、factor_C、unfolding_pivots、unfolding_ranks。本题的算法与验证负担是：用给定因子矩阵和核心张量重构原张量，检查因子列空间秩，并从各模展开矩阵证明 multilinear rank。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 用给定因子矩阵和核心张量重构原张量，检查因子列空间秩，并从各模展开矩阵证明 multilinear rank。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 124. `H4TY31` — Hindley–Milner principal typing with a canonical MGU

- Public statement: [tasks/124_H4TY31/task.md](tasks/124_H4TY31/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：ground_specializations、let_schemes、mgu_substitution、node_types）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Hindley–Milner principal typing with a canonical MGU”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 ground_specializations、let_schemes、mgu_substitution、node_types、principal_quantified、principal_type、unification_trace。本题的算法与验证负担是：对表达式生成 Hindley–Milner 类型方程，执行带 occurs-check 的统一，返回主类型与规范 MGU，并重放每个替换。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对表达式生成 Hindley–Milner 类型方程，执行带 occurs-check 的统一，返回主类型与规范 MGU，并重放每个替换。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 125. `H4WFA23` — Weighted-automata equivalence by invariant reachable space

- Public statement: [tasks/125_H4WFA23/task.md](tasks/125_H4WFA23/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：output_pairings、reachable_difference_basis、reachable_rank、transition_closure_coordinates）→ 独立验收回源结论
- Difficulty basis: 本题对象是“Weighted-automata equivalence by invariant reachable space”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 output_pairings、reachable_difference_basis、reachable_rank、transition_closure_coordinates。本题的算法与验证负担是：从两个加权自动机的初始差向量生成可达线性空间基，验证其对每个字母转移不变且所有基向量输出差为零。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从两个加权自动机的初始差向量生成可达线性空间基，验证其对每个字母转移不变且所有基向量输出差为零。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 126. `P5BIN19` — 容量/冲突/同异箱约束的精确装箱证书

- Public statement: [tasks/126_P5BIN19/task.md](tasks/126_P5BIN19/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：b_minus_one_infeasibility_search、bin_loads、contracted_conflicts、contracted_groups）→ 独立验收回源结论
- Difficulty basis: 本题对象是“容量/冲突/同异箱约束的精确装箱证书”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 b_minus_one_infeasibility_search、bin_loads、contracted_conflicts、contracted_groups、contracted_weights、item_to_bin、packing_search、pb_source_bridge。本题的算法与验证负担是：对 24 件物品及 79 对冲突/同异箱关系给出完整分箱，逐箱复算载荷；用 22863 节点分支界证书排除更少箱数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 24 件物品及 79 对冲突/同异箱关系给出完整分箱，逐箱复算载荷；用 22863 节点分支界证书排除更少箱数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 127. `P5BRN13` — 受约束着色的 Burnside 共轭类证书

- Public statement: [tasks/127_P5BRN13/task.md](tasks/127_P5BRN13/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：burnside_weighted_sum、conjugacy_classes、group_elements、identity_histogram_dp_layers）→ 独立验收回源结论
- Difficulty basis: 本题对象是“受约束着色的 Burnside 共轭类证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 burnside_weighted_sum、conjugacy_classes、group_elements、identity_histogram_dp_layers、orbit_total、valid_coloring_count。本题的算法与验证负担是：按约束着色集合上的群作用枚举共轭类，计算各代表元固定点着色数，再用 Burnside 平均得到轨道数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 按约束着色集合上的群作用枚举共轭类，计算各代表元固定点着色数，再用 Burnside 平均得到轨道数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 128. `P5CAP18` — 三元仿射空间 cap 的完整仿射线与最优性证书

- Public statement: [tasks/128_P5CAP18/task.md](tasks/128_P5CAP18/task.md)
- Mathematical domain: 离散数学 / 有限几何与极值组合
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 有限几何与极值组合中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：affine_line_constraints、branch_bound_optimality、cap_point_ids、cap_vectors）→ 独立验收回源结论
- Difficulty basis: 本题对象是“三元仿射空间 cap 的完整仿射线与最优性证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 affine_line_constraints、branch_bound_optimality、cap_point_ids、cap_vectors、source_to_constraint_bridge。本题的算法与验证负担是：枚举 F3^3 的 117 条仿射线验证候选 cap 无三点共线，再重放 75573 节点搜索证明不存在更大 cap。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 枚举 F3^3 的 117 条仿射线验证候选 cap 无三点共线，再重放 75573 节点搜索证明不存在更大 cap。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 129. `P5CAY12` — 重标号有限群的 Cayley 直径证书

- Public statement: [tasks/129_P5CAY12/task.md](tasks/129_P5CAY12/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：bfs、cayley_adjacency、diameter、diameter_witness）→ 独立验收回源结论
- Difficulty basis: 本题对象是“重标号有限群的 Cayley 直径证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 bfs、cayley_adjacency、diameter、diameter_witness、group_law。本题的算法与验证负担是：从给定小生成集对 96 阶重标号群做 Cayley BFS，返回每个元素的最短生成词和距离层，并核对最大层即直径。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从给定小生成集对 96 阶重标号群做 Cayley BFS，返回每个元素的最短生成词和距离层，并核对最大层即直径。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 130. `P5DES14` — 仿射 2-设计的 PB 对计数与轨道稳定子证书

- Public statement: [tasks/130_P5DES14/task.md](tasks/130_P5DES14/task.md)
- Mathematical domain: 离散数学 / 组合设计与群作用
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 组合设计与群作用中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：block_orbits、generator_block_maps、group_elements、parameters）→ 独立验收回源结论
- Difficulty basis: 本题对象是“仿射 2-设计的 PB 对计数与轨道稳定子证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 block_orbits、generator_block_maps、group_elements、parameters、pb_pair_equations。本题的算法与验证负担是：生成 v≥25 仿射设计的块轨道，核对每对点的出现次数，并用轨道—稳定子与 PB 计数证明设计参数完整。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 生成 v≥25 仿射设计的块轨道，核对每对点的出现次数，并用轨道—稳定子与 PB 计数证明设计参数完整。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 131. `P5DMN02` — 73 状态 DFA 的可达最小商与逐对区分词证书

- Public statement: [tasks/131_P5DMN02/task.md](tasks/131_P5DMN02/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：distinguishing_words、old_to_quotient、quotient_accepting、quotient_transitions）→ 独立验收回源结论
- Difficulty basis: 本题对象是“73 状态 DFA 的可达最小商与逐对区分词证书”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 distinguishing_words、old_to_quotient、quotient_accepting、quotient_transitions、reachability_parents、refinement_rounds。本题的算法与验证负担是：从初态 BFS 标记 73 状态可达性，以分割细化得到最小商，并为每对不同等价类返回可核验区分词。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从初态 BFS 标记 73 状态可达性，以分割细化得到最小商，并为每对不同等价类返回可核验区分词。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 132. `P5EIG26` — 96 维整数对称三对角谱证书

- Public statement: [tasks/132_P5EIG26/task.md](tasks/132_P5EIG26/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：all_endpoint_count_trace_complete、close_pair_indices、common_interval_denominator、dimension）→ 独立验收回源结论
- Difficulty basis: 本题对象是“96 维整数对称三对角谱证书”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 all_endpoint_count_trace_complete、close_pair_indices、common_interval_denominator、dimension、dyadic_eigenpairs、irreducible_offdiagonal_nonzero、minimum_interval_gap_numerator。本题的算法与验证负担是：对不可约 96 阶整数三对角矩阵做精确 Sturm–LDL 计数，在 192 个有理端点隔离各特征值，并验证近邻谱对和残差界。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对不可约 96 阶整数三对角矩阵做精确 Sturm–LDL 计数，在 192 个有理端点隔离各特征值，并验证近邻谱对和残差界。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 133. `P5FAC23` — 18 设施、60 客户的容量设施选址

- Public statement: [tasks/133_P5FAC23/task.md](tasks/133_P5FAC23/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：assignment_cost_total、client_assignment、cost_capacity_tables、exact_total_cost）→ 独立验收回源结论
- Difficulty basis: 本题对象是“18 设施、60 客户的容量设施选址”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 assignment_cost_total、client_assignment、cost_capacity_tables、exact_total_cost、facility_loads、lower_cost_infeasibility_branch_bound、opened_facilities、opening_cost_total。本题的算法与验证负担是：选择 18 个设施中的开放集并分配 60 个客户，核对容量与成本；用完整分支界给出最优下界和剪枝理由。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 选择 18 个设施中的开放集并分配 60 个客户，核对容量与成本；用完整分支界给出最优下界和剪枝理由。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 134. `P5FFP21` — 20 次扩域的本原元与完整模幂轨迹

- Public statement: [tasks/134_P5FFP21/task.md](tasks/134_P5FFP21/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：exact_order、irreducibility_frobenius_trace、modulus_bits、order_factorization）→ 独立验收回源结论
- Difficulty basis: 本题对象是“20 次扩域的本原元与完整模幂轨迹”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 exact_order、irreducibility_frobenius_trace、modulus_bits、order_factorization、prime_divisor_order_tests、primitive_element_bits。本题的算法与验证负担是：在 20 次有限域扩张中验证候选元素满足定义多项式，按群阶各素因子做模幂测试，并返回完整平方乘轨迹。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 20 次有限域扩张中验证候选元素满足定义多项式，按群阶各素因子做模幂测试，并返回完整平方乘轨迹。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 135. `P5HAM15` — 非 Hamilton 图的 successor-CNF 与子集递推不可行证书

- Public statement: [tasks/135_P5HAM15/task.md](tasks/135_P5HAM15/task.md)
- Mathematical domain: 理论计算机科学 / 逻辑、电路与判定程序
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 逻辑、电路与判定程序中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：graph_checks、held_karp_infeasibility、source_bridge、successor_cnf）→ 独立验收回源结论
- Difficulty basis: 本题对象是“非 Hamilton 图的 successor-CNF 与子集递推不可行证书”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 graph_checks、held_karp_infeasibility、source_bridge、successor_cnf、successor_variables。本题的算法与验证负担是：把 successor-CNF 的每顶点唯一前后继约束与 Held–Karp 子集状态对应，完整 DP 证明不存在覆盖全图的 Hamilton 回路。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把 successor-CNF 的每顶点唯一前后继约束与 Held–Karp 子集状态对应，完整 DP 证明不存在覆盖全图的 Hamilton 回路。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 136. `P5HEA28` — 32×32 稳态热反应精确场证书

- Public statement: [tasks/136_P5HEA28/task.md](tasks/136_P5HEA28/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 高
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：boundary_contribution_table、boundary_values、energy_denominator、energy_lhs_numerator）→ 独立验收回源结论
- Difficulty basis: 本题对象是“32×32 稳态热反应精确场证书”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 boundary_contribution_table、boundary_values、energy_denominator、energy_lhs_numerator、energy_rhs_numerator、exact_error_bound_numerator、field_denominator、field_numerators。本题的算法与验证负担是：在 32×32 内点上返回完整稳态温度场，逐点复算离散扩散—反应残差、边界条件、M-matrix 单调性和离散能量。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 32×32 内点上返回完整稳态温度场，逐点复算离散扩散—反应残差、边界条件、M-matrix 单调性和离散能量。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 137. `P5IIR09` — degree-18 IIR 的 Jury–Schur/Sturm 双路线稳定证书

- Public statement: [tasks/137_P5IIR09/task.md](tasks/137_P5IIR09/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：bilinear_polynomial、jury_table、route_agreement、schur_rows）→ 独立验收回源结论
- Difficulty basis: 本题对象是“degree-18 IIR 的 Jury–Schur/Sturm 双路线稳定证书”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 bilinear_polynomial、jury_table、route_agreement、schur_rows、stable、strict_margins、sturm_sequence、sturm_variations。本题的算法与验证负担是：对 degree-18 分母执行 Jury–Schur 递推并同步构造单位圆映射后的 Sturm 链，以两条独立路线确认全部根严格在圆内。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 degree-18 分母执行 Jury–Schur 递推并同步构造单位圆映射后的 Sturm 链，以两条独立路线确认全部根严格在圆内。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 138. `P5ISI27` — 宽 10、长 40 的周期边界 Ising 传递证书

- Public statement: [tasks/138_P5ISI27/task.md](tasks/138_P5ISI27/task.md)
- Mathematical domain: 数学物理 / 物理、化学与科学计算
- Structural difficulty: 高
- Certificate: 守恒量、量纲、传递矩阵或完整场证书
- Representation route: 冻结自然语言/结构化输入 → 物理、化学与科学计算中的精确表示 → 守恒量、量纲、传递矩阵或完整场证书（核心公开字段：final_partition_value、length、periodic_boundary_contributions、symmetry_checks）→ 独立验收回源结论
- Difficulty basis: 本题对象是“宽 10、长 40 的周期边界 Ising 传递证书”；需核验的特有证书结构为 守恒量、量纲、传递矩阵或完整场证书，公开合同核心项包括 final_partition_value、length、periodic_boundary_contributions、symmetry_checks、transfer_vectors、width。本题的算法与验证负担是：对宽 10、长 40 的非均匀 Ising 条带枚举每列 2^10 状态，生成完整 40960 条传递向量并闭合周期边界配分函数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对宽 10、长 40 的非均匀 Ising 条带枚举每列 2^10 状态，生成完整 40960 条传递向量并闭合周期边界配分函数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 139. `P5ISO01` — 固定加权有理等序回归的 PAVA/KKT 双证书

- Public statement: [tasks/139_P5ISO01/task.md](tasks/139_P5ISO01/task.md)
- Mathematical domain: 运筹与优化 / 离散与凸优化
- Structural difficulty: 高
- Certificate: 原始—对偶、KKT、动态规划或分支界证书
- Representation route: 冻结自然语言/结构化输入 → 离散与凸优化中的精确表示 → 原始—对偶、KKT、动态规划或分支界证书（核心公开字段：blocks、dual_multipliers、dual_objective、fit）→ 独立验收回源结论
- Difficulty basis: 本题对象是“固定加权有理等序回归的 PAVA/KKT 双证书”；需核验的特有证书结构为 原始—对偶、KKT、动态规划或分支界证书，公开合同核心项包括 blocks、dual_multipliers、dual_objective、fit、objective。本题的算法与验证负担是：对固定加权有理序列运行 PAVA 合并违序块，返回块均值与 KKT 乘子，逐点核对单调性、互补性和精确目标。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对固定加权有理序列运行 PAVA 合并违序块，返回块均值与 KKT 乘子，逐点核对单调性、互补性和精确目标。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 140. `P5KSX05` — 137×149 双样本 KS 尾概率的格路/CRT 证书

- Public statement: [tasks/140_P5KSX05/task.md](tasks/140_P5KSX05/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：crt、dp_mod、forbidden、probability）→ 独立验收回源结论
- Difficulty basis: 本题对象是“137×149 双样本 KS 尾概率的格路/CRT 证书”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 crt、dp_mod、forbidden、probability、statistic。本题的算法与验证负担是：在 137×149 格路上避开 KS 禁带做整数 DP，分别模两个素数计算路径数，经 CRT 重构后除以总路径数并检查边界唯一性。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 137×149 格路上避开 KS 禁带做整数 DP，分别模两个素数计算路径数，经 CRT 重构后除以总路径数并检查边界唯一性。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 141. `P5LIN10` — 180 阶稀疏有理线性系统的后验误差与模解证书

- Public statement: [tasks/141_P5LIN10/task.md](tasks/141_P5LIN10/task.md)
- Mathematical domain: 应用数学 / 数值分析与线性代数
- Structural difficulty: 高
- Certificate: 矩阵分解、区间、残差或后验误差证书
- Representation route: 冻结自然语言/结构化输入 → 数值分析与线性代数中的精确表示 → 矩阵分解、区间、残差或后验误差证书（核心公开字段：dominance_margins、error_bound、gamma、modular_solutions）→ 独立验收回源结论
- Difficulty basis: 本题对象是“180 阶稀疏有理线性系统的后验误差与模解证书”；需核验的特有证书结构为 矩阵分解、区间、残差或后验误差证书，公开合同核心项包括 dominance_margins、error_bound、gamma、modular_solutions、residual、x_dyadic。本题的算法与验证负担是：对 180 阶稀疏有理系统先做模素数求解与有理重构，代回计算精确残差，再以逆范数后验界证明解误差。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对 180 阶稀疏有理系统先做模素数求解与有理重构，代回计算精确残差，再以逆范数后验界证明解误差。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 142. `P5LPC08` — 192 点 order-24 LPC 的完整 Levinson 有理递推证书

- Public statement: [tasks/142_P5LPC08/task.md](tasks/142_P5LPC08/task.md)
- Mathematical domain: 数值与信号 / 信号处理、张量与数值变换
- Structural difficulty: 高
- Certificate: 完整递推表、精确变换或残差证书
- Representation route: 冻结自然语言/结构化输入 → 信号处理、张量与数值变换中的精确表示 → 完整递推表、精确变换或残差证书（核心公开字段：ar_rows、autocorrelations、final_coefficients、prediction_errors）→ 独立验收回源结论
- Difficulty basis: 本题对象是“192 点 order-24 LPC 的完整 Levinson 有理递推证书”；需核验的特有证书结构为 完整递推表、精确变换或残差证书，公开合同核心项包括 ar_rows、autocorrelations、final_coefficients、prediction_errors、reflection_coefficients、yule_walker_residuals。本题的算法与验证负担是：由 192 点数据计算 order-24 自相关，完整执行 Levinson 递推，记录每阶反射系数与正预测误差并复算正规方程。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由 192 点数据计算 order-24 自相关，完整执行 Levinson 递推，记录每阶反射系数与正预测误差并复算正规方程。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 143. `P5MRK06` — 64+5 状态吸收链的有理解/模重构证书

- Public statement: [tasks/143_P5MRK06/task.md](tasks/143_P5MRK06/task.md)
- Mathematical domain: 概率统计 / 精确概率与统计推断
- Structural difficulty: 高
- Certificate: 精确分布、计数递推或有理概率证书
- Representation route: 冻结自然语言/结构化输入 → 精确概率与统计推断中的精确表示 → 精确分布、计数递推或有理概率证书（核心公开字段：absorption_probabilities、hitting_times、modular_tables、reconstruction_bounds）→ 独立验收回源结论
- Difficulty basis: 本题对象是“64+5 状态吸收链的有理解/模重构证书”；需核验的特有证书结构为 精确分布、计数递推或有理概率证书，公开合同核心项包括 absorption_probabilities、hitting_times、modular_tables、reconstruction_bounds。本题的算法与验证负担是：把 64 个瞬态与 5 个吸收状态写成有理线性方程，模多个非奇异素数求解并有理重构，代回检查每行吸收概率。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 把 64 个瞬态与 5 个吸收状态写成有理线性方程，模多个非奇异素数求解并有理重构，代回检查每行吸收概率。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 144. `P5NTT07` — 257×383 有符号卷积的双素数 NTT/CRT 证书

- Public statement: [tasks/144_P5NTT07/task.md](tasks/144_P5NTT07/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：coefficient_bound、convolution、crt_coefficients、padded_length）→ 独立验收回源结论
- Difficulty basis: 本题对象是“257×383 有符号卷积的双素数 NTT/CRT 证书”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 coefficient_bound、convolution、crt_coefficients、padded_length、prime_traces。本题的算法与验证负担是：在两个素数下验证原根阶，按 bit-reversal 执行正反 NTT 完成有符号卷积，再用 CRT 唯一重构整数系数。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在两个素数下验证原根阶，按 bit-reversal 执行正反 NTT 完成有符号卷积，再用 CRT 唯一重构整数系数。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 145. `P5ROT11` — 旋转系统、面轨道与曲面亏格证书

- Public statement: [tasks/145_P5ROT11/task.md](tasks/145_P5ROT11/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：dart_head、dart_involution、dart_tail、euler）→ 独立验收回源结论
- Difficulty basis: 本题对象是“旋转系统、面轨道与曲面亏格证书”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 dart_head、dart_involution、dart_tail、euler、face_orbits、vertex_rotations。本题的算法与验证负担是：由每条 dart 的反向配对与顶点循环组成面置换，枚举全部面轨道，再用 V−E+F 计算非平面曲面亏格。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 由每条 dart 的反向配对与顶点循环组成面置换，枚举全部面轨道，再用 V−E+F 计算非平面曲面亏格。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 146. `P5RS25` — 127 长度 Reed–Solomon 完整译码证书

- Public statement: [tasks/146_P5RS25/task.md](tasks/146_P5RS25/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：berlekamp_massey_trace、chien_search_table、corrected_codeword、corrected_syndromes）→ 独立验收回源结论
- Difficulty basis: 本题对象是“127 长度 Reed–Solomon 完整译码证书”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 berlekamp_massey_trace、chien_search_table、corrected_codeword、corrected_syndromes、error_count、error_evaluator、error_locator、error_positions。本题的算法与验证负担是：对长度 127 接收词计算综合，运行 Berlekamp–Massey 和 Chien 搜索，给出错误值并复编码检查纠正码字。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 对长度 127 接收词计算综合，运行 Berlekamp–Massey 和 Chien 搜索，给出错误值并复编码检查纠正码字。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 147. `P5SUB24` — 48 阶群表的完整子群格

- Public statement: [tasks/147_P5SUB24/task.md](tasks/147_P5SUB24/task.md)
- Mathematical domain: 代数学 / 群环域与符号计算
- Structural difficulty: 高
- Certificate: 代数恒等式、正规形、有限域或消元证书
- Representation route: 冻结自然语言/结构化输入 → 群环域与符号计算中的精确表示 → 代数恒等式、正规形、有限域或消元证书（核心公开字段：canonical_generators、completeness_multiplication_checks、exhaustive_generator_closure_trace、hasse_covers）→ 独立验收回源结论
- Difficulty basis: 本题对象是“48 阶群表的完整子群格”；需核验的特有证书结构为 代数恒等式、正规形、有限域或消元证书，公开合同核心项包括 canonical_generators、completeness_multiplication_checks、exhaustive_generator_closure_trace、hasse_covers、subgroup_bitsets、subgroup_count。本题的算法与验证负担是：从 48 阶群表闭包生成每个子群，计算包含关系的传递约简，并逐对验证乘法封闭、逆元与覆盖无遗漏。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 从 48 阶群表闭包生成每个子群，计算包含关系的传递约简，并逐对验证乘法封闭、逆元与覆盖无遗漏。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 148. `P5SYN03` — 48 状态同步自动机的完整幂集 BFS 最短证书

- Public statement: [tasks/148_P5SYN03/task.md](tasks/148_P5SYN03/task.md)
- Mathematical domain: 理论计算机科学 / 自动机、形式语言与程序语义
- Structural difficulty: 高
- Certificate: 形式推导、轨迹、闭包或不可满足性证书
- Representation route: 冻结自然语言/结构化输入 → 自动机、形式语言与程序语义中的精确表示 → 形式推导、轨迹、闭包或不可满足性证书（核心公开字段：first_singleton_distance、subset_bfs、word）→ 独立验收回源结论
- Difficulty basis: 本题对象是“48 状态同步自动机的完整幂集 BFS 最短证书”；需核验的特有证书结构为 形式推导、轨迹、闭包或不可满足性证书，公开合同核心项包括 first_singleton_distance、subset_bfs、word。本题的算法与验证负担是：在 48 状态集合的幂集自动机上 BFS，记录每个子集的父边，直至单元素集合；由层号证明同步词最短。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 48 状态集合的幂集自动机上 BFS，记录每个子集的父边，直至单元素集合；由层号证明同步词最短。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 149. `P5TFV22` — 36 点加权 tournament 反馈顶点集

- Public statement: [tasks/149_P5TFV22/task.md](tasks/149_P5TFV22/task.md)
- Mathematical domain: 离散数学 / 图论与组合算法
- Structural difficulty: 高
- Certificate: 组合结构、上下界相遇或穷尽证书
- Representation route: 冻结自然语言/结构化输入 → 图论与组合算法中的精确表示 → 组合结构、上下界相遇或穷尽证书（核心公开字段：branch_bound_lower_certificate、deleted_vertices、directed_triangles、exact_weight）→ 独立验收回源结论
- Difficulty basis: 本题对象是“36 点加权 tournament 反馈顶点集”；需核验的特有证书结构为 组合结构、上下界相遇或穷尽证书，公开合同核心项包括 branch_bound_lower_certificate、deleted_vertices、directed_triangles、exact_weight、residual_total_order。本题的算法与验证负担是：在 36 点加权 tournament 上做删除集分支界；候选删除后给出拓扑序，下界分支覆盖所有更轻选择。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 36 点加权 tournament 上做删除集分支界；候选删除后给出拓扑序，下界分支覆盖所有更轻选择。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.

## 150. `P5VIT04` — 160 步卷积码 Viterbi 完整 survivor 表证书

- Public statement: [tasks/150_P5VIT04/task.md](tasks/150_P5VIT04/task.md)
- Mathematical domain: 信息与编码 / 编码、压缩与信息论
- Structural difficulty: 高
- Certificate: 编码/译码轨迹、谱或有限域证书
- Representation route: 冻结自然语言/结构化输入 → 编码、压缩与信息论中的精确表示 → 编码/译码轨迹、谱或有限域证书（核心公开字段：branch_metrics、decoded_bits、final_metric、information_bits）→ 独立验收回源结论
- Difficulty basis: 本题对象是“160 步卷积码 Viterbi 完整 survivor 表证书”；需核验的特有证书结构为 编码/译码轨迹、谱或有限域证书，公开合同核心项包括 branch_metrics、decoded_bits、final_metric、information_bits、state_path、survivor_metrics、survivor_predecessors。本题的算法与验证负担是：在 160 个时刻对卷积码状态做 Viterbi 递推，保存每状态度量与 survivor 前驱，回溯消息并重新编码核对路径度量。 结构等级生成规则为“高：H4/P5 新题要求跨表示的完整结构证书、针对性负控与独立重放”。该等级仅依据证书宽度、精确重放和独立验收负担评定，未做模型难度校准。
- Solution outline: 在 160 个时刻对卷积码状态做 Viterbi 递推，保存每状态度量与 survivor 前驱，回溯消息并重新编码核对路径度量。
- Pilot status: PILOT_PENDING
- Answer location: not in the public release; any blind evaluation uses a refreshed private overlay.
