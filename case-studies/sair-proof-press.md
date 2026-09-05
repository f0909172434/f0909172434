# SAIR Proof Press: retain a checkable answer through bounded search

[Public repository](https://github.com/f0909172434/sair-stage2-proof-press) · [Interactive site](https://f0909172434.github.io/sair-stage2-proof-press/) · [English paper](https://f0909172434.github.io/sair-stage2-proof-press/paper/sair_stage2_solver_research.pdf)

This public companion documents solvers for equational implication: decide
whether one magma identity implies another. A true answer needs a replayable
Lean proof; a false answer needs a Lean-checkable finite countermodel.

## Problem and engineering approach

Candidate search can produce plausible answers that fail formal replay. A
Marathon solver also has to retain its best verified answers as a shared time
budget runs down.

The solver tries bounded routes including short proofs, finite countermodels,
proof-producing paramodulation and symbolic search. These routes propose
candidates; Lean decides whether a certificate is accepted. The Marathon path
performs cheap deterministic work first, retains verified answers and does not
overwrite them with worse candidates. The aggressive variant also has a bounded
waypoint fallback.

## Published evidence

| Public workload | Recorded result |
|---|---|
| Released Normal/Hard inputs | All four frozen Solo/Marathon × Safe/Aggressive artifacts accepted 1,669 / 1,669 inputs; no actual model calls in the final runs |
| Released Order-5 | Marathon Safe 198 / 200; Aggressive 200 / 200 |
| Same-host released Marathon batch | Safe 169.00 s; Aggressive 152.23 s |

The records bind these results to evaluator commit
`817a4653bf762584931d49c6714c9fcfab7df66a` and Lean 4.33.1. The batch timing is a
descriptive measurement on that workload, not a causal estimate of private-set
improvement. The four public solver files' byte sizes and SHA-256 hashes were
read back against the published manifest on September 5, 2026; this portfolio
maintenance check did not rerun the complete competition evaluation.

Sources: [aggregate results](https://github.com/f0909172434/sair-stage2-proof-press/blob/main/docs/results.md),
[machine-readable evidence](https://github.com/f0909172434/sair-stage2-proof-press/tree/main/docs/evidence),
[frozen artifacts](https://github.com/f0909172434/sair-stage2-proof-press/tree/main/dist/final).

## What this demonstrates

The engineering work connects search, certificate replay, budget management,
artifact identity and conservative reporting. Negative results remain in the
public research timeline, so a failed experiment is still inspectable.

The records establish released-input coverage. They do not provide an
organizer-published private score or rank. Portal participation readback records
delivery, not evaluation success. The complete private research history remains
outside this public companion. See the [claim boundaries](https://github.com/f0909172434/sair-stage2-proof-press/blob/main/docs/claim-boundaries.md).
