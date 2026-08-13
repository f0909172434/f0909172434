# Chih-Kai Wang

**B.S. Student | AI for Mathematics and Verifiable Reasoning**

[Email](mailto:f0909172434@gmail.com) | [GitHub](https://github.com/f0909172434) | Taipei, Taiwan

## Education

**National Taipei University of Education** | Expected 2028

B.S. student, Mathematics Education Division, Department of Mathematics and Information Education, National Taipei University of Education. Expected 2028.

## Research Interests

AI for Mathematics; automated theorem proving and autoformalization; verifier-guided research agents; evaluation and calibration; reproducible scientific computing; nonlinear differential equations and bifurcation theory.

## Research Direction

**[ClaimPromoteBench](https://github.com/f0909172434/claimpromote-bench) - Policy-Governed Evidence-State Transitions for Mathematical Research Agents** | In development

- Designing a benchmark protocol for deciding whether evidence justifies a requested mathematical claim-state transition.
- Separating research, computation, formal-certificate, and independent-review states, with deterministic policy checks and counterfactual pairs.
- Current status: public 20-pair / 40-instance alpha validates the data and evaluation pipeline; no model result or technical report has been published.

## Selected Open-Source Work

**[ProofWeave Core v2](https://github.com/f0909172434/proofweave-math-lab)** | Python, Lean 4

- Built model-independent infrastructure for parsing mathematical claims and proofs and checking constrained Lean 4 / Mathlib certificates.
- Keeps formal-certificate status, natural-language alignment, and claim lifecycle orthogonal; no model is called at runtime.
- Public identifiers: repository release v0.1.0; Core package 2.0.0.

**[RigorGraph](https://github.com/f0909172434/rigorgraph)** | Python

- Built a local-first claim-evidence graph and deterministic audit workflow with provenance, dependency, snapshot, independence, and hash checks.
- Produces self-contained offline reports and preserves explicit truth boundaries. Public beta; package 1.0.1.

**[HonestCI](https://github.com/f0909172434/honest-ci)** | TypeScript

- Built a CLI and GitHub Action that checks fresh JUnit evidence and detects missing reports, zero-test runs, and suspicious test-count reductions.
- Publishes versioned evidence bundles without treating CI success as proof of program correctness. Stable version 1.0.4.

## Technical Skills

**Languages:** Python, TypeScript | **Mathematics and research:** SymPy, LaTeX, reproducible computation

**Formal methods:** Lean 4 / Mathlib (developing) | **Engineering:** JSON Schema, GitHub Actions, cross-platform CI, deterministic validation

_Last updated: August 2026_
