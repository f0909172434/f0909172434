# Finite Witness: make a counterexample inspectable

[Live workbench](https://f0909172434.github.io/finite-witness-webmcp/) · [Source](https://github.com/f0909172434/finite-witness-webmcp) · [CV](../cv/CV.md)

Finite Witness is a browser workbench for finite graph conjectures. It returns the graph that breaks a claim, together with the properties that explain why it is a counterexample. A person using the interface and an agent using WebMCP operate the same application.

## Problem and observable result

Consider the claim: every simple graph with at least three vertices and minimum degree at least two contains a triangle.

For the default search range of 3–6 vertices, the recorded run examined 39 candidates before finding a four-cycle, C₄. It has four vertices, four edges, degree sequence `[2, 2, 2, 2]`, and zero triangles. It satisfies the assumptions and violates the conclusion. Its deterministic certificate is `fw-b20670c4`.

One counterexample disproves this universal claim. A different search that returns no counterexample establishes only the absence of a witness in its recorded search range.

## Engineering decisions

- **Keep search off the UI thread.** Graph enumeration runs in a Web Worker so the interface can remain responsive during bounded exhaustive search.
- **Use one engine for people and agents.** Eight WebMCP operations expose the same workbench behavior. This reduces the chance that an agent-specific implementation disagrees with the visible interface.
- **Record the actual searched prefix.** Search stops at the first witness in vertex-count and edge-mask order. The certificate distinguishes the requested range from the prefix that was actually visited; finding C₄ does not imply that all six-vertex graphs were checked.
- **Make repairs inspectable.** Suggested assumption changes exclude the current witness and can be searched again. Excluding one witness does not prove a repaired claim.

## Verification

The repository's nine tests cover graph properties, known counterexamples, bounded claim formatting, shareable experiment round-trips, repair behavior, damaged evidence handling, and deterministic certificates. On September 5, 2026, the suite passed locally; an earlier live browser check in the same review confirmed agreement between the visible result, WebMCP search response, and certificate.

Source pointers: [graph engine](https://github.com/f0909172434/finite-witness-webmcp/blob/main/src/graph-engine.js), [worker](https://github.com/f0909172434/finite-witness-webmcp/blob/main/src/search-worker.js), [WebMCP adapter](https://github.com/f0909172434/finite-witness-webmcp/blob/main/src/webmcp.js), [tests](https://github.com/f0909172434/finite-witness-webmcp/tree/main/tests).

## Next useful experiment

Observe a first-time user checking a conjecture and explaining the difference between a requested range and an exhausted range. Record where the interface fails to communicate that distinction before changing it.
