# Method Forge

**A practical knowledge base for selecting, combining, and validating methodologies.**

Method Forge helps people and AI agents turn underspecified problems into small, defensible method stacks. It distinguishes methodologies from frameworks, standards, techniques, representations, assurance mechanisms, artifacts, and metrics before comparing them.

The repository currently contains 39 reference catalogs: 37 domain and cross-domain catalogs, plus two meta-reference catalogs for taxonomy and source discovery. Coverage ranges from strategy, software, evidence, statistics, and AI to finance, law, sustainability, supply chains, health, assets, geospatial analysis, and urban planning.

## Why it exists

Method selection often starts with a familiar acronym and ends with unnecessary process. Method Forge starts with the decision, context, constraints, evidence needs, and failure modes. It then composes only the capabilities the problem requires.

Its working principles are:

- compare candidates only when they compete for the same role;
- treat mandatory legal, safety, and regulatory requirements as gates rather than scores;
- separate canonical definitions from evidence that a method works;
- preserve rejected alternatives and negative findings;
- verify volatile versions and jurisdictions at the time of use;
- prefer the smallest sufficient stack.

## Use the agent skill

The installable skill lives at [`skills/select-methodologies`](skills/select-methodologies/SKILL.md).

With Codex, ask the skill installer to install:

```text
https://github.com/raphaelmarra/method-forge/tree/main/skills/select-methodologies
```

Then invoke it explicitly:

```text
$select-methodologies compare and operationalize methods for this problem
```

The skill can also trigger implicitly for methodology discovery, comparison, composition, operationalization, or audit requests.

## Explore the knowledge base

- [Taxonomy and selection protocol](skills/select-methodologies/references/00-taxonomy-selection.md)
- [Method engineering and composition patterns](skills/select-methodologies/references/10-composition-patterns.md)
- [Probability, statistics, and inference](skills/select-methodologies/references/37-probability-statistics-inference.md)
- [Urban, territorial, and regional planning](skills/select-methodologies/references/38-urban-territorial-planning.md)
- [Primary source and status registry](skills/select-methodologies/references/11-source-registry.md)
- [Repository architecture](docs/architecture.md)
- [Contribution guide](CONTRIBUTING.md)

Domain catalogs are stored in [`skills/select-methodologies/references`](skills/select-methodologies/references). The skill routes each problem to only the relevant catalogs to preserve context and reduce method soup.

## Validate the repository

Run the dependency-free validator before proposing a change:

```bash
python tools/validate_repository.py
```

Continuous integration runs the same checks for every push and pull request.

## Status

Method Forge is an actively curated knowledge project. Source-status snapshots are starting points for live verification, not permanent claims of currency.

## License and citation

Original repository content is available under the [MIT License](LICENSE). Names, trademarks, standards, and linked third-party materials remain the property of their respective owners. Citation metadata is provided in [`CITATION.cff`](CITATION.cff).
