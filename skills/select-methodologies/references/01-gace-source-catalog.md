# GACE source catalog, normalized

## Contents

1. Purpose and discovery/process improvement
2. Contracts, goals, requirements, and planning
3. API, workflow, data, evidence, and entity reasoning
4. Optimization, architecture, verification, and gates
5. Risk, testing, state, concurrency, and transactions
6. Artifact lifecycle, metrics, and local compositions

## Purpose

This file preserves every concept from the supplied GACE list while correcting its object type. It is a discovery index, not evidence that every item should be implemented. Expand shortlisted entries with the method-card schema in `00-taxonomy-selection.md` and verify current versions online.

## Discovery and process improvement

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Double Diamond | discovery/design framework | diverge and converge around an unclear problem and possible solutions | a control system, implementation method, or substitute for validation |
| DMAIC | process-improvement methodology within Six Sigma | an existing process is measurable and defect or variation reduction is the goal | a greenfield discovery method or synonym for all of Six Sigma |
| Root Cause Analysis | family of analysis techniques | evidence of a failure exists and the causal mechanism must be found | a ritual that stops at the first “why” or assumes one root cause |
| Trade-off Analysis | decision-analysis family | alternatives create explicit conflicts among objectives | a choice without criteria, uncertainty, or stakeholder values |
| MECE | structuring heuristic | organize a decomposition to reduce overlap and obvious omission | proof that coverage is actually exhaustive |
| Coverage Criteria | acceptance concept and metrics | define observable completion for search, requirements, states, branches, or evidence | the vague claim “we researched everything” |

## Contracts, goals, and requirements

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Design by Contract (DbC) | software design method | operations can expose preconditions, postconditions, and invariants | a complete requirements-discovery or distributed-transaction method |
| Hoare Logic / triples | formal logic | prove partial or total correctness of commands against assertions | the sole model for concurrency, time, or uncertain external effects |
| Assume–Guarantee Reasoning | compositional verification method | component guarantees can be proven under explicit environmental assumptions | reliable assurance when assumptions are unverified or interactions escape boundaries |
| Contract-Based Design | systems/design framework family | compose components through formalized assumptions and guarantees | mere API schema validation |
| Goal-Oriented Requirements Engineering (GORE) | requirements discipline/family | stakeholder intent must be refined into goals, obstacles, and responsibilities | endpoint-level interface specification by itself |
| KAOS | GORE methodology and notation | goals, obstacles, agents, and requirements need systematic refinement | a lightweight choice when goals and ownership are already obvious |
| IOPE | semantic capability-description model | describe service inputs, outputs, preconditions, and effects for discovery/composition | a transport protocol, complete workflow language, or runtime guarantee |

## Automated planning and semantic composition

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Classical Automated Planning | AI planning discipline/model family | actions, states, goals, and effects can be modeled explicitly | a default for partially observable, stochastic, or continuously changing domains |
| STRIPS | planning representation | a compact add/delete action model is sufficient | a rich model for numeric, temporal, probabilistic, or conditional effects |
| PDDL | planning-domain language family | planner interoperability and explicit domain/problem files justify the modeling cost | a simple fixed business workflow with no dynamic planning need |
| HTN planning | planning formalism | business goals decompose through reusable domain methods into primitive actions | open-ended planning when no trustworthy method library exists |
| OWL-S | ontology for semantic web services | RDF/OWL semantics, capability discovery, and grounding are ecosystem requirements | a lightweight wrapper around conventional REST APIs |
| Semantic Web Services | research/engineering discipline | machine discovery and composition require shared semantics across services | a single product with stable, controlled endpoints |
| Service Grounding | mapping technique/layer | connect an abstract capability or semantic operation to concrete protocol calls | a replacement for capability semantics or workflow reasoning |
| Semantic Service Composition | planning/composition technique family | services can be selected and chained from semantic inputs, outputs, and conditions | reliable execution without handling identity, state, side effects, and recovery |

## API and workflow representation

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| OpenAPI | API description specification | describe HTTP API operations, messages, security schemes, and reusable schemas | business semantics, multi-call workflow proof, or runtime correctness |
| JSON Schema | schema language | validate JSON structure, constraints, and conditional shape | validate external truth, authorization, or semantic intent by itself |
| Specification-first / API-first | lifecycle principle | a machine-readable contract should lead implementation and integration | a guarantee that the contract is complete, usable, or current |
| Arazzo | API-workflow description specification | express multi-call sequences, dependencies, data bindings, and success criteria around API descriptions | a full business-process engine or general-purpose planner |
| MCP | tool/context interoperability protocol | expose resources and callable tools consistently to AI applications | an orchestration, planning, authorization, or business-contract methodology |
| Tool / function calling | model capability and interaction pattern | constrain model actions to typed callable interfaces | evidence that the model selected the right tool or that execution was correct |
| DMN | decision notation, metamodel, and expression language | separate repeatable decision logic from process flow | orchestration of long-running work or unstructured judgment without explicit rules |
| BPMN | business-process notation and metamodel | communicate and exchange process flow, events, roles, and orchestration semantics | automatic correctness, root-cause analysis, or a universal runtime model |

## Data resolution, evidence, and entity reasoning

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Dataflow Analysis | analysis family | trace definitions, uses, transformations, and downstream consumption | business-authority or semantic-equivalence proof |
| Data Dependency Analysis | analysis technique | required fields depend on outputs from prior operations or sources | complete process, control-flow, or state analysis |
| Resolver Pattern / Contracts | architectural pattern, local contract form | required facts need explicit acquisition, ambiguity, validation, and failure rules | a single hidden “lookup” that guesses identities or authorization |
| Data Provenance | information-management discipline | values and transformations must be attributable and reproducible | evidence quality by itself; provenance can faithfully record a bad source |
| W3C PROV / PROV-DM / PROV-O | provenance model family and ontology | interoperable entity–activity–agent lineage is valuable | mandatory RDF complexity for every local audit log |
| Claim–Evidence Model | assurance/argument pattern | material claims must link to supporting evidence and status | proof that evidence is sufficient without an inference rule or review |
| Epistemic Reasoning | logic/philosophical discipline | distinguish known, inferred, unknown, conflicting, and agent-relative knowledge | a database truth flag without source and inference semantics |
| GAT-R | organization-local evidence methodology | classify relation and evidence strength inside GACE | an externally standardized or independently validated method unless evidence is added |
| Entity Lifecycle Analysis | domain-analysis technique | absence, creation, update, duplication, historical state, and retirement affect actions | a static CRUD inventory |
| Cardinality Analysis | data/query analysis technique | zero, one, or multiple matches imply different safe behavior | identity resolution based only on row count |
| Decision Tables | decision artifact and technique | finite conditions and actions require completeness and overlap checks | complex temporal behavior or tacit judgment that cannot be enumerated |
| Case-Based Reasoning (CBR) | reasoning paradigm | prior cases can inform similarity-based suggestions or adaptation | current authorization, factual truth, or policy without independent validation |

## Optimization and structural architecture

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Multi-objective Optimization | optimization discipline/family | cost, risk, latency, uncertainty, or quality conflict and a feasible set exists | a decision with unknown objectives, constraints, or incomparable consequences |
| Pareto frontier | dominance concept and analysis | expose non-dominated alternatives without forcing premature weights | a unique recommendation; Pareto optimal does not mean acceptable |
| Irreducibility Analysis | local minimality heuristic | test whether removing an operation breaks goal, safety, or proof | global optimality or evidence that no better plan exists |
| Design Structure Matrix (DSM) | dependency-modeling method/artifact | sequence, cluster, and analyze coupled components, tasks, or teams | behavior, timing, or semantic correctness beyond dependencies |
| Cost Function / Plan Cost | optimization model artifact | encode calls, latency, tokens, risk, and uncertainty for plan comparison | objective truth when weights and penalties are arbitrary or gameable |

## Verification, traceability, and gates

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Systems Engineering V&V | lifecycle discipline | distinguish conformance to specification from fitness for intended use | a single final testing phase |
| Requirements Traceability | lifecycle practice and relation model | connect needs to requirements, design, implementation, tests, and evidence | proof that traced requirements are correct or complete |
| Requirements Verification Matrix | assurance artifact | make each requirement's verification method, result, and evidence explicit | the verification activity itself |
| Stage-Gate | governance process | investment or risk decisions need independent checkpoints between stages | rapid low-risk flow when gates add delay without decision value |
| Shift-left verification/testing | lifecycle principle | earlier feedback can reduce expensive downstream escape and rework | shifting every test earlier regardless of realism or environment needs |

## Risk, hazards, and assurance

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Pre-mortem | prospective risk elicitation technique | counter optimism by assuming failure and generating plausible causes | quantified risk analysis or evidence that controls work |
| FMEA | bottom-up failure analysis method | enumerate component/process failure modes, effects, causes, and controls | system-interaction hazard analysis or precise risk ranking from subjective scores alone |
| STPA | systems-theoretic hazard analysis method | unsafe control actions and interactions matter in complex sociotechnical systems | a lightweight defect list for simple non-safety work |
| Assurance Case | structured argument and evidence artifact/family | stakeholders need an explicit justification that a critical claim is acceptably supported | a decorative claim tree detached from test evidence and defeaters |
| GSN | assurance-case notation | communicate goal–strategy–context–solution argument structures | an assurance method or sufficiency proof by notation alone |
| SACM | assurance-case metamodel/specification | exchange or tool assurance artifacts across structured ecosystems | a necessary representation for small local arguments |

## Testing and adversarial validation

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Fault Injection | resilience-test technique | observe behavior under deliberate dependency, resource, or timing failures | uncontrolled experiments on production without blast-radius controls |
| Property-Based Testing | generative-test technique | invariants hold across broad generated input spaces | a substitute for oracle design or stateful/system tests when generators are weak |
| Model-Based Testing | test-generation/verification method | a behavioral model can generate sequences and expected outcomes | a cheap choice when maintaining a faithful model costs more than risk warrants |
| Contract Testing | integration-test family | consumer/provider expectations must be checked independently of full end-to-end tests | validation of business intent or compatibility outside modeled interactions |
| Fuzzing | automated robustness/security-test technique | parsers, schemas, protocols, and input boundaries face malformed or unexpected values | coverage of semantic workflows or authorization logic by itself |
| Mutation Testing | test-suite assessment technique | determine whether tests detect plausible code or rule changes | routine execution when mutation cost is disproportionate or mutants are meaningless |
| Red Teaming | adversarial evaluation practice | an independent attacker perspective should challenge controls and assumptions | a one-off performance that replaces systematic testing and remediation |
| Iterative Red Teaming | improvement loop | attack findings will be fixed, retested, and regression-controlled | an unbounded cycle without risk-based stopping criteria |

## State, concurrency, and transaction semantics

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Finite State Machine | behavioral model/formalism | finite states and allowed transitions determine safe behavior | a natural fit for unbounded data or highly concurrent interaction without extensions |
| Model Checking | exhaustive/state-space verification family | formal models and properties justify exploring reachable behaviors | a proof about the implementation when the model is unfaithful |
| TLA+ | formal specification language and method ecosystem | distributed/concurrent protocols need temporal invariants and behavior exploration | a default for simple stateless CRUD or teams unable to maintain the specification |
| Safety and Liveness Properties | temporal-property classes | state what must never happen and what must eventually happen | a complete specification without fairness, assumptions, and domain properties |
| Idempotency Analysis | operation-analysis technique | retries can repeat writes or effects | an assumption that an HTTP verb alone makes business effects idempotent |
| Compensating Transactions | distributed-workflow pattern | committed steps cannot be atomically rolled back and semantic undo is possible | true rollback or restoration when side effects are irreversible |
| Transaction Semantics | database/distributed-systems model family | distinguish commit, rollback, isolation, partial failure, and uncertain outcomes | a single boolean success/failure model for external writes |

## Artifact and compilation lifecycle

| Candidate | Type | Use when | Do not use as |
| --- | --- | --- | --- |
| Reproducible Builds | engineering property and practice | the same declared inputs should yield verifiably identical artifacts | provenance or security assurance without controlled inputs and dependencies |
| Artifact Sealing | local lifecycle/control pattern | freeze a reviewed package and prevent silent post-approval drift | proof that the sealed contents are correct |
| Checksums / cryptographic hashes | integrity primitive | detect byte-level change and bind manifests to content | authentication, trust, provenance, or semantic equivalence by itself |
| Docs-as-Code | documentation practice | review, version, test, and publish technical documentation through engineering workflows | justification for treating every collaborative document like source code |
| Artifact Lifecycle Management | lifecycle practice/model | artifacts mature through explicit states with entry/exit criteria | a cosmetic status field without transitions, ownership, or evidence |
| Canonical Intermediate Representation (IR) | compiler artifact/architectural pattern | normalize heterogeneous source representations before analysis and generation | a second source of truth that drifts from inputs and outputs |
| Compiler Architecture / IR pipeline | architectural pattern | parse, normalize, enrich, validate, and compile knowledge into executable artifacts | a metaphor that hides non-deterministic or human decisions |
| Incremental Compilation | compilation technique | changed inputs should reprocess only affected artifacts while preserving correctness | use without dependency invalidation and cache-consistency rules |
| Claim Lifecycle | local evidence-state pattern | claims progress explicitly from candidate to supported, verified, or rejected | a confidence score without criteria, provenance, and transition evidence |

## Proposed GACE metrics

These are local metrics, not established methodologies. Define denominator, sampling window, exclusions, and gaming controls before use.

| Metric | Intended signal | Main caution |
| --- | --- | --- |
| LLM Decision Surface | decisions still delegated to nondeterministic model judgment | not all decisions have equal risk; count weighted material decisions |
| Output Utilization Rate | outputs consumed downstream divided by outputs produced | a used output can still be low-value or harmful |
| Gate Escape Rate | faults first detected after their intended gate | requires reliable defect origin and detection-stage attribution |
| Evidence Coverage | material claims with adequate support divided by material claims | “adequate” needs an evidence policy and risk weighting |
| Machine-Verifiability Rate | criteria checked deterministically divided by all criteria | deterministic checks can verify the wrong property |
| Rework Rate | work repeated because prior outputs were defective or incomplete | separate learning-driven iteration from avoidable failure demand |

## Local composition proposals

| Composition | Classification | Intended use | Boundary |
| --- | --- | --- | --- |
| Pre-mortem → FMEA → Assurance Case | local risk-to-assurance chain | elicit failures, structure/prioritize them, then demand evidence for controls | add hazard/system methods when interaction risk exceeds component failure analysis |
| DMAIC with Double Diamond microcycles | local improvement/discovery composition | control a stable improvement program while diverging/converging inside Analyze and Improve | do not force Double Diamond into every DMAIC activity |
| DSM with Stage Contracts | local meta-architecture | analyze cross-stage dependencies while formalizing each stage's obligations and gate | add dynamic/state modeling when a static dependency matrix is insufficient |
