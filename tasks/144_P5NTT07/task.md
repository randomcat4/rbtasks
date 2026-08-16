# P5NTT07 — 257×383 有符号卷积的双素数 NTT/CRT 证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

对两条固定整数序列求长度 639 的精确卷积，padding 为 1024。 同目录 `input.json` 是唯一权威输入；索引约定写在 input。JSON integer 必须精确；有理数必须是约分 `[numerator,denominator]` 且 denominator>0。

## artifact.json 合同

padded_length、coefficient_bound、两条 prime_traces（root、全部 forward/pointwise/inverse stages）、639 个 crt_coefficients 和 convolution。 机器可读字段/形状见 `certificate_schema.json`；不允许额外顶层字段。

## 精确验收

检查 N 次单位根的精确阶、bit reversal、每个 butterfly、逆变换、signed CRT 唯一界和全量 schoolbook 卷积。 裁判只使用 Python 3 标准库整数和 Fraction，不接受浮点近似、最终标签替代完整 trace、遗漏表项或上游 solver 作为 oracle。

允许任意工具生成证书；验收资源上限为 512 MiB/120 秒。

## 非同质性

时域、频域、模域三重表示，明显强于小型 DFT。

实例、题面和 schema 为 ReturnBench 项目原创。`source.json` 中的上游版本仅作定义/交叉检查来源；没有复制其代码、fixture、数据或解答。
