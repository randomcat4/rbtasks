# P5LIN10 — 180 阶稀疏有理线性系统的后验误差与模解证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定输入与数学对象

固定 180×180 严格行对角占优稀疏有理系统 Ax=b。提交 dyadic 近似解及严格后验误差证书。 权威输入为同目录 `input.json`；所有数组使用其中声明的零基索引。
整数必须是 JSON integer；有理数必须编码为约分 `[numerator, denominator]`，其中 denominator > 0。

## 输出合同

artifact.json 必须给出 180 个 x_dyadic、精确 residual、全部 dominance_margins、gamma、Varah infinity error_bound，以及三个固定素数上 12 个固定坐标的 modular_solutions。

## 精确验收

裁判以有理数重算 r=b-Ax、全部占优余量与界，并独立模消元核对选定精确解剩余。 不接受浮点近似、只给 headline answer、遗漏表项或依赖上游优化器的输出。

## 工具、边界与资源

允许使用任意本地数学/编程工具生成证书；最终验收只读取 `input.json` 与 `artifact.json`，
由 Python 3 标准库精确重放。提交应在 256 MiB 内存和 120 秒内完成验收。

## 表示能力与非同质性

近似解、严格后验界和模表示的三重证书；不同于普通矩阵求解。

来源与再发布说明见 `source.json` 和 `license.json`。固定实例、题面与证书 schema 为
ReturnBench 项目原创；上游项目仅作为定义或独立交叉检查来源，没有复制其代码、fixture、
示例或解答。
