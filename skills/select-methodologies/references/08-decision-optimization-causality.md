# Decision analysis, optimization, uncertainty, and causality

Use this catalog when alternatives, preferences, constraints, uncertainty, learning, or causal effects determine the answer. Do not optimize before confirming the objective and causal model. A mathematically optimal answer to the wrong model is still wrong.

## Contents

1. Problem framing and decision rights
2. Multicriteria and preference modeling
3. Risk, uncertainty, optimization, and search
4. Experimentation and adaptive decisions
5. Causal framing, identification, mechanisms, and research anchors

## Problem framing and decision rights

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Decision Analysis | discipline/process family | choices, uncertainties, objectives, consequences, and preferences should be explicit | the problem is purely factual or a mandatory constraint dictates one option |
| Decision Quality | decision-process framework | assess frame, alternatives, information, values, reasoning, commitment, and action | score a decision by outcome hindsight alone |
| Cynefin | sense-making framework | choose response style for clear, complicated, complex, chaotic, or confused contexts | permanent labeling, ranking options, or avoiding domain analysis |
| OODA Loop | adaptive decision cycle | observation and action must update rapidly in a changing/adversarial environment | irreversible regulated actions without deliberate verification gates |
| RAPID / DACI | decision-rights frameworks | cross-functional decisions stall because recommend/input/decide/perform roles are unclear | simple local decisions or multiply acronyms without solving authority |
| RACI | responsibility artifact | execution/accountability/consultation/information roles need clarity | identify the actual decision maker in contentious decisions without extension |
| Decision Journal | learning artifact | preserve forecasts, assumptions, alternatives, confidence, and expected signals before outcomes | post-hoc narrative or sensitive decisions without access controls |

## Multicriteria and preference modeling

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| MCDA / MCDM | decision-method family | monetary and nonmonetary criteria conflict across alternatives/stakeholders | hard constraints already decide or criteria/alternatives remain ill-defined |
| Multi-Attribute Utility Theory (MAUT) | compensatory preference method | cardinal value functions and trade-offs can be elicited defensibly | criteria dependence and utility assumptions are ignored |
| Weighted Sum Model | simple MCDA technique | normalized comparable criteria and transparent weights suffice | scales are incompatible, thresholds/veto matter, or weights are arbitrary |
| AHP | pairwise hierarchical MCDA method | a modest hierarchy benefits from structured relative judgments and consistency checks | many alternatives/criteria, rank reversal concerns, or dependence dominates |
| ANP | network pairwise MCDA method | criteria and alternatives influence one another and pairwise elicitation is feasible | complexity overwhelms reliable judgments |
| ELECTRE | outranking method family | veto, incomparability, and non-compensatory preferences matter | stakeholders require one smooth cardinal utility function |
| PROMETHEE | outranking/ranking family | preference functions and pairwise outranking fit criteria | thresholds/functions cannot be justified or ranking hides incomparability |
| TOPSIS | distance-to-ideal ranking technique | normalized criteria and ideal/anti-ideal comparison are meaningful | compensation and distance metric lack decision meaning |
| Pareto Frontier | dominance analysis | expose non-dominated trade-off options before preference aggregation | return one recommendation without acceptability constraints or values |
| Value-Focused Thinking | alternative-generation approach | objectives should drive creative alternatives rather than compare a fixed list | objectives are mandated and option generation is not possible |

## Risk and uncertainty

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 31000 | risk-management principles/framework/process | organization or decision needs integrated identification, analysis, evaluation, treatment, monitoring, and communication | treat as certification or a specific quantitative risk technique |
| IEC 31010 | risk-assessment technique guidance | select an assessment technique suited to purpose, data, complexity, and lifecycle | choose by familiarity without checking method assumptions |
| Risk Matrix | qualitative/semiquantitative artifact | initial communication and triage with well-defined scales are sufficient | precise ranking, aggregation, or thresholds where category compression distorts risk |
| Decision Tree | sequential decision model | choices, chance events, probabilities, and consequences form a manageable tree | combinatorial state explosion or dependencies violate the tree |
| Influence Diagram | probabilistic decision representation | compactly show decisions, uncertainty, information, and utility dependencies | causal/probabilistic arcs are speculative or temporal detail is essential |
| Expected Utility Theory | normative decision model | probabilities and utility under risk can be elicited and accepted | deep uncertainty or stakeholder values cannot be reduced to one utility |
| Bayesian Decision Theory | probabilistic decision framework | new evidence should update beliefs and action optimizes posterior expected utility | priors/likelihoods/utilities are fabricated or safety constraints are averaged away |
| Monte Carlo Simulation | uncertainty propagation technique | input distributions and a computational model can expose outcome ranges/tails | structural model error dominates or distributions/correlations lack basis |
| Sensitivity Analysis | robustness technique | determine which assumptions/weights/parameters alter decisions | one-at-a-time checks miss interactions or ranges are implausibly narrow |
| Scenario Analysis | discrete uncertainty technique | coherent alternative futures illuminate conditional outcomes | scenarios are treated as probabilities or one preferred forecast |
| Robust Decision Making (RDM) | decision-making-under-deep-uncertainty method | many plausible futures and contested models favor robust strategies and vulnerability analysis | well-characterized simple risk or computation/stakeholder capacity is absent |
| Minimax Regret | robust decision criterion | avoid options with severe opportunity loss under uncertain states | extreme states dominate despite low relevance or probabilities are reliable enough for utility analysis |
| Info-Gap Decision Theory | robustness/opportuneness method | uncertainty is severe and unbounded around an estimate | use without understanding its local uncertainty model and criticism |
| Real Options Analysis | staged-investment method | defer, expand, contract, switch, or abandon flexibility has material value | no managerial flexibility, irreversible immediate commitment, or pseudo-option assumptions |
| Value of Information (EVPI/EVSI) | decision-research valuation method | decide whether more data/testing/research can change a choice enough to justify cost | new information cannot affect decision/action or probability model is baseless |

## Optimization and search

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Linear Programming (LP) | mathematical optimization | linear objective/constraints and divisible decisions approximate resource allocation | nonlinear, discrete, uncertain, or qualitative structure is material |
| Mixed-Integer Linear Programming (MILP) | mathematical optimization | discrete choices and linear constraints represent scheduling, routing, selection, or design | model scale or uncertain coefficients make exact optimization misleading/intractable |
| Constraint Programming | combinatorial solving paradigm | complex logical/global constraints and feasible schedules/configurations dominate | a smooth numeric objective is the main structure |
| Dynamic Programming | optimization technique | sequential subproblems exhibit optimal substructure and manageable state | state explosion or changing model invalidates recursion |
| Network Flow / Shortest Path | graph optimization family | routing, allocation, matching, or flow maps to graph structure | non-network constraints dominate |
| Stochastic Programming | optimization under uncertainty | distributions/scenarios and recourse decisions can be represented | probabilities are deeply uncertain or scenario set hides model risk |
| Robust Optimization | optimization under uncertainty | bounded uncertainty sets and worst-case feasibility are appropriate | conservatism cost is unacceptable or uncertainty set is arbitrary |
| Multi-objective Optimization | optimization family | multiple mathematical objectives generate trade-off solutions | criteria are qualitative/unmodeled or one hard rule decides feasibility |
| Metaheuristics | approximate optimization family | exact methods are infeasible and solution quality can be evaluated | no validation/bounds, small solvable problem, or randomness obscures reproducibility |
| Simulation Optimization | search over simulated systems | analytic objective is unavailable but a validated simulator exists | simulator fidelity and noise are not characterized |
| Bayesian Optimization | sample-efficient black-box optimization | evaluations are expensive and parameter dimension is modest | unsafe exploration, high-dimensional/categorical space, or nonstationarity overwhelms surrogate |

## Experimentation and adaptive decisions

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Randomized Controlled Trial / A/B Test | experimental causal design | treatment can be randomized ethically with adequate units and stable measurement | interference, spillovers, rare harms, or inadequate power invalidate inference |
| Multivariate / Factorial Experiment | experimental design | interactions among several controlled factors matter | sample size, safety, or operational complexity cannot support cells |
| Sequential Testing | adaptive statistical design | evidence should be monitored with controlled stopping/error properties | repeatedly peek at fixed-horizon p-values without correction |
| Multi-Armed Bandit | adaptive allocation method | reward is observed quickly and exploration/exploitation can occur safely | long-term/rare harms, delayed feedback, nonstationarity, or inference needs are ignored |
| Contextual Bandit | adaptive decision method | treatment value depends on observed context and online learning is safe | hidden state/sequential consequences require reinforcement learning or causal confounding persists |
| Reinforcement Learning | sequential control method | repeated interaction, delayed reward, and learnable environment justify exploration/control | high-stakes real-world exploration without simulator, constraints, and assurance |

## Causal framing and identification

Always separate prediction from intervention. Use the sequence:

`causal question → target population and estimand → causal graph/assumptions → identification strategy → estimator → diagnostics/refutations → sensitivity → decision`.

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Structural Causal Models / DAGs | causal modeling framework/artifact | make assumed causal structure, confounders, mediators, colliders, and interventions explicit | claim the drawn graph is discovered truth or condition on variables mechanically |
| Potential Outcomes / Rubin Causal Model | causal estimand framework | define treatments, counterfactuals, populations, effects, and assignment assumptions | the question is prediction or treatment versions/interference are undefined |
| Target Trial Emulation | observational study-design method | observational data should emulate eligibility, assignment, time zero, follow-up, outcomes, and analysis of a hypothetical trial | data cannot align time zero or avoid immortal-time/selection bias |
| Randomized Experiment | identification design | ethical random assignment identifies an intervention effect under stated conditions | noncompliance, attrition, interference, or external validity are ignored |
| Difference-in-Differences | quasi-experimental design | treated/control groups and pre/post periods support plausible parallel trends | anticipatory effects, staggered-treatment pitfalls, or differential shocks are ignored |
| Regression Discontinuity | quasi-experimental design | treatment assignment changes at a non-manipulated threshold with enough local data | sorting/manipulation, discontinuous covariates, or weak local sample |
| Instrumental Variables | identification method | instrument relevance, independence, exclusion, and monotonicity can be defended | “instrument” affects outcome through other paths or weak-instrument bias dominates |
| Synthetic Control | comparative case method | one/few treated units have long pre-period and a suitable donor pool | poor pre-treatment fit or contamination of donors |
| Interrupted Time Series | quasi-experimental design | many observations surround a well-timed intervention and trends/seasonality can be modeled | concurrent interventions or too little pre/post history |
| Matching / Propensity Scores | observational adjustment family | all material confounders are measured and overlap exists | unmeasured confounding, positivity violations, or balance is assessed only by propensity fit |
| Doubly Robust Estimation | causal estimation family | combine outcome and treatment models so one correct model may suffice under assumptions | both models are misspecified or identification assumptions fail |
| Causal Forests / Heterogeneous Treatment Effects | causal ML family | treatment-effect variation is decision-relevant and sample/support are sufficient | post-hoc subgroup fishing or point estimates without uncertainty/overlap checks |
| Negative Controls | causal diagnostic method | outcomes/exposures known not to be causal can reveal residual bias | passing one negative control proves identification |
| Placebo / Refutation Tests | robustness technique | alternative timings/groups/outcomes can challenge the causal story | cherry-pick tests or treat non-rejection as proof |
| Sensitivity Analysis for Unmeasured Confounding | causal robustness family | quantify how strong hidden bias must be to alter conclusions | report one sensitivity parameter without domain interpretation |
| Causal Discovery | hypothesis-generation method family | observational conditional independencies can propose candidate graph structure under explicit assumptions | present learned edges as confirmed causality without intervention/domain validation |

## Complex interventions and mechanisms

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Theory of Change | program causal model | stakeholders need explicit mechanisms, assumptions, intermediate outcomes, and indicators | causal identification proof |
| Contribution Analysis | theory-based evaluation method | multiple influences make attribution difficult but a contribution claim can be strengthened | precise isolated effect estimate is required and feasible |
| Process Tracing | within-case causal inference method | evidence about mechanisms and sequence within cases can discriminate explanations | broad population effect estimation or storytelling without diagnostic evidence |
| Realist Evaluation | theory-driven evaluation | ask what works, for whom, in what circumstances, and how | homogeneous intervention effect is the sole question |
| System Dynamics | feedback simulation methodology | stocks, flows, delays, nonlinear feedback, and policy resistance matter | uncalibrated causal-loop diagrams are treated as forecasts |
| Agent-Based Modeling | simulation method | heterogeneous autonomous actors and local interactions generate emergent outcomes | rules/calibration lack evidence or one run is treated as prediction |

## Research anchors

- ISO 31000 and IEC 31010 for risk framing and technique selection.
- Government analytical guidance for MCDA, appraisal, and decision making under uncertainty.
- Primary texts/software documentation for causal inference; World Bank impact evaluation and PyWhy/DoWhy are useful gateways.
- Report estimand, assumptions, identification, diagnostics, uncertainty, and external validity—not just an estimator name.
