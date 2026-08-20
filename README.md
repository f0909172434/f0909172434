# Chih-Kai Wang

**B.S. student, Mathematics Education Division, Department of Mathematics and Information Education, National Taipei University of Education. Expected 2028.**

Taipei, Taiwan · [Email](mailto:f0909172434@gmail.com) · [GitHub](https://github.com/f0909172434)

I am interested in **AI for Mathematics, verifiable reasoning, and reproducible research tools**. Much of my current work asks a practical question: when an AI system produces a proof, computation, review, or other piece of evidence, what can we actually conclude from it, and what still needs to be checked?

## Featured research

### ClaimPromoteBench

**When does evidence justify a stronger research claim?**  
[Repository](https://github.com/f0909172434/claimpromote-bench) · [Revised manuscript source](https://github.com/f0909172434/claimpromote-bench/tree/agent/iclr2027-v2-low-cost-study/technical-report)

ClaimPromoteBench studies whether a requested change in claim status is justified by the evidence already available. Each case asks for one of four actions: `ALLOW`, `HOLD`, `DEMOTE`, or `ESCALATE` under a fixed policy.

Version 1 contains 200 controlled pairs / 400 instances. The primary hidden study uses 150 pairs / 300 instances, two Qwen3 models, four intervention arms, and three seeds, for **24 runs / 7,200 hidden decisions**. The hidden data and exact model prompts were committed before scored inference, and numerical and formal cases are tied to executable artifacts.

The primary result is negative. **5,327 / 7,200 outputs (73.99%) are `FORMAT_ERROR`, and all 1,873 parseable raw decisions are `ALLOW`.** A deterministic gate prevents invalid promotion among parseable cases, but coverage is low. Because the gate uses the same fixed policy as the benchmark labels, this is evidence about rule enforcement rather than evidence that the models learned the policy or reasoned better.

I then ran a separately labeled **post-v1 public formatting-control pilot** with the same two model artifacts and identical model-facing prompts under free versus JSON-schema-constrained decoding. The constraint raises coverage from 0.75 to 1.00 for Qwen3-0.6B and from 0 to 0.95 for Qwen3-1.7B. However, all **78 / 80 constrained parseable decisions remain `ALLOW`**, and raw controlled-pair accuracy and decision-flip rate remain zero over **38 / 40 complete pairs**. For these two small models on the public controlled set, fixing the output contract does not recover sensitivity to the decisive evidence change.

The submission does not rely on a human annotation study. Its labels are deterministic outputs of a published versioned policy, so they are policy-conformance labels rather than claims about universal human judgment. Credibility instead comes from a committed hidden test, complete artifact-bound run matrices, no-inference recovery, an audit of all 20 public pair contracts, exact-rational and pinned-Lean replay, shortcut and metamorphic checks, a controlled formatting intervention, and an anonymous bundle that reruns the public checks. I keep the author-defined-policy, small-model, synthetic-data, public-pilot, and post-v1 limitations explicit.

**Publication status:** the revised ICLR/arXiv packages are in final verification. The manuscript uses the official ICLR style and is constrained by an automated 9-page main-text gate, citation/overflow/anonymity checks, machine-readable result bindings, and page-by-page visual review. No human-subject study is included. The remaining steps are account-side arXiv/OpenReview submission and the final archival release. I will add an arXiv or conference link only after it actually exists.

## Selected open-source work

| Project | What it does | Status |
|---|---|---|
| [ClaimPromoteBench](https://github.com/f0909172434/claimpromote-bench) | Tests whether typed scientific evidence justifies a requested change in research-claim status, separating structured-output coverage, raw decision sensitivity, and deterministic enforcement | v1 hidden study and post-v1 public formatting control complete; technical submission verification |
| [ProofWeave Core v2](https://github.com/f0909172434/proofweave-math-lab) | Parses mathematical claims and proofs and checks Lean/Mathlib certificates while keeping certificate validity separate from natural-language scope | Repository release `v0.1.0`; Core package `2.0.0` |
| [RigorGraph](https://github.com/f0909172434/rigorgraph) | Tracks claims, evidence, provenance, and deterministic checks in a local-first workflow | Public beta; package `1.0.1` |
| [HonestCI](https://github.com/f0909172434/honest-ci) | Detects missing, stale, zero-test, and unexpectedly reduced JUnit evidence in CI | Stable package and GitHub Action; `1.0.4` |

## Research interests

`AI for Mathematics` · `automated theorem proving` · `autoformalization` · `verifiable research agents` · `AI evaluation` · `reproducible scientific computing` · `nonlinear differential equations` · `bifurcation theory`

## Technical stack

`Python` · `TypeScript` · `SymPy` · `LaTeX` · `JSON Schema` · `GitHub Actions` · `Lean 4 / Mathlib (developing)`

## CV and collaboration

- [One-page CV](cv/Chih-Kai-Wang-CV.pdf) — updated August 2026.
- I am preparing for research-based graduate study and looking for opportunities in AI4Math, theorem proving, verifiable research agents, and AI evaluation.
- For research, internship, or open-source collaboration: [f0909172434@gmail.com](mailto:f0909172434@gmail.com).
