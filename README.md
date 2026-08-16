# ReturnBench-150

ReturnBench-150 is an open, reproducible benchmark of **150 mathematical representation and
certificate tasks**. Every public package contains a self-contained statement and its declared
input/output contract. The collection tests whether a system can transform a mathematical object
between representations and return a checkable certificate rather than only a final scalar answer.

This repository is the **public task bank**, not a contamination-free hidden evaluation. Reference
answers, targeted controls, sham construction, per-run arm assignments, private judge material and
raw server logs are deliberately absent. Blind four-arm/Pilot measurements must use a separately
maintained, refreshed private evaluation overlay.

## Start here

- [150-task catalog](CATALOG.md)
- [Machine-readable release index](RELEASE_TASKS.json)
- [Per-task domains, difficulty and solution outlines](TASK_GUIDE.md)
- [Machine-readable task guide](TASK_GUIDE.json)
- [Design](DESIGN.md)
- [Dataset card](DATASET_CARD.md)
- [Publication boundary](PUBLICATION_BOUNDARY.md)
- [Third-party notices](THIRDPARTY.md)

## Composition

- Task count: **150 exactly**
- Difficulty distribution: {"中": 29, "中高": 51, "高": 70}
- Mathematical-domain distribution: {"代数学": 20, "信息与编码": 10, "几何学": 11, "应用数学": 8, "数值与信号": 8, "数学物理": 7, "数论": 2, "概率统计": 13, "理论计算机科学": 19, "离散数学": 38, "系统与控制": 5, "运筹与优化": 9}
- Source freeze: `e59f784e38302353b5ac57685d4ffcde428c26b2`
- Project-original material: MIT
- Third-party material: retains its upstream license

## Package layout

Each directory under `tasks/` contains a normalized `task.md`, the public input/schema files listed
by the frozen release manifest, `metadata.json`, and a public provenance projection. Some formal
tasks are checked directly by their proof assistant kernel. The private Pilot overlay is not part of
this repository and is not required to read or reuse the public task bank.

No model score is claimed by this release. Structural difficulty is a curator assessment, not a
measured model calibration.
