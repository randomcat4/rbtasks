# P5HAM15 — 非 Hamilton 图的 successor-CNF 与子集递推不可行证书

状态：`RELEASE_READY`（公开任务库）；四臂 Pilot 资格单独记录。

## 固定对象

同目录 `input.json` 是唯一权威输入，所有编号、规范序和桥接规则均在其中冻结。只允许精确 JSON 整数、数组、布尔值和字符串；不接受浮点近似。

## artifact.json 合同

必须返回 `certificate_schema.json` 列出的全部顶层字段，禁止额外字段。所有列表都使用 `input.json` 给定的规范序；等价但非规范的重排不接受，以保证可重放与确定性。

## 精确验收

重建完整 exactly-one 与防子环 CNF，并逐状态重放 Held–Karp 可达端点表，验证满集无闭合端点。 裁判只使用 Python 标准库从公开输入独立重算，不读取参考答案，不调用上游求解器。遗漏中间表、只给最终数、别名字段或非规范结构均拒绝。
本冻结实现采用完整 Held–Karp 子集递推作为与 LRAT 等价的独立可检查不可行证书；服务器没有可用 LRAT 工具链，故不声称生成或重放 LRAT。

验收资源上限为 512 MiB/120 秒；允许任意工具生成证书。

## 非同质性

不用 SAT 求解器作 oracle；同时检查图到 CNF 的精确桥接和独立可重放不可行证书。

实例、题面和 schema 为 ReturnBench 项目原创；来源、版本、许可用途与再发布边界见 `source.json` 和 `license.json`。
