---
name: select-methodologies
description: Select, compare, research, combine, and operationalize methodologies, frameworks, standards, techniques, artifacts, and metrics across project/programme/portfolio management, product, process, operations, software, systems, data, knowledge, evidence, AI, finance, marketing, design, implementation, workforce, sales, content, journalism, innovation, law, policy, crisis, engineering, manufacturing, assets, geospatial analysis, construction, sustainability, supply chains, agriculture, health, and education. Use to discover/classify options, identify omissions, distinguish method-rich domains from laws/data/source collections, choose a fit-for-context stack, verify versions/jurisdictions, avoid overengineering, or deepen a chosen approach. Also use for Portuguese requests about metodologia, frameworks, gestão de projetos/programas/portfólio/processos, pesquisa, marketing, design, conteúdo, vendas, inovação, viabilidade, engenharia, regulação, logística, ativos, geoespacial, crise, or avaliação.
---

# Praxis Atlas — Select Methodologies

## Objective

Transform an underspecified problem into a defensible methodological stack. Apply Situational Method Engineering: retrieve, tailor, and compose reusable method fragments according to context. Distinguish things that are often mislabeled as “methodologies,” shortlist the smallest sufficient set, verify current sources, and translate the selection into concrete artifacts, gates, tests, and metrics.

Do not treat the catalog as a checklist to maximize. Select by problem-to-method fit.

## Operating modes

Infer the requested mode; ask only when the difference changes the deliverable materially.

1. **Classify** — label a supplied list by type, domain, role, and overlap.
2. **Discover** — find plausible families and candidates without selecting prematurely.
3. **Select** — compare candidates and recommend a minimal stack.
4. **Deepen** — research one chosen candidate, its variants, evidence, version, and implementation.
5. **Operationalize** — convert the chosen stack into stages, responsibilities, artifacts, gates, tests, and metrics.
6. **Audit** — find omissions, duplication, cargo culting, obsolete versions, and methods used outside their valid context.

## Core distinction

Never compare unlike objects as direct alternatives. Assign every item one primary type:

| Type | Meaning | Examples |
| --- | --- | --- |
| Discipline or theory | Explanatory body of knowledge | systems engineering, epistemic reasoning |
| Management system or governance model | Organization-wide control and accountability | ISO 9001, ISO/IEC 42001 |
| Lifecycle or methodology | End-to-end sequence with roles or phases | DMAIC, PRINCE2, CRISP-DM |
| Framework or reference model | Structured guidance to tailor | Scrum, NIST AI RMF, APQC PCF |
| Method or technique | Bounded procedure producing an analysis or decision | FMEA, AHP, Event Storming |
| Language, notation, schema, or protocol | Formal expression or interchange mechanism | BPMN, DMN, OpenAPI, TLA+, MCP |
| Pattern or architectural tactic | Reusable solution shape | Saga, circuit breaker, resolver pattern |
| Artifact or template | Concrete output used by another activity | decision table, ADR, verification matrix |
| Test or assurance mechanism | Means of finding faults or supporting confidence | fuzzing, model checking, assurance case |
| Principle or heuristic | Directional rule without a complete procedure | API-first, shift-left, MECE |
| Metric | Operational measure | gate escape rate, DORA metrics |
| Composite or local method | Deliberate combination or organization-specific construct | GAT-R, premortem + FMEA + assurance case |

Use `references/00-taxonomy-selection.md` for the complete axes, scoring rubric, method-card schema, and saturation rule.

Use SPEM, Essence, or ISO/IEC 24744 only when the method repository itself needs a formal metamodel or interoperable tooling. The compact card schema is the default.

## Workflow

### 1. Frame the decision

Extract or state:

- intended outcome and decision to make;
- unit of analysis: organization, capital/project, portfolio, process, product, facility, asset, supply network, place, ecosystem, population, learning program, system, API, model, claim, or incident;
- lifecycle phase: explore, frame, design, plan, build, verify, deploy, operate, improve, or govern;
- uncertainty, reversibility, coupling, criticality, regulation, time, skills, and evidence constraints;
- required output: map, model, contract, plan, test, proof, control, decision, or metric.

For domain work, also record jurisdiction, geography, target population, observation period, decision horizon, technology/evidence maturity, baseline/counterfactual, and the authority or competence required. These are hard validity boundaries, not optional metadata.

Distinguish an unclear problem from an unclear solution. Use discovery approaches for the former and evaluation approaches for the latter.

### 2. Route to relevant catalogs

Read only the files needed:

| Problem signal | Read |
| --- | --- |
| Classify the supplied GACE list or preserve its original intent | `references/01-gace-source-catalog.md` |
| Strategy, product discovery, governance, organization, or change | `references/02-strategy-product-organization.md` |
| Process discovery/design, adaptive flow, operations, service management, quality, or continuous improvement | `references/03-process-operations-quality.md` |
| Software lifecycle, architecture, APIs, distributed systems, or delivery | `references/04-software-systems-architecture.md` |
| Requirements, planning, formal specification, contracts, or state reasoning | `references/05-requirements-formal-planning.md` |
| Verification, testing, reliability, safety, security, or assurance | `references/06-testing-reliability-safety-security.md` |
| Data/information governance, metadata, semantics, knowledge management, data quality, lineage, or provenance | `references/07-data-information-knowledge.md` |
| Decision analysis, optimization, uncertainty, or causal inference | `references/08-decision-optimization-causality.md` |
| ML lifecycle, LLMs, agents, evaluation, AI governance, or AI security | `references/09-ai-ml-agents.md` |
| Combine methods into one coherent operating system | `references/10-composition-patterns.md` |
| Verify canonical owners, standards, and current status | `references/11-source-registry.md` |
| Finance, investment economics, market intelligence, audit, controls, procurement, or due diligence | `references/12-finance-market-audit-procurement.md` |
| Law, regulation, compliance, public policy, ethics, or rights | `references/13-legal-policy-ethics.md` |
| Physical products, systems engineering, manufacturing, industrialization, metrology, qualification, or production acceptance | `references/14-physical-engineering-manufacturing.md` |
| Environment, LCA, circular economy, material flows, energy, industrial process, or TEA | `references/15-sustainability-circular-energy.md` |
| Supply chain, inventory, logistics, reverse flows, routing operations, traceability, or supply resilience | `references/16-supply-chain-logistics.md` |
| Agriculture, farm systems, pests, biosecurity, biological systems, or bioremediation | `references/17-agriculture-biological-systems.md` |
| Learning, training, curriculum, instructional design, or assessment | `references/18-learning-training-education.md` |
| Marketing strategy, positioning, brand, GTM, channels, acquisition, retention, media, CRM, or incrementality | `references/19-marketing-growth-brand-commercial.md` |
| Design research, UX, interaction, information architecture, service design, visual communication, accessibility, or design systems | `references/20-design-experience-communication.md` |
| Strategic foresight, horizon scanning, futures, scenarios, backcasting, roadmapping, or deep uncertainty | `references/21-futures-foresight.md` |
| Behavior change, intervention design, implementation science, adoption, adaptation, scale, or sustainment | `references/22-behavior-change-implementation.md` |
| Negotiation, bargaining, mediation, conflict resolution, grievance, agreement, or dispute-system design | `references/23-negotiation-mediation-conflict.md` |
| Participation, facilitation, deliberation, citizen engagement, consensus, co-creation, or collective decisions | `references/24-participation-facilitation-collective-decisions.md` |
| Workforce planning, job/role design, selection, competencies, performance, rewards, talent, succession, or people analytics | `references/25-people-workforce-talent.md` |
| Sales methodology, qualification, account/deal/pipeline management, forecasting, RevOps, onboarding, customer success, renewal, or expansion | `references/26-sales-revenue-customer-success.md` |
| Communication strategy, public relations, reputation, editorial/content operations, content distribution, risk/crisis communication, or corrections | `references/27-communication-reputation-content-operations.md` |
| Innovation management, R&D, ideas/opportunities, technology readiness, roadmapping, open innovation, IP, transfer, or commercialization | `references/28-innovation-rd-technology-management.md` |
| Journalism, reporting, fact-checking, source/document/data verification, OSINT, editorial integrity, or corrections | `references/29-journalism-verification-editorial-integrity.md` |
| Project, programme, portfolio, PMO, project governance, scope, schedule, cost, resources, benefits, stage gates, project assurance, or recovery | `references/30-project-programme-portfolio-management.md` |
| Research questions, reviews, primary/qualitative research, evidence synthesis, OSINT, investigations, claim assurance, or epistemic uncertainty | `references/31-research-evidence-investigation.md` |
| Crisis leadership, organizational resilience, business continuity, BIA, incident/emergency management, disaster recovery, exercises, or recovery | `references/32-crisis-continuity-emergency-management.md` |
| GIS, spatial-data quality, geocoding, spatial statistics/econometrics, remote sensing, service areas, suitability, or location decisions | `references/33-geospatial-location-analysis.md` |
| Asset management, criticality, maintenance strategy, RCM, RBI, condition monitoring, spares, obsolescence, or lifecycle renewal | `references/34-asset-maintenance-reliability.md` |
| Human factors, ergonomics, human-systems integration, workload, medical devices, clinical evidence, usability engineering, or medical QMS | `references/35-human-factors-health-medical-devices.md` |
| Construction, infrastructure, BIM, ISO 19650, constructability, Last Planner, commissioning, or built-asset handover | `references/36-construction-infrastructure-bim.md` |

For a cross-domain problem, begin with the primary decision catalog and at most two adjacent domain catalogs. Add another only when a selected fragment is canonically owned there or a material hard gate remains uncovered. Route by decision and missing capability, not by every noun in the prompt. `references/10-composition-patterns.md` and `references/11-source-registry.md` do not count as domain catalogs. Do not load all references by default.

### 3. Build a role-aware longlist

Search by problem signal, deliverable, and failure mode—not only by familiar names. Include candidates from distinct roles where warranted:

- one backbone lifecycle or governance frame;
- zero to three analysis/design techniques;
- zero to two representations, standards, or contracts;
- one verification or assurance mechanism for material claims or critical actions;
- two to five outcome, quality, risk, flow, or learning metrics.

Do not count a standard, a notation, and a test as three rival “methodologies.” They may be complementary layers.

### 4. Apply hard exclusions

Reject a candidate before scoring when:

- its required inputs, skills, authority, data, or tooling do not exist;
- its output does not feed a real downstream decision or control;
- its overhead exceeds the risk or reversibility of the task;
- it assumes stability while the problem is exploratory or complex;
- it assumes iteration while certification requires a fixed baseline and traceability;
- it duplicates another selected item without adding a distinct role;
- evidence of suitability is only vendor marketing or name recognition;
- a draft version is being presented as a stable normative standard.

### 5. Score surviving candidates

Use the rubric in `references/00-taxonomy-selection.md`. Score 0–4 for outcome fit, context fit, verifiability, evidence/maturity, composability, implementation feasibility, and proportionality. Compare scores only among candidates competing for the same stack role and decision output; never rank a backbone against a specialist or a mandatory gate. Treat safety, legal, and mandatory-standard fit as constraints, not compensable scores.

When precise weights are unjustified, present a qualitative comparison rather than fake numerical accuracy. Run sensitivity analysis when close scores depend on subjective weights.

### 6. Select the smallest sufficient stack

Prefer a coherent stack over a famous method:

1. **Backbone:** govern the overall lifecycle or decision cadence.
2. **Specialists:** solve bounded subproblems.
3. **Representation:** make inputs, decisions, interfaces, or state machine-verifiable.
4. **Assurance:** attack failure modes and support confidence.
5. **Measurement:** detect value, flow, quality, risk, and escape.

Apply the subtraction test: remove each element and state what material capability is lost. Remove elements whose loss is negligible.

### 7. Research online in two passes

Do not perform equal-depth research on every candidate.

**Pass A — option validation**

- Confirm canonical name, owner/standards body, scope, status, and current stable version.
- For legal, tax, regulatory, clinical, environmental, spatial, or sector claims, confirm jurisdiction, effective date, competent authority, and applicability to the exact activity and unit of analysis.
- Read an authoritative overview or normative source.
- Check whether the candidate is a method, reporting guideline, certification body of knowledge, notation, or tool ecosystem.
- Find at least one source about limitations, empirical results, or implementation outside the promoter when stakes justify it.

**Pass B — selected-method deep dive**

- Read the primary specification, guide, or seminal paper.
- Compare relevant variants and the current stable release; label drafts explicitly.
- Extract prerequisites, steps, roles, inputs, outputs, tailoring rules, failure modes, adoption cost, and validation evidence.
- Translate the method into this problem's artifacts and acceptance tests.
- For high-stakes domain execution, identify the boundary between agent research/design and work requiring a licensed professional, accredited body, laboratory, field inspection, or public authority.

For technical claims, prefer official specifications, standards bodies, maintainers, and original research. Separate “the source defines” from “evidence shows it works.” Never claim universal efficacy from popularity.

### 8. Stop at explicit saturation

Use the catalog and query-family rule in `references/00-taxonomy-selection.md`. Saturation means additional search is no longer changing the shortlist or risk controls—not that every named framework on the internet was collected.

### 9. Produce an actionable answer

Default output:

1. **Problem classification** — context, phase, criticality, and required output.
2. **Taxonomy correction** — what kinds of objects are being discussed.
3. **Candidate matrix** — candidate, type, role, when to use, when not to use, evidence/version, overhead, and fit.
4. **Selected stack** — backbone, specialists, representation, assurance, and metrics.
5. **Rejected alternatives** — only serious contenders, with reasons.
6. **Operationalization** — steps, owners, artifacts, gates, tests, and measures.
7. **Research status** — verified stable sources, drafts, uncertain claims, and remaining questions.

If the user asks only for a concise market map, stop after items 1–5. If the user asks to implement, continue through item 7.

## Non-negotiable quality rules

- Preserve the difference between `when not to use` and a mere disadvantage.
- Distinguish alternatives from complements, prerequisites, and supersets.
- Name versions only after checking current status; attach an “as of” date to volatile standards.
- Label proprietary, certification-oriented, emerging, contested, and organization-local methods.
- Do not infer maturity from an acronym or standards number.
- Do not prescribe heavyweight formality to low-risk reversible work without a proportionality argument.
- Do not use Agile, Lean, design thinking, systems thinking, or “best practices” as catch-all labels.
- Do not let the selected method approve its own output; use an independent gate for critical work.
- Preserve negative results and rejected candidates so later agents do not repeat the same search.
- Treat metrics as sensors, not targets; note gaming risk and pair leading with lagging indicators.

## Examples

- “Which methods should guide the refactoring of an API-contract compiler?” → read software, formal planning, testing, and the GACE source catalog; compose a stack rather than choose one acronym.
- “Our order process has stable steps but high defect and rework rates.” → compare DMAIC, PDCA, TOC, process mining, VSM, FMEA, and statistical control; avoid product-discovery frameworks as the backbone.
- “We need an auditable investigation from public sources.” → combine a review/search protocol, source evaluation, provenance, claim–evidence modeling, competing-hypothesis analysis, and coverage metrics.
- “Should this agent workflow use PDDL or HTN?” → classify planning structure, observability, state uncertainty, action model, and runtime cost before comparing formalisms.
- “Should we invest in a circular industrial technology after a laboratory result?” → combine maturity and scale-up evidence, balances/TEA, LCA, supply network, regulatory/process-safety gates, and staged investment economics; do not equate laboratory yield with commercial readiness.
- “Did this training program work?” → separate satisfaction, learning, workplace transfer, operational outcome, and causal attribution before choosing assessments and evaluation methods.
- “How should we launch this B2B offer?” → combine market evidence, STP/ICP, positioning, offer/price, route-to-market, launch readiness, retention, and causal measurement; a campaign is not a GTM strategy.
- “Should we redesign this service or only its interface?” → map the end-to-end service, actors, failures, capacity, information, and recovery before selecting UX, service-design, accessibility, and operational methods.
- “How should we distribute the same evidence-based content across channels?” → combine communication objectives, content lifecycle/model, channel roles, rights, accessibility, distribution preflight, and outcome evidence; do not create a platform-posting checklist.
- “Should this public decision use a consultation or citizen assembly?” → define actual decision space, participation promise, representation, evidence, deliberation, response, and evaluation before selecting the format.
- “How do we move a laboratory technology toward commercialization?” → combine opportunity evidence, TMA/TRL, maturation experiments, integration/manufacturing readiness, IP/regulatory/economic gates, demonstration, and staged investment.
