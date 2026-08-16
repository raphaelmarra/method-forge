# Process, service operations, quality, and continuous improvement

Use this catalog when repeatable work must be discovered, flowed, controlled, improved, standardized, operated, or restored. Do not use process, project, product, and operations methods interchangeably. For temporary delivery, programme coordination, portfolio governance, project controls, or recovery, use `30-project-programme-portfolio-management.md`.

## Agile and flow delivery

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Agile Manifesto / principles | values and principles | uncertainty and feedback reward adaptive delivery | cite as permission to omit engineering discipline or governance |
| Scrum | product-development framework | a small stable team tackles complex product work toward one Product Goal | interrupt-driven service desk, independent project fragments, or no empowered Product Owner |
| Kanban Method / Kanban Guide | flow-management method/framework | visualize work, limit WIP, manage policies, and improve continuous flow | a task board without WIP policies, service expectations, or flow metrics |
| Extreme Programming (XP) | software-development method/practice set | requirements change and technical feedback must remain fast through TDD, CI, pairing, refactoring | teams unwilling or unable to sustain technical practices |
| SAFe | proprietary scaling framework | many coordinated teams need a shared operating model and accept substantial governance overhead | small organizations or when hierarchy and synchronized cadence worsen local flow |
| Disciplined Agile | context-driven toolkit | teams need guided tailoring across lifecycle and enterprise constraints | selection becomes an excuse for incoherent pick-and-mix |

## Process discovery and design

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| SIPOC | high-level process-scoping artifact | align suppliers, inputs, process, outputs, and customers before detailed analysis | detailed control logic, root cause, or performance diagnosis |
| BPMN | notation/metamodel | explicit events, flows, roles, gateways, and messages need shared representation | assume drawing a process improves or automates it |
| Value Stream Mapping | Lean mapping method | quantify end-to-end value and information flow, waits, handoffs, and waste | dynamic behavior or services that cannot be reduced to one representative flow |
| Process Mining | evidence-based process-analysis family | event logs can reveal actual variants, bottlenecks, conformance, and rework | logs lack case identity/timestamps or observed traces are mistaken for causal explanation |
| Task Mining | user-interaction discovery technique | desktop-level work and variation are otherwise invisible | intrusive collection without privacy/governance or as proof of business value |
| APQC Process Classification Framework | process taxonomy/reference model | build a common enterprise process inventory and benchmark categories | prescribe how a particular process must operate |
| Theory of Constraints (TOC) | system-improvement methodology | one or few constraints dominate throughput | optimize a locally visible bottleneck without testing whether it constrains the whole system |
| Business Process Reengineering (BPR) | radical redesign approach | incremental improvement cannot overcome obsolete process assumptions | high-risk “clean slate” change without evidence, adoption, and transition controls |
| Standard Work | Lean operational artifact/practice | a repeatable best-known method needs stability and a baseline for improvement | freeze exploratory knowledge work or suppress frontline learning |

## Quality and continuous improvement

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| PDCA / PDSA | iterative improvement cycle | test a change, study observed results, and adapt | relabel ordinary task execution without prediction or learning |
| DMAIC | data-driven improvement methodology | an existing process has measurable defects/variation and needs sustained control | design a new product from an unclear need |
| DMADV / DFSS | design-for-quality methodology | a new or radically redesigned process/product must meet measurable critical requirements | a small fix to a stable existing process |
| Lean | management system and principles | reduce delay, inventory, handoffs, overburden, and non-value work while improving flow | equate Lean with headcount cuts or remove resilience blindly |
| Six Sigma | quality-management methodology/toolkit | variation and defect reduction justify statistical rigor and specialist capability | low-volume work with no stable measurement system |
| Lean Six Sigma | composite improvement approach | both flow waste and process variation materially constrain outcomes | stack branding without diagnosing which mechanism matters |
| Statistical Process Control (SPC) | statistical monitoring/control method | repeated process measures permit common- vs special-cause distinction | one-off projects or unstable definitions/data collection |
| FMEA | failure-mode analysis | proactively rank and control plausible component/process failures | infer exact risk from ordinal RPN or analyze complex unsafe interactions alone |
| 8D | corrective-action method | cross-functional containment, root-cause correction, and recurrence prevention are needed | exploratory innovation or incident learning without a discrete nonconformity |
| A3 Problem Solving | structured improvement/communication method | one problem needs concise current state, analysis, countermeasures, and follow-up | compress complexity until uncertainty and dissent disappear |
| 5 Whys / Ishikawa | root-cause elicitation techniques | structure causal hypotheses for a bounded problem | claim causality without data or assume one linear root |
| Quality Function Deployment (QFD) | needs-to-requirements translation method | customer needs must trace into prioritized design characteristics | substitute the “voice of customer” matrix for observed use and engineering trade-offs |
| ISO 9001 | quality management system standard | organization-wide quality processes, audit, accountability, and improvement are required | a project method or product-quality specification |

## Structured improvement and learning

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| IHI Model for Improvement | improvement framework; aim, measures, change ideas, and PDSA learning loop | a team needs to test and implement changes quickly while tracking whether improvement is real and equitable | call a few unmeasured experiments a completed improvement program or ignore system constraints |
| Run chart | time-series improvement artifact | process measures need a simple view of level, trend, shift, or run before formal control limits | treat every fluctuation as a special cause or use it without stable measurement definitions |
| Driver diagram | causal improvement artifact | a team must connect an aim to primary/secondary drivers and change ideas | present assumed drivers as causal proof or turn the diagram into an exhaustive strategy |
| 5S | workplace-organization method | safe, visible, repeatable work benefits from sorting, setting, cleaning, standardizing, and sustaining | use housekeeping as a proxy for flow, quality, or respect for workers |
| Failure demand analysis | service-improvement analysis | avoidable contacts, rework, complaints, or repeat demand consume capacity | classify all demand as failure or optimize contact volume without resolving the cause |
| Hoshin Kanri catchball | strategy deployment method | strategic priorities must translate into aligned local objectives, measures, review, and learning | cascade targets without negotiation, capacity, or countermeasures |

## Operations, service, and resilience

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ITIL | IT service-management practice framework | value streams, incidents, changes, service levels, and continual improvement need governance | software-development lifecycle or copy-all-practices rollout |
| ISO/IEC 20000-1 | service-management system standard | auditable organization-wide service management and certification may matter | detailed runbook or engineering architecture |
| SLI / SLO / Error Budget | reliability decision framework | user-facing reliability can govern release vs reliability investment | arbitrary uptime targets or SLAs copied directly into internal SLOs |
| Golden Signals / RED / USE | observability heuristics | choose an initial compact set of service/resource signals | a closed list that replaces domain-specific indicators |
| Incident Command System | incident-coordination structure | multi-party incidents require clear command, operations, planning, and communications | trivial incidents where structure costs more than coordination |
| Blameless Postmortem | learning practice/artifact | analyze contributing conditions and own corrective actions after incidents | remove accountability, omit human factors, or produce action lists with no follow-through |
| Chaos Engineering | controlled experimental method | observable systems have a steady-state hypothesis, bounded blast radius, and abort conditions | the first test of an unknown system or uncontrolled production fault injection |
| Business Impact Analysis / BCP / DR | continuity discipline | prioritize services, dependencies, RTO/RPO, recovery, and exercises | assume backup possession proves restoration ability |
| OEE | operations metric | availability, performance, and quality jointly constrain equipment effectiveness | knowledge work or a target that encourages unsafe local utilization |
| Queueing Theory / Little's Law | operations-analysis theory | flow, WIP, throughput, and waiting time need quantitative reasoning | assumptions are violated and averages hide priority/tail behavior |

## Research anchors

- Scrum Guide and Kanban Guide for adaptive delivery/flow; route project governance and controls to `30-project-programme-portfolio-management.md`.
- ISO 9001, ISO/IEC 20000-1; APQC PCF.
- IEEE Task Force on Process Mining and the Process Mining Manifesto.
- Google SRE books for SLOs, incident response, toil, overload, and canarying.
- Principles of Chaos Engineering for the canonical experimental framing.
- [IHI Model for Improvement](https://www.ihi.org/library/model-for-improvement) and the Improvement Guide for aim-setting, measures, change ideas, PDSA testing, implementation, and spread.
