# Requirements, contracts, formal methods, and planning

Use this catalog when intent must become explicit requirements, operations, states, properties, plans, and proofs. Select the least formal representation that can control the material risk; increase rigor where ambiguity, concurrency, irreversibility, or certification demands it.

## Requirements discovery and specification

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 29148 | requirements engineering standard | establish disciplined elicitation, analysis, specification, validation, and management | adopt every artifact in low-risk work without tailoring |
| Stakeholder Needs / Concept of Operations | early lifecycle artifacts | intended use, users, environment, missions, and operational scenarios must align | jump directly to implementation-specific requirements |
| GORE | requirements engineering family | goals, soft goals, obstacles, and responsibility refinement matter | interfaces are stable and the missing issue is implementation detail |
| KAOS | goal-oriented method/notation | formal goal refinement, obstacle analysis, and agent assignment justify rigor | a tiny feature or no access to goal owners |
| i* / GRL | goal/actor modeling family | actor dependencies, intentions, and trade-offs drive the system | detailed executable behavior is the main need |
| Use Cases | interaction-specification technique | actor–system scenarios and alternate flows clarify functional behavior | nonfunctional qualities, data invariants, or concurrent protocols alone |
| User Stories | lightweight requirement placeholders | collaborative product teams can refine value and acceptance near implementation | complete contractual specification, architecture quality, or no access to users |
| Job Stories | context/motivation requirement form | situation and desired progress explain behavior better than persona framing | precise system responses and constraints are required |
| BDD / Specification by Example | collaborative specification/testing method | business rules can be clarified through concrete executable examples | replace generalized properties, performance, security, or exploration |
| EARS | controlled natural-language pattern | reduce ambiguity in event/state-driven requirements without full formalism | complex quantitative or temporal logic exceeds the templates |
| Quality Attribute Scenarios | nonfunctional-requirement technique | source, stimulus, environment, artifact, response, and measure can make qualities testable | list “fast/scalable/secure” without scenarios and priorities |
| ISO/IEC 25010 quality model | product-quality reference model | systematically consider relevant product quality characteristics | treat every characteristic as equally important or as a test plan |
| Requirements Traceability | lifecycle practice | needs must connect to design, implementation, tests, evidence, and change impact | create links without verifying their semantics and completeness |

## Contracts and decision logic

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Design by Contract | programming/design method | local operations expose executable preconditions, postconditions, and invariants | environment assumptions, distributed effects, and business authorization remain implicit |
| Hoare Logic | correctness logic | prove command behavior against pre/post assertions | concurrency, time, I/O uncertainty, or liveness dominates |
| Assume–Guarantee Reasoning | compositional verification method | component proofs can be decomposed with explicit environmental contracts | circular or unverified assumptions make the proof vacuous |
| Contract-Based Design | system/component method family | compose independently developed components through assumptions and guarantees | use “contract” to mean schema only |
| IOPE | capability-description model | machine composition needs inputs, outputs, preconditions, and effects | operational semantics, identity, transaction recovery, and trust are missing |
| Decision Tables | tabular decision technique | finite condition combinations need gap/overlap analysis and actions | temporal/stateful behavior or irreducible human judgment |
| DMN | decision notation/metamodel/language | repeatable business decisions should be separated from workflow and made executable/explainable | open-ended strategy or long-running orchestration |
| SBVR | business vocabulary/rules specification | shared terms and declarative business rules need semantic discipline | procedural workflow and implementation details |
| OCL | constraint language | invariants and pre/postconditions over UML/MOF models need formal expression | general distributed behavior or team lacks model/tooling adoption |

## State and formal specification

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Finite State Machines | behavioral formalism | a finite lifecycle with allowed transitions drives correctness | unbounded variables/concurrency explode the model without abstraction |
| Statecharts | hierarchical/concurrent state formalism | state hierarchy, orthogonal regions, and events exceed flat FSMs | simple linear lifecycle |
| Petri Nets | concurrency/workflow formalism | synchronization, resource tokens, reachability, deadlock, or process mining matter | rich data/continuous behavior needs another formalism |
| Temporal Logic | property formalism | safety, liveness, ordering, and eventuality must be stated precisely | stakeholders cannot validate the abstraction and no verification follows |
| TLA+ | temporal specification language/method | distributed/concurrent algorithms need invariant and behavior exploration | simple stateless logic or specification cannot be maintained |
| PlusCal | algorithm language translating to TLA+ | imperative/pseudocode form makes temporal modeling more accessible | use without understanding generated TLA+ semantics/properties |
| Alloy | relational modeling language/analyzer | structural constraints, scopes, and counterexample search fit the problem | unbounded proof or real-time behavior is central |
| Z / B / Event-B | state-based formal specification families | refinement and proof obligations justify mathematical rigor, often in critical systems | low-risk work or no formal-method capability/toolchain |
| Model Checking | verification family | finite/abstract state exploration can find counterexamples to explicit properties | claim the implementation is proven when only an incomplete model was checked |
| Theorem Proving | deductive verification family | high-assurance properties need machine-checked proofs beyond bounded exploration | specification/proof cost exceeds impact or proof assumptions cannot connect to code |
| Runtime Verification | monitoring method | properties can be checked on execution traces when static proof is impractical | detect violations only after irreversible harm without prevention controls |

## Automated planning and orchestration

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Classical Planning | planning model family | deterministic, fully observable discrete state/actions approximate the domain | uncertainty, partial observability, exogenous change, or continuous control dominates |
| STRIPS | action representation | add/delete effects and conjunctions provide sufficient abstraction | conditional, numeric, temporal, or probabilistic behavior is material |
| PDDL | planning language family | standardized planner/domain interchange and automated search justify modeling | fixed short workflows or agent cannot trust the learned action model |
| HTN Planning | hierarchical planning formalism | trusted domain procedures can decompose business goals into primitive operations | novel tasks lack methods or methods conceal unsafe assumptions |
| Temporal Planning | planning variant | duration, deadlines, overlap, and resources influence feasible plans | time is irrelevant or model precision is unavailable |
| Numeric / Metric Planning | planning variant | quantities, resources, and plan costs affect action selection | numeric fluents create false precision without reliable updates |
| Contingent Planning | planning variant | observations during execution determine branches | outcome uncertainty is too broad for enumerable contingencies |
| Probabilistic Planning / MDP | sequential decision model | transitions/rewards are stochastic and estimable under full observability | probabilities/rewards are undefendable or safety cannot be reduced to expected reward |
| POMDP | sequential decision model | hidden state and information-gathering actions are central | state/action spaces and models make computation or validation infeasible |
| Behavior Trees | reactive control representation | modular fallback/sequence/parallel control suits robotics or game agents | business transactions need explicit durable state and audit semantics |
| BPMN / Workflow Engines | process representation/runtime family | known roles, events, messages, timers, and long-running coordination dominate | dynamic goal planning or business rules are buried inside gateway spaghetti |
| Arazzo | API workflow description | a known outcome requires a documented sequence of API calls and data bindings | general planning, human organizational process, or recovery semantics exceed the spec |

## Model-Based Systems Engineering

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| MBSE | systems engineering approach | multiple disciplines need an authoritative connected model across lifecycle | models become documentation duplicates without decisions or verification |
| SysML | systems modeling language | structure, behavior, requirements, and parametrics need integrated system models | software-only implementation detail or no model governance/tooling |
| Digital Thread | lifecycle information architecture | artifacts and evidence must remain connected across engineering/manufacturing/operation | marketing label without identifiers, configuration control, and provenance |
| Digital Twin | live model/system pattern | decisions benefit from synchronized operational representation and validated models | any dashboard or static model is relabeled a twin |

## Formality ladder

Escalate only as needed:

1. examples and acceptance criteria;
2. controlled language, schemas, and decision tables;
3. state machines, contracts, and executable models;
4. property-based/model-based tests and runtime monitors;
5. model checking or bounded analyzers;
6. theorem proving and certified artifacts.

Do not skip validation with domain stakeholders at higher levels; formalizing the wrong requirement only makes the wrong thing precise.

## Research anchors

- ISO/IEC/IEEE 29148 and ISO/IEC 25010.
- OMG specifications for DMN, SBVR, OCL, UML/SysML.
- Official TLA+, Alloy, Event-B, and planning-language sources or seminal papers.
- Planning formalisms must be researched by their assumptions: observability, determinism, time, cost, uncertainty, and hierarchy.
