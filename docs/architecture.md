# Repository architecture

Praxis Atlas has two audiences but one canonical knowledge source.

## Human interface

The root documentation explains purpose, governance, contribution, citation, and maintenance. GitHub provides immediate browsing without requiring a documentation build.

## Agent interface

`skills/select-methodologies` is a self-contained installable skill. Its `SKILL.md` routes a problem to the relevant files, and its `references/` directory owns the taxonomy, domain catalogs, composition patterns, and source registry.

## Validation boundary

The dependency-free repository validator checks package structure, frontmatter, local links, catalog headings, route integrity, placeholders, and duplicate ownership signals that can be detected mechanically. Human review remains responsible for methodological fit, evidence quality, proportionality, and jurisdiction.

## Evolution

Prefer Markdown while the catalog remains primarily curated prose and tables. Introduce a machine-readable method-card schema only when repeated automation requires it; do not maintain parallel Markdown and structured sources without a generated, drift-checked boundary.
