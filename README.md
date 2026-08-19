# Chih-Kai Wang

**B.S. student, Mathematics Education Division, Department of Mathematics and Information Education, National Taipei University of Education. Expected 2028.**

Taipei, Taiwan · [Email](mailto:f0909172434@gmail.com) · [GitHub](https://github.com/f0909172434)

I am interested in **AI for Mathematics, verifiable reasoning, and reproducible research tools**. Much of my current work asks a practical question: when an AI system produces a proof, computation, or other piece of evidence, what can we actually conclude from it, and what still needs to be checked?

## Featured research

### ClaimPromoteBench

**When does evidence justify a stronger research claim?**  
[Repository](https://github.com/f0909172434/claimpromote-bench) · [Manuscript source](https://github.com/f0909172434/claimpromote-bench/tree/paper/v1-submission-prep/technical-report)

ClaimPromoteBench studies whether a requested change in claim status is justified by the evidence already available. Each case asks for one of four actions: `ALLOW`, `HOLD`, `DEMOTE`, or `ESCALATE` under a fixed policy.

Version 1 contains 200 controlled pairs / 400 instances. The primary hidden study uses 150 pairs / 300 instances, two Qwen3 models, four intervention arms, and three seeds, for **24 runs / 7,200 hidden decisions**. The hidden data and exact model prompts were committed before the scored runs, and numerical and formal cases are checked with executable artifacts.

The main result is negative. **5,327 / 7,200 outputs (73.99%) are `FORMAT_ERROR`, and all 1,873 parseable raw model decisions are `ALLOW`.** A deterministic gate prevents invalid promotion among parseable cases, but coverage is low. Because the gate uses the same fixed policy as the benchmark labels, this is a result about rule enforcement, not evidence that the models learned the policy or reasoned better.

A separate blinded audit was completed by two independent human reviewers and did not meet the preregistered pass criterion. I keep that result in the paper rather than changing the benchmark after seeing it.

**Publication status:** the v1 study and manuscript are complete and are in final arXiv / conference submission preparation. I will add the public preprint link after it is actually submitted.

## Selected open-source work

| Project | What it does | Status |
|---|---|---|
| [ClaimPromoteBench](https://github.com/f0909172434/claimpromote-bench) | Tests whether recorded evidence justifies a requested change in research-claim status | v1 hidden study complete; submission preparation |
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
