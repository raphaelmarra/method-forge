# Probability, statistics, inference, and uncertainty

Use this catalog when probability models, sampling, estimation, statistical evidence, prediction, measurement error, or uncertainty communication determine the answer. It is the canonical owner for general statistical reasoning. Domain catalogs should link here for the generic method and retain only the domain-specific design, authority, outcome, and validation constraints.

## Contents

1. Ownership boundary and routing
2. Probability and stochastic models
3. Sampling and study design
4. Description, estimation, and uncertainty
5. Testing and decision thresholds
6. Regression, hierarchical, and multivariate models
7. Time, event, and reliability data
8. Bayesian inference and probabilistic prediction
9. Missingness, measurement, and robustness
10. Validation and communication
11. Composition patterns
12. Research anchors

## Ownership boundary and routing

This catalog owns generic statistical procedures and their assumptions. Route a request here when the main question is how to represent variation, draw a sample, estimate a quantity, test a claim, predict an outcome, or quantify uncertainty.

Keep the domain catalog as the primary owner when the domain changes the governing decision or validity boundary:

- causal identification and treatment effects remain in `08-decision-optimization-causality.md`;
- evidence-search and synthesis protocols remain in `31-research-evidence-investigation.md`;
- clinical-guideline appraisal and medical-device evidence remain in `35-human-factors-health-medical-devices.md`;
- spatial estimands and spatial dependence remain in `33-geospatial-location-analysis.md`;
- process control and manufacturing capability remain in `03-process-operations-quality.md` and `14-physical-engineering-manufacturing.md`;
- reliability-specific models and maintenance decisions remain in `06-testing-reliability-safety-security.md` and `34-asset-maintenance-reliability.md`;
- learning assessment and transfer remain in `18-learning-training-education.md`.

The generic statistical method is linked rather than copied. Create a domain specialization only when it changes the experimental unit, sampling frame, estimand, authority, measurement system, or failure modes.

## Probability and stochastic models

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Probability model | mathematical representation | uncertain states, events, or outcomes need explicit assumptions | assign precise probabilities without a defensible reference class or elicitation process |
| Conditional probability and Bayes' rule | probabilistic reasoning technique | evidence changes the plausibility of hypotheses or events | confuse `P(A\|B)` with `P(B\|A)` or omit base rates |
| Random variables and distributions | probability model family | variation, tail behavior, and dependence need a generative description | fit a familiar distribution without checking support, tails, or dependence |
| Joint, marginal, and conditional distributions | dependence representation | multiple uncertain quantities interact or information arrives sequentially | assume independence because the model is easier |
| Markov chains and state-space models | stochastic process family | future state depends on current state and transitions are meaningful | collapse long memory, seasonality, or hidden state without testing the assumption |
| Poisson processes and counting models | event-arrival model family | events occur over exposure, time, or space and rates are meaningful | ignore overdispersion, clustering, censoring, or changing exposure |
| Monte Carlo simulation | uncertainty propagation technique | a computational model can propagate input distributions and dependencies into outcome ranges | structural model error dominates or input distributions are invented |

## Sampling and study design

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Target population and estimand definition | study-framing method | the quantity, population, time, and decision must be explicit before analysis | treat an available dataset as if it automatically defines the target |
| Probability sampling | sampling design family | inclusion probabilities and population-level estimation matter | claim population coverage from convenience or volunteer samples |
| Stratified sampling | sampling design | important subgroups differ or require precision/representation | strata are poorly defined or allocation is unrelated to the decision |
| Cluster and multistage sampling | sampling design | units are naturally grouped, dispersed, or expensive to enumerate individually | analyze clustered observations as independent without design correction |
| Survey weighting and calibration | estimation adjustment | unequal inclusion, nonresponse, or known population margins affect representation | weights are treated as a cure for unmeasured selection bias |
| Randomized experiment | causal study design | assignment can be randomized and the intervention/outcome are measurable | interference, noncompliance, rare harms, or inadequate power invalidate the design; see `08` |
| Factorial and blocked design | experimental design | several factors, interactions, or nuisance gradients need efficient controlled comparison | cells are too small or treatment assumptions are not stable |
| Quasi-experimental design | causal design family | randomization is unavailable but a credible assignment rule or comparison exists | call adjustment alone causal without identification assumptions; see `08` |
| Power and sample-size analysis | design planning method | detectable effect, precision, error rates, or resource limits must be made explicit | use a conventional threshold without specifying estimand, variance, attrition, or practical importance |

## Description, estimation, and uncertainty

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Exploratory data analysis | discovery/diagnostic method | distributions, outliers, missingness, transformations, and relationships need inspection | use exploratory patterns as confirmatory evidence without a new analysis plan |
| Robust summaries | descriptive technique family | skew, outliers, or heavy tails make mean/standard deviation fragile | hide important tail behavior behind resistant summaries |
| Sampling distribution and standard error | inferential concept | repeated-sample variation of an estimator needs quantification | mistake standard error for individual prediction uncertainty |
| Confidence interval | frequentist interval procedure | repeated-sampling coverage is the intended interpretation | describe it as the probability that this fixed parameter lies in this interval |
| Prediction interval | uncertainty interval | a future individual or aggregate outcome needs a range | use a confidence interval when outcome-level variation matters |
| Bootstrap | resampling inference method | analytic uncertainty is difficult and the data reasonably represent the sampling process | small, dependent, censored, or boundary data violate the resampling design |
| Jackknife | leave-one-out resampling method | influence, bias, or variance can be approximated by deleting observations | highly nonlinear or small-sample behavior makes the approximation unstable |
| Robust estimation | estimation family | contamination, heavy tails, or bounded influence are material | select a robust estimator without explaining the target estimand |
| Measurement uncertainty budget | uncertainty-analysis method | instruments, processes, and inputs contribute identifiable uncertainty components | report a single error bar without traceable components or calibration context |

## Testing and decision thresholds

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Null and alternative hypotheses | inferential framing | a claim needs a specified reference model and departure of interest | use a null merely because software requires one |
| Permutation test | randomization-based test | exchangeability or a valid assignment mechanism supports the reference distribution | permute observations that are clustered, dependent, or structurally different |
| Randomization inference | design-based inference | treatment assignment itself defines the exact reference distribution | assignment was not randomized or the estimand is left implicit |
| Likelihood-ratio test | model comparison test | nested models and likelihood assumptions are credible | use asymptotic thresholds with sparse, boundary, or weakly identified models without checks |
| Multiple-comparisons control | error-control family | many hypotheses or searches increase false-discovery risk | suppress exploration or treat adjusted significance as practical importance |
| False discovery rate control | error-control method | many findings are screened and a controlled discovery proportion is useful | confirmatory safety or legal gates require familywise or deterministic evidence |
| Equivalence and non-inferiority testing | decision test | acceptable difference bounds are defined before comparison | declare equivalence from a non-significant difference |
| Sequential analysis | adaptive inference design | data arrive over time and stopping rules must preserve error properties | repeatedly inspect fixed-horizon tests without a valid sequential design |
| Calibration analysis | probabilistic-quality assessment | predicted probabilities must match observed frequencies | use discrimination alone as evidence of reliable probabilities |

## Regression, hierarchical, and multivariate models

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Linear regression | conditional-mean model | a continuous outcome and additive effects are adequate approximations | extrapolate beyond support or treat association as causation |
| Generalized linear model | regression model family | binary, count, rate, or non-Gaussian outcomes need a link and mean-variance model | ignore separation, overdispersion, zero inflation, or exposure offsets |
| Generalized additive model | flexible regression model | smooth nonlinear relationships are plausible and interpretable partial effects are useful | tune smoothness until a desired story appears |
| Mixed-effects model | hierarchical regression | observations are nested, repeated, or grouped with partial pooling | ignore the grouping process or treat random effects as automatic causal correction |
| Bayesian hierarchical model | probabilistic multilevel model | sparse groups, prior knowledge, and full posterior uncertainty are valuable | priors are hidden, untested, or used to overwhelm contradictory data |
| Quantile regression | distributional regression | effects differ across the outcome distribution or tails matter | interpret quantile effects as mean effects |
| Principal component analysis | dimension-reduction technique | correlated variables need a lower-dimensional representation for exploration or modeling | components are treated as discovered constructs without interpretation or stability checks |
| Cluster analysis | unsupervised grouping family | similarity-based segmentation is exploratory and downstream action is defined | clusters are treated as natural categories or validated outcomes without stability evidence |

## Time, event, and reliability data

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Time-series decomposition | temporal diagnostic | trend, seasonality, cycles, and residual variation must be separated | infer causal effects from decomposed patterns alone |
| ARIMA/ETS forecasting | forecasting model family | serial dependence and forecast horizons are reasonably stable | structural breaks, interventions, or regime changes are ignored |
| State-space and Kalman filtering | dynamic estimation method | latent state evolves over time and noisy observations arrive sequentially | linear/Gaussian assumptions are materially false without a suitable extension |
| Survival analysis | time-to-event method family | censoring, event timing, and hazard are central | censoring is informative but treated as independent |
| Kaplan–Meier estimator | nonparametric survival estimator | survival curves need transparent group description under right censoring | competing risks or time-varying exposures are ignored |
| Cox proportional-hazards model | semiparametric survival model | hazard ratios are useful and proportionality is defensible | proportional hazards fail and no time-varying or alternative model is considered |
| Competing-risks analysis | event-history method | multiple mutually exclusive event types alter the risk set | cumulative incidence is replaced by an incompatible survival interpretation |

## Bayesian inference and probabilistic prediction

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Bayesian model specification | inferential framework | priors, likelihood, posterior, and predictive quantities can be made explicit | use a prior as an unreviewed value judgment or hide sensitivity |
| Posterior predictive checking | model criticism method | simulated outcomes should be compared with relevant observed features | check only average fit and ignore failures important to the decision |
| Bayesian model comparison | predictive/model-selection family | competing models and uncertainty about model structure matter | interpret a selected model as true or ignore prior/model sensitivity |
| Probabilistic forecasting | prediction method | decisions depend on calibrated distributions rather than point forecasts | reward sharpness without calibration or penalize honest uncertainty |
| Conformal prediction | distribution-free predictive inference family | finite-sample marginal coverage is useful under exchangeability | claim conditional coverage under drift, dependence, or distribution shift without evidence |

## Missingness, measurement, and robustness

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Missing-data mechanism analysis | diagnostic/framing method | MCAR, MAR, MNAR assumptions affect what can be learned | label missingness from the pattern alone without process knowledge |
| Multiple imputation | missing-data method | uncertainty from incomplete observations can be modeled under defensible assumptions | fill values once and treat them as observed data |
| Sensitivity analysis for missingness | robustness method | conclusions may change under departures from the primary missingness model | present one arbitrary scenario as a bound |
| Measurement invariance | measurement-validation method | scores must be compared across groups, times, or contexts | assume the same instrument has the same meaning everywhere |
| Inter-rater reliability | measurement agreement family | human judgments or coding require consistency assessment | agreement is treated as validity or disagreement is removed silently |
| Error-in-variables analysis | measurement-error method | predictors are measured with material error | regress noisy proxies as if they were exact causes |
| Influence and outlier diagnostics | model-criticism technique | individual observations can materially alter estimates or decisions | delete inconvenient observations without a predeclared rule and explanation |
| Robustness and sensitivity analysis | uncertainty-assurance family | reasonable analytic choices could change the conclusion | run a large undisclosed garden of analyses and report only favorable ones |

## Validation and communication

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Simulation-based calibration | Bayesian computation diagnostic | posterior computation and inferential recovery need testing on known simulated data | treat computational agreement as substantive model validation |
| Cross-validation | predictive validation family | out-of-sample prediction or model comparison is the target | use random folds with leakage, temporal dependence, or grouped data |
| Nested cross-validation | tuning/evaluation design | model selection and performance estimation must be separated | data are too scarce for stable outer estimates without reporting uncertainty |
| Temporal or group-aware validation | validation design | deployment predicts future periods or new groups/sites | random split leaks information across the deployment boundary |
| External validation | transportability check | a model or estimate must work in a new population, site, period, or system | call a held-out split from the same source external validation |
| Reproducible analysis | evidence practice | code, data transformations, environments, and decisions should be rerun and inspected | assume a notebook alone proves provenance or correctness |
| Statistical reporting checklist | communication assurance | analysis decisions, estimands, uncertainty, missingness, and limitations must be reviewable | use reporting compliance as a substitute for sound design |

## Composition patterns

### Estimate a population quantity

`target population + estimand → sampling frame/design → measurement validation → weighted/adjusted estimator → uncertainty interval → sensitivity to nonresponse/missingness → decision interpretation`

### Compare an intervention

`causal question → estimand → randomized or quasi-experimental design → power/precision → pre-specified analysis → effect estimate + uncertainty → diagnostics/refutations → practical and distributional interpretation`

### Build a predictive model

`deployment decision → target and prediction horizon → leakage-safe split → baseline → model family → calibration + discrimination/error → subgroup and shift checks → external/temporal validation → monitoring and recalibration`

### Analyze a small, messy dataset

`data-generating process → provenance and measurement audit → exploratory analysis → missingness/outlier diagnosis → robust/simple model → sensitivity analysis → cautious inference or decision rule`

Do not use a p-value, confidence interval, model score, or posterior as a substitute for a clear estimand, valid design, measurement quality, or decision relevance.

## Research anchors

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) for generic statistical concepts, diagnostics, and methods.
- [ICH E9(R1) estimands and sensitivity analysis](https://www.ich.org/page/efficacy-guidelines) for clinical-study estimands and robustness boundaries; use domain authority and jurisdiction-specific requirements for regulated work.
- [ASA Ethical Guidelines for Statistical Practice](https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice) for integrity, transparency, competence, and communication boundaries.
- Use primary design, sampling, measurement, and domain sources when the statistical result controls a legal, clinical, safety, financial, environmental, or public decision.
