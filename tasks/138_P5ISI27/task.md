# P5ISI27 — 宽 10、长 40 的周期边界 Ising 传递证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

`input.json` 是唯一权威输入，明确冻结整数或有限域对象、规模和边界条件。所有验收使用精确算术。

## artifact.json 合同

必须恰好返回 `certificate_schema.json` 的顶层字段和完整中间证书；禁止省略行或仅返回最终值。

## 精确验收

用因子化整数传递独立重算每列 1024 状态向量、边界权与自旋反转对称。 验证器只使用 Python 标准库独立重算，不调用上游求解器作为 oracle。

good、targeted wrong、第二 mutant、additional wrong 各双重重放；限制 512 MiB/120 秒。

## 非同质性

本题验收跨表示的完整中间轨迹或全场证书，不是一行库定理、最终浮点数或只换常数的包装。

来源、许可和再发布边界见 `source.json` 与 `license.json`。
