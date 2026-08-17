# ReturnBench-150

[![Release](https://img.shields.io/badge/release-v1.0.1-2F6F4E)](https://github.com/randomcat4/rbtasks/releases/tag/v1.0.1)
[![Tasks](https://img.shields.io/badge/tasks-150-3056D3)](RELEASE_TASKS.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

ReturnBench-150 is an open, reproducible benchmark of **150 mathematical representation and
certificate tasks**. It tests whether a system can transform a mathematical object into an explicit
representation and return a checkable certificate—not merely a final scalar answer.

Each task is published as a self-contained contract with its statement, metadata, provenance, and
the public input/output files needed for development and replay. The collection spans discrete
mathematics, algebra, geometry, probability and statistics, optimization, theoretical computer
science, coding, numerical analysis, signal processing, mathematical physics, and control.

> **This is the public task bank, not a contamination-free hidden evaluation.** Reference answers,
> administrator controls, sham definitions, arm assignments, private judges, and raw evaluation logs
> are deliberately excluded. Blind or Pilot measurements require a separately maintained,
> refreshed private overlay.

## Release at a glance

| Item | Value |
|---|---:|
| Public tasks | 150 |
| Structurally medium | 29 |
| Structurally medium-high | 51 |
| Structurally high | 70 |
| Pilot-eligible public contracts | 80 |
| Pilot-held existing contracts | 10 |
| Pilot-pending public contracts | 60 |
| Frozen source revision | `e59f784e38302353b5ac57685d4ffcde428c26b2` |
| Public release | [`v1.0.1`](https://github.com/randomcat4/rbtasks/releases/tag/v1.0.1) |

Difficulty labels describe certificate width, exact replay, and verification burden. They are
curator assessments, not measured model-performance scores.

## Start here

- [Browse all 150 tasks](CATALOG.md)
- [Read the task-by-task guide](TASK_GUIDE.md)
- [Load the machine-readable release index](RELEASE_TASKS.json)
- [Load the machine-readable task guide](TASK_GUIDE.json)
- [Understand the benchmark design](DESIGN.md)
- [Read the dataset card](DATASET_CARD.md)
- [Review the publication boundary](PUBLICATION_BOUNDARY.md)
- [Check provenance and third-party terms](THIRDPARTY.md)

## Task families

The release uses progressively richer public contracts:

| Ordinals | Family | Public package shape |
|---|---|---|
| 001–090 | Baseline | Statement, metadata, provenance, and task-specific public inputs or submission schemas where required |
| 091–125 | H4 | Exact input plus a structured output schema for a multi-field certificate |
| 126–150 | P5 | Full certificate package with input, schema, source, license, package, provenance, and verifier descriptors |

All 150 packages contain `task.md`, `metadata.json`, and `provenance.json`. Across the release,
116 tasks include `input.json`; the contract-specific schema is named `submission.schema.json`,
`output_schema.json`, or `certificate_schema.json` according to the task family. The 25 P5 tasks
also publish `verifier.json`, with shared public judge implementations under
[`verifiers/p5/`](verifiers/p5/).

## Repository layout

```text
.
├── tasks/                    # 150 numbered public task packages
│   ├── 001_LCSP-01/
│   ├── 091_H4AIF34/
│   └── 150_P5VIT04/
├── verifiers/p5/             # shared public P5 certificate judges
├── RELEASE_TASKS.json        # canonical release index
├── TASK_GUIDE.md             # human-readable guide to every task
├── TASK_GUIDE.json           # machine-readable guide
├── CATALOG.md                # compact task catalog
├── DESIGN.md                 # representation-to-certificate design
├── DATASET_CARD.md           # intended uses and limitations
└── PUBLICATION_BOUNDARY.md    # explicit public/private separation
```

## Use the dataset

Clone the frozen public task bank:

```bash
git clone --branch v1.0.1 https://github.com/randomcat4/rbtasks.git
cd rbtasks
```

Load the release index with only the Python standard library:

```python
import json
from pathlib import Path

root = Path(".")
release = json.loads((root / "RELEASE_TASKS.json").read_text(encoding="utf-8"))

assert release["schema"] == "returnbench-public-release-v1"
assert release["count"] == len(release["tasks"]) == 150

first = release["tasks"][0]
statement = (root / first["task_file"]).read_text(encoding="utf-8")
print(first["task_id"], first["release_status"])
print(statement)
```

To work on one task:

1. Find it in [`RELEASE_TASKS.json`](RELEASE_TASKS.json) or [`CATALOG.md`](CATALOG.md).
2. Read its `task.md` and treat the listed input/schema files as the complete public contract.
3. Produce the requested Lean file or JSON certificate exactly as specified.
4. Validate against the published schema or verifier when one is included.
5. Keep every reference answer and private evaluation control outside this repository.

## What the benchmark measures

Every task follows the same high-level route:

```text
source mathematical object
  -> explicit representation transform
  -> checkable certificate
  -> independently recoverable source conclusion
```

Accepted certificate forms include proof terms, exact witnesses, primal/dual pairs, recurrences,
residual bounds, complete search traces, and independently replayable structural certificates.
Tasks that only rename a library theorem, change constants, or collapse to a one-line wrapper are
outside the release design.

## Public and private boundaries

Included here:

- statements and public inputs;
- output and certificate schemas;
- structural difficulty and non-answer solution outlines;
- public verifier descriptors and shared P5 judges;
- provenance and licensing records.

Excluded from this repository:

- correct or incorrect reference artifacts;
- targeted controls and sham-break definitions;
- hidden judges and administrator-only checks;
- arm prompts, assignments, server paths, credentials, and raw logs;
- private evaluation instances.

Previously exposed evaluation material cannot be made secret again by rewriting Git history. Future
blind results therefore require fresh private instances rather than reuse of this public task bank.

## Reproducibility and versioning

[`RELEASE_TASKS.json`](RELEASE_TASKS.json) is the canonical ordered index for the 150-task release.
Task packages declare their release and Pilot status independently: public release readiness means
the statement, provenance, license boundary, and certificate contract passed review; Pilot
eligibility additionally depends on a fresh private evaluation package that is not distributed here.

Use the `v1.0.1` tag for a stable snapshot. The source-freeze commit records the reviewed assembly
lineage; it is not a location from which private evaluation material should be recovered.

## Contributing

Contributions may repair or extend public task contracts, but must not add answers, hidden controls,
arm assignments, credentials, absolute machine paths, or raw evaluation logs. A new task requires a
self-contained statement, an explicit input/output contract, provenance, license analysis, a
positive certificate maintained through the review process, targeted negative controls kept outside
the public package, and a non-duplication/difficulty review. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Project-original code, prose, generated instances, and documentation are available under the
[`MIT License`](LICENSE). Third-party material retains its upstream terms and attribution; consult
[`THIRDPARTY.md`](THIRDPARTY.md) and each task's provenance and license records before reuse.
