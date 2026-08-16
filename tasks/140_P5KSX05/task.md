# P5KSX05 — 137×149 双样本 KS 尾概率的格路/CRT 证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

对固定无并列两样本精确计算双侧 P(D≥D_obs)。 同目录 `input.json` 是唯一权威输入；索引约定写在 input。JSON integer 必须精确；有理数必须是约分 `[numerator,denominator]` 且 denominator>0。

## artifact.json 合同

statistic、完整 forbidden[138][150]、三个固定模数的完整 dp_mod 表、CRT safe/total/tail 计数和约分 probability。 机器可读字段/形状见 `certificate_schema.json`；不允许额外顶层字段。

## 精确验收

重算秩统计、严格安全边界、全部模递推、CRT 唯一性和概率。 裁判只使用 Python 3 标准库整数和 Fraction，不接受浮点近似、最终标签替代完整 trace、遗漏表项或上游 solver 作为 oracle。

允许任意工具生成证书；验收资源上限为 512 MiB/120 秒。

## 非同质性

精确格路径与多模表示，不同于置换检验最终小数。

实例、题面和 schema 为 ReturnBench 项目原创。`source.json` 中的上游版本仅作定义/交叉检查来源；没有复制其代码、fixture、数据或解答。
