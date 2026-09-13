# Human factors, ergonomics, health systems, and medical devices

Use this catalog when human–system performance, physical/cognitive ergonomics, use-related risk, clinical evidence, or a regulated medical-device lifecycle determines the method. Clinical, medical-device, and health-system work is jurisdiction- and product-class-specific. Agent research cannot authorize treatment, market entry, human studies, or product release.

## Human factors and ergonomics

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Ergonomic design of work systems — ISO 6385/26800 | human-factors design framework | tasks, organization, tools, environment, physical/cognitive demand, and worker variability must be designed jointly | “train the operator” compensates for a preventable design hazard |
| Human Systems Integration — HSI | program integration framework | manpower, personnel, training, human factors, safety, survivability, habitability, and maintainability interact across acquisition | add a usability review at the end or optimize headcount independently of workload/safety |
| Human-centred design — ISO 9241-210 | iterative design lifecycle specialized for human–system engineering | interactive physical/digital systems require explicit users, context, requirements, design, and evaluation | UI preference testing substitutes for system safety, domain correctness, or accessibility obligations; UX/service execution belongs to `20-design-experience-communication.md` |
| Work / task analysis | analysis family | work-as-done, goals, variability, coordination, and error opportunities must be understood; select HTA or CTA below by required output | document only work-as-imagined or assume one decomposition captures every aspect of work |
| [Hierarchical Task Analysis — HTA](#hierarchical-task-analysis--hta) | established analysis method; goal/subgoal hierarchy plus execution plans | observed or explicitly proposed tasks must become procedures, interface requirements, job aids, or a basis for error analysis | a hierarchy alone is expected to reveal tacit expertise, predict task time/error probability, or prove safety |
| [Cognitive Task Analysis — CTA](#cognitive-task-analysis--cta) | elicitation and analysis family; cognitive demands, cues, strategies, and decision requirements | expert judgment, diagnosis, uncertainty, or novice/expert differences must inform training, interfaces, or decision support | domain experts/representative work evidence are unavailable, only physical actions need description, or one self-report is treated as verified cognition |
| Anthropometric accommodation | physical-design method | reach, clearance, strength, posture, fit, egress, and population coverage determine geometry | design to an “average person,” mix incompatible percentiles, or ignore clothing/PPE/dynamics |
| Human-in-the-loop evaluation | iterative assurance method | representative users must perform representative tasks under realistic conditions before release | experts substitute for target users or scripted happy paths hide workload and recovery |
| NASA-TLX / workload measures | subjective workload measurement technique | compare workload across tasks/designs with a validated protocol and complementary performance evidence | one score diagnoses the causal source or replaces errors, physiology, observation, and context |
| Revised NIOSH Lifting Equation | specialist ergonomic assessment | specified two-handed lifting conditions fit the model's scope | apply outside assumptions, to pushing/pulling/carrying or complex unstable loads as a universal safe limit |
| Human Reliability Analysis — HRA | risk-analysis family | human actions, dependencies, context, recovery, and performance-shaping factors affect safety/reliability | assign generic “human error probabilities,” blame operators, or ignore system design |
| [SHERPA](#sherpa) | task-based human-error prediction method; credible errors, consequences, recovery, and remedies | a validated HTA and practitioner evidence can support systematic analysis of operational or interface errors | invented probabilities, operator blame, or a completed worksheet is treated as proof of safety |
| Cognitive Work Analysis — CWA | constraint-based analysis framework | work is complex/adaptive and must remain safe under unanticipated conditions | a stable routine task only needs direct task analysis or analysts lack domain access |

## Task analysis: canonical cards and selection

Both methods support human factors across operational, physical, digital, and training contexts. HTA describes goal-directed task structure; CTA investigates the knowledge and cognitive demands that make performance possible. They are complements when both outputs feed a real decision, not two mandatory stages for every task. Preserve the distinction between observed current work and a proposed future task model.

`HTA` also means Health Technology Assessment in the health section below. Resolve the acronym from the decision/output before selecting it. HTN is an AI planning formalism, not HTA; CWA analyzes work-system constraints, and cognitive walkthrough evaluates learnability rather than eliciting expert cognition.

### Hierarchical Task Analysis — HTA

- **Type / domain / lifecycle role / stack role:** method/technique; human factors and ergonomics; frame/design/improve; specialist, producing a task representation.
- **Purpose and output:** explain how a top-level goal is achieved through subordinate goals and operations. Produce a numbered hierarchy with execution plans specifying order, conditions, alternatives, repetition, and coordination where relevant. A tree or numbered checklist without plans is incomplete HTA.
- **Use when:** a procedure, interface, job aid, allocation of function, training analysis, or error-analysis input needs explicit task structure and representative work can be observed or elicited. Label future-design models as proposals for evaluation.
- **Do not use when:** the required output is tacit decision expertise, a performance-time prediction, a quantified human-error rate, or an independent safety demonstration. Add the appropriate method rather than infer these from the hierarchy. Do not force variable/adaptive work into one supposedly universal sequence.
- **Preconditions and required capability:** explicit goal, actors, context, system boundary, analysis purpose, and access to representative practitioners and task evidence; an analyst able to distinguish goals from interface features. Agree on numbering and decomposition grain. If evidence is unavailable, deliver a provisional model and an evidence-collection plan.
- **Typical procedure:**
  1. Define the goal, scope, context, current versus proposed work, and decisions the analysis will support.
  2. Observe or elicit representative task execution, including relevant variations; record evidence and unresolved assumptions.
  3. Decompose goals into subordinate goals/operations, with stable IDs and traceable parent relationships. Avoid a fixed number of levels or decomposition into every click by default.
  4. Write plans for each decomposed goal: sequence, guards, branches, repetition, and concurrent or coordinated work where observed or proposed. State completion conditions and recovery/escalation when material to the task.
  5. Stop decomposing when the chosen grain supports the downstream decision and further detail adds no material clarity or risk control; deepen uncertain or consequential operations. The historical probability × consequence stopping principle is a tailoring aid, not permission to invent numerical probabilities or acceptance thresholds.
  6. Walk through the model with representative practitioners and task evidence; check plan coverage, alternatives, completion, and recovery. Revise disputed branches before using the model to derive requirements or procedures.
- **Complements:** CTA for selected judgment-intensive operations; [SHERPA](#sherpa) for credible task errors and recovery; HRA or hazard analysis for use-related risk; UX evaluation, training design, or job-aid evaluation for the artifact derived from the model.
- **Alternatives or variants:** generic task analysis for a lightweight description; GOMS/KLM when their assumptions fit performance prediction; BPMN for process/handoff representation; HTN for executable AI planning. These differ in output and are not equivalent HTA variants. Graphical and tabular HTA are alternative representations of the same model.
- **Failure modes and gaming risks:** work-as-imagined, arbitrary decomposition, missing plans, one ideal user/path, stale numbering, inconsistent diagram/table, and treating fewer steps as proof of better performance. Validate usability, performance, and safety separately.
- **Adoption cost:** low for a bounded sketch; medium or high for a validated model with many roles/branches. Evidence access, analyst training, and maintenance dominate; software is optional.
- **Maturity:** established, research-grounded practice; no single normative owner or universal release version.
- **Canonical research anchors:** [Stanton (2006)](https://doi.org/10.1016/j.apergo.2005.06.003), [UXPA HTA guidance](https://www.usabilitybok.org/hierarchical-task-analysis), and its Annett–Duncan origin reference. [Hornsby (2010)](https://www.uxmatters.com/mt/archives/2010/02/hierarchical-task-analysis.php) provides a UX worked example rather than universal validation evidence.
- **Current version/status checked on:** 2026-09-12; an established technique, not a versioned normative specification.
- **Evidence and unresolved questions:** the primary review abstract identifies broad applications; professional guidance documents plans, stopping logic, training needs, and analyst variability. The full Stanton manuscript was unavailable during this research. Validate task coverage and downstream effects in the target context; the method itself proves neither time savings nor safety.

**Suggested output fields:** goal ID and parent; actor/context; operation or subordinate goal; evidence reference; plan and completion condition; material exception/recovery; decomposition-stop rationale. Treat these as a compact local reporting shape, not an external mandatory standard.

### Cognitive Task Analysis — CTA

- **Type / domain / lifecycle role / stack role:** elicitation and analysis family; human factors/cognitive ergonomics; frame/design/improve; specialist, producing evidence-based decision and cognitive-demand representations.
- **Purpose and output:** identify knowledge, cues, situation assessment, goals, strategies, uncertainty, and difficult judgments required for proficient task performance. Produce traceable cognitive demands and implications for training, information/interface design, or decision support; descriptions of actions alone are insufficient.
- **Use when:** diagnosis, anomaly detection, prioritization, expert decisions, or adaptive performance depends on knowledge not captured by a procedure, and domain practitioners and representative episodes/tasks are accessible.
- **Do not use when:** only simple observable actions require description; the needed experts/task evidence are inaccessible; or outputs will be treated as a direct readout of cognition, an exhaustive expert rulebook, or an independently validated safety claim. Mark evidence-poor reconstructions as hypotheses.
- **Preconditions and required capability:** a bounded task and downstream decision, domain-appropriate practitioners, representative routine and difficult work, trained interviewing/analysis, and consent/confidentiality where required. Preserve differences between expertise levels and contexts; do not prescribe a universal sample size.
- **Typical procedure:**
  1. Define the task, population/context, cognitive question, and the artifact or decision that will consume findings.
  2. Select a CTA technique by scope and evidence: ACTA for an applied overview of cognitive demands; CDM for probing specific challenging episodes. Use observation/protocol analysis when appropriate to the task and record any limits introduced by that choice.
  3. Elicit concrete examples: what was noticed, what it meant at that time, what goals/constraints mattered, which options were considered, what could go wrong, and what a less experienced performer might miss. Separate contemporaneous knowledge from hindsight.
  4. Analyze demands, cues, strategies, uncertainty, and errors with links to their episode/source. Preserve divergent strategies and context instead of merging them into one invented universal rule.
  5. Validate interpretations with practitioners and, where available, observation, records, contrasting episodes, or other participants. Distinguish testimony, corroborated findings, and unresolved analyst inference.
  6. Translate supported findings into information requirements, practice scenarios, job aids, or decision-support requirements; evaluate those products on representative tasks. Claims of improved performance need separate outcome evidence.
- **Complements:** HTA for task/goal structure where useful; learning and assessment in `18`; UX/information design in `20`; workload and human-reliability methods for distinct measurement/risk questions.
- **Alternatives or variants:** CTA is the family. ACTA and CDM have different interview structures and evidence focus; choose and document the technique instead of using the family name as a complete protocol. CWA is a complementary constraint-based framework, not an interchangeable interview method.
- **Failure modes and gaming risks:** retrospective/hindsight bias, leading questions, expert omission of automated knowledge, unsupported generalization across roles/sites, conflating confident explanation with observed performance, and ignoring physical/social/resource constraints.
- **Adoption cost:** medium for bounded applied elicitation, high for multi-context studies and triangulated analysis. ACTA streamlines some CTA work but does not eliminate practitioner access or evidence-analysis cost.
- **Maturity:** established research/practice family; no single owner or universal normative release version.
- **Canonical research anchors:** [UXPA CTA guidance](https://www.usabilitybok.org/cognitive-task-analysis); [Militello and Hutton (1998), ACTA](https://doi.org/10.1080/001401398186108); [Klein, Calderwood, and MacGregor (1989), CDM](https://doi.org/10.1109/21.31053).
- **Current version/status checked on:** 2026-09-12. Original publication identities and ACTA abstract were verified; technique choice and local tailoring remain context-specific.
- **Evidence and unresolved questions:** the ACTA abstract reports an evaluation of usability/usefulness, not universal performance benefits. An [open 2023 coaching study](https://doi.org/10.3389/fpsyg.2023.1154168) documents application, protocol adaptation, and retrospective/context-transfer limitations. Original ACTA/CDM full texts were not available during this research; consult them before claiming exact replication of either protocol.

#### Choosing and representing CTA techniques

| Technique | Evidence focus and procedure shape | Output / boundary |
| --- | --- | --- |
| Applied Cognitive Task Analysis — ACTA | task-diagram interview identifies demanding parts; knowledge audit probes expertise; simulation interview probes assessment/actions/cues and potential errors in a scenario | synthesize a cognitive-demands table and product implications; the three interviews are elicitation methods, while the table is the synthesis artifact. A task diagram is not automatically a complete HTA. Document omitted/adapted components rather than claim full protocol replication |
| Critical Decision Method — CDM | reconstruct and probe a concrete challenging incident and its decision points, cues, goals, judgments, and alternatives | incident/decision account with source-linked knowledge requirements; retrospective evidence needs checking for hindsight and transfer limits. Use the original/authoritative protocol for its exact interview sequence |

**Suggested output fields:** task/decision or episode ID; context and performer expertise; cognitive demand; cue/information source; interpretation and goal; strategy/alternatives; uncertainty and potential novice error; evidence and validation status; design/training implication. Adapt the fields to the selected technique; this is a local reporting aid, not a claim that all CTA protocols share one template.

### SHERPA

- **Type / domain / lifecycle role / stack role:** Systematic Human Error Reduction and Prediction Approach; established human-error identification method / human factors across operational and digital work / design, review, and improvement / task-risk analysis.
- **Purpose and output:** identify credible errors in HTA operations, their consequences and recovery opportunities, and remedies. Produce a traceable worksheet linking task ID, behavior category, error mode/description, consequence, recovery, supported ordinal likelihood, criticality, remedy, evidence, and validation status.
- **Use when:** operational or interface errors need systematic prediction and redesign, and a bounded HTA can be reviewed with practitioners who know the real task/context.
- **Do not use when:** task structure or practitioner evidence is unavailable, the question is chiefly tacit judgment rather than task errors, or quantitative human-error probabilities or demonstrated safety are required from this method alone.
- **Preconditions and required capability:** current HTA with operations/plans, credible work observations or incident evidence, trained analyst, practitioner review, and explicit system boundaries. Distinguish proposed tasks from observed work.
- **Typical procedure:**
  1. Establish and validate the HTA; retain operation IDs and context.
  2. Classify lowest-level operations as action, checking, retrieval, information communication, or selection.
  3. Apply the relevant SHERPA error taxonomy and retain only credible modes with a task-specific explanation; consult the chosen source for exact codes.
  4. Describe consequences and identify later checks, actors, or system functions that permit recovery; state when recovery is absent or only assumed.
  5. Assess ordinal likelihood and consequence criticality separately using declared scales and supporting evidence. Mark unsupported judgments unknown; do not turn ordinal classes into numerical probabilities.
  6. Propose remedies in equipment/interface, procedures, training, and organization; assign ownership and test the control and recovery under representative conditions.
- **Complements:** [HTA](#hierarchical-task-analysis--hta) supplies task structure; CTA investigates difficult judgments; [safety/hazard analysis](06-testing-reliability-safety-security.md#safety-and-hazard-analysis) covers wider system mechanisms; usability and recovery evaluation test resulting changes.
- **Alternatives or variants:** broader HRA methods for context/dependency or quantitative questions when their data assumptions hold; FMEA for component/process failure effects; STPA for unsafe control actions. Fuzzy risk scoring is an extension, not a required part of base SHERPA.
- **Failure modes and gaming risks:** apply every taxonomy code mechanically; omit recovery or context; equate possible-error counts with observed frequencies; rank unsupported likelihood; blame individuals or prescribe training for interface/resource defects; report proposed remedies as validated risk reduction.
- **Adoption cost:** medium for a bounded task, high for large HTAs, multiple contexts, and independent validation.
- **Maturity:** established technique; no universal normative edition or certification implied.
- **Canonical research anchors:** [maritime SAR application, full methods (2024)](https://doi.org/10.1016/j.heliyon.2024.e32043), which describes the eight-step procedure and taxonomy and cites Embrey's origin work.
- **Current version/status checked on:** 2026-09-12. Full open article consulted; local reporting fields and validation gate are explicit implementation aids.
- **Evidence and unresolved questions:** the application supports understanding of procedure, not universal effectiveness. Its ordinal labels and domain-specific criticality scheme should not be transplanted as calibrated probabilities or a generic severity scale. Exact replication requires the selected original taxonomy/protocol and domain validation.

## Health and medical devices

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 13485 + applicable regulatory QMS | medical-device QMS | lifecycle controls, records, supplier, production, CAPA, complaint, and regulatory evidence require an audited system | use ISO 9001 alone for regulated medical-device compliance or assume a certificate grants market authorization |
| Design and development controls / design history | regulated lifecycle/control system | user needs, inputs, outputs, reviews, V&V, transfer, and changes require traceability | prototype iteration is undocumented or design freeze occurs before intended use and risk are stable |
| ISO 14971 risk management | medical-device risk-management process | hazards, foreseeable sequences, harms, controls, residual risk, benefit–risk, and production/postproduction information must be governed | FMEA alone represents patient harm or risk acceptability is invented without policy/regulation |
| IEC 62366-1 usability engineering | medical-device usability/safety process | use-related hazards and critical tasks require formative and summative evidence with intended users/context | general satisfaction testing or consumer UX substitutes for use-safety validation |
| ISO 10993-1 biological evaluation | risk-based biological evaluation framework | body-contact materials, nature/duration of contact, chemistry, existing evidence, and testing require a justified plan | run a fixed checklist of animal tests or biocompatibility of one material proves the finished device safe |
| ISO 14155 clinical investigation GCP | regulated clinical-investigation methodology | human-subject device investigations need scientific/ethical design, conduct, records, monitoring, and reporting | conduct an informal product test on people or use the standard outside applicable law/ethics review |
| IQ/OQ/PQ medical-device process validation | regulated process-validation family | sterilization, sealing, molding, software-controlled or other processes cannot be fully verified by later inspection | retrospective paperwork or one nominal lot proves control across worst cases |
| IEC 62304 software lifecycle interface | medical-device software process standard | software safety classification, development, maintenance, risk interface, configuration, and problem resolution are required | treat it as a complete system-safety, cybersecurity, clinical, or AI standard |
| Production acceptance and release | controlled assurance activities | approved criteria, validated processes, batch/device records, deviations, and authorized disposition support release | PPAP/FAI analogies substitute for applicable QMS/product/process requirements |
| Clinical evidence / GRADE / target trial methods | evidence family | safety/effectiveness claims depend on clinical question, study design, bias, precision, applicability, and synthesis | mechanistic plausibility, uncontrolled case series, or regulatory authorization proves comparative effectiveness |

## Health systems and clinical guidance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Health Technology Assessment (HTA) | multidisciplinary appraisal method | clinical, economic, ethical, organizational, equity, and social consequences must inform adoption, reimbursement, or disinvestment | reduce HTA to cost-effectiveness or treat a manufacturer dossier as an independent assessment |
| Health needs assessment | population-health planning method | burden, unmet need, inequalities, service capacity, evidence, and priorities must guide resource allocation | equate observed service demand with need or omit access and prevention |
| Clinical practice guideline development | evidence-to-recommendation lifecycle | evidence must become transparent recommendations with scope, values, benefits, harms, feasibility, and update rules | copy a guideline across jurisdictions or treat consensus without evidence appraisal as sufficient |
| AGREE II | guideline-appraisal instrument | rigor, scope, stakeholder involvement, clarity, applicability, and editorial independence of a guideline need review | use an appraisal score as proof that recommendations are correct or locally applicable |
| Evidence-to-Decision | deliberative recommendation framework | certainty, benefits, harms, values, equity, acceptability, and feasibility must be visible before a recommendation | hide value judgments behind evidence grades or skip stakeholder/implementation context |
| Clinical pathway / care pathway | service-coordination method | evidence, roles, transitions, variation, escalation, and outcomes must be coordinated across a care process | turn a pathway into a rigid protocol that ignores clinical judgment, patient preference, or local capacity |

## Composition pattern

`jurisdiction/classification/intended use → QMS + design controls → clinical/user needs → ISO 14971 risk → usability/biological/software specialists → traceable design V&V → process validation/transfer → clinical/regulatory evidence → authorized production release → postmarket surveillance/CAPA`

## Research anchors and status

Status checked 2026-08-12.

- ISO 9241-210 remains the human-centred-design anchor; ISO 6385/26800 frame ergonomic work-system design. Check the exact edition and national adoption before conformity claims.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), ISO 14971:2019, IEC 62366-1, ISO 10993-1:2025, ISO 14155:2026, and IEC 62304 are current owner-page anchors subject to regulatory recognition/transition by jurisdiction.
- [FDA Quality Management System Regulation](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) became effective in 2026; its applicability and enforcement details must be checked live.
- [WHO health technology assessment](https://www.who.int/health-topics/health-technology-assessment) defines HTA as a multidisciplinary evaluation that supports health-system policy decisions; the 2025 WHO medical-device edition covers clinical, economic, ethical, and social implications.
- [AGREE II](https://www.nccmt.ca/knowledge-repositories/search/100) is an appraisal instrument for the methodological rigor and transparency of clinical-practice guidelines, not a clinical recommendation method.
