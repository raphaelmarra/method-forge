# AI, machine learning, LLMs, agents, evaluation, and assurance

Use this catalog for AI lifecycle, ML delivery, retrieval, agent architecture, tool authority, evaluations, governance, and adversarial safety. Treat model quality, system quality, organizational governance, and task outcomes as separate layers.

## Contents

1. AI/ML lifecycle and retrieval
2. LLM reasoning and control
3. Agent orchestration, memory, transaction, and execution assurance
4. Evaluation and monitoring
5. Governance, assurance, and security
6. Selection by agent shape and status discipline

## AI/ML lifecycle and operations

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| CRISP-DM | analytics/data-mining lifecycle | business understanding, data understanding/preparation, modeling, evaluation, and deployment need a simple iterative backbone | modern production ML operations, governance, and monitoring are assumed covered |
| Team Data Science Process (TDSP) | data-science lifecycle framework | collaborative analytics projects need roles, artifacts, and iterative delivery | tool-specific ceremony or non-Microsoft ecosystems without tailoring |
| SEMMA | analytics process model | sample/explore/modify/model/assess suits a modeling workbench | business framing, deployment, governance, and operation are needed |
| MLOps | practice/operating-model family | data, code, models, pipelines, deployment, monitoring, and retraining must be reproducible and governed | relabel CI/CD without data/model-specific controls |
| ML Test Score | production-readiness checklist/framework | identify testing and monitoring debt across data, model, infrastructure, and pipeline | one score is treated as universal assurance or replaces task-specific evals |
| Hidden Technical Debt analysis | risk lens | feedback loops, undeclared consumers, data dependencies, and pipeline complexity threaten ML systems | use as a lifecycle recipe or quantified debt measure without context |
| Model Cards | transparency artifact | communicate intended use, performance slices, limitations, and evaluation context | marketing summary without negative results and system-level limits |
| Datasheets for Datasets | dataset documentation artifact | provenance, composition, collection, preprocessing, use, distribution, and maintenance need transparency | documentation retroactively legitimizes unsuitable data |
| Data Statements / System Cards | documentation artifact families | language/data/system context and deployment behavior need broader disclosure | substitute for validation, audit, or access controls |

## Retrieval and knowledge-grounded generation

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Retrieval-Augmented Generation (RAG) | system architecture pattern | external/private/mutable knowledge should be retrieved and cited at answer time | transactional truth should come from an authoritative API or retrieval cannot meet recall/security needs |
| Dense Retrieval | retrieval technique | semantic similarity and paraphrase recall matter | exact identifiers, rare terms, or out-of-distribution content dominate |
| Sparse / Lexical Retrieval | retrieval technique | exact terms, codes, names, and interpretable scoring matter | semantic paraphrases dominate without expansion |
| Hybrid Retrieval | retrieval composition | combine lexical precision with semantic recall | complexity adds no measured retrieval benefit |
| Reranking | retrieval-stage technique | a larger candidate set needs stronger query–document relevance ordering | candidate recall is already poor; reranking cannot recover absent evidence |
| Query Expansion / Decomposition | retrieval technique | multi-hop or vocabulary-mismatch queries need multiple targeted searches | expansion drifts intent or creates uncontrolled cost/noise |
| Knowledge Graph RAG | retrieval/representation pattern | relational/multi-hop structure and entity grounding add measurable value | graph construction/governance exceeds need or relations are unreliable |
| Contextual Compression | context-management technique | retrieved documents need relevant excerpts within token budget | compression drops qualifiers, tables, or evidence needed for fidelity |
| Citation / Attribution Evaluation | eval family | answers must link claims to supporting passages and sources | citation existence is mistaken for entailment or source quality |
| Retrieval Evaluation | eval family | measure recall, precision, ranking, coverage, and failures on task-specific queries | answer-level scores alone hide missed evidence |

## LLM reasoning and control patterns

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Chain-of-Thought Prompting | prompting technique | internal deliberation may improve multi-step tasks and no external verifier is available | require exposed private reasoning or treat fluent rationale as evidence |
| ReAct | agent reasoning/action pattern | tool observations should iteratively change reasoning and next action | fixed deterministic workflow or irreversible actions lack gates |
| Planner–Executor | agent architecture pattern | long-horizon tasks benefit from explicit decomposition and separate execution | short task or plan becomes stale faster than execution |
| Plan-and-Execute with Replanning | agent architecture | environment changes and execution feedback require plan revision | unrestricted replanning can expand authority/scope |
| Tree of Thoughts / Search | deliberative search family | a bounded branching space and evaluable partial states justify lookahead | open-ended branching, weak evaluator, or routine task |
| Self-Consistency | sampling/aggregation technique | independent reasoning samples can reduce some stochastic errors | correlated misconception, factual sourcing, or high cost/latency makes voting misleading |
| Self-Refine / Reflexion | feedback iteration patterns | a reliable evaluator/feedback signal permits safe retries and learning | same model self-approval, irreversible effects, or no external signal |
| Program-aided / Tool-aided Reasoning | neuro-symbolic pattern | calculators, code, solvers, databases, or validators can externalize exact operations | generated tool inputs and result interpretation remain unchecked |
| Constrained Decoding / Structured Outputs | output-control technique | syntax/schema compliance must be enforced | schema-valid output is mistaken for semantic truth or authorization |
| Guardrails / Policy Enforcement | runtime control layer | inputs, outputs, actions, and permissions need explicit policy checks | model prompt alone is called a guardrail or controls lack adversarial tests |

## Agent orchestration and memory

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Tool / Function Calling | model interaction mechanism | models choose among typed capabilities and pass structured arguments | tool choice, authorization, side effects, and postconditions are assumed safe |
| MCP | interoperability protocol | expose tools/resources/prompts across AI hosts and servers | orchestration, identity governance, business contracts, or assurance by itself |
| Router / Supervisor | multi-agent pattern | tasks can be classified and assigned to distinct capabilities/policies | one model role adds latency without real specialization or verification |
| Parallel Specialists | orchestration pattern | independent subproblems can run concurrently and results can be reconciled | tasks share mutable state, are not separable, or outputs are correlated duplicates |
| Critic / Verifier | review pattern | a check can use distinct evidence, rules, tools, or model capability | same model/context merely restates confidence and is called independent |
| Debate / Multi-Agent Deliberation | aggregation pattern | genuinely diverse perspectives and an adjudication rule can expose assumptions | identical agents/sources produce correlated errors or rhetoric wins over evidence |
| Blackboard Architecture | coordination pattern | specialists iteratively contribute to a shared structured problem state | shared state lacks schema, provenance, concurrency, and conflict rules |
| Working Memory | transient state pattern | the task needs bounded current context and intermediate artifacts | long-term truth or authorization is stored informally in prompt history |
| Episodic Memory | experience memory pattern | prior trajectories/cases may help future adaptation | historical behavior is current policy, identity, or permission |
| Semantic Memory | knowledge memory pattern | durable factual/conceptual knowledge should be retrieved independently of episodes | mutable truth lacks version/provenance and freshness checks |
| Procedural Memory / Skills | reusable procedure pattern | recurring workflows need explicit steps, tools, constraints, and validation | hide broad authority or stale external facts inside instructions |
| Human-in-the-Loop / Approval Gate | governance pattern | ambiguity or irreversible financial/legal/safety/security effects require accountable human judgment | decorative approval for every low-risk action or humans lack evidence/time/authority |
| Least-Privilege Capabilities | security principle/pattern | agents can take external actions or access sensitive resources | broad tool grants justified by convenience or prompt-only restrictions |

## Agent transaction and execution assurance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Goal Contract | local/custom artifact | define intended outcome, constraints, success evidence, and stop conditions before planning | vague natural-language intention with no acceptance oracle |
| Operation Contract | local/custom artifact | each tool operation needs typed input, preconditions, effects, authorization, and postconditions | schema alone or undocumented side effects |
| Resolver Contract | local/custom pattern | required data/identity must be obtained through explicit sources, match rules, ambiguity handling, and proof | agent guesses from nearest semantic match |
| Plan Validation | assurance step | proposed steps can be checked for prerequisites, reachability, cost, policy, and irreducibility | validator shares the same unsupported action model without runtime checks |
| State Reconciliation | runtime method | observations after actions must align internal plan state with external truth | trust tool return text without authoritative read-back where effects matter |
| Idempotent Execution / Deduplication | reliability pattern | retries and duplicate messages can repeat side effects | business equivalence and deduplication scope/window are undefined |
| Unknown-Commit Handling | transaction-state pattern | network failure may hide whether an external write committed | classify every exception as safe failure and blindly retry |
| Compensation / Recovery Plan | workflow pattern | partial effects require explicit semantic repair or escalation | compensation is assumed to restore all consequences exactly |
| Authority Boundary / Action Budget | governance control | agent autonomy must be limited by operation, amount, time, data, or risk | model decides its own permissions or budgets are not enforced externally |
| Execution Provenance / Trace | evidence artifact | every material input, decision, action, observation, and artifact must be reconstructable | verbose logs without stable IDs, privacy controls, or evidence semantics |

## Evaluation and monitoring

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Eval-Driven Development | engineering practice | prompts/models/tools/contracts change and regression decisions need task-specific evals | rely only on public benchmarks or one final benchmark run |
| Gold Set / Reference Cases | evaluation artifact | representative inputs and expected properties/outcomes can anchor regression | static set leaks into development, becomes stale, or lacks hard cases |
| Behavioral Evaluation | system eval family | test observable task behavior across scenarios, slices, refusals, and edge cases | only score average answer similarity |
| Trajectory Evaluation | agent eval family | action sequence, tool selection, state, cost, safety, and recovery matter beyond final answer | only evaluate final success and miss unsafe paths |
| Field Evaluation | deployment eval family | real users/environment reveal impacts, adaptation, and emergent failures | uncontrolled rollout with no monitoring, consent, or rollback |
| LLM-as-Judge | scalable evaluation technique | subjective outputs need rubric-based triage calibrated to human/reference judgments | judge shares model bias, sees irrelevant metadata, or is treated as ground truth |
| Pairwise Preference Evaluation | comparative eval | relative quality is easier to judge than absolute scores | position/order/style bias and transitivity are untested |
| Calibration / Selective Prediction | uncertainty-control family | system should abstain/escalate at thresholds tied to cost | verbal self-confidence is treated as calibrated probability |
| Robustness / Perturbation Testing | eval technique | paraphrase, noise, formatting, and distribution shifts should preserve behavior | perturbations are unrealistic or semantic meaning changes unnoticed |
| Counterfactual / Slice Evaluation | fairness/robustness technique | performance may vary across relevant groups or controlled attributes | sensitive attributes are changed in causally incoherent ways |
| Drift Monitoring | production monitoring | data, retrieval, model, policy, and behavior may change | detect drift without linked impact, thresholds, or response plan |
| Incident Learning | operational loop | AI failures need classification, containment, causal learning, remediation, and regression cases | hide incidents or count reports without closing controls |

## AI governance and assurance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| NIST AI RMF | voluntary risk-management framework | organize Govern, Map, Measure, and Manage outcomes for trustworthy AI | certification claim or detailed model test method |
| NIST Generative AI Profile | cross-sector profile | GenAI-specific risks/actions should extend AI RMF | agent/tool-specific threat model or local prioritization by itself |
| ISO/IEC 42001 | AI management system standard | organization-wide AI policy, objectives, roles, risk, lifecycle, monitoring, and continual improvement are required | product performance test or ethical badge from documentation alone |
| ISO/IEC 23894 | AI risk-management guidance | adapt risk principles/process to AI systems and stakeholders | complete assurance case or sector-specific compliance |
| ISO/IEC 42005 | AI system impact-assessment standard | structured impact assessment across AI lifecycle is needed | substitute impact management, affected-party engagement, and technical validation |
| ISO/IEC 5338 | AI system lifecycle process standard | align AI-specific lifecycle processes with system/software engineering | detailed ML implementation playbook |
| Algorithmic Impact Assessment | governance method/artifact family | deployment affects rights, access, public services, or vulnerable stakeholders | checkbox scoring after procurement/deployment |
| Assurance Case for AI | structured argument approach | system acceptability must be justified with claims, evidence, assumptions, defeaters, and monitoring | one-time narrative or model metrics disconnected from use context |
| NIST ARIA / TEVV frameworks | AI evaluation programs/frameworks | model testing, red teaming, and field testing need structured evidence | present draft/experimental guidance as a stable normative standard |

## AI and agent security

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| OWASP LLM Top 10 | risk-awareness reference | cover common LLM application risk categories and mitigations | verification standard or exhaustive system threat model |
| OWASP Agentic Applications Top 10 | agent-specific risk reference | agents plan, use tools, hold memory, delegate, or cross trust boundaries | substitute detailed threat modeling and control testing |
| OWASP Agentic Skills Top 10 | skill execution risk reference | reusable agent skills can carry instructions, dependencies, permissions, and supply-chain risk | assume listing risks secures a skill |
| MITRE ATLAS | adversarial AI knowledge base | threat-informed modeling, emulation, and detection need AI tactics/techniques/case studies | likelihood calculation or full risk program |
| Prompt Injection Testing | adversarial test family | untrusted content can influence model instructions or tool use | rely on prompt filters alone or ignore indirect/cross-modal injection |
| Tool Abuse / Goal Hijack Testing | agent red-team family | agent goals, plans, permissions, or tools can be manipulated | test only chat output without real authority boundaries |
| Data / Model Poisoning Assessment | ML security analysis | training, fine-tuning, retrieval, feedback, or memory sources may be adversarial | pipeline provenance and influence paths are unknown |
| Model Extraction / Inversion / Membership Tests | privacy/IP security tests | exposed interfaces may leak model behavior, training membership, or sensitive information | apply without threat relevance, legal authority, and rate/budget controls |

## Selection by agent shape

| Agent shape | Preferred backbone | Necessary complements |
| --- | --- | --- |
| Fixed deterministic business workflow | workflow/contract-first | typed tools, operation contracts, state reconciliation, idempotency, audit |
| Dynamic but well-modeled goal planning | HTN/PDDL or planner–executor | plan validation, action model tests, runtime replan, authority boundary |
| Open-ended research agent | ReAct plus research protocol | retrieval eval, provenance, claim–evidence states, stopping rule, source appraisal |
| High-stakes action agent | constrained workflow with human approval | least privilege, transaction semantics, independent verification, assurance case, monitoring |
| Multi-agent analysis | router/parallel specialists | task independence, source diversity, reconciliation rule, conflict record, marginal-value measurement |

## Research anchors and status discipline

- NIST AI RMF, GenAI Profile, and official AIRC publications.
- ISO AI standards catalog for 42001, 23894, 42005, 5338, and related current standards.
- OWASP GenAI Security Project and MITRE ATLAS for current adversarial risks.
- Original papers for RAG, ReAct, Reflexion, Tree of Thoughts, Model Cards, and Datasheets; follow later replications/criticisms.
- Label initial public drafts, beta specifications, community guides, and local patterns explicitly. Recheck current versions at use time.
