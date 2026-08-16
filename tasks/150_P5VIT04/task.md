# P5VIT04 — 160 步卷积码 Viterbi 完整 survivor 表证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定输入与数学对象

固定 rate-1/2、memory 4 卷积码及 160 对接收比特，采用整数 Hamming branch metric 和冻结 tie-break。 权威输入为同目录 `input.json`；所有数组使用其中声明的零基索引。
整数必须是 JSON integer；有理数必须编码为约分 `[numerator, denominator]`，其中 denominator > 0。

## 输出合同

artifact.json 必须给出 156 个 information_bits、160 个 decoded_bits、161 个 state_path、完整 branch_metrics[160][16][2]、survivor_metrics 与 survivor_predecessors[161][16]、final_metric。

## 精确验收

裁判重算编码器输出、所有 branch metric、每个 DP cell 与 lexicographic tie-break、终止状态和 traceback。 不接受浮点近似、只给 headline answer、遗漏表项或依赖上游优化器的输出。

## 工具、边界与资源

允许使用任意本地数学/编程工具生成证书；最终验收只读取 `input.json` 与 `artifact.json`，
由 Python 3 标准库精确重放。提交应在 256 MiB 内存和 120 秒内完成验收。

## 表示能力与非同质性

动态规划完整 trace 证书且不依赖浮点似然；不同于只给译码比特。

来源与再发布说明见 `source.json` 和 `license.json`。固定实例、题面与证书 schema 为
ReturnBench 项目原创；上游项目仅作为定义或独立交叉检查来源，没有复制其代码、fixture、
示例或解答。
