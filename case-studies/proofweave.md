# ProofWeave: certify a formal target without overstating its meaning

[Repository](https://github.com/f0909172434/proofweave-math-lab) · [Actual run and artifacts](https://github.com/f0909172434/proofweave-math-lab/tree/main/docs/walkthroughs/simple-ring)

ProofWeave Core is experimental Python infrastructure for structured mathematical
claims. It produces inspectable Lean certification artifacts and tracks proof
status, semantic alignment and claim lifecycle separately.

## Problem and observable result

A correct formal proof can still prove a different statement from the one a
person intended. Reporting only “verified” hides that distinction.

On September 5, 2026, the bundled integer identity `(x + 1)² = x² + 2x + 1` was run
with pinned Lean/Mathlib 4.32.2 on macOS arm64. Lean certified its one deductive
obligation. The result remained **CERTIFIED + UNCONFIRMED**: no human had attested
to the prose-to-target alignment. The first run called the certifier once and no
model. An unchanged second run checked and reused the same artifacts, with zero
certifier calls.

The walkthrough retains the exact input, generated Lean source, certificate,
coverage and SHA-256 checksums. Its JSON summary selects fields from actual CLI
output and removes absolute host paths.

## Engineering decisions

- **Keep the certificate language small.** Author-supplied targets and allowed
  tactics can be inspected. Unsupported obligations remain partial.
- **Bind results to bytes and the formal environment.** Input, statement,
  certificate and toolchain identities make cached results checkable.
- **Use independent status axes.** Formal validity cannot silently become a
  semantic alignment attestation or an active claim revision.
- **Test refusal as well as success.** The released finite corpus includes paired
  negatives and escape attempts; a missing toolchain must fail closed.

## Scope

This walkthrough is one actual run. The separate `v0.1.0` evidence release reports
42 fixed-corpus cases; the Core package/protocol version is 2.0.0. Neither result
establishes global soundness, arbitrary natural-language formalization, novelty
or peer review. The next useful evaluation would be a preregistered set of new,
independently authored claims with reviewed formal alignments.
