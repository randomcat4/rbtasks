# P5FAC23 — 18 设施、60 客户的容量设施选址

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

`input.json` 是唯一权威输入，包含冻结规模与最快证伪说明。所有运算精确，不接受浮点近似。

## artifact.json 合同

必须恰好返回 `certificate_schema.json` 的字段；规范序由 verifier 从输入确定。

## 精确验收

核验开设、分配、容量与成本表，并重放全部设施子集及精确最小费用流下界搜索。 服务器没有 PB/GAP 运行工具，本实现只使用 Python 标准库完整独立重算闭包或分支定界，不声称任何外部工具通过。

good、targeted wrong、第二 mutant、additional wrong 均双重重放；限制 512 MiB/120 秒。

## 非同质性

必须返回完整表示桥和中间证书；单个最终值、调用库函数或缺行轨迹均拒绝。

来源、许可与再发布边界见 `source.json`、`license.json`。
