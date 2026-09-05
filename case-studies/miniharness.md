# MiniHarness: turn a curriculum outline into executable lessons

[Repository](https://github.com/f0909172434/miniharness) · [Course website](https://f0909172434.github.io/miniharness/) · [Assessment rubrics](https://github.com/f0909172434/miniharness/blob/main/academy/ASSESSMENT.md)

MiniHarness combines a standard-library Python agent harness, an eight-step
workshop and a curriculum from computing basics to agent engineering.

## Problem and resulting behavior

The curriculum had 38 module entries but only two ready modules. A learner could
see the roadmap without being able to follow most of it. The workshop checker
also returned a successful process exit when an assignment failed.

The September 2026 completion adds the remaining 36 Traditional Chinese lessons,
per-goal assessment criteria, 32 concept questions, five fixed assignment
checkers and versioned progress import/export. The website now searches real
lesson titles, module IDs and Goal IDs, and links to the matching source lesson.
Failed or missing assignments return a nonzero exit. Reference solutions and
quizzes never mark a learner's goals complete.

## Engineering choices and evidence

- **One curriculum manifest.** Readiness counts and website links derive from the
  same source as CLI validation.
- **Fixed checker contracts.** The verifier runs known scripts with time limits;
  it does not execute arbitrary command strings stored in lesson metadata.
- **Keep the core small.** The harness uses the Python standard library. Optional
  ML examples use a separate environment and do not become runtime dependencies.
- **Retain negative outcomes.** A 14,676-parameter causal Transformer learns small
  self-authored phrases. Adaptation improved a two-prompt development score from
  0/2 to 1/2 while worsening held-out perplexity from 2.14 to 16.47. Both results
  remain visible.

Local checks passed 46 core/course tests, four optional ML tests, all five
reference contracts and the eight-step workshop. The ML tests check causal
isolation, finite nonzero gradients, parameter updates and context limits.
The examples were executed on CPU; their tiny fixtures are not a general
language benchmark.

## Limits

All 38 modules now have a Traditional Chinese teaching baseline. English module
titles exist, but English lessons are not yet translated. `ready` describes
available teaching material; it is not evidence of learner completion or
instructional effectiveness. First-user trials and learner projects need actual
participants and are tracked separately.
