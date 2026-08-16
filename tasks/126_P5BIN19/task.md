# P5BIN19 — 容量/冲突/同异箱约束的精确装箱证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

`input.json` 是唯一权威输入，并给出生成说明与预规模指标。所有算术和比较均精确；禁止浮点近似。

## artifact.json 合同

必须返回 `certificate_schema.json` 的全部字段且不得增加字段。规范序由共享 verifier 从输入机械确定。

## 精确验收

核验装箱、约束收缩和 PB 源桥，并完整重放少一箱的零解分支搜索。 服务器缺少冻结设计中的 LRAT/VeriPB 工具链，本实现明确改用完整独立可重放的 exact-cover、穷尽、动态规划或 branch-bound 证书，不声称上游证明工具通过，也不调用 solver 作 oracle。

每题同时接受正确工件并拒绝冻结 targeted wrong、第二 mutant 和 additional wrong；资源上限 512 MiB/120 秒。

## 非同质性

本题必须返回完整源表示桥、搜索/递推证书与结构见证，单个最终答案、库函数结果或缺行编码不能通过。

来源、版本、许可用途与再发布边界见 `source.json` 和 `license.json`。
