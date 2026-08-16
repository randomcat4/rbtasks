# P5IIR09 — degree-18 IIR 的 Jury–Schur/Sturm 双路线稳定证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

判断固定 18 次有理分母是否 Schur stable。 同目录 `input.json` 是唯一权威输入；索引约定写在 input。JSON integer 必须精确；有理数必须是约分 `[numerator,denominator]` 且 denominator>0。

## artifact.json 合同

stable、完整 jury_table、schur_rows、strict_margins、固定双线性多项式、完整 sturm_sequence/variations 和 route_agreement。 机器可读字段/形状见 `certificate_schema.json`；不允许额外顶层字段。

## 精确验收

逐行重放 Schur/Jury 严格不等式；核对 z=(1+s)/(1-s) 变换和 Sturm 的18个负实根计数，两路线必须一致。 裁判只使用 Python 3 标准库整数和 Fraction，不接受浮点近似、最终标签替代完整 trace、遗漏表项或上游 solver 作为 oracle。

允许任意工具生成证书；验收资源上限为 512 MiB/120 秒。

## 非同质性

双精确稳定见证，不是根近似或单一路线标签。

实例、题面和 schema 为 ReturnBench 项目原创。`source.json` 中的上游版本仅作定义/交叉检查来源；没有复制其代码、fixture、数据或解答。
