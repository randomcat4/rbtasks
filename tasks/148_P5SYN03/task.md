# P5SYN03 — 48 状态同步自动机的完整幂集 BFS 最短证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定输入与数学对象

固定 48 状态、3 字母完整 DFA；给出最短同步词。 权威输入为同目录 `input.json`；所有数组使用其中声明的零基索引。
整数必须是 JSON integer；有理数必须编码为约分 `[numerator, denominator]`，其中 denominator > 0。

## 输出合同

artifact.json 必须给出 word，以及从全状态 48-bit mask 开始、按 FIFO 和字母 0,1,2 顺序生成、直到首个 singleton layer 的完整 subset_bfs；每行含 mask/distance/parent/symbol。

## 精确验收

裁判独立重建整个可达子集 BFS，逐行比较距离与前驱，确认更早层无 singleton，并重放同步词。 不接受浮点近似、只给 headline answer、遗漏表项或依赖上游优化器的输出。

## 工具、边界与资源

允许使用任意本地数学/编程工具生成证书；最终验收只读取 `input.json` 与 `artifact.json`，
由 Python 3 标准库精确重放。提交应在 256 MiB 内存和 120 秒内完成验收。

## 表示能力与非同质性

幂集状态表示和全层最短性证书；不同于普通 DFA 等价或只给同步词。

来源与再发布说明见 `source.json` 和 `license.json`。固定实例、题面与证书 schema 为
ReturnBench 项目原创；上游项目仅作为定义或独立交叉检查来源，没有复制其代码、fixture、
示例或解答。
