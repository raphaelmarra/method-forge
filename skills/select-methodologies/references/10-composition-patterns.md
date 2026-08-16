# Method engineering and composition patterns

Use this file after candidate discovery. Its purpose is to create a coherent situational method, not a pile of branded frameworks.

## Contents

1. Meta-methods and composition grammar
2. Method-fragment interface
3. Reusable stack patterns
4. Compatibility and conflict patterns
5. Anti-patterns
6. Subtraction and interface tests
7. Criteria for separate executable skills

## Meta-methods for this catalog

| Candidate | Type and purpose | Use when | Avoid when |
| --- | --- | --- | --- |
| Method Engineering | meta-discipline for designing methods | methods themselves need explicit construction, representation, evaluation, or evolution | a mandatory ready-made procedure already fits |
| Situational Method Engineering (SME) | context-driven method assembly/tailoring | select and compose method fragments/chunks for a particular problem, organization, and risk | arbitrary pick-and-mix without interfaces, rationale, or validation |
| Method Fragment / Method Chunk | reusable method unit | store a bounded activity with context, inputs, process, outputs, and validation | split concepts so finely that they no longer produce usable outcomes |
| ISO/IEC 24744 | methodology metamodel standard | information-intensive domains require a rigorous metamodel for development methodologies | compact Markdown catalog with no interchange/tool need |
| SPEM | OMG software/systems process metamodel | model roles, tasks, work products, guidance, and process structures in compatible tooling | process enactment or a general management ontology is expected automatically |
| Essence | kernel/language for software engineering methods | express practices on a common kernel and reason about endeavor progress | non-software domains or use of an evolving draft without status label |
| SKOS | knowledge-organization model | represent broader/narrower/related concepts and aliases for catalog retrieval | full method semantics, execution, or logical constraints are expected |

Default to the lightweight card schema. Escalate to SKOS for reusable taxonomy relations; to SPEM, Essence, or ISO/IEC 24744 only if machine interoperability or method-authoring tooling creates real value.

## Composition grammar

A situational method may contain five orthogonal roles:

| Role | Governing question | Examples |
| --- | --- | --- |
| Backbone | How does the work progress and who decides? | DMAIC, Scrum, PRINCE2, research protocol, AI RMF |
| Specialist | How is one bounded uncertainty or failure solved? | FMEA, Event Storming, AHP, causal DAG, threat modeling |
| Representation | How are decisions and interfaces made explicit? | BPMN, DMN, OpenAPI, state machine, PROV, ADR |
| Assurance | How will error, risk, and false confidence be attacked? | contract tests, STPA, model checking, red team, assurance case |
| Measurement | How will value, flow, quality, risk, and learning be observed? | SLOs, DORA, evidence coverage, effect estimates, adoption measures |

Not every low-risk task requires all five. Every included element must have a unique job, an output consumer, and a validation rule.

## Method-fragment interface

Before composing, define each selected fragment as:

```yaml
trigger: context conditions that justify invocation
requires: inputs, skills, authority, evidence, and predecessor states
produces: artifact, decision, state change, or measurement
procedure: bounded activities and decision points
verified_by: acceptance test, review, experiment, or evidence rule
failure_modes: invalid assumptions, misuse, gaming, and escape paths
next: consumers and compatible successor fragments
```

Reject a composition when the output of one fragment does not satisfy the next fragment's input semantics, even if field names appear to match.

## Reusable stack patterns

### Improve a stable process

`SIPOC/process mining → DMAIC backbone → MSA/SPC → RCA/TOC → controlled experiment → FMEA → control plan → outcome + escape metrics`

Use when the process exists and repeated evidence is available. Replace DMAIC with PDCA/A3 for a smaller, lower-risk loop. Add change/adoption methods when human behavior is a material constraint.

### Discover and deliver a product

`strategy/outcome → continuous discovery + Double Diamond → JTBD/service blueprint → opportunity tree → prototype/experiment → prioritization → Scrum or Kanban delivery → product + guardrail metrics`

Do not let RICE/WSJF invent precision. Add architecture/security/compliance gates before experiments that can harm users.

### Govern a project or program

`business case + benefits map → PRINCE2/PMI-tailored governance → rolling-wave plan → risk/decision log → stage evidence → independent gate → benefits realization/post-evaluation`

Use predictive CPM/EVM only for sufficiently stable baselines; integrate iterative delivery inside the governance shell when learning remains high.

### Engineer an API workflow

`stakeholder goal/GORE → capability and IOPE → OpenAPI/AsyncAPI + schemas → canonical IR → DMN rules → Arazzo/BPMN/HTN flow → operation contracts → translation validation → transaction/idempotency semantics → contract/model tests → runtime reconciliation → provenance`

OpenAPI describes interfaces, not business truth. Arazzo describes known call sequences, not a general planner. MCP publishes capabilities to AI systems, not authorization or assurance.

### Engineer a distributed transaction

`business invariant → state machine → failure/consistency model → idempotency → outbox/inbox → saga/compensation → timeout/retry/isolation → TLA+/model-based tests when warranted → SLO/telemetry → recovery drill`

Explicitly represent `UNKNOWN_COMMIT`; do not collapse it into `FAILED`.

### Conduct an auditable public-source investigation

`question framework → protocol/scope matrix → multichannel search + citation chaining → source/version resolution → screening/extraction → source/risk-of-bias appraisal → triangulation/ACH → synthesis → claim–evidence + PROV → contradiction/gap register → saturation rule`

Use three evidence states at minimum: verified, rejected, and possible-not-proven. PRISMA is a reporting layer, not the search/review method.

### Make a high-impact investment decision

`decision frame + hard constraints → theory of change/causal model → scenarios/uncertainty → economic model → MCDA/utility/robust method → Monte Carlo/sensitivity → value of information/real options → premortem → decision record → monitoring triggers`

Keep preferences distinct from empirical estimates. Test whether reasonable weights or assumptions reverse the recommendation.

### Develop a circular industrial technology venture

`feedstock/source characterization → mass and energy balance → flowsheet/simulation → scale-up maturity plan → TEA + investment model → LCA/MFA → reverse-supply network → regulatory/process-safety gates → pilot evidence → independent technical/commercial due diligence → staged investment + operating M&V`

Do not use laboratory yield as commercial throughput, a circularity score as environmental proof, or early-stage TEA as a bankable forecast.

### Choose facilities and design a logistics network

`demand/supply frame → geocoding and spatial-quality audit → constraints + candidate sites → network service areas → spatial MCDA → location–allocation + capacity/inventory/route model → cost-to-serve + resilience stress test → field/permitting due diligence → staged pilot`

Do not call a weighted heatmap “econometrics,” and do not optimize routes before validating source density, participation, service time, and vehicle constraints.

### Design an agricultural or biological intervention

`farm/ecosystem frame → baseline + pathway/hazard map → agronomic or biological hypothesis → blocked/factorial/on-farm trial → economic/environmental/welfare outcomes → IPM/biosecurity controls → seasonal and spatial replication → adoption analysis → monitored decision rule`

Use bioremediation only for contaminant treatment. It is not a substitute name for pest management, biosecurity, or ecological restoration.

### Build and evaluate a learning system

`performance-gap analysis → task/cognitive task analysis → competency + observable objectives → backward design → evidence-aligned instruction/practice → formative feedback → authentic mastery gate → workplace support → transfer and outcome evaluation → causal/cost analysis when the decision requires it`

Satisfaction is not learning, learning is not workplace transfer, and transfer is not causal proof of operational impact.

### Launch and grow a market offer

`decision + market evidence → STP/ICP/buying committee → positioning + claim–proof → experience/offer/price → GTM + route-to-market → launch-readiness gate → instrumented beachhead → acquisition + activation + retention → experiments/MMM → staged expansion`

A campaign is not a go-to-market strategy, attributed revenue is not incremental revenue, and awareness cannot compensate for unavailable distribution or weak retention.

### Design and assure an end-to-end service

`outcome + affected actors → inclusive field research → journey/ecosystem + service blueprint → task/IA/state/error recovery → service and interface prototypes → usability + accessibility + operational assurance → bounded pilot → user/service/business outcomes → recovery and continuous improvement`

Do not let a visual redesign conceal broken policy, capacity, handoffs, data, rights, or failure recovery. Accessibility conformance and usability evidence are complementary claims.

### Build a foresight-to-action system

`decision/horizon → diverse scanning → drivers/cross-impacts → coherent scenarios → wind-tunnel options → robust/adaptive pathways → signposts/triggers → periodic refresh`

Do not present scenarios as forecasts or roadmaps as fixed promises.

### Change behavior and implement at scale

`specified behavior → COM-B/TDF diagnosis → BCW/BCT options → APEASE/ethics gate → intervention test → CFIR context → specified implementation strategies → RE-AIM/Proctor outcomes → adaptation/sustainment`

Intervention effectiveness, implementation fidelity, adoption, and maintenance are separate claims.

### Design a legitimate collective decision

`decision space/authority → participation promise → affected-rights map → representative/inclusive recruitment → balanced evidence → facilitated deliberation → decision/dissent record → response → feedback/evaluation`

Do not use participation to legitimize a fixed decision.

### Build a revenue and customer-value system

`ICP/coverage → buyer discovery/qualification → claim proof + mutual action → stage exits + forecast → agreement → onboarding/time-to-value → adoption/outcomes → renewal/expansion → churn/win-loss learning`

Pipeline activity is not buyer progress, and usage is not customer value.

### Operate evidence-based content distribution

`audience decision → communication objective → content audit/model/lifecycle → claim–proof → editorial workflow → channel roles/PESO → rights/accessibility preflight → publication → outcome/incrementality → correction/sunset`

Do not create a new domain for every platform. Platform mechanics are volatile implementations of channel roles.

### Conduct and publish a journalistic investigation

`public-interest test → hypothesis/disconfirmers → source/document/data plan → legal/safety gates → reporting/OSINT/analysis → claim–evidence + chronology → right of reply → independent fact/legal/standards review → publication → corrections/follow-up`

Association is not culpability, provenance is not truth, and a verdict label cannot replace evidence.

### Build a causal evaluation

`causal question + estimand → DAG/assumptions → experimental/quasi-experimental identification → estimator → diagnostics/placebos/negative controls → sensitivity → external validity → decision analysis`

Root-cause analysis and process maps do not substitute for counterfactual identification.

### Build a knowledge system for agents

`knowledge audit → taxonomy/SKOS → metadata/DCAT/registry → quality rules → data contracts → lineage/PROV → retrieval architecture → retrieval + citation evals → claim freshness/retention → incident learning`

RAG is a consumer of governed knowledge, not the governance method.

### Build a tool-using agent

`goal contract → deterministic workflow or HTN/ReAct selection → scoped typed tools → resolver contracts → plan/policy validation → idempotent transaction layer → authoritative read-back → behavioral + trajectory evals → adversarial tests → approval/assurance gate → monitoring`

Favor deterministic orchestration when the workflow is known. Use model judgment only on a declared decision surface with abstention/escalation.

### Release a high-impact AI system

`AI RMF/ISO management context → impact/risk assessment → data/model/system documentation → task/slice/trajectory/field TEVV → privacy/security threat models → OWASP/ATLAS red team → safety/AI assurance case → independent gate → monitored release + incident learning`

Model metrics alone cannot establish system acceptability in a real use context.

## Compatibility patterns

| Elements | Relationship |
| --- | --- |
| GORE → DMN → BPMN | goals and requirements → decision logic → process flow |
| QAW → ADD → ATAM → ADR | elicit measurable qualities → design → evaluate trade-offs → preserve rationale |
| OpenAPI + JSON Schema + Arazzo + MCP | HTTP interface → instance constraints → API call workflow → AI interoperability |
| OpenAPI + AsyncAPI + CloudEvents | synchronous contract → message API contract → transport-neutral event envelope |
| DbC + property tests + contract tests | local invariants → generative cases → consumer/provider boundary verification |
| FSM/TLA+ + model checking + runtime verification | behavior model → pre-release counterexamples → live trace checking |
| Premortem → FMEA/FTA/STPA → assurance case | elicit feared failure → analyze mechanisms/interactions → justify control adequacy |
| Threat model → ASVS/control baseline → security tests → red team | design threats → verifiable requirements → systematic checks → adversarial challenge |
| Idempotency + outbox/inbox + saga | safe repetition → state/message consistency → business transaction recovery |
| PROV + SBOM/SLSA/in-toto + assurance case | data/artifact lineage → software supply-chain evidence → justified confidence claim |
| SLO + observability + incident command/postmortem | acceptable reliability → signals → coordinated response and learning |
| DMAIC + Double Diamond | improvement backbone with bounded divergence/convergence inside analysis/design |
| DSM + stage contracts | global dependencies plus local entry/output/exit obligations |

## Conflict patterns

| Conflict | Resolution rule |
| --- | --- |
| Scrum cadence vs interrupt-driven operations | use Kanban/service classes or separate bounded operational capacity |
| Predictive baseline vs high discovery uncertainty | govern outcomes/stages predictively but plan delivery in rolling waves |
| Central enterprise standard vs autonomous teams | fix minimum interfaces/controls; decentralize implementation choices |
| Formal proof vs changing requirements | stabilize the high-risk kernel/interface; keep exploratory edges iterative |
| Optimized utilization vs flow/resilience | optimize end-to-end throughput and tail risk, not local utilization |
| Fast autonomy vs approval gates | scope authority by reversibility/risk and automate low-risk validations |
| RAG flexibility vs authoritative state | use retrieval for knowledge; use read-through APIs/databases for transactional truth |
| Metric targets vs learning | pair measures, audit behavior, preserve qualitative evidence, and rotate/review targets |

## Anti-patterns

- **Method soup:** stack overlapping frameworks with no distinct output or consumer.
- **Name-first selection:** choose a famous acronym, then search for justification.
- **Error of category:** compare a protocol, notation, metric, and methodology as substitutes.
- **Cargo-cult completeness:** adopt every ceremony while omitting the causal mechanism.
- **Local optimization:** improve one stage while increasing total lead time, failure demand, or risk.
- **False formality:** precise scores, models, or contracts built from unsupported inputs.
- **Provenance equals truth:** lineage authenticates history, not validity.
- **PRISMA equals systematic review:** reporting checklist does not perform the review.
- **RCA equals causal inference:** plausible cause is not an identified counterfactual effect.
- **Pareto/MCDA equals objective decision:** values, weights, vetoes, and uncertainty remain judgments.
- **RAG equals grounding:** retrieval recall, source quality, entailment, and freshness still require evaluation.
- **Self-critique equals independent verification:** correlated model errors require external evidence or deterministic checks.
- **Multi-agent equals diversity:** identical models, contexts, and sources can amplify the same error.
- **Red team equals assurance:** attacks sample a threat space and require remediation/regression/monitoring.
- **Seal equals correctness:** immutability preserves mistakes as faithfully as correct artifacts.
- **Draft equals current standard:** status and stability matter more than the highest version number.
- **Metric equals target:** apply Goodhart-aware paired measures and review unintended behavior.

## Subtraction and interface tests

For each selected fragment, answer:

1. What unique failure or uncertainty does it handle?
2. What artifact or decision does it produce?
3. Who or what consumes that output?
4. How is the output validated independently?
5. What happens if it is removed?
6. Does it duplicate or contradict another fragment?
7. Are its assumptions preserved at the interface?
8. Is its cost proportional to criticality and reversibility?

Remove a fragment when answers 1–5 are weak. Redesign an interface when answer 7 is no.

## When to split this router into separate executable skills

Keep a method as a catalog card until it has most of these properties:

- a distinct trigger unlikely to collide with general method selection;
- a repeatable end-to-end workflow;
- low degrees of freedom or safety-critical sequencing;
- dedicated templates, scripts, tools, or schemas;
- domain-specific validation and failure handling;
- reference volume that burdens unrelated requests.

Good future skill candidates include systematic-review execution, causal-impact analysis, process mining, formal model checking, ISO management-system implementation/audit, secure threat modeling, AI-system assurance, regulated legal research, investment-model assurance, life-cycle assessment, technology/manufacturing-readiness review, logistics-network optimization, medical-device assurance, emergency/continuity planning, go-to-market design, marketing-incrementality evaluation, content-distribution planning, journalistic verification, behavior-intervention design, participation-process design, usability research, service-design execution, and accessibility assurance. Split only after the catalog router identifies a stable executable workflow, inputs, gates, and validation rules. Do not create one skill per acronym or platform.
