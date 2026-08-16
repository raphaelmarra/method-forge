# Software, systems, architecture, integration, and delivery

Use this catalog for lifecycle design, system boundaries, architecture decisions, APIs, events, distributed state, deployment, and software-delivery flow. Combine it with requirements/formal methods and testing/security for critical systems.

## Contents

1. Lifecycle and engineering approaches
2. Compiler, contract-pipeline, discovery, and documentation
3. Enterprise, business, domain, and component architecture
4. API and message contracts
5. Distributed state and resilience
6. Delivery, change risk, and research anchors

## Lifecycle and engineering approaches

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 12207 | software lifecycle process standard | establish a comprehensive, tailorable map of acquisition, development, operation, maintenance, and disposal responsibilities | copy every process as a prescriptive team workflow |
| ISO/IEC/IEEE 15288 | systems lifecycle process standard | manage a system-of-interest across conception, development, use, support, and retirement | software-only sprint recipe or detailed engineering technique |
| Waterfall | predictive lifecycle model | scope, interfaces, technology, and verification baseline are unusually stable and change is costly/controlled | exploratory product work or use as a strawman for all predictive work |
| V-Model | lifecycle/V&V mapping | decomposition levels need corresponding integration and verification/validation plans | interpret as strictly one-pass or postpone all feedback until the end |
| Iterative and Incremental Development | lifecycle strategy | reduce technical and requirement risk through successive working increments | increments cannot be independently evaluated or integrated safely |
| Spiral Model | risk-driven lifecycle | large/high-risk work benefits from repeated objective, risk, development, and review cycles | small low-risk delivery where risk-analysis overhead dominates |
| Rational Unified Process (RUP) | iterative process framework | use-case, architecture-centric work needs explicit inception/elaboration/construction/transition tailoring | install the full historical process or tool suite mechanically |
| DevOps | sociotechnical operating philosophy/practice family | shorten development-to-operations feedback and share delivery/reliability ownership | rename an operations team “DevOps” or treat it as CI tooling only |
| DevSecOps | security-integrated delivery approach | security feedback, controls, provenance, and remediation must live throughout delivery | add scanners without ownership, threat models, or risk decisions |
| Continuous Integration | integration practice | changes can be merged frequently and validated automatically | long-lived branches, flaky suites, or no actionable feedback |
| Continuous Delivery / Deployment | delivery discipline | software should remain releasable or release automatically through trusted pipelines | environments, tests, migrations, and rollback are uncontrolled |
| Trunk-Based Development | branching practice | teams can integrate small changes frequently behind suitable controls | work cannot be decomposed safely or mainline verification is too slow/unreliable |

## Compiler and contract-pipeline architecture

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Canonical Intermediate Representation (IR) | compiler architecture pattern/artifact | heterogeneous documentation/specifications must normalize into one analyzable and generatable semantic model | IR becomes an unversioned second source of truth or cannot express source uncertainty |
| Parse → Normalize → Enrich → Validate → Lower/Generate | compiler pipeline pattern | distinct transformations need explicit inputs, invariants, diagnostics, and incremental invalidation | stages are names only and probabilistic decisions remain hidden |
| Typed AST / Structured Command | execution representation | commands and arguments must remain typed, inspectable, escapable, and policy-checkable | generate opaque shell strings from untrusted or model-produced text |
| Translation Validation | per-compilation assurance technique | verify each generated artifact preserves the input IR semantics when proving the entire compiler is impractical | validator duplicates the compiler's same bug or semantic equivalence is undefined |
| Compiler Verification | formal assurance approach | a stable critical compiler and semantic model justify a proof of transformation correctness | volatile pipeline, unsupported source assumptions, or per-output validation is sufficient |
| Differential / Golden Translation Tests | compiler regression techniques | old/new compilers or reviewed fixtures can reveal changed translations | legacy output is assumed perfect or fixtures omit semantic edge cases |
| Incremental Compilation | compilation technique | changed sources should reprocess only affected nodes with correct dependency invalidation | caches/dependencies cannot be proven fresh or total rebuild is cheap |
| Source Map / Field Provenance | traceability artifact | every generated field/action must trace to source, transformation, version, and confidence | provenance is mistaken for semantic correctness |

## Architecture discovery and documentation

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | architecture-description standard | stakeholders, concerns, viewpoints, views, and rationale require disciplined representation | expect it to prescribe an architecture style or implementation |
| C4 Model | multilevel architecture-communication model | explain system context, containers, components, and code to distinct audiences | behavioral, deployment, timing, or data semantics are the main question |
| Architecture Decision Records (ADR/MADR) | decision artifact/practice | material, durable decisions need context, alternatives, status, and consequences | log trivial choices or rewrite history instead of superseding decisions |
| Architecture Tradeoff Analysis Method (ATAM) | scenario-based evaluation method | quality-attribute trade-offs and architectural risks need stakeholder evaluation | detailed code review or small feature choice |
| Quality Attribute Workshop (QAW) | elicitation method | stakeholders must turn “secure/fast/reliable” into prioritized scenarios | requirements are already measurable and agreed |
| Attribute-Driven Design (ADD) | architecture-design method | architecture should be decomposed from prioritized quality-attribute drivers | solution shape is trivial or drivers remain unvalidated |
| Cost Benefit Analysis Method (CBAM) | economic extension to architecture analysis | architectural strategies need value, cost, schedule, and uncertainty comparison | estimates cannot be made even as ranges or options are not yet concrete |
| Architecture Fitness Functions | evolutionary-architecture mechanism | continuously test architectural characteristics as systems evolve | critical qualities cannot be observed by the chosen proxy |
| Architecture Recovery / Reverse Engineering | analysis family | actual system structure differs from or lacks documentation | infer intent or correctness solely from code dependencies |
| Dependency Structure Matrix | structure-analysis method | coupling, sequencing, clustering, and cycles among components or teams matter | dynamic interaction or semantic behavior requires richer models |

## Enterprise and business architecture

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| TOGAF | enterprise-architecture framework/method | a large organization needs governed capability, architecture-development, transition, and repository practices | a small product architecture or wholesale template adoption |
| ArchiMate | enterprise-architecture modeling language | business, application, technology, motivation, strategy, implementation, and migration views need a shared notation | detailed software behavior, data schema, or decision logic |
| Zachman Framework | enterprise-architecture taxonomy | classify architectural descriptions by interrogative and stakeholder perspective | treat the ontology as a delivery method or require every cell |
| BIZBOK / Business Architecture | business-architecture body of knowledge | capabilities, value streams, organization, information, products, and initiatives need strategic alignment | software component design or process notation by itself |
| Capability Mapping | business-architecture technique | plan investments and ownership around what the enterprise must be able to do | infer process performance or system design from capability names |
| Value Stream Mapping (business architecture) | strategic flow artifact | relate stakeholder value stages to capabilities and initiatives | confuse with Lean's detailed operational value-stream map without declaring level |

## Domain and component design

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Domain-Driven Design (DDD) | strategic/tactical design discipline | complex business rules and language justify bounded contexts and domain models | simple CRUD, commodity domain, or ceremony without domain experts |
| Event Storming | collaborative domain-discovery technique | surface domain events, commands, policies, actors, hotspots, and boundaries | treat workshop output as final architecture or canonical truth |
| Context Mapping | DDD relationship technique | bounded contexts evolve under different teams/models and need integration strategy | one coherent small model with no boundary tension |
| Hexagonal / Ports and Adapters | architectural pattern | business logic needs isolation from volatile interfaces and infrastructure | create empty layers around a trivial application |
| Clean Architecture / Onion | dependency-direction pattern family | stable policies must remain independent of frameworks and delivery details | apply diagram dogmatically or duplicate models without change pressure |
| Layered Architecture | architectural pattern | responsibilities naturally separate and call direction can remain disciplined | latency, independent scaling, or cross-layer behavior makes layers a tax |
| Modular Monolith | deployment/architecture strategy | strong module boundaries are useful but distributed operational cost is not justified | independent scaling/deployment or trust boundaries are hard requirements |
| Microservices | distributed architecture style | bounded capabilities need independent ownership/deployment/scale and the organization can operate distribution | modularity alone; weak boundaries, small team, or no platform/observability maturity |
| Service-Oriented Architecture (SOA) | service architecture style | enterprise capabilities, integration, contracts, and reuse cross many systems | central governance becomes a bottleneck or services lack genuine autonomy |
| Event-Driven Architecture (EDA) | architecture style | decoupling in time, reactive flows, and event histories are valuable | causal order, contracts, failure semantics, and observability are unspecified |
| CQRS | read/write separation pattern | query and command models have materially different scale, shape, or consistency needs | ordinary CRUD or system-wide default |
| Event Sourcing | persistence/modeling pattern | events are the source of truth and audit/replay/temporal decisions justify complexity | mutable history, privacy deletion, schema evolution, and replay cannot be governed |

## API and message contracts

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| REST architectural style | distributed-system constraints/style | resource-oriented network interactions benefit from uniform interface and HTTP semantics | merely label any JSON-over-HTTP endpoint “REST” |
| OpenAPI | HTTP API description specification | operations, parameters, messages, schemas, and security need machine-readable contracts | business workflow, correctness proof, or event contract |
| Arazzo | API workflow specification | call sequences, dependencies, runtime expressions, and success criteria span API operations | general business-process engine or dynamic planner |
| JSON Schema | data-validation language | JSON instances need structural constraints and reusable vocabularies | truth, authorization, referential integrity, or business effects by itself |
| AsyncAPI | message-driven API description specification | channels, messages, operations, servers, and bindings need machine-readable contracts | purely synchronous HTTP flow |
| CloudEvents | event-envelope specification | event metadata should interoperate across transports and producers | domain event semantics, delivery guarantee, or schema governance by itself |
| Protocol Buffers / gRPC | IDL and RPC framework | typed low-overhead service communication and streaming fit the ecosystem | browser-first public APIs or teams needing simple debuggable HTTP/JSON |
| GraphQL | query language/runtime specification | clients need flexible graph-shaped reads and one evolving schema | simple command APIs, field-level authorization becomes unsafe, or caching/cost controls are absent |
| Consumer-Driven Contracts | integration-testing practice | independently deployed consumers must declare and verify provider expectations | provider semantics cannot be reduced to examples or all components deploy atomically |
| Semantic Versioning | versioning convention | public compatibility meaning maps coherently to major/minor/patch releases | automatically version unbounded behavior or APIs without a compatibility policy |
| API evolution/deprecation policy | lifecycle governance | consumers update asynchronously and breaking change risk is material | a closed disposable integration updated atomically |
| HTTP problem details | error representation standard | machine-readable HTTP errors need common shape and extension points | conceal domain-specific recovery semantics or security-sensitive detail |
| OAuth/OIDC patterns | authorization/identity protocol family | delegated authorization and federated authentication match the trust model | invent flows, confuse authentication with authorization, or omit current security BCPs |

## Distributed state and resilience patterns

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Failure Models | reasoning model | crashes, omission, timing, Byzantine behavior, or partitions change design guarantees | assume all remote errors are identical |
| Consistency Models | reasoning model | replicas/clients need explicit read/write visibility guarantees | use “eventual consistency” without bounded business behavior |
| CAP / PACELC | trade-off models | reason about consistency, availability, partitions, and normal-operation latency | cite CAP as a universal database ranking or ignore the exact operation/guarantee |
| Saga | distributed transaction pattern | multi-step business transactions need forward recovery/compensation across services | a local ACID transaction suffices or effects cannot be compensated acceptably |
| Transactional Outbox | consistency pattern | database state and event/message publication must not diverge | external effect is not coupled to a local transaction or consumers cannot deduplicate |
| Inbox / Idempotent Consumer | message-processing pattern | at-least-once delivery can repeat processing | deduplication key/scope and retained history are undefined |
| Idempotency Key | API reliability pattern | clients may retry a logically single write after uncertain outcomes | key reuse, request equivalence, storage duration, and response replay are unspecified; verify provider semantics rather than assume one universal HTTP standard |
| Timeout / Deadline / Cancellation | remote-call control | bounded waiting and abandoned work must propagate | timeout is chosen arbitrarily or cancellation cannot safely stop effects |
| Retry with exponential backoff and jitter | transient-failure tactic | failures are plausibly transient and operations/retries are safe | permanent errors, overload amplification, or non-idempotent effects |
| Circuit Breaker | resilience pattern | repeated dependency failure should fail fast and allow recovery probes | use without timeouts, fallback semantics, or monitoring |
| Bulkhead | isolation pattern | one dependency/tenant/workload can exhaust shared resources | hard partitions create waste without protecting a material failure boundary |
| Rate Limiting / Load Shedding | overload controls | demand can exceed safe capacity and rejection/degradation policy is explicit | silently discard obligated work or substitute for capacity planning |
| Backpressure | flow-control mechanism | downstream capacity must regulate upstream production | protocols cannot carry demand signals or buffers merely shift overload |
| Optimistic Concurrency / ETag / CAS | concurrency-control pattern | conflicts are uncommon, detectable, and retry/merge semantics exist | high contention or invariants need serialization |
| Lease with Fencing Tokens | distributed coordination pattern | stale lock holders could still act after a lease expires | ordinary in-process mutex or storage cannot enforce fencing |
| Consensus / Leader Election | distributed algorithm family | components need one ordered decision or authoritative leader despite failures | coordination-free convergence is acceptable or operational complexity outweighs value |
| CRDT | convergent data-type family | concurrent/offline updates must merge without coordination and a lawful merge exists | global invariants or business conflict semantics cannot be encoded |

## Delivery and change risk

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Infrastructure as Code | operations practice | infrastructure needs versioned, repeatable, reviewable desired state | unmanaged secrets, manual drift, or generated code without state governance |
| GitOps | operations model | reconciliation from declarative versioned desired state fits platform operations | non-declarative systems or emergency paths lack controlled reconciliation |
| Blue–Green Deployment | release pattern | parallel environments permit rapid traffic switch and rollback | state/data migration prevents backward compatibility or duplicate cost is prohibitive |
| Canary Release | progressive-delivery pattern | reliable guardrail metrics can bound exposure to a change | low traffic, long-latency harm, or metrics cannot distinguish regressions |
| Feature Flags | release/control technique | separate deployment from exposure and target controlled cohorts | flags lack ownership, expiry, test matrices, or security boundary controls |
| Expand–Migrate–Contract | compatibility migration pattern | schemas/interfaces must evolve without coordinated downtime | consumers cannot coexist across versions or cleanup never happens |
| Strangler Fig | modernization pattern | incrementally replace a legacy boundary while preserving service | routing/boundary is unclear or dual operation creates unacceptable inconsistency |
| DORA Metrics | delivery-performance measures | evaluate software delivery throughput and instability at team/system level | rank individuals, optimize one metric, or compare unlike contexts without interpretation |

## Research anchors and volatile versions

- ISO/IEC/IEEE 12207 and 15288; ISO/IEC/IEEE 42010.
- OpenAPI Initiative for OpenAPI and Arazzo; JSON Schema organization; AsyncAPI Initiative; CNCF CloudEvents.
- IETF/RFC Editor for HTTP, OAuth, problem details, and deprecation semantics.
- Official GraphQL and gRPC specifications.
- DORA and Google SRE primary guidance for delivery and reliability measures.
- The Open Group for TOGAF and ArchiMate; Business Architecture Guild for BIZBOK. Treat proprietary bodies of knowledge as references, not efficacy proof.
- Recheck all live specifications at research time. Record stable vs draft rather than copying the numerically largest release.
