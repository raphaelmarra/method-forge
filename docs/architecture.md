# Repository architecture

Method Forge has two audiences but one canonical knowledge source.

## Human interface

The root documentation explains purpose, governance, contribution, citation, and maintenance. GitHub provides immediate browsing without requiring a documentation build.

## Agent interface

`skills/select-methodologies` is a self-contained installable skill. Its `SKILL.md` routes a problem to the relevant files, and its `references/` directory owns the taxonomy, domain catalogs, composition patterns, and source registry.

## Validation boundary

The dependency-free repository validator checks required package structure, frontmatter, local links, catalog headings, reference count, route integrity, and unresolved TODO markers. Canonical ownership and duplicate-method signals are reviewed through the taxonomy, composition patterns, architecture decisions, contribution checklist, and scenario contracts; the validator does not infer those judgments as facts. Human review also remains responsible for methodological fit, evidence quality, proportionality, and jurisdiction.

## Evolution

Prefer Markdown while the catalog remains primarily curated prose and tables. Introduce a machine-readable method-card schema only when repeated automation requires it; do not maintain parallel Markdown and structured sources without a generated, drift-checked boundary.
