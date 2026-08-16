# Design, experience, communication, and design systems

Use this catalog when the decision concerns understanding people and contexts, structuring information, designing interactions or services, communicating clearly, evaluating usability/accessibility, or governing reusable interface patterns. Design is not one method: discovery, synthesis, generation, representation, evaluation, and governance require different fragments.

## Contents

1. Design framing and lifecycle
2. Design and user research
3. Synthesis, information architecture, and interaction
4. Prototyping and usability evaluation
5. Service and experience design
6. Visual, information, and communication design
7. Inclusive design and accessibility
8. Design systems and design operations
9. Boundaries and composition patterns
10. Research anchors and status

## Design framing and lifecycle

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Human-Centred Design — ISO 9241-210 | lifecycle framework; context, user requirements, design solutions, and evaluation | interactive products/services need iterative evidence from representative users and contexts | preference overrides safety, technical truth, accessibility, business constraints, or sector regulation |
| Double Diamond | divergence/convergence representation | teams must separate understanding/definition from generating/developing solutions | treat four labels as a detailed method, assume linearity, or use divergence when requirements are fixed and verified |
| Design Thinking | human-centred innovation family | desirability and problem/solution uncertainty justify empathy, reframing, ideas, prototypes, and learning | workshop theater, generic creativity, or ideation substitutes for domain evidence and implementation |
| Design sprint | time-boxed/proprietary workshop pattern | a bounded high-priority question can be prototyped and tested rapidly with decision makers available | foundational research, complex ecosystems, regulated validation, or production readiness is compressed into a few days |
| Co-design / participatory design | participation method family | people affected by a system should shape needs, concepts, trade-offs, and evaluation | token participation, unsafe power imbalance, unrepresentative voices, or participants are made responsible for expert/legal decisions |
| Critical / speculative design | exploratory/critical practice | provoke discussion about futures, values, consequences, and assumptions | artifact is presented as forecast, validated demand, implementation plan, or risk control |
| Systems-oriented design | synthesis/design approach | services, organizations, policies, environments, and feedback create distributed outcomes | a rich system map substitutes for causal evidence, responsibility, prioritization, and intervention testing |
| Experience strategy | strategy artifact; target experience, principles, moments, capabilities, and measures | product/service/brand touchpoints require a coherent intended experience | emotional aspiration lacks task, accessibility, operational, economic, and failure-recovery requirements |
| Design principles | decision heuristics | repeated design choices need explicit priorities and trade-off guidance | vague slogans cannot resolve a real conflict or are never tested against outcomes |
| Design brief / outcome contract | framing artifact; problem, users, context, constraints, evidence, outcomes, exclusions, and decision | multidisciplinary work needs a shared question and acceptance frame | the brief preselects a solution, hides uncertainty, or turns outputs into outcomes |

`02-strategy-product-organization.md` owns product discovery and portfolio strategy. This catalog owns design research, interaction, experience, communication, accessibility, and reusable interface governance.

## Design and user research

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Research plan / protocol | governance artifact; questions, participants, method, tasks, data, analysis, ethics, and decision use | research must produce decision-relevant and auditable learning | method is chosen from convenience, questions are leading, or no downstream decision consumes findings |
| Contextual inquiry | field research method combining observation and inquiry | work-as-done, environment, artifacts, interruptions, and tacit practices matter | remote opinion interviews can answer the question or observation creates unacceptable safety/privacy risk |
| Design ethnography | qualitative field research family | culture, routines, meaning, relationships, adaptation, and context require sustained understanding | a few visits are labeled ethnography or interpretation is generalized without sampling/reflexivity |
| Semi-structured interview | qualitative elicitation method | experiences, goals, decisions, language, workarounds, and meanings need exploration | stated memory or preference is treated as observed behavior, prevalence, or causal effect |
| Diary study / experience sampling | longitudinal self-report method | events, habits, context, emotion, and intermittent experiences unfold over time | burden causes selective reporting or recall/self-presentation is ignored |
| Observation / shadowing | behavioral/context method | sequences, coordination, tools, errors, waiting, and workarounds must be seen | observation alone reveals intention or participants cannot act naturally/safely under observation |
| Focus group | facilitated group-research method | social language, norms, reactions, and concept diversity are relevant | sensitive individual behavior, usability, prevalence, consensus, or dominant voices distort the question |
| Generative / co-creation session | exploratory method | participants can externalize needs, experiences, metaphors, or future possibilities through making | creative artifacts are treated as prioritized requirements or realistic adoption evidence |
| Critical incident technique | structured recall method | unusually successful/failed episodes can reveal triggers, actions, context, and consequences | ordinary frequency/base rates or prospective behavior is inferred from memorable incidents alone |
| Task analysis | analysis method; goals, actions, conditions, information, dependencies, and error opportunities | workflows must become design requirements or evaluation tasks | adaptive/knowledge work is forced into one ideal linear sequence; cognitive specialization in `35` |
| Mental-model elicitation | research/synthesis family | users' concepts, causal beliefs, categories, and expectations affect comprehension and navigation | analyst diagram is called the user's model or misconceptions are preserved despite safety/domain truth |
| Survey research for design | quantitative self-report specialization | prevalence, attitudes, satisfaction, segmentation, or tracking requires a defensible instrument and sample | convenience responses prove behavior, causality, usability, or unmet need severity; generic survey design and evidence ownership belong to `31-research-evidence-investigation.md` |
| Concept testing | evaluative research family | alternative value propositions, concepts, comprehension, relevance, and concerns need early evidence | stated liking predicts purchase, use, feasibility, or safety |
| Research repository / insight governance | knowledge system | findings, evidence, participants, decisions, contradictions, freshness, and reuse need controlled access | quote library becomes truth without provenance, scope, negative findings, consent, and retention controls |

Recruit participants by the target population and relevant capability/context—not convenient demographics alone. Separate user, purchaser, operator, administrator, supporter, bystander, and person bearing risk. Include nonusers, abandonment, assistive-technology use, low literacy, adverse cases, and edge conditions when material.

## Synthesis, information architecture, and interaction

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Affinity mapping / thematic synthesis | qualitative synthesis technique | observations and excerpts need transparent clustering into patterns and open questions | workshop consensus replaces traceability, negative cases, frequency limits, or analyst reflexivity |
| Persona | evidence-synthesis artifact | stable behavior, goal, context, and capability patterns help teams reason about differing needs | fictional demographics, stereotypes, or one persona stands in for sampling and ongoing research |
| Jobs-to-be-Done model | needs/circumstance representation | desired progress, triggers, barriers, alternatives, and trade-offs guide design | a catchy job statement replaces observed context, prioritization, or market evidence; commercial ownership in `12/19` |
| Journey map | temporal experience representation | actions, channels, actors, evidence, pain, emotion, and opportunities across a scenario need alignment | generic happy path, unsupported emotion curves, or map substitutes for service operations and outcome evidence |
| Story map / scenario map | planning/representation technique | end-to-end user activity and release slices need shared structure | backlog order becomes user evidence or nonfunctional/risk requirements disappear |
| Service blueprint | cross-layer representation | customer actions, frontstage, backstage, support, systems, evidence, waits, and failure points interact | decorative journey map lacks ownership, timing, capacity, controls, and recovery |
| Ecosystem / stakeholder map | relationship representation | value, information, authority, dependency, and harm cross organizational boundaries | all actors appear equal or map is not tied to decisions, incentives, and evidence |
| Open card sorting | generative information-architecture method | users' grouping and labels can inform a new taxonomy | sample is unrepresentative, content is ambiguous, or raw clusters directly become navigation |
| Closed / hybrid card sorting | evaluative IA method | candidate categories and placement need comparison/refinement | task requires finding paths in a hierarchy or categories constrain discovery prematurely |
| Tree testing | navigation-findability test | label and hierarchy effectiveness must be tested without visual/interface cues | visual interaction, search behavior, content comprehension, or full workflow is the actual question |
| Content inventory and audit | governance/analysis method | content ownership, purpose, accuracy, duplication, accessibility, performance, and lifecycle need decisions | spreadsheet completion replaces user need, content model, and removal/migration authority |
| Content model / structured content | information architecture/schema | reusable content types, fields, relationships, metadata, and channels need consistency | structure reflects a page mock-up or CMS limitation rather than semantic use and governance |
| Task flow / user flow | interaction representation | states, choices, system responses, errors, and exits for a bounded goal need design | only happy path, screens rather than state, or business process is confused with user interaction |
| State model / statechart | formal interaction representation | asynchronous, conditional, modal, undoable, or failure-prone interaction needs explicit state and transitions | static wireframes are sufficient or semantics are too unstable; formal ownership in `05` |
| Interaction pattern / affordance analysis | design technique | controls, signifiers, mapping, feedback, constraints, and consistency influence action | familiar appearance is assumed accessible, safe, or understood without testing |
| Error prevention and recovery design | interaction assurance method | high-cost mistakes, invalid input, interruption, undo, retry, timeout, and uncertain state must be handled | blame-oriented error messages or confirmation dialogs substitute for safer defaults and reversible operations |
| Progressive disclosure | information/interaction pattern | complexity can be staged by frequency, expertise, or dependency | critical conditions are hidden, navigation becomes deep, or experts lose efficient access |

## Prototyping and usability evaluation

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Sketch / paper prototype | low-fidelity prototype | structure, sequence, terminology, and concepts need cheap change | timing, dynamic state, accessibility technology, visual hierarchy, or physical properties determine validity |
| Wireframe | structural representation | information hierarchy, layout regions, flow, and content priority need discussion | grayscale polish is treated as usable implementation or real content/responsiveness is absent |
| Clickable prototype | interactive simulation | navigation, flow, comprehension, and selected state behavior can be tested before code | fake data/speed, missing errors, and scripted paths are mistaken for operational validation |
| Wizard-of-Oz prototype | experimental simulation | a hidden human can cheaply simulate uncertain automation/service behavior | participants are deceived unethically, safety/privacy risk exists, or manual feasibility is confused with scalable operation |
| Service prototype / role play | experiential prototype | handoffs, scripts, environment, physical evidence, capacity, and recovery need enactment | enthusiastic staff performance proves repeatable operations or real constraints are omitted |
| Technical proof of concept | feasibility experiment | one risky mechanism/interface must be demonstrated | usability, desirability, reliability, security, scale, and production readiness are inferred; engineering ownership in `04/14` |
| Moderated usability testing | behavioral evaluation method | representative participants should attempt realistic tasks while observers probe behavior and understanding | facilitator coaching, leading tasks, preference questions, or a convenience sample substitutes for task evidence |
| Unmoderated usability testing | remote behavioral method | standardized tasks and instrumentation can reach more participants cheaply | complex/sensitive tasks, assistive technology, troubleshooting, or context requires observation and probing |
| Formative usability evaluation | iterative assurance | identify and prioritize design problems during development | statistical benchmarking or summative conformity is claimed from a small diagnostic study |
| Summative usability evaluation | validation/benchmark method | predefined users, tasks, context, measures, and thresholds must support a release or comparison claim | design is still changing, sample/power is inadequate, or one mean hides critical task/user failures |
| Heuristic evaluation | expert inspection technique | an interface can be screened efficiently against recognized interaction principles | expert opinion replaces user testing, accessibility audit, domain safety, or evidence of severity/prevalence |
| Cognitive walkthrough | expert task inspection | learnability and action visibility for specific tasks/new users need structured examination | habitual/expert use, emotional response, visual accessibility, and real context are inferred |
| Pluralistic walkthrough | collaborative inspection | users, designers, developers, and domain experts can expose differing task assumptions | workshop agreement substitutes for representative behavioral evidence |
| Accessibility audit | technical/expert conformance evaluation | code/content/interface needs systematic checks against applicable accessibility criteria | automated scan alone, conformance equals usability, or disabled-user testing is omitted |
| Task success / error / time metrics | performance measurement | effectiveness and efficiency for defined users, tasks, and context need objective measures | incomparable tasks, coached sessions, learning effects, and critical-error severity are ignored |
| System Usability Scale — SUS | standardized post-use questionnaire | a compact perceived-usability score can complement task evidence and benchmark iterations | score diagnoses specific problems, proves accessibility, or compares different contexts without caution |
| UMUX-LITE / concise UX scales | standardized questionnaire family | lower respondent burden is necessary and psychometric fit is verified | metric is selected only for brevity or one score replaces behavior and qualitative explanation |
| Single Ease Question — SEQ | post-task perceived-difficulty item | task-level perceived ease should complement success/time/error evidence | ease rating alone establishes usability or respondents rate different task variants |
| A/B interface experiment | causal field experiment | a bounded change, stable outcome, adequate units, guardrails, and ethical assignment support causal comparison | local metric wins while comprehension, accessibility, long-term value, novelty, interference, or multiple changes are ignored |
| Usability evaluation report — CIF | reporting/assurance standard | users, context, tasks, methods, results, limitations, and decisions require a consistent evaluation record | report format is treated as the evaluation method or undocumented raw findings imply conformity |

Usability is an outcome of use for specified users, goals, and context—not an intrinsic beauty score. Satisfaction, task success, accessibility conformance, safety, adoption, and business performance are related but distinct claims.

## Service and experience design

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Service design | multidisciplinary method family | value depends on coordinated people, processes, information, technology, channels, and evidence over time | interface redesign alone can solve the problem or workshops ignore operating authority and capacity |
| Service ecology | systems representation | actors, exchanges, dependencies, platforms, rules, and externalities shape service outcomes | map complexity prevents choosing leverage points, ownership, and testable interventions |
| Moments-of-truth analysis | prioritization technique | selected interactions disproportionately affect trust, completion, recovery, or relationship | dramatic moments obscure mundane recurring friction and end-to-end outcome |
| Omnichannel journey orchestration | operating/design method | users move across digital, physical, assisted, partner, and asynchronous channels | visual consistency is called continuity while state, identity, promise, and ownership break |
| Service standard / service assessment | governance and assurance framework | public or enterprise services need repeatable gates for user need, accessibility, privacy, reliability, operations, and outcomes | checklist certification substitutes for evidence from real end-to-end use |
| Failure-demand analysis | service diagnostic | avoidable contacts/rework occur because prior service failed, confused, or did not complete | all contact is classified waste or frontline staff are blamed for system causes |
| Service recovery design | resilience/interaction method | failures require detection, explanation, ownership, compensation, retry, escalation, and learning | apology text substitutes for restoring state, rights, money, safety, and root-cause correction |
| Frontline / employee-experience research | organizational/service research | staff capability, tools, incentives, workload, and discretion materially affect customer outcomes | employee preference overrides user rights or process/safety constraints |
| Assisted-digital / inclusive service design | channel/support design | some users cannot complete independently because of access, capability, language, disability, or exceptional circumstance | assisted route becomes inferior, stigmatizing, insecure, or a substitute for fixing the primary service |
| Service pilot / living lab | field experimentation pattern | a bounded real context can test demand, operations, handoffs, failure, and measurement before scale | pilot uses exceptional staff/resources, lacks comparison/exit criteria, or quietly becomes permanent |

## Visual, information, and communication design

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Visual hierarchy | design principle/technique | importance, sequence, grouping, action, and status must be perceived quickly | size/color alone carries meaning or hierarchy contradicts task and accessibility needs |
| Grid and layout system | spatial representation/system | alignment, rhythm, responsiveness, density, and cross-page consistency need shared rules | rigid grid harms content, localization, reflow, zoom, or device adaptation |
| Typographic system | communication/design system | legibility, hierarchy, voice, language coverage, and reusable styles need governance | brand typeface, tiny text, all caps, or visual novelty overrides reading conditions and accessibility |
| Color system | semantic/visual system | brand, hierarchy, status, data, interaction, and themes need reusable accessible roles | color alone communicates meaning, contrast is untested, or aesthetic palette becomes semantic truth |
| Gestalt grouping principles | perceptual heuristics | proximity, similarity, enclosure, continuity, and figure-ground can improve grouping and scan | heuristic application substitutes for task testing, culture/context, and accessibility |
| Plain language — ISO 24495-1 | communication framework | intended readers must find, understand, and use written information | oversimplification removes necessary precision or text clarity is expected to fix a broken process |
| Content design | user-centred communication method | content must answer a need at the right moment with usable structure, language, and action | copy is written after layout/flow decisions or tone replaces completeness and accuracy |
| Progressive / layered information | communication pattern | audiences need a concise path with optional detail, evidence, or specialist depth | caveats, risks, price, consent, or critical instructions are hidden behind optional layers |
| Information visualization workflow | analytical communication method; question, data, encoding, annotation, interaction, and validation | relationships, distributions, change, uncertainty, or spatial patterns are clearer visually | decorative chart, misleading scale/aggregation, or visual salience exceeds evidential importance |
| Dashboard design | decision-support method | recurring monitoring and action need prioritized status, comparison, thresholds, context, and drill-down | every metric is shown, real-time implies relevance, or dashboard replaces investigation and ownership |
| Risk / uncertainty communication | communication and decision-support family | probability, range, severity, evidence, trade-offs, and action must be understood | false precision, verbal labels without calibration, fear appeals, or uncertainty is hidden to persuade |
| Wayfinding / signage system | environmental information-design method | people must orient, choose routes, recognize destinations, and recover from mistakes in physical spaces | signs compensate for confusing architecture or are tested only by designers/familiar users |
| Icon / symbol comprehension test | empirical evaluation | pictograms, controls, warnings, or cross-language symbols need recognition and interpretation evidence | icon familiarity is assumed, labels are removed prematurely, or cultural/safety ambiguity is ignored |
| Editorial design system | communication system | long-form reports, evidence, tables, figures, references, and navigation need readable consistency | visual polish obscures source, uncertainty, hierarchy, or document accessibility |
| Brand identity execution | visual/verbal realization | positioning and distinctive assets must become coherent touchpoint rules | aesthetics create strategy or an identity guide proves market recognition; brand strategy ownership in `19` |

## Inclusive design and accessibility

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Inclusive design | design approach | human diversity, situational limitation, exclusion, and adaptability should shape mainstream solutions | “one design for everyone” erases conflicting needs or inclusion claims lack affected-person participation |
| Universal design | principle framework | physical/digital products and environments should maximize broad equitable use | principles substitute for context-specific accessibility requirements and user validation |
| WCAG 2.2 / ISO/IEC 40500:2025 | web-content accessibility standard | web content and interfaces need testable conformance criteria and supporting techniques | checklist alone proves end-to-end usability, legal compliance in every jurisdiction, or accessibility beyond its scope |
| WAI-ARIA | semantic interoperability specification | custom web widgets need accessibility semantics not supplied by native elements | ARIA repairs incorrect interaction or replaces native HTML, keyboard behavior, names, states, and testing |
| Accessibility Conformance Testing — ACT Rules | test-rule framework | repeatable machine/manual tests need explicit applicability, expectation, and outcomes | passing available ACT rules proves full WCAG conformance or user accessibility |
| Assistive-technology compatibility testing | empirical technical evaluation | screen readers, magnification, voice, switches, keyboard, captions, or platform accessibility APIs affect use | one tool/browser combination represents all users or scripted checks replace representative tasks |
| Disabled-user usability research | inclusive behavioral evaluation | real strategies, barriers, workarounds, and combined impairments/context must inform design | participants are treated as a final audit, one impairment represents disability, or inaccessible research excludes people |
| Cognitive accessibility design | inclusive design family | memory, attention, language, executive function, neurodiversity, or learning differences affect completion | reducing content alone, infantilizing language, or assuming one cognitive profile |
| Accessibility statement and issue workflow | transparency/governance artifact | known conformance, limitations, alternatives, contact, remediation, and ownership must remain current | boilerplate statement masks unresolved barriers or contact route is inaccessible/ineffective |
| Accessibility acceptance gate | assurance gate | critical journeys and releases require criteria, evidence, owner, exceptions, severity, and remediation | deadline accepts blockers without authority/alternative or automated score is the sole gate |

Accessibility is a continuous design, engineering, content, procurement, and operational responsibility. Verify controlling law and sector rules through `13-legal-policy-ethics.md`; do not infer legal compliance from WCAG alone.

## Design systems and design operations

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Design system | governed product/service; principles, components, patterns, content, accessibility, code, and contribution | multiple teams/products need coherent reusable decisions and faster validated delivery | component library alone, premature standardization, or central control blocks domain needs and learning |
| Component library | reusable implementation asset | stable repeated interface elements need documented states, behavior, content, accessibility, and tests | page templates are decomposed without semantic reuse or components omit failure/loading/permission states |
| Pattern library | reusable solution knowledge | recurring user problems and interaction/service patterns need contextual guidance | patterns become mandates outside assumptions or examples lack evidence and anti-patterns |
| Design tokens — DTCG 2025.10 | interoperable representation standard | color, typography, dimension, border, transition, theme, alias, and platform outputs need shared machine-readable decisions | tokens provide component behavior, accessibility, governance, or visual quality automatically |
| Content style guide | governance reference | terminology, tone, grammar, inclusive language, formatting, and examples need consistent application | rigid voice reduces comprehension, localization, legal accuracy, or contextual sensitivity |
| Design-system governance model | operating model; ownership, contribution, review, release, deprecation, adoption, and exception | distributed contributors and consumers need decision rights and quality assurance | committee bottleneck, unowned commons, or adoption is coerced without support and value evidence |
| Contribution / RFC process | governance workflow | new components, variants, tokens, and breaking changes require transparent evidence and review | process overhead exceeds reuse/risk or local forks bypass unresolved central gaps |
| Design-system maturity assessment | diagnostic model | strategy, coverage, code parity, accessibility, governance, adoption, support, and outcomes need improvement priorities | maturity level becomes prestige score or a proprietary ladder dictates irrelevant investment |
| Design debt register | risk/backlog artifact | inconsistent, inaccessible, obsolete, duplicated, or unsupported decisions need impact and remediation ownership | every visual inconsistency is called debt or debt volume replaces outcome/risk prioritization |
| Design QA / design–code reconciliation | assurance process | released interfaces must match intended behavior, content, tokens, responsiveness, accessibility, and states | pixel matching ignores semantics, platform conventions, performance, and user outcomes |
| DesignOps | organizational capability | research, tools, systems, staffing, workflow, procurement, and knowledge must scale across teams | operations optimizes artifact throughput while reducing user contact and design judgment |
| ResearchOps | organizational capability | participant management, consent, tooling, repositories, governance, safety, and research quality need scale | centralized efficiency creates participant fatigue, inaccessible recruitment, or distance from product decisions |
| Design outcome measurement | measurement framework | system adoption, reuse, consistency, cycle time, defects, accessibility, usability, and product outcomes need balanced evidence | component count, Figma use, or adoption percentage becomes the target irrespective of user value |

## Boundaries and composition patterns

| Decision | Primary owner | Consult when needed |
| --- | --- | --- |
| Which market/segment and commercial position? | `19-marketing-growth-brand-commercial.md` | `12` for research/economics; this catalog for experience and communication |
| Which customer problem/product outcome? | `02-strategy-product-organization.md` | this catalog for research, prototyping, and usability |
| How should a digital/service experience work? | this catalog | `04/05` for architecture/contracts/state; `06` for technical assurance |
| How should a physical product be shaped and produced? | `14-physical-engineering-manufacturing.md` | this catalog for experience, information, and user evaluation |
| How should learning be designed? | `18-learning-training-education.md` | this catalog for interaction, accessibility, and information design |
| What is legally required? | `13-legal-policy-ethics.md` | this catalog turns applicable requirements into design/evaluation evidence |

### Design and test a digital product

`outcome/constraints → research protocol + representative contexts → task/mental model → IA + flows/state/error recovery → low-to-high fidelity prototypes → formative usability + accessibility → engineering contracts → summative critical-journey gate → field experiment/monitoring → design-system contribution`

### Redesign an end-to-end service

`service outcome + affected actors → field research → journey/ecosystem + service blueprint → failure-demand/capacity diagnosis → co-designed concepts → service prototype → accessibility/privacy/safety gates → bounded pilot → operational and user outcomes → recovery/continuous improvement`

### Build an accessible design system

`experience/design principles → inventory/audit → semantic foundations + content rules → token architecture → accessible components/patterns with full states → documentation and code parity → contribution/release/deprecation governance → adoption support → automated + manual + disabled-user assurance → outcome/debt monitoring`

### Design an evidence-rich report or dashboard

`reader decision + information questions → content/data audit → hierarchy and narrative → appropriate visual encodings + uncertainty → plain language + layered detail → accessibility/reflow/alternative formats → comprehension/task test → source/provenance and update governance`

### Operationalize a brand identity

`positioning/distinctive assets from 19 → verbal/visual hierarchy → typography/color/layout/icon systems → content and accessibility rules → design tokens/components/templates → cross-channel prototypes → recognition/comprehension/usability tests → governance and brand tracking`

## Research anchors and status

Status checked 2026-08-12. Verify jurisdiction, target population, platform, assistive-technology combinations, and the exact standard part at use time.

- [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) is the current human-centred-design lifecycle standard and was confirmed in 2025. [ISO 9241-11:2018](https://www.iso.org/standard/63500.html) defines usability concepts but does not prescribe an evaluation method.
- [Design Council Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) is the canonical representation; it is a process map, not a complete methodology.
- [GOV.UK Service Manual user research](https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design) and [moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) provide public operational guidance for continuous, inclusive, decision-linked research.
- [ISO 25062:2025](https://www.iso.org/standard/84255.html) is the current Common Industry Format for reporting usability evaluations and supersedes the older ISO/IEC 25066 reporting anchor.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is a W3C Recommendation and was approved as [ISO/IEC 40500:2025](https://www.w3.org/press-releases/2025/wcag22-iso-pas/). Check controlling law and procurement/sector requirements separately.
- [W3C WAI](https://www.w3.org/WAI/standards-guidelines/) is the canonical route for WCAG, ARIA, ACT, authoring/user-agent accessibility, and implementation material. Community drafts and supporting techniques do not have the same normative status.
- [ISO 24495-1:2023](https://www.iso.org/standard/78907.html) provides governing principles for plain-language documents; it does not cover every communication format or replace domain accuracy.
- The [W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/) published stable final reports for the 2025.10 Format, Color, and Resolver modules. Community Group reports are not W3C Recommendations; label status accurately.
- For usability questionnaires and inspection heuristics, consult the original instrument/method publication, licensing, validated translation, population/context evidence, and current scoring guidance. Do not silently modify standardized items.
