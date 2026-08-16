# ADR 0003: Use canonical method ownership with faceted routing

- **Date:** 2026-08-16
- **Status:** accepted

## Context

The catalog is intentionally cross-domain. A method such as Bayesian inference, design of experiments, or failure-mode analysis can be relevant to several domains, but copying its full definition into each catalog would create drift and ambiguous ownership.

The project also needs to distinguish a generic method from a domain specialization. Clinical, spatial, manufacturing, legal, or safety use may change the unit of analysis, authority, evidence, measurement system, estimand, or validation boundary.

## Decision

Use faceted classification for discovery and a single canonical owner for each generic method family. The canonical catalog owns the generic procedure, selection logic, preconditions, failure modes, and source anchors. Other catalogs may contain routing aliases and domain-specific specializations. A specialization is justified only when the domain changes a material validity boundary or produces a distinct artifact.

Use Situational Method Engineering as the composition method: retrieve the canonical fragment, tailor it to context, add domain gates, and validate the interface. Use SKOS relations later only if machine-maintained taxonomy interoperability becomes a real requirement.

## Alternatives considered

- **Duplicate the complete method in every relevant catalog** — rejected because definitions, sources, and boundaries would drift.
- **Force every method into exactly one domain with no aliases** — rejected because discovery would fail for cross-domain work.
- **Use a formal metamodel immediately, such as SPEM or ISO/IEC 24744** — rejected because the current Markdown corpus does not yet require process-tool interoperability.
- **Use keyword search alone** — rejected because retrieval cannot distinguish object type, role, ownership, or changed validity boundaries.

## Consequences

- **Positive:** methods remain discoverable from multiple domains without duplicate canonical cards.
- **Positive:** domain tailoring becomes explicit and reviewable.
- **Cost:** contributors must maintain links and state what a specialization changes.
- **Cost:** routing quality depends on stable terminology and periodic alias review.
