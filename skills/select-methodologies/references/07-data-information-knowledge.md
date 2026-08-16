# Data, information, knowledge, semantics, quality, and provenance

Use this catalog when the core problem is governing, organizing, modeling, validating, retrieving, transferring, or preserving data and organizational knowledge. Provenance answers “where did it come from?”; it does not answer “is it true?” For research design, evidence synthesis, OSINT, claims, and epistemic uncertainty, use `31-research-evidence-investigation.md`.

## Contents

1. Data and information governance
2. Metadata, semantics, and knowledge representation
3. Data quality and contracts
4. Lineage and provenance
5. Knowledge management and organizational learning

## Data and information governance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| DAMA-DMBOK | data-management body of knowledge | establish broad coverage across governance, quality, metadata, architecture, master data, security, and lifecycle | implement every discipline equally or treat certification content as a method |
| DCAM | data-management capability framework | assess enterprise data-management capabilities and gaps | detailed technical implementation or small local dataset |
| COBIT Data / information governance practices | governance reference | decision rights, value, risk, and control for enterprise information/technology matter | use as data modeling or analytics methodology |
| Data Mesh | sociotechnical data architecture approach | domain ownership, data products, federated governance, and self-service can be supported organizationally | relabel distributed pipelines without product ownership and interoperability |
| Data Fabric | architecture concept/pattern family | metadata-driven integration and automation span heterogeneous data environments | buy a platform and claim governance/semantics are solved |
| FAIR Principles | data stewardship principles | digital assets should become findable, accessible under conditions, interoperable, and reusable | equate FAIR with open, correct, unbiased, or high quality |
| Records Management / ISO 15489 | records discipline | authenticity, reliability, integrity, usability, retention, and disposition of institutional records matter | semantic knowledge discovery or data-quality process |
| Data Retention / Disposition Schedule | governance artifact | legal, operational, privacy, and evidence needs require time-bounded lifecycle rules | keep everything forever or delete without holds/provenance |

## Metadata, semantics, and knowledge representation

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Controlled Vocabulary / Taxonomy | knowledge-organization system | consistent categories, aliases, filtering, and navigation are needed | complex polyhierarchy/inference is required but unsupported |
| Thesaurus / ISO 25964 | semantic vocabulary model | preferred terms, synonyms, broader/narrower/related relations improve retrieval | logical axioms and rule inference are needed |
| SKOS | RDF vocabulary for knowledge-organization systems | publish/interoperate taxonomies, thesauri, and concept schemes | rich ontological restrictions require OWL |
| Ontology / RDF / OWL | semantic modeling stack | shared machine-interpretable entities, relationships, constraints, and inference justify rigor | local schema is simple or ontology governance is absent |
| SHACL | RDF graph-validation language | validate graph shapes, cardinalities, paths, and constraints | infer truth or replace ontology/reasoning semantics |
| Knowledge Graph | architecture/data product pattern | heterogeneous entities and evidence need connected queryable relations | any graph database is called a knowledge graph without semantics/provenance |
| ISO/IEC 11179 | metadata registry standard family | data elements, concepts, representations, and stewardship need consistent registration | full enterprise registry overhead for a small controlled schema |
| DCAT | dataset/catalog vocabulary | datasets and data services need interoperable catalog metadata | data model, lineage, or quality assessment by itself |
| Schema.org / domain vocabularies | web/domain semantic schemas | external discoverability/interchange benefits from established terms | force a generic vocabulary where domain meaning is lost |

## Data quality and contracts

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 8000 family | data-quality standard family | principles, quality management, master data, and roles need a normative reference | choose parts without matching scope or assume conformance proves usefulness |
| ISO/IEC 25012 / 25024 | data-quality model and measurement standard | define and measure data quality characteristics systematically | syntactic quality is mistaken for representativeness or causal validity |
| ISO/IEC 5259 family | data quality for analytics/ML | ML/analytics lifecycle requires quality measures and process guidance | generic transactional data management alone |
| Data Quality Dimensions | assessment technique family | accuracy, completeness, consistency, timeliness, validity, uniqueness, and fitness need operational definitions | use generic dimensions without business rules and sampling strategy |
| Data Profiling | analysis technique | discover distributions, nulls, patterns, anomalies, and constraints before modeling/migration | infer semantics or quality acceptance automatically |
| Statistical Data Validation / Drift Detection | monitoring technique | distributions and relationships may change over time | alerts without action thresholds, seasonality handling, and business context |
| Data Contracts | producer–consumer governance pattern | schema, semantics, quality, ownership, compatibility, and service expectations need explicit agreement | replace API/legal contracts or centralize every change in one bottleneck |
| Open Data Contract Standard (ODCS) | data-contract specification | portable machine-readable data contracts fit the ecosystem | standard adoption overhead exceeds interoperability value |
| Master Data Management | data-management discipline | authoritative shared entities and stewardship must span systems | one application's local lookup table or no ownership/governance |
| Entity Resolution / Record Linkage | matching method family | identities must be reconciled across noisy sources with uncertainty | high-impact actions require exact identity but no manual/authoritative resolution path exists |

## Lineage and provenance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Data Lineage | operational metadata practice | trace source-to-target transformations and change impact | provenance, business meaning, and quality are assumed from a lineage graph |
| W3C PROV-DM / PROV-O | provenance model/ontology | entity–activity–agent derivation needs interoperable representation | full RDF stack is unnecessary for a local signed audit log |
| OpenLineage | runtime lineage specification | jobs, runs, inputs, outputs, and facets across data tooling need integration | document-level research claims or manual evidence without jobs/runs |
| Event Sourcing / Audit Log | operational history patterns | state changes must be reconstructed or audited | log mutability, identity, retention, and privacy are unresolved |
| Content-Addressed Storage / Hash Manifests | integrity mechanism | immutable artifact identity and change detection matter | provenance/authenticity/trust is inferred from a digest alone |

## Knowledge management and organizational learning

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 30401 | knowledge-management system standard | organization-wide knowledge creation, sharing, application, protection, and improvement need governance | one-off research or a document repository project |
| APQC Knowledge Flow Process | KM process framework | map creation, identification, collection, review, sharing, access, and use of knowledge | assume knowledge flows because a portal exists |
| Knowledge Audit | diagnostic method | find critical knowledge, gaps, risks, owners, and flows | domain/ownership are already explicit and the bottleneck is execution |
| Knowledge Mapping | representation technique | visualize who knows what, sources, dependencies, and handoffs | expose sensitive expertise without access/governance controls |
| SECI Model | knowledge-creation conceptual model | reason about socialization, externalization, combination, and internalization | treat contested abstractions as a deterministic implementation recipe |
| Communities of Practice | organizational learning model/practice | practitioners need sustained peer learning around a shared domain | mandate a “community” with no identity, practice, or participation incentive |
| Knowledge-Centered Service (KCS) | service knowledge methodology | support/operations should create and improve knowledge in the workflow | write-before-solving bureaucracy or publish unreviewed sensitive content |
| After Action Review (AAR) | team learning method | compare intent, actual events, causes, and future adaptation soon after action | blame session or generic lessons detached from owners/context |
| Lessons Learned System | knowledge lifecycle practice | reusable lessons need validation, context, retrieval, application, and feedback | archive unsearchable anecdotes or call recommendations universal best practices |
| Knowledge Retention / Critical Knowledge Transfer | continuity method family | retirement, turnover, or scarce expertise threatens operations | capture everything rather than prioritize critical tacit knowledge |

## Research anchors

- ISO 30401; APQC Knowledge Flow; ISO 15489; ISO 8000; ISO/IEC 25012/25024/5259.
- W3C SKOS, RDF/OWL, SHACL, PROV, and DCAT; OpenLineage; ODCS.
- FAIR Guiding Principles and original paper.
- Route research conduct, evidence synthesis, investigation, and claim assurance to `31-research-evidence-investigation.md`.
