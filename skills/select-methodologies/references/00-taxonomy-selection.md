# Taxonomy and selection protocol

## Contents

1. Classification axes
2. Method-card schema
3. Context triage
4. Scoring rubric
5. Catalog ownership and specialization
6. Methodological-density gate
7. Saturation protocol
8. Research record

## Classification axes

Classify every candidate independently on five axes. Do not collapse them into one label.

| Axis | Values |
| --- | --- |
| Object type | discipline/theory; management system; lifecycle/methodology; framework/reference model; method/technique; language/notation/schema/protocol; pattern/tactic; artifact/template; test/assurance; principle/heuristic; metric; composite/local |
| Primary domain | strategy/organization/product; portfolio/project/process/operations; requirements/software/systems; testing/reliability/safety/security; data/knowledge/research/evidence; decision/optimization/causality; AI/ML/agents; finance/investment/market/audit/procurement; marketing/growth/brand/commercial activation; design/experience/accessibility; futures/foresight; behavior/implementation/adoption; negotiation/mediation/conflict; participation/facilitation/deliberation; people/workforce/talent; sales/revenue/customer success; communication/reputation/content operations; innovation/R&D/technology management; journalism/verification/editorial integrity; legal/regulatory/policy/ethics/crisis; physical engineering/manufacturing/assets/human factors/health/construction; environment/circularity/energy/process engineering; supply chain/logistics/geospatial; agriculture/biological systems; learning/education; meta-engineering |
| Lifecycle role | explore; frame; decide; design; plan; build; verify; deploy; operate; improve; govern; retire |
| Stack role | backbone; specialist; representation; assurance; measurement |
| Maturity/source | normative standard; official framework; established practice; research method; emerging practice; proprietary method; local/composite |

Secondary tags may express problem shape, artifact, sector, criticality, and scale.

For domain methods, also record jurisdiction, geography, time horizon, technology or evidence maturity, and the authoritative regulator/owner when any of these can change validity. Do not generalize a sector standard, tax/legal rule, environmental factor, clinical requirement, or spatial model outside the population and context for which it was verified.

## Method-card schema

Use this schema when adding or deeply researching a method:

```markdown
### Canonical name — acronym

- Type / domain / lifecycle role / stack role:
- Purpose and output:
- Use when:
- Do not use when:
- Preconditions and required capability:
- Typical procedure:
- Complements:
- Alternatives or variants:
- Failure modes and gaming risks:
- Adoption cost: low | medium | high
- Maturity: normative | established | emerging | local
- Canonical research anchors:
- Current version/status checked on:
- Evidence and unresolved questions:
```

For a discovery catalog, the compact fields `type`, `purpose`, `use`, `avoid`, `complements`, and `source anchor` are sufficient. Expand only shortlisted methods.

## Context triage

### Problem topology

| Signal | Bias the search toward | Be cautious with |
| --- | --- | --- |
| Goal and causal path are unclear | discovery, systems mapping, theory of change, experiments | detailed execution workflows |
| Solution is known but performance is poor | DMAIC, PDCA, SPC, process mining, TOC | broad ideation as the backbone |
| Requirements are volatile | iterative discovery, prototypes, dual-track, evolutionary architecture | frozen exhaustive specifications |
| Interfaces are stable and regulated | requirements traceability, V-model, contracts, conformance tests | informal stories as sole specification |
| Stateful or distributed effects exist | state machines, temporal properties, idempotency, sagas, model checking | happy-path sequence diagrams alone |
| Human adoption is the main risk | change, stakeholder, sociotechnical, service design methods | purely technical optimization |
| Evidence is contested or incomplete | systematic search, triangulation, provenance, Bayesian/ACH reasoning | single-source narratives |
| Consequences are severe or irreversible | hazard analysis, independent V&V, assurance cases, formal methods | “move fast” defaults |
| Decisions must remain adaptive | OODA, rolling-wave planning, real options, monitoring triggers | one-time deterministic plans |

For physical, financial, regulatory, environmental, agricultural, spatial, health, or educational work, also extract as applicable:

- scale and maturity: concept, laboratory, pilot, demonstration, production, or operating system;
- geography, jurisdiction, target population, season, observation period, and decision horizon;
- baseline/counterfactual, measurement system, estimate class, and uncertainty source;
- competent authority, professional capability, permit, certification, or independent review required.

### Proportionality tiers

| Tier | Context | Expected stack |
| --- | --- | --- |
| 1 | reversible, low impact, short-lived | one lightweight backbone or technique plus basic validation |
| 2 | meaningful cost or several teams | backbone, one or two specialists, explicit acceptance criteria, outcome metrics |
| 3 | material financial/operational impact | traceability, risk analysis, independent test/gate, monitoring and rollback |
| 4 | safety, rights, regulation, high irreversibility | normative requirements, independent assurance, formal or model-based analysis where suitable, audit evidence, controlled change |

## Scoring rubric

Score each surviving candidate from 0 to 4. State weights before seeing totals.

| Criterion | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Outcome fit | unrelated output | partially supports decision | directly produces required capability |
| Context fit | assumptions conflict | tailoring required | assumptions match |
| Verifiability | subjective only | mixed | machine- or independently verifiable |
| Evidence/maturity | unsupported/obsolete | plausible or limited | current authoritative basis plus implementation evidence |
| Composability | conflicts/duplicates | manageable overlap | cleanly fills a distinct role |
| Feasibility | unavailable inputs/skills | attainable with effort | usable now |
| Proportionality | overhead dominates | balanced | strong risk reduction per unit cost |

Do not average away hard constraints. Mark mandatory compliance, safety, privacy, and legal requirements as pass/fail gates.

When uncertainty in weights can reverse the winner, show the reversal threshold or use an unweighted ordinal comparison.

Score only genuine alternatives for the same stack role and required output. Resolve backbone, specialist, representation, assurance, and measurement needs separately. A mandatory gate is pass/fail and cannot lose to a higher-scoring optional technique.

## Catalog ownership and specialization

When the same family appears in multiple catalogs, retrieve its generic definition from the canonical owner and use the domain card only for tailoring:

| Family | Canonical owner | Domain specialization examples |
| --- | --- | --- |
| Project, programme, portfolio, PMO, project controls, benefits, and recovery | `30-project-programme-portfolio-management.md` | investment economics in `12`; engineering lifecycle in `04`/`14`; adoption in `22`; operations transition in `03` |
| Process improvement, SPC, generic operations control | `03-process-operations-quality.md` | manufacturing in `14`; agriculture in `17` |
| Reliability, hazard analysis, generic FMEA/FMECA | `06-testing-reliability-safety-security.md` | DFMEA/PFMEA in `14`; biological hazards in `17` |
| Data governance, semantics, quality, lineage, provenance, and knowledge management | `07-data-information-knowledge.md` | AI data in `09`; evidence infrastructure in `31`; BIM information in `36` |
| Research design, evidence synthesis, investigation, claims, and epistemic assurance | `31-research-evidence-investigation.md` | causal identification in `08`; journalism in `29`; legal research in `13` |
| Experiments, causal inference, optimization, uncertainty | `08-decision-optimization-causality.md` | field designs in `17`; learning evaluation in `18`; process DOE in `15` |
| Financial appraisal, DCF, BoE, investment gates | `12-finance-market-audit-procurement.md` | TEA inputs in `15`; manufacturing cost/readiness evidence in `14` |
| Market research, sizing, conjoint, WTP, commercial diligence | `12-finance-market-audit-procurement.md` | activation/positioning in `19`; research interaction/prototypes in `20` |
| Marketing strategy, brand, GTM, channels, lifecycle, media measurement | `19-marketing-growth-brand-commercial.md` | market/economics in `12`; communication/experience in `20` |
| Design research, UX, service/interaction/information design, accessibility, design systems | `20-design-experience-communication.md` | product strategy in `02`; safety-oriented HFE in `35`; learning design in `18` |
| Legal applicability, licensing, policy, compliance | `13-legal-policy-ethics.md` | sector-specific environmental, health, agricultural, or construction gates |
| Crisis, continuity, emergency/incident management, resilience, and recovery | `32-crisis-continuity-emergency-management.md` | crisis communication in `27`; cyber incident response in `06`; service incidents in `03` |
| Product realization and manufacturing readiness | `14-physical-engineering-manufacturing.md` | process scale-up in `15` |
| Asset management, maintenance, inspection, condition monitoring, spares, and renewal | `34-asset-maintenance-reliability.md` | manufacturing equipment in `14`; built-asset handover in `36` |
| Human factors, ergonomics, medical devices, and clinical-device evidence | `35-human-factors-health-medical-devices.md` | UX in `20`; product realization in `14`; health regulation in `13` |
| Construction, infrastructure, BIM, constructability, and commissioning | `36-construction-infrastructure-bim.md` | project controls in `30`; asset operations in `34`; physical engineering in `14` |
| LCA, environmental claims, TEA, industrial processes | `15-sustainability-circular-energy.md` | agricultural sustainability in `17` |
| Supply chains, inventory, logistics, reverse networks, and traceability | `16-supply-chain-logistics.md` | circular feedstock/recovery in `15`; spatial network design in `33` |
| Geospatial data, spatial analysis/econometrics, remote sensing, and location decisions | `33-geospatial-location-analysis.md` | route/facility operations in `16`; causal inference in `08`; investigations in `31` |
| Strategic foresight, scenarios, backcasting, adaptive pathways | `21-futures-foresight.md` | strategy in `02`; technology roadmaps in `28`; robust decisions in `08` |
| Behavior-change and implementation/adoption | `22-behavior-change-implementation.md` | organizational change in `02`; learning in `18`; marketing activation in `19` |
| Negotiation, mediation, agreements, dispute systems | `23-negotiation-mediation-conflict.md` | grievance/workforce in `25`; legal procedure in `13` |
| Participation, facilitation, deliberation, collective decisions | `24-participation-facilitation-collective-decisions.md` | research participation in `31`; co-design in `20`; public policy in `13` |
| Workforce, selection, performance, talent, people analytics | `25-people-workforce-talent.md` | organization/change in `02`; learning in `18`; employment law in `13` |
| Sales, pipeline, RevOps, customer success | `26-sales-revenue-customer-success.md` | GTM/offer in `19`; negotiation in `23`; economics in `12` |
| Communication, reputation, editorial/content operations and distribution | `27-communication-reputation-content-operations.md` | marketing acquisition in `19`; content design in `20`; journalism in `29` |
| Innovation systems, R&D, technology maturity/transfer | `28-innovation-rd-technology-management.md` | product/strategy in `02`; engineering readiness in `14`; finance/IP in `12`/`13` |
| Journalism, fact-checking, editorial verification | `29-journalism-verification-editorial-integrity.md` | generic evidence/OSINT in `31`; legal investigation in `13`; communication distribution in `27` |

A specialization may change preconditions, experimental unit, authority, metric, or failure modes. Do not add both generic and specialized cards to the stack as if they were separate work unless each produces a distinct artifact.

## Methodological-density gate

Create or expand a domain catalog only when the area contains reusable ways to act and choose, not merely subject matter to retrieve. Apply this gate before broad domain research.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Procedural corpus | mostly facts, rules, sources, or tools | a few reusable procedures | several distinct method families with steps and outputs |
| Selection logic | no meaningful alternatives | informal context differences | explicit triggers, preconditions, and `do not use` boundaries |
| Artifacts and gates | information summaries only | some templates/checklists | decisions, models, plans, tests, controls, or acceptance gates |
| Validation | authority/source lookup only | descriptive metrics | independent review, experiment, conformance, outcome, or failure tests |
| Canonical anchors | vendors/listicles dominate | mixed practitioner sources | standards, official owners, seminal research, or mature professional guidance |
| Distinct ownership | duplicates an existing catalog | useful specialization | coherent decision family with clear interfaces to adjacent catalogs |

Interpret the proposed score as an architecture heuristic, not a scientific measurement:

- `9–12`: a separate reference catalog is usually justified;
- `6–8`: add a section or specialization to an existing owner;
- `0–5`: treat it as subject matter, source registry, legal/data overlay, or tool/platform detail—not as a methodological domain.

Reject a proposed domain when most search results would necessarily be laws, rates, registries, datasets, vendors, platform features, or current facts. Tax, legislation, case law, and sector data may constrain a method stack, but do not become catalogs merely because they are important. Add a sector catalog only when the sector changes the procedure, unit of analysis, authority, evidence, validation, or failure modes materially.

## Saturation protocol

### Candidate saturation

Scale discovery to the proportionality tier:

| Tier | Minimum discovery depth |
| --- | --- |
| 1 | primary domain; canonical definition/status; one focused expansion only if fit is unclear |
| 2 | primary plus one adjacent domain when warranted; problem/failure and artifact queries; one no-change expansion |
| 3 | primary plus up to two adjacent domains; all four query families; citation/version chasing; two successive no-change expansions |
| 4 | Tier 3 plus jurisdiction/authority, independent limitation/effectiveness evidence, and explicit adversarial search for invalidating conditions |

The four query families are problem/failure, desired artifact, lifecycle phase, and known candidate alternatives. Stop when the required successive expansions add no candidate that changes the top stack, hard constraints, or material risk controls. Expand beyond the initial catalog cap only when this test reveals a specific uncovered capability or gate.

Record a newly found synonym as an alias, not a new candidate. Record a variant separately only when it changes procedure, assumptions, outputs, governance, or evidence.

### Evidence saturation

For a selected method, seek:

- a canonical definition or normative specification;
- current version/status from the owner;
- implementation guidance or a worked example;
- limitations, failure conditions, or empirical evaluation;
- one independent source when a high-stakes claim depends on efficacy.

Stop when new sources repeat known claims without changing implementation, boundary conditions, confidence, or risk.

## Research record

Maintain this compact ledger:

| Candidate | Search anchors | Type/status | Included or rejected | Decisive evidence | Version checked | Open question |
| --- | --- | --- | --- | --- | --- | --- |

Separate three claim states:

- **Verified:** supported by an authoritative or appropriately strong source.
- **Rejected:** contradicted, obsolete, out of scope, or excluded by a hard constraint.
- **Possible:** relevant but not yet supported strongly enough for selection.
