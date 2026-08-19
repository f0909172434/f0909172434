# Chih-Kai Wang

**B.S. student, Mathematics Education Division, Department of Mathematics and Information Education, National Taipei University of Education. Expected 2028.**

Taipei, Taiwan · [Email](mailto:f0909172434@gmail.com) · [GitHub](https://github.com/f0909172434)

I work on **AI for Mathematics, verifiable reasoning, and reproducible research engineering**. My current focus is the boundary between probabilistic AI systems and machine-checkable research workflows: what evidence a model may legitimately promote, what a verifier can certify, and what must remain explicitly unresolved.

> Model agreement is not proof. Numerical evidence is not a theorem. A verified artifact establishes only the claim and scope it actually checks.

## Featured research

### ClaimPromoteBench

**Policy-Governed Evidence-State Transitions for Mathematical Research Agents**  
[Repository](https://github.com/f0909172434/claimpromote-bench) · [Manuscript source](https://github.com/f0909172434/claimpromote-bench/tree/paper/v1-submission-prep/technical-report)

ClaimPromoteBench studies a narrow research-agent governance problem: given a claim, typed evidence, a current evidence state, and a requested transition, should the system `ALLOW`, `HOLD`, `DEMOTE`, or `ESCALATE` under a frozen policy?

**Version 1 is now experimentally complete:**

- 200 controlled pairs / 400 benchmark instances across 20 policy factors;
- 50-pair public development split and 150-pair / 300-instance committed hidden primary test;
- 2 Qwen3 models × 4 intervention arms × 3 seeds = **24 runs / 7,200 hidden decisions**;
- hidden dataset and exact model-facing prompts cryptographically committed before scored inference;
- executable exact-rational numerical artifacts and pinned Lean artifacts;
- supplementary blinded policy audit by two real independent reviewers;
- artifact-only recovery preserved the frozen inference matrix without re-querying the models or rewriting valid decisions.

The main result is deliberately negative and useful: **5,327 / 7,200 outputs (73.99%) are `FORMAT_ERROR`, and all 1,873 parseable raw model intents request `ALLOW`.** A deterministic transition gate eliminates measured false promotion among parseable covered decisions, but coverage remains low. The conclusion is therefore about **system-level enforcement**, not improved model reasoning or calibration.

**Publication status:** the v1 manuscript and artifact-bound results are complete; arXiv and ICLR 2027 submission packages are undergoing final automated compilation, anonymity, page-limit, citation, and PDF checks. I will add the public preprint identifier after submission rather than pre-announce one.

## Selected open-source work

| Project | What it does | Status |
|---|---|---|
| [ClaimPromoteBench](https://github.com/f0909172434/claimpromote-bench) | Preregistered controlled-pair benchmark for policy-governed evidence-state transitions, separating raw model intent from deterministic enforcement | v1 primary hidden study complete; submission preparation |
| [ProofWeave Core v2](https://github.com/f0909172434/proofweave-math-lab) | Model-independent parsing of mathematical claims and proofs; deterministic Lean/Mathlib certificate checks; separates certificate, natural-language alignment, and lifecycle state | Repository release `v0.1.0`; Core package `2.0.0` |
| [RigorGraph](https://github.com/f0909172434/rigorgraph) | Local-first claim-evidence graphs, deterministic audits, provenance/hash checks, and offline reports | Public beta; package `1.0.1` |
| [HonestCI](https://github.com/f0909172434/honest-ci) | Checks fresh JUnit evidence and detects missing, stale, zero-test, and reduced-count results in CI | Stable package and GitHub Action; `1.0.4` |

These projects are built around explicit evidence boundaries. A green CI run, numerical scan, formal certificate, reviewer decision, or model output is never silently promoted into a broader claim than it supports.

## Research interests

`AI for Mathematics` · `automated theorem proving` · `autoformalization` · `verifier-guided research agents` · `AI evaluation` · `reproducible scientific computing` · `nonlinear differential equations` · `bifurcation theory`

## Technical stack

`Python` · `TypeScript` · `SymPy` · `LaTeX` · `JSON Schema` · `GitHub Actions` · `Lean 4 / Mathlib (developing)`

## CV and collaboration

- [One-page CV](cv/Chih-Kai-Wang-CV.pdf) — updated August 2026.
- I am preparing for research-based graduate study and looking for opportunities in AI4Math, theorem proving, verifiable research agents, and trustworthy evaluation.
- For research, internship, or open-source collaboration: [f0909172434@gmail.com](mailto:f0909172434@gmail.com).
