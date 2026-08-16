# Contributing

Method Forge welcomes corrections, stronger sources, clearer selection boundaries, new composition patterns, and domain coverage that passes the methodological-density gate.

## Contribution standard

A contribution should improve a real decision. It must not add a method only because it is popular, branded, or adjacent to a domain.

For every new or materially changed candidate:

1. Assign its object type, lifecycle role, stack role, domain, and maturity.
2. State the output it produces and who or what consumes that output.
3. Distinguish `use when` from `avoid when`.
4. Identify prerequisites, limitations, failure modes, and relevant complements.
5. Link to the canonical owner or primary specification.
6. Separate definition/status evidence from effectiveness evidence.
7. Record the date when volatile status, version, or jurisdiction was checked.

Do not copy substantial third-party text. Summarize in original language and link to the source.

## Adding a domain

Apply the methodological-density gate in the [taxonomy and selection protocol](skills/select-methodologies/references/00-taxonomy-selection.md). A subject deserves a separate catalog only when it contains reusable procedural families, meaningful selection logic, artifacts or gates, independent validation, canonical anchors, and distinct ownership.

Laws, vendors, datasets, registries, rates, and platform features may constrain a stack without becoming methodological domains.

## Pull request checklist

- [ ] The change has one clear purpose.
- [ ] Terminology is stable and does not duplicate an existing owner.
- [ ] Local links resolve.
- [ ] Volatile claims include a check date.
- [ ] Proprietary, emerging, contested, and draft material is labeled.
- [ ] Serious rejected alternatives are preserved when selection changes.
- [ ] `python tools/validate_repository.py` passes.
- [ ] Structural decisions include or update an ADR.

## Review model

Maintainers review taxonomy fit, source strength, internal consistency, proportionality, and downstream usability. A standards number, certification, citation count, or vendor adoption claim is not sufficient evidence by itself.
