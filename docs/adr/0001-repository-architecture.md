# ADR 0001: Package the catalog as Praxis Atlas

- **Date:** 2026-08-16
- **Status:** accepted

## Context

The project began as a standalone `select-methodologies` skill with a large reference catalog. Public release requires a clear human interface, contribution and governance rules, validation, and an installable unit without duplicating the catalog.

## Decision

Use **Praxis Atlas** as the repository identity while preserving `select-methodologies` as the stable skill identifier. Keep the canonical catalog inside the self-contained skill package and place repository-level documentation, governance, ADRs, and validation outside it.

## Alternatives considered

- **Rename the skill to `praxis-atlas`** — rejected because it would weaken descriptive triggering and break the existing invocation identity.
- **Copy the catalog into a separate documentation tree** — rejected because two editable sources would drift.
- **Convert every catalog entry to YAML immediately** — rejected because the current prose and tables contain contextual boundaries that would require a premature, complex schema.
- **Publish the original flat skill directory unchanged** — rejected because it lacks a public-project interface, governance, licensing, and repository validation.

## Consequences

- **Positive:** the repository has a memorable identity, the skill remains compatible, and humans and agents share one canonical catalog.
- **Positive:** future structured data or a documentation site can be generated behind an explicit validation boundary.
- **Cost:** repository navigation must link into the nested skill package.
- **Cost:** changes must satisfy both public documentation quality and agent progressive-disclosure constraints.

## Notes

Revisit machine-readable method cards only after real consumers require stable queries, exports, or interoperability.
