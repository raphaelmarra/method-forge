# ADR 0002: Rename the repository to Method Forge

- **Date:** 2026-08-16
- **Status:** accepted

## Context

The repository is a curated knowledge base and installable agent skill for selecting, composing, and operationalizing methods. The previous name, Praxis Atlas, emphasized catalog breadth but did not clearly signal the project's transformation and composition role.

## Decision

Rename the repository and public project identity to **Method Forge**. Preserve `select-methodologies` as the stable skill identifier and package path so existing installation and invocation workflows remain compatible.

## Consequences

- **Positive:** the name better communicates method composition and practical transformation.
- **Positive:** the installable skill remains discoverable and backwards-compatible.
- **Cost:** repository URLs and citation metadata change, while GitHub redirects the former repository URL.
