# Project, programme, and portfolio management

Use this catalog when the primary unit is a temporary project, a coordinated programme, a portfolio of investments, or the governance capability that supports them. Select the management layer and delivery approach before selecting tools. Do not mistake a product operating model, an engineering lifecycle, a process-improvement cycle, or an investment appraisal for project management.

## Contents

1. Ownership boundaries and routing
2. Project, programme, portfolio, and PMO governance
3. Delivery approaches and lifecycle tailoring
4. Definition, scope, schedule, and resources
5. Cost, uncertainty, and integrated control
6. Risk, quality, procurement, stakeholders, and change
7. Benefits, transition, assurance, closure, and recovery
8. Proportional stacks and selection rules
9. Research anchors and status

## Ownership boundaries and routing

| Unit or discipline | Primary decision | Canonical owner in this skill |
| --- | --- | --- |
| Strategy | which direction, position, and outcomes to pursue | `02-strategy-product-organization.md` |
| Product management | which user/customer problem and product outcome to pursue continuously | `02-strategy-product-organization.md` |
| Portfolio | which projects/programmes to authorize, fund, balance, pause, or stop | this catalog; use `12` for investment economics |
| Programme | how related components jointly produce capabilities, outcomes, and benefits | this catalog |
| Project | how to govern and deliver a temporary agreed change | this catalog |
| Engineering or software lifecycle | how to design, build, integrate, and verify the solution | `04`, `05`, `06`, or `14` |
| Process and operations | how to run and improve repeatable ongoing work | `03-process-operations-quality.md` |
| Organizational change and implementation | how people and settings adopt, adapt, scale, and sustain the change | `22-behavior-change-implementation.md` |
| Finance and business case | whether the investment is economically justified | `12-finance-market-audit-procurement.md` |

Apply these tests before routing:

- Treat work as a **project** only when it has a temporary governance boundary, a defined change or output, and accountable authorization/closure. A ticket queue is not automatically a project.
- Treat work as a **programme** only when coordinated components create benefits or capabilities that would not arise from managing each independently. A large project is not automatically a programme.
- Treat work as a **portfolio** when the decision is allocation and balance across investments. Portfolio management does not manage every component's daily execution.
- Treat a **PMO** as a governance/support capability whose form follows the decisions it must improve. Do not create reporting bureaucracy without authority, services, or measurable decision value.
- Keep product discovery and project control coupled but distinct: discovery changes what is valuable; project control manages commitments and consequences of change.

## Project, programme, portfolio, and PMO governance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| PMBOK Guide / Standard for Project Management | body of knowledge, principles, domains, and tailoring reference | establish broad project-management coverage, shared vocabulary, and fit-for-context practices | treat it as one prescriptive lifecycle or load every practice into every project |
| ISO 21502 | high-level project-management guidance | a sector-neutral reference must cover predictive, incremental, iterative, adaptive, or hybrid delivery | claim certification or expect a detailed execution method from guidance alone |
| PRINCE2 Project Management | tailorable project-management method | continuing business justification, defined products/roles, staged control, and management by exception fit | continuous operations/product work has no temporary project boundary or decision authority cannot operate the controls |
| Project charter / mandate | authorization artifact | sponsor, purpose, objectives, boundaries, authority, and initial constraints must be explicit | use a ceremonial document that does not actually authorize resources or decisions |
| Governance plan and decision-rights matrix | governance artifact | sponsor, board, project manager, product/technical authorities, and escalation rights are ambiguous | duplicate organization charts or make every decision require a committee |
| Stage-Gate / phase-gate governance | investment and evidence-gating process | uncertainty and exposure justify staged evidence with stop, redirect, hold, and continue authority | small reversible work or gates that only collect presentations and cannot change funding |
| Management by exception / tolerances | escalation-control principle | delegated teams need freedom inside explicit time, cost, scope, quality, risk, and benefit bounds | thresholds are arbitrary, late, or used to hide emerging problems until breach |
| ISO 21503 / programme-management guidance | programme governance reference | related components must coordinate dependencies, capabilities, outcomes, transition, and benefits | one project is renamed a programme only because it is large |
| PMI Standard for Program Management | programme principles and performance-domain reference | complex cross-component governance and benefits realization need a mature reference | use as a component-project scheduling manual |
| MSP-style programme management | benefits- and tranche-oriented programme method | transformation is delivered through coordinated tranches and an evolving target operating model | outputs are independent or programme-level governance cannot influence adoption and benefits |
| ISO 21504 / portfolio-management guidance | portfolio governance reference | projects and programmes must be selected, balanced, prioritized, monitored, and aligned | manage securities/financial portfolios or component execution details |
| Lean Portfolio Management | strategy-to-funding operating model | funding should follow value streams and strategic bets with feedback and decentralized delivery | preserve annual project budgeting and governance unchanged under a new label |
| Portfolio Kanban | portfolio flow visualization and WIP-control method | initiatives need transparent states, explicit policies, WIP limits, and aging/escalation signals | a board merely inventories projects without limiting starts or enabling stop decisions |
| Portfolio optimization / balance matrix | decision-analysis technique | risk, return, strategic fit, capacity, timing, dependencies, and mandatory work must be balanced | one weighted score hides hard constraints, uncertainty, or correlated portfolio risk |
| Benefits Realization Management | governance discipline and benefits map/register | investment outputs must trace to owned outcomes before and after delivery | benefits are vague aspirations or the project manager owns outcomes outside their control |
| Directive, controlling, or supportive PMO | organizational capability patterns | governance, assurance, standards, data, coaching, or shared services have an explicit demand | copy a PMO type without diagnosing decision latency, capability gaps, and authority |
| Project/Programme/Portfolio Management Office — P3O family | office-design reference model | coordinated decision support and assurance are needed across several management layers | one small project needs only lightweight coordination |

## Delivery approaches and lifecycle tailoring

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Predictive lifecycle | delivery approach | outputs and acceptance basis can be baselined early and late change is costly | problem/solution discovery dominates and plans are treated as certainty |
| Iterative lifecycle | delivery approach | repeated versions can improve correctness or fitness through feedback | partial iterations cannot be evaluated meaningfully |
| Incremental lifecycle | delivery approach | usable capability can be delivered in valuable slices | architecture, certification, or dependency structure prevents safe partial release |
| Adaptive/agile lifecycle | delivery approach | requirements and solution evolve through short feedback cycles with empowered prioritization | fixed baseline, independent certification, or irreversible hazards prohibit uncontrolled change |
| Hybrid lifecycle | tailored combination | governance, hardware/regulatory baselines, and software/discovery loops have genuinely different uncertainty | “hybrid” becomes unprincipled mixing with duplicate roles, cadences, and artifacts |
| Rolling-Wave Planning | progressive-detail planning technique | near-term work is clearer than distant work and later planning can absorb learning | all detail is required for authorization now or late planning cannot change locked dependencies |
| Scrum | product-development framework | a stable cross-functional team works toward one Product Goal under complexity | use as complete project governance, interrupt queue, or disconnected project fragments; see `03` |
| Kanban Method / Kanban Guide | flow-management method | continuous or mixed work needs explicit workflow, WIP control, service expectations, and flow learning | a task board is expected to supply project authorization, business case, or benefits governance; see `03` |
| Critical Chain Project Management | schedule/flow method | resource contention, harmful multitasking, and protection of completion through buffers dominate | organization-wide buffer behavior cannot be adopted or uncertainty is primarily discovery |
| Last Planner System | collaborative production-planning system | construction/production commitments, constraint removal, make-ready work, and plan reliability matter | use outside production contexts without adapting work packaging and field authority; see `36` |
| Integrated Product Team / concurrent engineering | cross-functional delivery pattern | engineering, manufacturing, support, commercial, and assurance decisions must be concurrent | roles lack authority or concurrency removes necessary independent verification |

Choose an approach from uncertainty and control needs, not sector stereotypes. A regulated project can contain adaptive discovery inside controlled baselines; an unregulated project can still need predictive coordination when dependencies and physical lead times dominate.

## Definition, scope, schedule, and resources

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Product Breakdown Structure — PBS | deliverable decomposition artifact | product-based planning and acceptance boundaries should precede activity planning | outputs are unknown and discovery must first determine them |
| Work Breakdown Structure — WBS | scope decomposition artifact | total authorized work needs hierarchical definition, ownership, estimating, and control accounts | decompose into arbitrary departmental tasks or confuse the WBS with the schedule |
| Requirements traceability / verification matrix | representation and assurance artifact | scope must trace from need through requirements, implementation, verification, and acceptance | volatile hypotheses are frozen prematurely; use `05` and `06` for specialist selection |
| Scope baseline and configuration management | controlled artifact set and change discipline | accepted product scope, WBS, specifications, and versions must remain reconstructable | exploratory work has no justified baseline yet or change control blocks learning without risk benefit |
| Responsibility Assignment Matrix / RACI | work-to-accountability artifact | WBS/deliverables and accountable organizational owners must be reconciled | every person is consulted/informed or the matrix substitutes for decision rights |
| Milestone plan / milestone trend analysis | planning and control technique | governance decisions depend on a small set of objective events and forecast movement | milestones are arbitrary dates without exit evidence or underlying network logic |
| Critical Path Method — CPM | deterministic network-schedule analysis | durations and logical dependencies are sufficiently stable to identify completion drivers and float | uncertainty, resource contention, calendars, or discovery invalidate a nominal critical path |
| PERT / three-point estimation | uncertainty-aware estimating technique | optimistic, most-likely, and pessimistic judgments improve activity or cost ranges | arithmetic averages conceal correlation, tail risk, bias, and weak reference data |
| Schedule Risk Analysis / Monte Carlo | probabilistic schedule model | uncertainty, correlation, branching, and deadline confidence materially affect commitments | the deterministic schedule is logically invalid or input distributions are invented without calibration |
| Integrated Master Schedule — IMS | integrated network schedule artifact | multiple teams/contracts must share traceable logic, milestones, calendars, and status | small work needs a simple plan or integration creates false precision and maintenance burden |
| Dependency Structure Matrix — DSM | dependency representation/analysis method | dense technical or organizational dependencies require sequencing, clustering, and iteration analysis | simple precedence is already clear or undocumented semantics make the matrix decorative |
| Resource loading and leveling | constrained-schedule technique | shared skills/equipment cause over-allocation and dates must reflect feasible capacity | level everything mechanically without priorities, calendars, productivity, or critical-resource policy |
| Resource smoothing | schedule-preserving resource technique | peaks can be reduced within available float without moving completion | demand exceeds capacity beyond float or hidden multitasking remains |
| Takt planning / location-based scheduling | production-flow scheduling family | repetitive spatial units and trade flow determine construction/manufacturing performance | knowledge work or nonrepetitive packages lack stable production rates |
| Reference-class forecasting | outside-view estimating method | comparable completed projects can counter optimism and strategic misrepresentation | reference class is cherry-picked, noncomparable, or data omit failed/cancelled projects |

## Cost, uncertainty, and integrated control

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Analogous estimate | top-down estimating technique | an early decision has little definition but credible comparable work exists | similarity adjustments are undocumented or the estimate is presented as control-grade |
| Parametric estimate | model-based estimating technique | validated cost/duration drivers and historical relationships apply | extrapolate beyond calibration range or ignore structural/regime change |
| Bottom-up estimate | detailed estimating technique | scope definition supports work-package quantities, rates, productivity, and responsibility | early discovery is forced into detailed fiction or omitted integration/overhead dominates |
| Three-point cost estimate | uncertainty-range technique | bounded expert judgments can expose skew and contingency needs | apply a formula mechanically without dependencies, systemic bias, or risk events |
| Cost/Schedule Risk Analysis — CSRA | integrated probabilistic analysis | correlated uncertainty and discrete risks affect cost and completion jointly | cost and schedule models are inconsistent or outputs are treated as guarantees |
| Contingency and management reserve | risk-funded budget controls | identified uncertainty and unknown exposure need transparent, governed reserves | reserve is hidden padding, double-counted with estimates, or spent as ordinary budget |
| Basis of Estimate — BoE | estimating evidence artifact | assumptions, scope, data, methods, exclusions, uncertainty, and validity date must be auditable | a point estimate is accepted without reconstructable evidence |
| Earned Value Management — EVM | integrated scope/schedule/cost performance method | objective progress, time-phased baseline, actual cost, and disciplined change control are meaningful | discovery work uses subjective percent complete or baseline churn makes indices meaningless |
| Earned Schedule | EVM extension | time-based schedule performance interpretation is needed alongside cost-domain EVM measures | replace network schedule analysis or infer completion from one index |
| Integrated Baseline Review — IBR | joint baseline-assurance gate | major governed work needs evidence that scope, schedule, budget, resources, risks, and control accounts form an executable baseline | a low-risk project gains no decision value from formal review |
| Estimate at Completion / independent forecast | forecasting control | current performance and remaining-risk evidence must update the expected outcome | force historical indices onto genuinely changed future work or suppress an independent view |
| Trend analysis and milestone confidence | control technique | leading indicators and forecast movement reveal deterioration before formal variance thresholds | green status is based on current dates rather than forecast confidence and risk |
| Change-control system | governance workflow and decision record | baseline changes need impact analysis, authority, traceability, and implementation control | every backlog refinement requires bureaucracy or approved changes erase original performance history |
| Configuration status accounting | control/evidence practice | decision makers must know which approved scope, design, software, and documents apply | version lists exist without unique identifiers, baselines, or reconciliation to delivered state |

## Risk, quality, procurement, stakeholders, and change

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Project risk-management cycle / ISO 31000 tailoring | governance process | uncertain events and conditions require identification, analysis, response, owners, triggers, and review | a static risk register substitutes for decisions and action |
| RAID log | compact risk/assumption/issue/dependency artifact | a moderate project needs one visible register with ownership and aging | categories are conflated or serious risks receive no analysis beyond a traffic light |
| Risk Breakdown Structure — RBS | risk-taxonomy artifact | coverage gaps and aggregation across workstreams must be visible | categories create false completeness or correlated/systemic risks are fragmented |
| Qualitative probability–impact analysis | triage technique | scarce analysis effort must focus on material exposures | ordinal scores are multiplied as exact quantities or low-probability catastrophes disappear |
| Quantitative risk analysis | probabilistic decision analysis | material cost/schedule/outcome uncertainty justifies modeled exposure and response trade-offs | distributions and dependencies cannot be defended or precision exceeds evidence |
| Premortem / prospective hindsight | risk-elicitation technique | social pressure and optimism suppress plausible failure narratives | treat imagined causes as verified probabilities or omit follow-up controls |
| Project FMEA / interface-risk review | prospective failure analysis | delivery processes, interfaces, handoffs, and integration failure modes need preventive controls | ordinal priority numbers become exact risk or complex system hazards require specialist methods in `06` |
| Quality management plan and acceptance strategy | governance artifact | standards, responsibilities, assurance, control, evidence, nonconformance, and acceptance must align | quality is reduced to end inspection or vague “done” statements |
| Make-or-buy / sourcing strategy | procurement decision method | capability, capacity, IP, risk, lifecycle cost, market, and schedule determine delivery route | lowest bid substitutes for total value/risk or core capability implications are ignored |
| Contracting strategy and incentive alignment | commercial governance method | allocation of scope, risk, uncertainty, incentives, data, and change affects outcomes | transfer risks to parties unable to control them or use fixed price before scope is definable |
| Supplier qualification and surveillance | assurance lifecycle | supplier capability, quality, security, continuity, or compliance is material | an onboarding questionnaire becomes perpetual proof; deepen in `12` |
| Stakeholder analysis and engagement plan | analysis plus action artifact | influence, impact, legitimacy, information, consent, resistance, and decisions differ across parties | manipulate stakeholders or ignore low-power/high-impact groups |
| Communications management | decision-information design | audiences need specified information, cadence, format, owner, escalation, and feedback | produce status volume without decision relevance or conceal uncertainty |
| Organizational change and adoption plan | implementation interface | project outputs require behavior, capability, workflow, incentive, or institutional change | the project team assumes delivery automatically creates adoption; select execution methods in `22` |

## Benefits, transition, assurance, closure, and recovery

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Benefits map / dependency network | causal governance artifact | outputs, capabilities, behavior, operational outcomes, owners, and assumptions must connect | arrows are treated as causal proof or benefits lack baselines and accountable owners |
| Benefits register and realization plan | governance artifact | benefit definitions, measures, timing, disbenefits, owners, dependencies, and reviews must survive project closure | benefits are booked at approval and never re-estimated or measured |
| Transition-to-operations / service-readiness review | acceptance and handover gate | people, process, support, data, security, capacity, training, suppliers, and recovery must be ready | document handover is mistaken for operational capability |
| Operational Readiness Activation and Transition — ORAT | transition methodology family | airports, facilities, infrastructure, or complex operations need integrated trials before opening | small changes or use as a generic acronym without operational scenarios and accountable operators |
| Verification, validation, and acceptance plan | assurance interface | technical conformity, intended-use fitness, and customer/authority acceptance are different claims | one test or stakeholder sign-off is allowed to prove all three; deepen in `06` |
| Independent project assurance / health check | independent assessment | exposure, novelty, governance complexity, or public interest justify a view outside delivery management | routine reporting is relabeled assurance or reviewers lack independence and evidence access |
| Gateway review | decision assurance method | an accountable sponsor needs independent evidence before major commitment or transition | reviewers take over management or the gate has no consequence |
| Reference-class / red-team review | challenge method | optimism, sunk-cost effects, strategic bias, or single-plan lock-in threaten decisions | critics receive no evidence, scope, decision route, or response obligation |
| Post-project evaluation / benefits review | evaluation lifecycle | completion claims and longer-term outcomes must be checked after transition | closeout satisfaction is confused with benefits or causal impact; use `08` for attribution |
| Lessons-learned review and knowledge transfer | organizational-learning practice | reusable positive/negative evidence can change standards, estimates, and future decisions | a retrospective produces a document with no owner, retrieval, or process update |
| Project health diagnostic | structured assessment | a troubled initiative needs an evidence-based view of purpose, governance, scope, plan, capability, controls, suppliers, and benefits | recovery action begins from status colors or stakeholder blame alone |
| Root-cause and contributing-factor analysis | diagnostic method family | recurrent slippage, defects, conflict, or control failure requires mechanism-level explanation | one “root cause” is asserted without timeline, evidence, systemic conditions, and alternatives |
| Recovery / turnaround plan | reauthorization artifact and execution cadence | remaining value justifies a credible reset of scope, leadership, resources, dependencies, controls, and milestones | rebaseline merely hides past variance or sunk cost replaces prospective value |
| Terminate, pause, pivot, or rescope decision | portfolio/project decision gate | evidence shows continuing unchanged is no longer the best use of capital or risk capacity | escalation of commitment, political optics, or already-spent cost drives continuation |

## Proportional stacks and selection rules

### Lightweight internal project

`one-page charter → deliverable/outcome list → owner and decision rights → milestone/backlog plan → compact RAID → acceptance evidence → short closeout and owner handover`

Do not impose full EVM, a formal PMO, or multiple boards unless exposure and interdependence justify them.

### Exploratory digital product initiative

`product outcome and discovery in 02/20 → lightweight project authorization/funding boundary → adaptive delivery in 03/04 → rolling-wave dependencies and risk → release/operational assurance in 06 → outcome and benefit review`

Do not baseline speculative feature scope as though it were known. Preserve technical, privacy, security, and financial gates.

### Governed predictive or capital project

`business case in 12 → charter/governance → PBS/WBS + requirements/configuration → integrated cost/schedule/risk baseline → contracting and quality plans → IBR → objective progress/EVM + forecast → independent gates → commissioning/transition → post-project and benefits evaluation`

### Transformation programme

`strategic outcomes → programme mandate and blueprint/target state → benefits map and owners → component architecture/dependencies → tranche governance → organizational implementation in 22 → capability transition → benefit/disbenefit measures → adapt, close, or continue`

### Portfolio allocation and review

`strategy and constraints → candidate business cases → mandatory-work separation → comparable value/risk/capacity evidence → dependency and concentration view → portfolio selection/balance → WIP/funding decisions → periodic re-estimation → stop/pivot/reallocate decisions`

### Troubled-project recovery

`independent evidence freeze → purpose and remaining-value test → technical/commercial/governance diagnostic → credible forecast and scenario options → stop/pause/pivot/recover decision → explicit reauthorization → short recovery milestones and leading indicators → independent follow-up`

Use these selector rules:

- Select a **backbone** first: PMBOK/ISO guidance for coverage, PRINCE2 for staged method/governance, or a programme/portfolio standard for the higher management layer.
- Add only the controls needed by the decision: a WBS does not imply EVM; EVM requires an objective integrated baseline and change discipline.
- Use probabilistic cost/schedule analysis only after logic, quantities, rates, calendars, and dependencies are credible.
- Pair internal status with an independent gate when safety, public funds, irreversible capital, certification, or severe downside is material.
- Keep delivery success, transition readiness, benefit realization, and causal impact as separate claims.
- Preserve the original baseline and decision history when rebaselining; otherwise recovery erases learning and accountability.

## Research anchors and status

Status checked 2026-08-13. Recheck live owner pages before naming a version in a consequential recommendation.

- PMI's official PMBOK page identifies the PMBOK Guide — Eighth Edition as the current guide, published in November 2025; it is a standard/body-of-knowledge reference, not one universal prescriptive method.
- PeopleCert now brands the current method as PRINCE2 Project Management (Version 7); current official materials use the Version 7 name. Treat commercial certification material separately from evidence of project outcomes.
- ISO 21502:2020 is published guidance for project management across predictive, incremental, iterative, adaptive, and hybrid approaches. ISO 21503:2022 and ISO 21504:2022 separately cover programme and portfolio management; do not collapse their scopes.
- PMI's Standard for Program Management — Fifth Edition was published in March 2024. Check PMI's live portfolio-standard page before naming its current edition.
- ISO 21508:2026 is the current published earned-value guidance and replaces ISO 21508:2018. ISO 21512:2024 supplies EVM implementation guidance.
- ISO 21511:2018 on work breakdown structures is under revision; label the ISO/DIS 21511 draft as a draft rather than current normative replacement.
- ISO 21513:2026 is published guidance on post-project and post-programme evaluation. Do not mistake evaluation guidance for causal attribution of benefits.
- Use the US GAO Cost Estimating and Assessment Guide (GAO-20-195G) and Schedule Assessment Guide (GAO-16-89G) as public, auditable best-practice anchors for estimate and schedule credibility; tailor jurisdictional/government requirements rather than claiming universal conformity.
- Use ISO 31000 for general risk principles, then select sector hazard, safety, security, or financial methods from their canonical catalogs.
- Use official owners and primary standards for deep research. Treat proprietary maturity models, certification syllabi, and vendor PMO templates as secondary candidates until scope, version, and independent evidence are verified.
