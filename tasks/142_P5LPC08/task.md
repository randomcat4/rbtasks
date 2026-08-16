# P5LPC08 — 192 点 order-24 LPC 的完整 Levinson 有理递推证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

对固定整数信号执行精确 Levinson–Durbin。 同目录 `input.json` 是唯一权威输入；索引约定写在 input。JSON integer 必须精确；有理数必须是约分 `[numerator,denominator]` 且 denominator>0。

## artifact.json 合同

25 个 autocorrelations、24 个 reflection_coefficients、25 行 ar_rows、25 个 prediction_errors、final_coefficients 和 Yule–Walker residuals。 机器可读字段/形状见 `certificate_schema.json`；不允许额外顶层字段。

## 精确验收

逐步重算有理递推，要求所有分母非零、误差严格为正，并核对最终方程。 裁判只使用 Python 3 标准库整数和 Fraction，不接受浮点近似、最终标签替代完整 trace、遗漏表项或上游 solver 作为 oracle。

允许任意工具生成证书；验收资源上限为 512 MiB/120 秒。

## 非同质性

完整中间递推表，不同于浮点 LPC 最终系数。

实例、题面和 schema 为 ReturnBench 项目原创。`source.json` 中的上游版本仅作定义/交叉检查来源；没有复制其代码、fixture、数据或解答。
