# ADR 0005: Integrate task, error, interaction, and variability analysis

- **Date:** 2026-09-12
- **Status:** accepted

## Context

Task and cognitive analysis appeared as generic catalog entries. Users needed actionable selection boundaries and procedures for HTA and CTA, followed by credible task-error analysis, practiced interaction-time comparison, and analysis of everyday sociotechnical variability.

## Decision

Keep HTA, CTA, and SHERPA in human factors (`35`), GOMS/KLM in interaction design (`20`), and FRAM in safety and systems (`06`). Add canonical cards with prerequisites, procedures, outputs, sources, and evidence limits. Route training and UX task-analysis uses to the human-factors owner. Record ownership in the taxonomy and expose optional compositions without requiring every method.

HTA supplies goals, operations, and execution plans; CTA elicits cognitive demands and expert cues. SHERPA identifies credible task errors and recovery. KLM estimates execution time for a specified practiced, error-free method. FRAM distinguishes a potential-coupling model from scenario/event instantiations. No model or worksheet alone establishes achieved performance, calibrated error probabilities, causal proof, or safety.

## Alternatives and consequences

Separate domain-specific copies or new skills would duplicate definitions and weaken routing. A generic task-analysis entry would leave these different outputs and assumptions hidden. The selected owners preserve one definition per method while allowing downstream tailoring.

Source consultation is recorded in the [registry](../../skills/select-methodologies/references/11-source-registry.md). Where original full protocols were unavailable, the cards state that limitation. Exact protocol replication and effectiveness claims require further evidence.

Repository validation checks structure and links. The [selection scenarios](../../tests/scenarios/selection-invariants.md) define future behavioral evaluation expectations; they are not reported as executed model benchmarks.
