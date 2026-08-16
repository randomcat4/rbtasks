# P5ISO01 — 固定加权有理等序回归的 PAVA/KKT 双证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定输入与数学对象

长度 96 的整数观测与正整数权重。求加权平方误差最小的非降有理拟合。 权威输入为同目录 `input.json`；所有数组使用其中声明的零基索引。
整数必须是 JSON integer；有理数必须编码为约分 `[numerator, denominator]`，其中 denominator > 0。

## 输出合同

artifact.json 必须给出 fit（96 个约分有理数）、覆盖 [0,96) 的 maximal blocks（start/end/sum_w/sum_wy/mean）、95 个 dual_multipliers，以及相等的 objective 与 dual_objective。

## 精确验收

裁判精确检查分块加权均值、严格递增的相邻块均值、单调性、KKT stationarity、非负性、complementary slackness 与目标值。 不接受浮点近似、只给 headline answer、遗漏表项或依赖上游优化器的输出。

## 工具、边界与资源

允许使用任意本地数学/编程工具生成证书；最终验收只读取 `input.json` 与 `artifact.json`，
由 Python 3 标准库精确重放。提交应在 256 MiB 内存和 120 秒内完成验收。

## 表示能力与非同质性

PAVA 块表示与 KKT 对偶之间的返回证书；不同于通用 LP 最终值。

来源与再发布说明见 `source.json` 和 `license.json`。固定实例、题面与证书 schema 为
ReturnBench 项目原创；上游项目仅作为定义或独立交叉检查来源，没有复制其代码、fixture、
示例或解答。
