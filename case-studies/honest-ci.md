# HonestCI: a green process can contain zero tests

[Repository](https://github.com/f0909172434/honest-ci) · [Reproducible demo](https://github.com/f0909172434/honest-ci/blob/main/launch/DEMO.md) · [npm 1.0.4](https://www.npmjs.com/package/honest-ci/v/1.0.4)

HonestCI is a TypeScript CLI and GitHub Action that checks the test evidence behind a successful process. It inspects JUnit reports for missing files, stale results, zero tests, and unexpected count reductions against a trusted baseline.

## Problem and observable result

The launch demo deliberately writes a JUnit report with zero tests and exits with code 0. A workflow that checks only the process exit sees success.

Wrapping the identical runner with HonestCI produces `HCI004_ZERO_TESTS` and exits with code 1. The demo verifier checks both exit codes, the error code, and that the failure is not mistakenly attributed to a stale report.

## Engineering decisions

- **Treat reports as evidence.** A process exit code and a report's test count answer different questions. Both need to be retained when diagnosing a false green result.
- **Keep the baseline outside the proposed change's control.** A trusted revision supplies the reference count, so the code under review cannot silently lower its own expected test count.
- **Ship reproducible bundles.** The Action and CLI include built artifacts. CI rebuilds them and checks that the committed package matches the source and dependency lockfile.
- **Test the installed package.** Package smoke checks catch failures that source-level tests alone would miss.

## Maintenance example: September 2026

A dependency PR passed the execution checks but failed package consistency because its generated bundles had not been updated. Rebuilding the Action and CLI in the PR environment restored the package contract. The complete verification command passed 54 tests, type checks, documentation checks, seven demonstration scenarios, and package smoke checks. [PR #26](https://github.com/f0909172434/honest-ci/pull/26) then passed its required checks and was merged.

Separately, a prior macOS / Node 24 build failed with a segmentation fault. Rerunning the failed jobs at the same commit succeeded. That establishes recovery of the check, not a proven root cause.

## Limits

Fresh, non-empty test reports do not establish that assertions are useful, coverage is adequate, or software is correct. HonestCI checks evidence integrity within its declared report and baseline contract.

## Next useful experiment

Collect a few real configuration mistakes from a small repository and check whether the error report gives a maintainer enough information to repair each one without reading the implementation.
