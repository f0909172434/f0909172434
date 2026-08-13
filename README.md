# Chih-Kai Wang

**Undergraduate mathematics researcher working on nonlinear analysis, AI for Mathematics, and auditable research systems.**

[Email](mailto:f0909172434@gmail.com) · [ProofWeave](https://github.com/f0909172434/proofweave-math-lab) · [RigorGraph](https://github.com/f0909172434/rigorgraph) · [HonestCI](https://github.com/f0909172434/honest-ci) · Taipei, Taiwan

I study bifurcation and multiplicity in nonlinear boundary-value problems. I also build open-source tools that make mathematical claims, computation, evidence, and verification easier to inspect and reproduce.

> Model agreement is not proof, numerical evidence is not a theorem, and promoted claims should have traceable dependencies and independent checks.

## Choose an entry point

| If you need to... | Start with | What it checks | Current release |
|---|---|---|---|
| Stop a green CI job when expected tests did not actually run | [HonestCI](https://github.com/f0909172434/honest-ci) | Fresh JUnit XML, minimum and baseline test counts, failures, skipped-test limits, and suspicious workflow patterns | Stable [`1.0.4`](https://github.com/f0909172434/honest-ci/releases/tag/v1.0.4) |
| Keep research claims, evidence, dependencies, and independent reviews auditable | [RigorGraph](https://github.com/f0909172434/rigorgraph) | Schemas, graph integrity, evidence hashes and classes, reviewer independence, and invalid status promotion | Public beta [`1.0.1`](https://github.com/f0909172434/rigorgraph/releases/tag/v1.0.1) |
| Turn a mathematical statement and proof into a deterministic proof spine with optional Lean certification | [ProofWeave Core v2](https://github.com/f0909172434/proofweave-math-lab) | Structured proof coverage, an allowlisted Lean certificate, and hash-bound human/formal alignment | Repository preview [`v0.1.0`](https://github.com/f0909172434/proofweave-math-lab/releases/tag/v0.1.0); runtime/protocol `2.0.0` |

These projects share a verification-first philosophy, but they are not one coupled platform. HonestCI can emit an **Evidence Bundle v1** that RigorGraph validates and preserves; importing that bundle does not verify a research claim. ProofWeave is a separate, model-independent core for structured mathematical proofs and Lean-backed certificates.

## Try the tools

### Verify that CI really ran its tests

HonestCI wraps your existing JUnit-producing test command. A definite missing, stale, empty, reduced, or failing report blocks the run. After adding the [quick-start configuration](https://github.com/f0909172434/honest-ci#five-minute-quick-start):

```console
npm install --save-dev honest-ci@1.0.4
npx honest-ci run --config honest-ci.yml -- npm test -- --reporter=default --reporter=junit --outputFile.junit=reports/junit.xml
```

[Five-minute Action setup](https://github.com/f0909172434/honest-ci#five-minute-quick-start) · [Runner recipes](https://github.com/f0909172434/honest-ci/blob/main/docs/RUNNER_RECIPES.md) · [Finding codes](https://github.com/f0909172434/honest-ci/blob/main/docs/FINDINGS.md)

### Audit a claim-evidence graph offline

RigorGraph creates version-controlled JSONL records and a self-contained HTML report. It runs locally without an account, API key, telemetry, or model call.

```console
python -m pip install "rigorgraph==1.0.1"
rigorgraph demo --scenario math --open
```

[Three-minute quick start](https://github.com/f0909172434/rigorgraph#quick-start-three-minutes) · [Audit rules](https://github.com/f0909172434/rigorgraph#what-the-audit-enforces) · [Evidence bundles](https://github.com/f0909172434/rigorgraph/blob/main/docs/EVIDENCE_BUNDLES.md)

### Run a structured mathematical proof through ProofWeave

ProofWeave reads deterministic TOML + Markdown and can check a restricted Lean certificate. Its runtime contains no agents, providers, model router, or LLM calls. From a cloned repository root:

```console
python -m pip install --no-deps --editable .
lake update mathlib
lake exe cache get
python -m proofweave init
python -m proofweave run examples/simple_ring/theorem.md
```

The full path requires the repository-pinned Lean `4.32.2` and Mathlib `4.32.2` toolchain. `CERTIFIED` covers the formal target and deductive coverage; it does not by itself establish that the natural-language statement has the same meaning. Record `--confirm-alignment` only after a human compares the exact statement, quantifiers, assumptions, dependencies, and formal target. See the [Core usage and trust model](https://github.com/f0909172434/proofweave-math-lab/blob/main/README.en.md).

## How the verification layers differ

| Project | Primary inputs | Deterministic outputs | Explicit non-guarantee |
|---|---|---|---|
| HonestCI | Test command, JUnit XML, committed baseline, workflow YAML | Findings, exit code, annotations, Evidence Bundle v1 | Does not prove test quality, coverage, or program correctness |
| RigorGraph | YAML config plus claim, evidence, and verification JSONL | Audit codes, dependency graph, offline report | `VERIFIED` records workflow acceptance, not absolute truth or formal proof |
| ProofWeave | TOML + Markdown theorem, proof steps, optional Lean block | Proof spine, concept map, coverage, Lean result, orthogonal statuses | Does not generate a globally simplest proof or prove natural-language/formal equivalence |

## Technical focus

- **Mathematics:** nonlinear boundary-value problems, exact time-map methods, bifurcation geometry, multiplicity, and computer-assisted verification.
- **Research infrastructure:** dependency-closed evidence, content hashes, independent review records, explicit unresolved states, and reproducible release gates.
- **Implementation:** Python, TypeScript, Pydantic/JSON Schema, JUnit XML, self-contained HTML, GitHub Actions, SymPy, LaTeX, and Lean 4.
- **Trust boundaries:** deterministic tools can reject malformed or insufficient evidence; domain experts and proof-assistant kernels remain responsible for the claims within their scope.

My current research manuscript is in preparation. Unresolved statements remain marked as open rather than being presented as established theorems. I welcome research and internship discussions in applied mathematics, formal reasoning, AI4Math, and trustworthy research automation.

<details>
<summary><strong>中文簡介</strong></summary>

我是台灣的大學生數學研究者，研究非線性邊值問題、分岔與多解性，也開發可稽核的 AI 輔助研究工具。

- **HonestCI** 以 JUnit 證據檢查測試是否真的執行，降低「假綠燈」風險。
- **RigorGraph** 將主張、證據、相依關係與獨立審查保存成可版本控制、可離線稽核的圖。
- **ProofWeave Core v2** 讀取結構化數學命題與證明，輸出 proof spine、coverage，以及可用時的受限 Lean 認證。

我的核心原則是清楚區分猜想、數值證據、工作流程驗證、形式認證與數學證明，並如實保留尚未解決的邊界。

</details>
