# Selection skill invariants

These scenarios define behavioral expectations for future agent evaluations. They are not deterministic unit tests.

## Category distinction

**Prompt:** Compare Scrum, BPMN, contract tests, and DORA metrics for an API modernization effort.

**Expected invariants:** The response must not rank all four as rival methodologies. It should classify them as a framework, notation, assurance mechanism, and measurement family, then assign distinct stack roles.

## Proportionality

**Prompt:** Choose a method for a reversible, one-day internal documentation cleanup performed by one person.

**Expected invariants:** The response should select a lightweight technique and basic validation. It must reject heavyweight governance, formal assurance, and numerical scoring unless an undisclosed risk justifies them.

## Hard gate

**Prompt:** Choose methods for releasing a safety-critical AI-supported medical-device workflow.

**Expected invariants:** Legal, clinical, safety, competence, and jurisdictional requirements must be treated as pass/fail gates. The selected method must not approve its own output, and volatile versions must be verified from current primary sources.

## Cross-domain routing

**Prompt:** Evaluate an agricultural waste technology for commercial deployment.

**Expected invariants:** Start with the primary investment or technology-maturation decision and no more than two adjacent domain catalogs. Expand only for a specific uncovered gate such as environmental validity, process safety, or supply-network feasibility.

## Canonical ownership and secondary routing

**Prompt:** Choose a statistical method for evaluating a clinical intervention with repeated measurements and missing observations.

**Expected invariants:** Route generic sampling, missing-data, repeated-measures, and uncertainty methods to the statistics catalog; route clinical evidence, safety, and jurisdictional requirements to the health/medical-device catalog. Do not duplicate the generic method card. Create a health specialization only when the clinical estimand, authority, measurement system, or validation boundary changes.

## Urban planning routing

**Prompt:** Develop a climate-resilient transit-oriented redevelopment plan for a low-income neighborhood.

**Expected invariants:** Route plan-making, land-use, mobility integration, participation, displacement, and place-based implementation to urban/territorial planning; use geospatial, climate, health, construction, finance, and participation catalogs only for specific gates or distinct outputs. Do not treat a suitability map, workshop, or climate scenario as the plan itself.

## Subtraction test

**Prompt:** Recommend a complete stack for an auditable public-source investigation.

**Expected invariants:** Every selected fragment must produce a distinct consumed output. The response should remove any element whose absence causes no material loss and preserve verified, rejected, and possible evidence states.

## Task structure and expert cognition

**Prompt:** Choose methods to document an operational task and understand expert diagnostic judgments for training.

**Expected invariants:** Route HTA and CTA to human factors. HTA requires goals, operations, and execution plans; CTA requires practitioner/work evidence for cues and cognitive demands. Use one or both only when their distinct outputs are consumed. Distinguish task HTA from Health Technology Assessment and do not claim exact ACTA/CDM replication without the selected protocol.

## Credible task errors and recovery

**Prompt:** We have a practitioner-reviewed HTA of an equipment setup task. Identify likely mistakes and recovery opportunities.

**Expected invariants:** Select SHERPA in human factors; connect each credible mode to task context, consequences, recovery, evidence, and owned remedies. Keep ordinal likelihood separate from severity. Do not invent numerical probabilities or treat a worksheet or remedy proposal as proof of improved safety.

## Practiced interaction timing and its boundary

**Prompt:** Compare two fully specified interfaces for a routine task by experienced users, then estimate how quickly novices learn complex troubleshooting.

**Expected invariants:** KLM can support the routine execution comparison with an explicit method, sourced timings, justified mental operators, and only blocking waiting. It cannot establish novice learning or complex diagnostic time. Distinguish other GOMS variants from simple KLM and modeled savings from measured outcomes.

## Functional variability and instantiation

**Prompt:** Successful everyday coordination sometimes produces harmful delays across a sociotechnical operation. Investigate how adaptations interact.

**Expected invariants:** Consider FRAM in safety/systems using work-as-done evidence, relevant function aspects, and scenario instantiations. Account for couplings to preconditions, resources, control, and time as well as input. Do not fill all six aspects mechanically or infer actual event cause or probabilities from potential couplings alone.

## Repository model organization

**Prompt:** Add or revise a method that could be relevant to more than one domain catalog.

**Expected invariants:** Keep one canonical method definition, route secondary uses to that owner, and add a specialization only when the decision-relevant context changes. Update the relevant taxonomy or composition guidance, preserve a rationale in an ADR when the ownership boundary changes, and keep the dependency-free validator passing.
