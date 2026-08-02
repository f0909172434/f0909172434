# Wang Chih Kai

Building local-first tools for auditable AI-assisted research and CI.

I work on small, inspectable systems that keep evidence, claims, and verification status separate. The goal is not to make AI output look authoritative; it is to make the path from input to result easier to reproduce, audit, and challenge.

## Current projects

### [HonestCI](https://github.com/f0909172434/honest-ci)

Checks whether a green CI run actually executed the tests and configurations a maintainer expected. It can emit a versioned **Evidence Bundle v1** containing its result and digests of the observed inputs.

### [RigorGraph](https://github.com/f0909172434/rigorgraph)

A public-beta, local-first tool for claim-evidence graphs and offline audit reports. It can validate and preserve an HonestCI Evidence Bundle v1, but importing evidence never promotes or verifies a claim.

### [ProofWeave Math Lab](https://github.com/f0909172434/proofweave-math-lab)

An experimental 0.1 research workspace for statused mathematical claims, reproducible computation, model routing, and release checks. It is presented here as a standalone workflow, not as an integration that does not yet exist.

## How the implemented pieces fit

`HonestCI result` → `Evidence Bundle v1` → `RigorGraph import and audit`

ProofWeave Math Lab remains a separate, end-to-end research workspace.

## Working principles

- local-first artifacts before hosted lock-in;
- explicit `DRAFT`, `PROPOSED`, `COMPUTATIONAL`, and `VERIFIED` boundaries;
- reproducible checks and content digests;
- additive compatibility for published 1.x interfaces;
- evidence can support review, but does not become truth by ingestion.
