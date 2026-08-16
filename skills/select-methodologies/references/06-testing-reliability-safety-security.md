# Testing, reliability, safety, security, and assurance

Use this catalog to choose how confidence will be earned, not merely asserted. Separate verification of specified behavior, validation of intended use, safety/hazard control, reliability in operation, cybersecurity, and structured assurance.

## Contents

1. Test strategy, levels, generation, models, and oracles
2. Nonfunctional, operational, static, and change assurance
3. Safety, hazards, and reliability
4. Cybersecurity, privacy, and software supply chain
5. Structured assurance and research anchors

## Test strategy and levels

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 29119 family | software-testing standard family | a comprehensive tailorable test process, documentation, and technique baseline is needed | impose full documentation on small low-risk work without value |
| Risk-Based Testing | strategy | prioritize test depth and order by likelihood, impact, exposure, and detectability | permanently ignore “low-risk” areas or use subjective risk without review |
| Test Pyramid / Test Trophy | portfolio heuristics | balance fast local feedback against integration and user-facing confidence | enforce a shape independent of architecture and failure history |
| Unit / Component Testing | test levels | isolate logic and components for fast deterministic feedback | mock away every material contract or equate coverage with correctness |
| Integration Testing | test level | interfaces, persistence, protocols, and infrastructure interactions can fail | use only end-to-end tests or only mocked collaborators |
| System / End-to-End Testing | test level | realistic cross-component behavior and critical journeys require validation | build a slow brittle suite for every edge case |
| Acceptance Testing / UAT | validation practice | authorized stakeholders must assess fitness and contractual outcomes | defer all requirement clarification until final acceptance |
| Exploratory Testing | learning-oriented test approach | skilled testers need to investigate risks not captured by scripts | unstructured clicking without charter, notes, and follow-up |
| Session-Based Test Management | exploratory-test management method | exploratory work needs charters, timeboxes, debriefs, and coverage accounting | pretend session counts are quality outcomes |
| BDD / ATDD / Specification by Example | collaborative executable-specification family | concrete business examples can align requirement and acceptance | sole method for performance, security, concurrency, or generalized properties |
| Test-Driven Development (TDD) | design/development practice | rapid automated examples can drive small design steps and regression safety | UI/integration-heavy work without fast feedback or claim TDD proves requirement fitness |
| Characterization Testing | legacy-change technique | capture current observable behavior before refactoring poorly understood code | encode known defects as desired behavior without review |

## Generative, model, and oracle techniques

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Property-Based Testing | generative testing | invariants can be stated and generators/shrinking explore broad inputs | weak generators or tautological properties produce false confidence |
| Model-Based Testing | model-derived testing | a state/behavior model can generate sequences and expected results | model maintenance and oracle ambiguity exceed risk reduction |
| Combinatorial / t-way Testing | configuration technique | failures arise from interactions among many factors and exhaustive testing is infeasible | temporal sequences or rare high-order interactions dominate |
| Metamorphic Testing | oracle technique | exact expected outputs are unavailable but relations between runs are known | direct trustworthy oracle is cheap or metamorphic relations are speculative |
| Differential Testing | comparison technique | implementations, versions, or backends should agree on defined semantics | correlated defects or legitimate semantic differences are ignored |
| Golden / Snapshot Testing | regression technique | stable complex outputs need reviewable change detection | snapshots are approved blindly or hide semantic assertions |
| Fuzzing | automated robustness/security technique | parsers, protocols, and inputs face malformed/unexpected data | semantic authorization and long workflows remain untested |
| Grammar-Based / Stateful Fuzzing | fuzzing variants | structured languages or protocols need valid deep sequences | no grammar/state model or basic fuzzing is sufficient |
| Mutation Testing | test-suite assessment | determine whether tests kill plausible implementation/rule changes | cost is high, equivalent mutants dominate, or mutation operators are irrelevant |
| Fault Injection | failure-test mechanism | deliberate faults can reveal recovery and isolation behavior | no blast-radius control, abort condition, or observable oracle |

## Nonfunctional and operational testing

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Performance / Load Testing | performance test family | throughput and latency under representative load have targets | synthetic workload/environment cannot support inference |
| Stress / Spike Testing | overload test variants | saturation and abrupt demand behavior need characterization | confuse breaking point with normal capacity |
| Soak / Endurance Testing | longevity test | leaks, drift, accumulation, and degradation emerge over time | short test duration cannot expose the targeted mechanism |
| Scalability Testing | capacity test | scaling behavior, bottlenecks, and cost curves matter | report one benchmark point as scalability |
| Resilience Testing | system test family | failure/recovery/degradation across dependencies need validation | generic fault injection without expected system properties |
| Chaos Engineering | controlled experiment method | steady-state hypothesis, observability, blast radius, aborts, and learning loop exist | use as random breakage or before conventional tests and controls |
| Backup Restore / Disaster Recovery Drill | recovery validation | RPO/RTO and restoration integrity are material | possession of backups is treated as tested recovery |
| Game Day | operational rehearsal | teams need realistic practice of incidents, failover, or recovery | theater without objectives, observations, and corrective actions |
| Accessibility Testing | conformance/usability practice | users with disabilities and applicable accessibility standards matter | automated scans alone or compliance without user validation |
| Compatibility Testing | environment/contract testing | browsers, devices, protocols, versions, and consumers vary | undefined support matrix or exhaustive combinations without risk selection |

## Static and change-focused assurance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Static Analysis | analysis family | code/schema/config defects can be detected without execution | suppress findings wholesale or replace dynamic behavior tests |
| Type Systems / Refinement Types | correctness mechanism | classes of invalid states can be excluded at compile/check time | unsafe escape hatches or external truth/effects remain unmodeled |
| Formal Verification | assurance family | critical properties justify mathematical specification and proof/model checking | assumptions and abstraction cannot be validated against implementation |
| Code Review / Inspection | human verification method | design, maintainability, security, and context need independent review | rubber-stamp approval or sole control for mechanically detectable defects |
| Pair / Ensemble Programming | collaborative development technique | continuous review and shared design reduce handoff and concentration risk | participation is coerced or lacks psychological safety and focus |
| Change-Impact Analysis | analysis technique | select regression, reviewers, and controls from dependencies and traceability | hidden/runtime dependencies make selection unsound without escape monitoring |
| Regression Test Selection | optimization technique | a large suite needs safe change-aware subset execution | selection logic is unvalidated or full runs never detect escapes |

## Safety and hazard analysis

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Preliminary Hazard Analysis (PHA) | early hazard-identification method | early design needs hazard categories, consequences, and initial controls | final assurance or detailed causal analysis |
| FMEA / FMECA | bottom-up failure analysis | component/process failures and their effects/criticality can be enumerated | complex control interactions, software requirements flaws, or precise RPN ranking alone |
| Fault Tree Analysis (FTA) | top-down deductive hazard method | combinations of failures leading to a defined top event need analysis | discovery of unknown top events or human/system dynamics alone |
| Event Tree Analysis (ETA) | forward consequence analysis | initiating events branch through barrier success/failure to outcomes | state dependencies violate simple branch assumptions |
| HAZOP | structured deviation analysis | process parameters and guidewords can reveal hazardous deviations | software/control intent lacks meaningful process variables without adaptation |
| STPA | systems-theoretic hazard analysis | unsafe control actions, inadequate constraints, software/human interaction, and emergent behavior matter | low-risk simple component defect analysis |
| Bow-Tie Analysis | barrier-risk visualization | threats, top event, consequences, preventive and mitigative barriers need one view | quantitative proof or complex feedback dynamics |
| Safety Integrity Levels / assurance levels | risk-classification/control scheme family | domain standards require rigor proportionate to hazardous failure | invent generic SILs outside the applicable sector standard |
| Independent V&V | governance/assurance practice | consequences and conflicts of interest justify organizational independence | independence exists only on an org chart without technical authority/evidence access |
| Safety Case | assurance case for safety | regulator/stakeholders need explicit claims, argument, evidence, context, and defeaters | document created after design solely for approval |

## Reliability engineering

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Reliability Block Diagrams | reliability model | component configurations and failure probabilities approximate system success | dependencies, repair, software/common-cause failure invalidate independence assumptions |
| Markov / Semi-Markov Models | stochastic state model | failure/repair transitions and time-dependent availability need analysis | transition rates/stationarity cannot be defended |
| Weibull Analysis | lifetime/reliability method | failure-time data support lifecycle and hazard-rate inference | sparse/censored/mixture data are forced into one distribution |
| Reliability-Centered Maintenance (RCM) | maintenance decision process | physical assets need function/failure/consequence-based maintenance strategies | software-only systems or maintenance tasks lack economic/technical feasibility |
| FRACAS | closed-loop reliability process | failures need systematic reporting, analysis, corrective action, and verification | ticket collection without taxonomy, ownership, and recurrence controls |
| SLI / SLO / Error Budget | reliability operating method | service reliability trade-offs need user-centered measures and decision thresholds | metrics are internal-only, unowned, or copied from external SLA |
| Burn-Rate Alerting | SLO alert method | multi-window budget consumption should drive actionable paging | page on every deviation or use no runbook/action authority |

## Cybersecurity and privacy

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| NIST Cybersecurity Framework (CSF) | risk-governance framework | organize cybersecurity outcomes across govern, identify, protect, detect, respond, recover | detailed technical control catalog or certification claim |
| NIST SSDF | secure-development framework | integrate secure development outcomes into any SDLC | treat a draft revision as final or rely on compliance without threat context |
| ISO/IEC 27001 / 27002 | information-security management system/control guidance | organization-wide security governance, risk, audit, and certification are needed | application threat model or engineering recipe |
| Threat Modeling | security design practice family | assets, trust boundaries, data flows, attackers, and abuse paths change | one-time end-stage workshop or generic checklist detached from architecture |
| STRIDE | threat categorization technique | systematically prompt spoofing, tampering, repudiation, information disclosure, DoS, elevation risks | risk quantification or privacy analysis by itself |
| Attack Trees | adversarial decomposition method | enumerate alternative/combined attacker paths and prerequisites | completeness proof without attacker evidence and review |
| Abuse / Misuse Cases | requirements technique | specify harmful actor goals and system responses | replace broad threat discovery and control verification |
| PASTA | risk-centric threat-modeling methodology | business impact and technical attack paths justify a structured multi-stage assessment | small low-risk feature where overhead dominates |
| LINDDUN | privacy threat-modeling method | linkability, identifiability, non-repudiation, detectability, disclosure, unawareness, non-compliance matter | security threats outside privacy scope or no data-flow model |
| Privacy Impact Assessment / DPIA | governance/risk assessment | processing may materially affect privacy rights or regulation requires it | paperwork after design with no option to change processing |
| OWASP ASVS | application security requirements/verification standard | web application controls need testable assurance levels | awareness list or complete organization security program |
| OWASP Top 10 / API Top 10 | awareness/prioritization references | initial education and common risk coverage | verification standard or exhaustive threat model |
| OWASP WSTG | web security testing guide | structure manual/technical web assessment | assume guide coverage equals application assurance |
| Penetration Testing | adversarial assessment technique | deployed attack surface and exploitable chains require independent assessment | replace secure design, automated controls, or remediation verification |
| MITRE ATT&CK | adversary behavior knowledge base | threat-informed defense, detection coverage, and emulation need observed tactics/techniques | vulnerability list or probability model |
| Zero Trust Architecture | security architecture approach | access must be continuously evaluated with explicit identity, device, resource, and policy context | product purchase or slogan; do not ignore availability and recovery |

## Software supply chain

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| SBOM | inventory artifact | components, versions, licenses, and vulnerabilities need machine-readable transparency | generate and never validate, distribute, or use it |
| SPDX / CycloneDX | SBOM/data exchange standards | interoperable software component and related metadata are needed | treat format choice as supply-chain assurance |
| SLSA | supply-chain integrity framework | source/build provenance and increasing assurance levels guide controls | assume level labels prove application security |
| in-toto Attestations | supply-chain evidence framework | steps, materials, products, and authorized actors need verifiable attestations | no key/identity policy or verification at consumption |
| Sigstore | signing/transparency ecosystem | keyless identity-bound signing and public transparency fit artifact distribution | trust policy, issuer identity, and verification are undefined |
| Reproducible Builds | build property/practice | independently rebuild equivalent artifacts from declared source/environment | all dependencies/toolchains are uncontrolled or equality is confused with benignness |
| Dependency / SCA Scanning | detection practice | known vulnerable or disallowed components must be identified continuously | no reachability/context/remediation or assume database completeness |
| Secrets Scanning | detection practice | credentials may enter code, history, builds, or artifacts | scanning substitutes for secret minimization, rotation, and runtime controls |

## Structured assurance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Assurance Case | argument/evidence approach | confidence must be explicit, reviewable, and proportional to a material claim | claim tree is created without defeaters, evidence criteria, and maintenance |
| GSN | assurance argument notation | communicate goals, strategies, contexts, assumptions, justifications, and solutions | notation is mistaken for a complete assurance process |
| SACM | assurance-case metamodel | tools/organizations need interoperable structured assurance artifacts | small local case with no exchange/tool need |
| Claims–Arguments–Evidence (CAE) | argument pattern | a simpler assurance structure suffices | evidence relevance/inference remains implicit |
| Confidence Arguments | meta-assurance technique | uncertainty in the main argument, evidence, and inference must be assessed | recursively expand documentation without changing decisions |
| Defeater Analysis | argument-challenge technique | identify rebutting, undercutting, and undermining conditions | confirmation-only review |

## Research anchors

- ISO/IEC/IEEE 29119; applicable domain safety standards; NIST CSF and SSDF; ISO/IEC 27001.
- OWASP current release pages; MITRE ATT&CK/ATLAS where applicable.
- SLSA, SPDX, CycloneDX, in-toto, and Sigstore primary specifications.
- GSN Community Standard and OMG SACM.
- Verify whether a source is normative, a guide, an awareness list, or a draft before assigning assurance value.
