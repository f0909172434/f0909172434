# RigorGraph: keep claims connected to their evidence

[Repository](https://github.com/f0909172434/rigorgraph) · [PyPI 1.0.1](https://pypi.org/project/rigorgraph/1.0.1/)

RigorGraph is a Python CLI for version-controlled claim and evidence records. It performs deterministic audits and generates self-contained offline HTML reports. The released package is a public beta.

## Problem and observable result

A review can become outdated when the claim or supporting file changes. Keeping only a “verified” label hides that dependency.

RigorGraph records claims, evidence hashes, and review snapshots. Its tests demonstrate that changed evidence bytes produce `RG_HASH_MISMATCH`, while a changed claim invalidates the old acceptance snapshot with `RG_SNAPSHOT_MISMATCH`. The audit also checks dependency cycles, missing evidence requirements, unchecked evidence, and invalid transitions.

## Engineering decisions

- **Store records as version-controlled data.** JSON records and schemas make changes reviewable in the same workflow as source code.
- **Separate evidence identity from judgment.** A matching hash establishes byte identity. Review records carry scoped acceptance or rejection; a hash does not establish scientific validity.
- **Generate a portable report.** The offline HTML viewer travels with the result and does not require a running backend. This adds a generated artifact that must be kept reproducible.
- **Keep failure outcomes visible.** Missing evidence or invalid review state produces an audit finding rather than silently preserving an old status.

## Verification and maintenance

On September 5, 2026, the local maintenance checks passed 64 tests, lint, schema validation, and the full release check, including frontend and plugin builds. The dependency update in [PR #19](https://github.com/f0909172434/rigorgraph/pull/19) required rebuilding the offline viewer from its frontend source. The generated file was not edited by hand; the updated PR passed the required checks and was merged.

Source pointers: [audit tests](https://github.com/f0909172434/rigorgraph/blob/main/tests/test_audit.py), [frontend](https://github.com/f0909172434/rigorgraph/tree/main/frontend), [Python implementation](https://github.com/f0909172434/rigorgraph/tree/main/src/rigorgraph).

## Limits and next step

The audit verifies workflow and record integrity. It does not decide whether a scientific conclusion is true. A useful next step is a short walkthrough in which a reviewer opens a sample report, changes one evidence file, and explains the resulting audit finding.
