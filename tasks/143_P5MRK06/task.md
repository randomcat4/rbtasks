# P5MRK06 — 64+5 状态吸收链的有理解/模重构证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

固定 64 个 transient、5 个 absorbing class 的稀疏有理 Markov 链。 同目录 `input.json` 是唯一权威输入；索引约定写在 input。JSON integer 必须精确；有理数必须是约分 `[numerator,denominator]` 且 denominator>0。

## artifact.json 合同

hitting_times[64]、absorption_probabilities[64][5]、三个 modular_tables 和 reconstruction_bounds。 机器可读字段/形状见 `certificate_schema.json`；不允许额外顶层字段。

## 精确验收

检查随机行、(I-Q)h=1、(I-Q)B=R、边界概率、非奇异模 trace 与有理重构唯一界。 裁判只使用 Python 3 标准库整数和 Fraction，不接受浮点近似、最终标签替代完整 trace、遗漏表项或上游 solver 作为 oracle。

允许任意工具生成证书；验收资源上限为 512 MiB/120 秒。

## 非同质性

精确线性系统返回证书，不同于 HMM 或单个期望值。

实例、题面和 schema 为 ReturnBench 项目原创。`source.json` 中的上游版本仅作定义/交叉检查来源；没有复制其代码、fixture、数据或解答。
