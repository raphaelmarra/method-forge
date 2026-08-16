# ADR 0004: Add an urban and territorial planning catalog

- **Date:** 2026-08-16
- **Status:** accepted

## Context

The repository already covered geospatial analysis, construction/BIM, participation, climate, project governance, and public policy. It did not have a canonical owner for the planning decisions that connect those fragments: territorial diagnosis, land-use strategy, urban form, mobility integration, public-space choices, implementation rules, and place-based monitoring.

## Decision

Add `38-urban-territorial-planning.md` as the canonical catalog for urban, territorial, and regional plan-making. Keep geospatial computation in `33`, construction delivery in `36`, participation methods in `24`, and climate-risk methods in `15`/`21`/`32`. The urban catalog composes those fragments around a place-based planning decision and its implementation boundary.

## Consequences

- **Positive:** planning has a discoverable home without duplicating spatial, construction, or participation methods.
- **Positive:** land rights, local authority, infrastructure capacity, displacement, and climate resilience become explicit validity boundaries.
- **Cost:** contributors must distinguish a spatial model, participation process, project, and plan.
