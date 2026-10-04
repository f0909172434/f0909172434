# Chih-Kai Wang

**Software Engineering & AI Internship | Python, TypeScript, Inspectable Research Tools**

[Email](mailto:f0909172434@gmail.com) | [GitHub](https://github.com/f0909172434) | Taipei, Taiwan

## Profile

I build Python and TypeScript tools for inspectable AI and mathematical research: a CI check that reads the test report rather than the exit code, an audit that ties research claims to the bytes of their evidence, a counterexample search that reports the range it searched. I develop with Claude Code and Codex, review every change, and keep negative results public. Seeking a software engineering or AI internship.

## Education

**National Taipei University of Education** | Expected 2028

B.S. student, Mathematics Division, Department of Mathematics and Information Education.

## Selected Projects

**[HonestCI](https://github.com/f0909172434/honest-ci)** | TypeScript, Node.js, GitHub Actions

- CLI and GitHub Action that checks JUnit reports are present, fresh, and not below a trusted test-count baseline. Published as v1.0.4 on npm and GitHub Marketplace.
- In the launch demo, a zero-test report with exit code 0 passes a bare workflow; with HonestCI it fails as HCI004_ZERO_TESTS (exit code 1). It does not judge test quality.

**[RigorGraph](https://github.com/f0909172434/rigorgraph)** | Python, JSON Schema, HTML Reports

- Local-first Python CLI that links research claims to evidence files and independent review records, checks SHA-256 hashes, and writes offline audit reports (PyPI 1.0.1, public beta).
- Changed evidence bytes raise RG_HASH_MISMATCH and a changed claim invalidates the old acceptance. VERIFIED means accepted by the recorded workflow, not true.

**[Finite Witness](https://github.com/f0909172434/finite-witness-webmcp)** | JavaScript, Web Workers, WebMCP, Python

- Browser tool that exhaustively searches small graphs (up to 6 vertices) for counterexamples and writes certificates that an independent Python script replays.
- Default run: 39 candidates examined, then a four-cycle with no triangle. Surviving a bounded search is evidence, not proof.

**[SAIR Proof Press](https://github.com/f0909172434/sair-stage2-proof-press)** | Python, Lean 4

- Public companion to an equational-implication solver that outputs Lean-checked proofs or finite countermodels.
- Frozen artifacts accepted 1,669 / 1,669 released inputs with zero model calls. This is released-input coverage, not a private score or rank.

## Research & Open Source

**[RuleDiff negative result](https://github.com/f0909172434/rulediff-negative-result)**: four-page technical report; a lexical predictor scored 0.99 macro-F1 on development data and 0.67 on a held-out packet. Not peer reviewed. **[RuleShift](https://github.com/f0909172434/ruleshift)**: research pilot where simple retrieval matched more complex agent memory strategies. **[ProofWeave Core](https://github.com/f0909172434/proofweave-math-lab)**: checks author-written Markdown proofs against pinned Lean 4 / Mathlib and reports certification apart from human-confirmed alignment.

Merged upstream: DeepSeek Harness Desktop #740 (worktree path normalisation), dsh-engram #4 (conservative migration), Codex Dream Skin #10 (Windows verification).

Creative work (October 2026): ORACLE (short film), The Disease Called AI (song + watercolour MV), world.execute(me) (terminal PV) - each rendered entirely from code; links on the portfolio.

## Technical Skills

**Languages:** Python, TypeScript, Node.js, Lean 4 (learning), Bash

**Tools:** GitHub Actions, pytest, Vitest, JSON Schema, MLX, Blender (asset pipeline), Claude Code, Codex

_Last updated: October 2026_
