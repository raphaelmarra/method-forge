# Agriculture, biological systems, biosecurity, and bioremediation

Use this catalog when living systems, farms, pests, pathogens, soils, animals, ecosystems, or biological treatment determine the intervention. Do not transfer mechanical or software optimization assumptions into adaptive biological systems without seasonal, ecological, welfare, and biosafety constraints.

## Contents

1. Farm and food-system framing
2. Agricultural experimentation and adaptive management
3. Pest, disease, and biosecurity methods
4. Precision agriculture and biological models
5. Bioremediation and ecological restoration
6. Composition patterns
7. Research anchors and status

## Farm and food-system framing

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Farming Systems Analysis | systems-analysis family; household/farm resources, enterprises, constraints, interactions, and objectives | technical, economic, labor, seasonal, and livelihood effects interact at farm level | optimize one yield response while assuming land, labor, cash, and risk are unconstrained |
| Agroecosystem analysis | ecological systems method; boundaries, flows, diversity, feedback, resilience, and ecosystem services | productivity depends on soil, water, biodiversity, landscape, and management interactions | use a qualitative system map as a quantified impact estimate |
| Value-chain analysis for agriculture | market/system method; actors, functions, governance, margins, quality, and bottlenecks | farm outcomes depend on aggregation, processing, standards, logistics, and buyer power | assume more production creates demand or benefits producers proportionally |
| FAO SAFA | sustainability assessment framework for food and agriculture systems | assess environmental integrity, economic resilience, social well-being, and governance across an agricultural entity/value chain | treat indicator aggregation as causal proof or compare entities with inconsistent scopes and evidence |
| Climate-Smart Agriculture — CSA | planning approach; evidence, stakeholder dialogue, prioritization, investment, and monitoring across productivity, adaptation, and mitigation | climate risk materially changes agricultural development choices | assume every intervention produces a “triple win” or use the label without quantified trade-offs |
| One Health | cross-sector governance approach | human, animal, plant, and ecosystem health risks are interdependent and require coordinated surveillance/action | use as a vague slogan or replace domain-specific epidemiology, ecology, veterinary, and public-health methods |
| Participatory rural appraisal / co-design | participatory method family | local knowledge, feasibility, equity, and adoption shape the intervention | participation is extractive, unrepresentative, or used to override safety and scientific evidence |

## Agricultural experimentation and adaptive management

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Randomized Complete Block Design — RCBD | experimental design | field heterogeneity can be controlled with blocks and treatments randomized within each block | a strong spatial gradient is poorly represented by blocks or treatments contaminate neighbors |
| Factorial experiment | experimental design | interactions among input, variety, environment, or management factors are decision-relevant | sample size cannot estimate interactions or unsafe/unrealistic combinations are included |
| Split-plot design | experimental design | one factor is hard/expensive to randomize at small scale and another can vary within main plots | analyze observations as fully randomized and understate main-plot uncertainty |
| Response-surface methodology | experimental optimization method | curved responses and factor combinations around a safe operating region must be estimated | extrapolate beyond the design region or optimize one response without agronomic/economic constraints |
| On-farm participatory trials | pragmatic/participatory experiment | performance, adoption, labor, and variability under real management matter | uncontrolled demonstrations are described as causal trials or farmer selection is ignored |
| Multi-environment trials and G×E analysis | experimental/modeling family | genotype, practice, or technology performance varies across location/season | average yield alone is used when stability, tail loss, and target population of environments matter |
| Adaptive management | decision-learning cycle | ecological uncertainty is material, interventions can be monitored, and management can change | “learning by doing” lacks explicit hypotheses, triggers, controls, and decision authority |
| Farm record / cohort monitoring | longitudinal observational design | productivity, health, treatment, weather, and management histories support diagnosis and learning | associations are interpreted as intervention effects without confounding control |
| Bioeconomic modeling | integrated biological-economic model | population growth, yield, disease, resource dynamics, price, and harvest/control decisions interact | biological parameters, behavior, and market response are weakly identified but outputs appear precise |

Define the experimental unit before choosing a design or sample size. Crops, animals, colonies, pens, ponds, apiaries, farms, seasons, and landscapes form hierarchies; subsamples and repeated measurements are not independent replications. Match randomization and analysis to interference, spillover, reinfestation, attrition, seasonal/site replication, and the actual treatment-assignment level. Use `08-decision-optimization-causality.md` for generic identification/power logic and this catalog for biological specialization.

## Pest, disease, and biosecurity methods

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Integrated Pest Management — IPM/MIP | ecosystem-based management approach; monitoring, thresholds, prevention, biological/cultural/physical controls, and selective chemical use | pests must remain below economically, environmentally, and health-relevant thresholds | spray calendars replace monitoring, one control is called “integrated,” or beneficial organisms are ignored |
| Biological control — conservation, augmentative, or classical | pest-management technique family; protect, release, or establish natural enemies | a diagnosed pest has a defensible agent/pathway, monitoring, non-target assessment, and authorized deployment within IPM | release an organism from a vendor claim, ignore establishment/spread/reversibility, or bypass environmental, veterinary, pesticide, or food-safety authority |
| Economic injury level / action threshold | decision rule | sampling and expected damage can justify when intervention cost/risk is warranted | threshold is copied across crop stage, climate, price, and control efficacy without recalibration |
| Pest Risk Analysis — PRA, ISPM 2/11 family | regulatory risk-analysis process; initiation, assessment, management, documentation, and communication | entry, establishment, spread, and consequence of plant pests affect phytosanitary decisions | use for routine within-field pest control or treat absence of records as absence of the pest |
| Biosecurity risk analysis | cross-sector risk framework; hazard identification, assessment, management, and communication | animal, plant, food, invasive-species, or biological threats cross boundaries and institutions | infrastructure, surveillance, enforcement, and response capability are absent but a paper assessment implies control |
| HACCP | preventive food-safety system; hazard analysis, critical control points, limits, monitoring, correction, verification, and records | significant biological, chemical, or physical food hazards can be controlled at specific process steps | general quality improvement, farm strategy, or hazards lacking controllable critical points |
| Epidemiological surveillance | detection/measurement system | disease incidence, prevalence, vectors, outbreaks, and intervention performance require systematic observation | passive reports are treated as complete denominators or changing case definitions are ignored |
| Outbreak investigation | epidemiological workflow; verify, define cases, describe, hypothesize, test, control, and communicate | an unusual cluster or emerging disease requires rapid cause/source and control work | wait for perfect certainty before protective action or infer source from temporal sequence alone |
| Compartmental / transmission models | mathematical modeling family | infection dynamics, contact, latency, immunity, vector, or intervention scenarios need explicit structure | parameters and mixing assumptions lack calibration or forecasts are treated as deterministic |
| Biosecurity plan / barrier model | operational control artifact | introduction and spread pathways can be prevented, detected, contained, and recovered through layered measures | one disinfectant step is treated as a complete plan or human behavior and audit evidence are omitted |

Before any field pilot, determine whether the intervention is a veterinary medicine/pesticide, microbial or macro-organism release, feed/input, food-residue risk, movement/import, or response to a notifiable disease. These are hard authorization and biosafety gates under the competent national/local authorities; a favorable experimental score cannot compensate for failure.

## Precision agriculture and biological models

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Precision-agriculture measurement-to-action loop | decision pipeline; sensing, calibration, spatial prescription, application, and outcome validation | spatial/temporal variability supports economically actionable differential management | collect sensor maps without a decision rule or assume finer resolution always adds value |
| Management-zone delineation | spatial clustering/segmentation method | stable within-field patterns justify differentiated sampling or treatment | one season's noisy yield map defines permanent zones |
| Crop / livestock simulation model | mechanistic or empirical model | weather, soil/feed, genotype, management, and physiology scenarios need integration | calibration/validation domain is exceeded or model outputs replace field trials |
| Decision Support System — DSS | integrated information and rule/model system | repeated operational decisions can combine monitored state, forecasts, constraints, and expert rules | opaque recommendations lack override, uncertainty, provenance, or post-decision learning |
| Remote sensing and proximal sensing | measurement family | crop vigor, stress, canopy, moisture, land cover, or animal state can be observed indirectly | spectral proxy is equated with the target outcome without ground truth; see `33-geospatial-location-analysis.md` |
| Variable-rate application | control method | calibrated prescriptions and capable equipment can vary input by location | position error, lag, drift, weather, and application uniformity are unverified |
| Sampling and measurement-system analysis | assurance family | soil, water, pest, residue, yield, or sensor measurements drive consequential action | convenience sampling, pseudo-replication, composite samples, or laboratory uncertainty are ignored |

## Bioremediation and ecological restoration

Bioremediation treats contaminants using biological processes. It is not a pest-control synonym. For crop or hive pests, route first to IPM, veterinary/plant-health guidance, and biosecurity.

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Conceptual Site Model — CSM | representation artifact; source, contaminant, medium, pathway, receptor, and uncertainty | any remediation option must be grounded in site-specific exposure and transport | choose a treatment from contaminant name alone or freeze the model despite new evidence |
| Biodegradation treatability study | staged experimental method; feasibility, removal rate, conditions, by-products, and scale parameters | microbial treatment is plausible but site matrix, toxicity, nutrients, electron donors/acceptors, or kinetics are uncertain | deploy field amendments based on vendor claims or laboratory success without controls and mass balance |
| Monitored Natural Attenuation — MNA | remediation strategy with monitoring and contingency | demonstrated physical, chemical, or biological processes can meet protection goals in a reasonable timeframe | “do nothing,” plume is expanding, receptors are exposed, or monitoring cannot distinguish dilution from destruction |
| Biostimulation | enhanced bioremediation technique | indigenous organisms can perform the transformation if nutrients, donors/acceptors, oxygen, pH, or moisture are adjusted | limiting mechanism is unknown or amendments create mobilization, eutrophication, gas, or toxic by-products |
| Bioaugmentation | enhanced bioremediation technique | required metabolic capability is absent/insufficient and introduced organisms can survive, distribute, and remain controlled | add commercial cultures without site evidence, biosafety review, or comparison to native activity |
| Phytoremediation | plant-based remediation family | shallow contamination, stabilization/extraction/degradation, long time horizons, and controlled biomass are acceptable | deep/high-concentration contamination, food-chain exposure, invasive species, or rapid cleanup is required |
| Constructed wetland / ecological treatment | engineered ecosystem method | hydraulic residence, loading, vegetation, substrate, and maintenance can treat compatible flows | variable/toxic shock loads, insufficient land, vectors, or seasonal failure are uncontrolled |
| Ecological restoration reference model | restoration methodology; reference condition, trajectory, interventions, monitoring, and adaptive response | ecosystem structure/function and resilience must recover beyond contaminant concentration | beautification or planting count substitutes for ecological function and long-term persistence |
| Lines of evidence + mass balance | assurance method | concentration trends must be attributed to destruction, transformation, immobilization, or transport with converging evidence | decreasing concentration alone proves degradation or toxic daughter products are omitted |
| Pilot and performance-monitoring plan | scale-up/assurance artifact | field heterogeneity and delivery/control limitations must be tested before full deployment | pilot boundaries, control/comparison, rebound, seasonal variation, exit criteria, and contingency are missing |

## Composition patterns

### Improve farm productivity responsibly

`farm-system frame → baseline records + constraints → agronomic/biological hypothesis → RCBD/factorial or pragmatic on-farm trial → economic and environmental outcomes → IPM/biosecurity controls → adoption analysis → seasonal replication → decision rule and monitoring`

### Protect an apiary or animal-production system

`species/production objective + colony–apiary–season unit map → One Health/biosecurity scope → longitudinal baseline → hazard/pathway map → surveillance + diagnostic confirmation → threshold/risk analysis → layered preventive controls/IPM → cluster/block trial at the true assignment unit → authorized targeted treatment/biocontrol → residue/non-target/welfare checks → effectiveness, resistance, survival, production, cost/labor, and seasonal replication`

For apiaries, distinguish product yield/quality, pollination service, colony strength/survival, queen events, pest/pathogen burden, residue/non-target harm, cost, and labor. Low productivity is not itself a pest diagnosis: forage, climate, queen status, management, chemicals, and disease can confound both diagnosis and effect estimates.

Choose an apiary diagnostic or measurement protocol by: `decision and suspected agent/outcome → controlling national/WOAH method when official diagnosis or notification is involved → specimen and true sampling unit → timing relative to brood, season, treatment, and symptoms → detection versus burden/quantification purpose → sensitivity, specificity, repeatability, limit, and reference-laboratory needs → collection, preservation, transport, chain of custody, and biosafety → blinded/repeated quality controls`. Use the matching disease chapter in the WOAH Terrestrial Manual for recognized diagnostic approaches and BEEBOOK for comparable research measurements. A field count, molecular test, culture, clinical sign, and colony-strength estimate are not interchangeable; resolve discordance before causal attribution or release decisions.

### Evaluate a biological remediation option

`regulatory cleanup objective → CSM + sampling plan → contaminant/fate characterization → bench treatability with controls → mass balance/by-products/ecotoxicity → alternative-remedy comparison → pilot → monitored deployment + contingency → closure evidence`

### Select a climate-smart agricultural investment

`stakeholder and farming-system frame → climate hazard/exposure/vulnerability → baseline and counterfactual → candidate practices → agronomic + economic + mitigation/adaptation evidence → MCDA/robust scenarios → on-farm pilot → distribution/adoption analysis → adaptive triggers`

## Research anchors and status

Status checked 2026-08-12.

- [FAO Integrated Pest Management](https://www.fao.org/pest-and-pesticide-management/ipm/integrated-pest-management/en/) defines IPM as the considered integration of available techniques while minimizing pesticide risks.
- [IPPC adopted ISPMs](https://www.ippc.int/en/core-activities/standards-setting/ispms/) provide the current normative entry point for Pest Risk Analysis; confirm individual ISPM status because reorganization work remains active in 2026.
- [IPPC guidance for ISPM 3](https://www.ippc.int/en/centre-of-excellence/phytosanitary-systems/contributed-resources-pest-risk-analysis/pest-risk-analysis-ispms-to-guide-and-assist-with-pra/) covers responsibilities and risk management for export, shipment, import, and release of biological-control agents and other beneficial organisms. A revision topic is active in 2026; do not present draft work as the adopted replacement.
- [FAO Biosecurity Toolkit](https://www.fao.org/4/a1140e/a1140e.pdf) structures capacity assessment and risk assessment, management, and communication.
- [WOAH Codes and Manuals](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/) are the current official route for terrestrial/aquatic animal health and veterinary public-health requirements.
- The [WOAH Terrestrial Manual contents](https://www.woah.org/fileadmin/Home/eng/Health_standards/tahm/A_summry.htm) route to disease-specific diagnostic chapters for honey-bee conditions; chapter versions differ and must be checked individually.
- [COLOSS BEEBOOK](https://coloss.org/activities/beebook/) is a research-method anchor for standardized honey-bee measurements and experimental practice; jurisdictional veterinary, pesticide, food, import/movement, and disease-notification rules remain controlling.
- [FAO One Health](https://www.fao.org/one-health/overview/one-health-overview/en) and the Quadripartite Joint Plan provide the cross-sector governance anchor; One Health is an approach, not a single analytic technique.
- [FAO SAFA Guidelines](https://openknowledge.fao.org/handle/20.500.14283/i4113e) and [Climate-Smart Agriculture Sourcebook](https://openknowledge.fao.org/handle/20.500.14283/i3325e) are official sustainability and climate-planning anchors for food and agriculture systems.
- [U.S. EPA treatability-study guidance](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=1000228N.TXT) and [natural-attenuation protocol](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=30003ONO.TXT) emphasize site characterization, evidence, performance variables, and monitoring before remedy claims.
