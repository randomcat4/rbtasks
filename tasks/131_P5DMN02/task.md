# P5DMN02 — 73 状态 DFA 的可达最小商与逐对区分词证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定输入与数学对象

固定 73 状态、6 字母、完整且可达的 DFA；提交其 Myhill–Nerode 最小商。 权威输入为同目录 `input.json`；所有数组使用其中声明的零基索引。
整数必须是 JSON integer；有理数必须编码为约分 `[numerator, denominator]`，其中 denominator > 0。

## 输出合同

artifact.json 必须给出 old_to_quotient、quotient_transitions、quotient_accepting、从 final/nonfinal 初分开始的全部 canonical refinement_rounds、73 个 reachability_parents，以及按 p<q 排序的所有商状态对 distinguishing_words。

## 精确验收

裁判重算细化不动点、同态与终态一致性，追溯每个旧状态的可达父边，并重放每个区分词。 不接受浮点近似、只给 headline answer、遗漏表项或依赖上游优化器的输出。

## 工具、边界与资源

允许使用任意本地数学/编程工具生成证书；最终验收只读取 `input.json` 与 `artifact.json`，
由 Python 3 标准库精确重放。提交应在 256 MiB 内存和 120 秒内完成验收。

## 表示能力与非同质性

显式 quotient representation、可达性和逐对最小性证书；不同于单个 DFA 反例。

来源与再发布说明见 `source.json` 和 `license.json`。固定实例、题面与证书 schema 为
ReturnBench 项目原创；上游项目仅作为定义或独立交叉检查来源，没有复制其代码、fixture、
示例或解答。
