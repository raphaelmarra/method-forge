# Physical engineering, manufacturing, and industrialization

Use this catalog when a physical product or production system must move from concept through engineering into safe, repeatable production. Keep prototype maturity, engineering reviews, verification, validation, industrialization, qualification, production acceptance, and regulatory authorization distinct. Use `34-asset-maintenance-reliability.md` for operated assets, `35-human-factors-health-medical-devices.md` for human systems and medical devices, and `36-construction-infrastructure-bim.md` for built assets and BIM.

## Contents

1. Physical product and systems engineering
2. Manufacturing and industrialization
3. Composition patterns
4. Research anchors and status

## Physical product and systems engineering

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 15288 systems lifecycle | lifecycle/process framework | multidisciplinary stakeholders, requirements, architecture, interfaces, realization, operation, and retirement need coherent governance | treat process clauses as a detailed mechanical design recipe or impose full lifecycle overhead on a trivial prototype |
| V-model / product realization | lifecycle representation | requirements must trace through decomposition, implementation, integration, verification, and validation | assume sequential paperwork guarantees iteration-free design or call every left artifact “verified” by its paired test |
| Technology Readiness Assessment / TRL | maturity-assessment method | decision makers need evidence that a critical technology has progressed from principles to demonstrated operational use | average component TRLs, use calendar progress, or treat TRL as manufacturing, integration, commercial, or regulatory readiness |
| Prototype ladder: proof-of-principle → breadboard → engineering/qualification unit | development pattern | different uncertainties require progressively representative function, form, environment, and process | call a visually realistic mock-up a verified engineering prototype or reuse non-flight/nonproduction hardware without configuration evidence |
| Technical reviews — SRR/PDR/CDR/TRR/PRR/ORR | evidence-based decision gates | increasing commitment requires independent review of requirements, design, test, production, and operation readiness | ceremonial slides, schedule pressure, or same-team self-approval substitute for entry/exit evidence |
| Trade study | decision-analysis method | alternative architectures/materials/concepts face measurable performance, cost, risk, and lifecycle trade-offs | weighted scores compensate hard safety/regulatory constraints or unsupported assumptions create a predetermined winner |
| Requirements allocation and interface control | systems method/artifacts | system goals must decompose into verifiable subsystem requirements and controlled interfaces | allocate arbitrary numbers without budgets/margins or let interface drawings drift from configuration |
| Design margin / uncertainty budget | engineering-control artifact | load, strength, mass, power, thermal, tolerance, and performance uncertainties must remain visible | stack hidden conservatism, double-count safety factors, or consume margin without authority |
| Tolerance stack-up and GD&T | engineering representation/analysis | assembly fit, function, interchangeability, inspection, and manufacturing variation depend on geometry | nominal CAD is treated as manufacturable truth or tolerance is tightened without capability/cost evidence |
| Simulation credibility / V&V | model assurance family | FEA, CFD, multibody, thermal, or other simulations support consequential decisions | colorful plots replace code verification, solution verification, validation data, uncertainty, mesh/model sensitivity, and applicability domain |
| Design for Manufacture and Assembly — DfMA | design method | part count, joining, handling, process capability, inspection, service, and cost should influence design early | manufacturing simplification compromises safety, repair, tolerance, or lifecycle objectives |
| Design for disassembly / end of life | lifecycle design technique | repair, upgrade, reuse, remanufacture, separation, and recycling are material requirements | a recycling label substitutes for actual access, fasteners, contamination, recovery network, and economics |
| Configuration management — ISO 10007 interface | governance discipline | baselines, identifiers, change control, status accounting, and audits must preserve product definition | file naming alone, uncontrolled prototypes, or “latest CAD” becomes production authority |
| Verification matrix | assurance artifact | every requirement needs method, level, configuration, procedure, evidence, result, and closure | test existence substitutes for requirement coverage or “analysis” lacks validated model and acceptance threshold |

Verification asks whether the realization meets specified requirements. Validation asks whether the resulting system fulfills intended use in its operational context. Neither is equivalent to certification, homologation, approval, or safe production release.

## Manufacturing and industrialization

Before selecting industrialization evidence, record sector/customer rules, safety criticality, intended load spectrum and life, material and special processes, annual volume/rate, supplier/process change, and the configuration that production will actually use. “Production-representative” means the relevant material/grade, supplier, machine/process, tooling, program, operator/work instruction, inspection method, environment, rate, and configuration match the intended production system or any differences are justified.

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Manufacturing Readiness Assessment / MRL | maturity-assessment method | material, process, tooling, quality, workforce, supply, cost, capacity, and production control readiness must be evidenced | convert TRL directly to MRL, average weak dimensions, or use self-score without a production environment |
| Advanced Product Quality Planning — APQP | product-quality planning lifecycle | customer, design, process, supplier, validation, launch, and feedback artifacts must mature together | use an automotive manual by default outside context or run templates after design freeze |
| Design / Process FMEA — DFMEA/PFMEA | failure-analysis methods | proactively analyze design or manufacturing failure modes and prevention/detection controls | combine design and process causes indiscriminately or rank risk solely by RPN; see `06-testing-reliability-safety-security.md` |
| Process flow + Control Plan | manufacturing representation/control artifact | characteristics, process steps, methods, reaction plans, sampling, and owners must trace from risk analysis | inspection-heavy control plan substitutes for capable process and prevention |
| Production Part Approval Process — PPAP | supplier/customer production-approval evidence package | automotive/customer rules require evidence that design records and production process can repeatedly meet requirements | call PPAP universal certification, use prototype tooling/material, or infer future capability from paperwork |
| Measurement Systems Analysis — MSA | measurement assurance family | gauge repeatability, reproducibility, bias, linearity, stability, and discrimination affect acceptance/control | control a process with an unqualified measurement system or treat gauge R&R as all measurement uncertainty |
| Measurement uncertainty and conformity decision — JCGM GUM/JCGM 106 | generic metrology assurance; measurand/model, uncertainty budget, result, decision rule, and conformity risk | measurement uncertainty can change acceptance, tolerance, calibration, or comparability | report only instrument resolution, use gauge R&R as the entire uncertainty budget, or accept/reject without a declared decision rule |
| Statistical Process Control and capability | statistical monitoring/assurance | stable repeated measurements support common/special cause reasoning and capability against specifications | compute Cp/Cpk on unstable data, small convenience samples, autocorrelated process, or moving specifications |
| First Article Inspection — FAI | production verification method | first production run/configuration must demonstrate manufacturing-plan realization against design records | one conforming article proves stable process capability or substitutes for qualification/validation |
| Material/process pedigree and traceability | assurance artifacts; specification, heat/batch, certificate, supplier, route, special process, and configuration linkage | material state, treatment, coating, joining, or supplier history can change safety/performance | accept certificates without identity/lot linkage, verification, change control, or applicable customer/regulatory rules |
| Structural durability and fatigue qualification | engineering assurance; load spectrum, analyses, coupons/components, proof/ultimate/fatigue tests, and damage evidence | strength, stiffness, crack growth, fatigue life, or environmental degradation constrain intended service | static success of two prototypes proves life, or test articles/configurations/load spectra are unrepresentative |
| Nondestructive examination and special-process qualification | manufacturing assurance family | hidden discontinuities or process-controlled outcomes cannot be assured by final dimensional inspection alone | choose NDE without defect mechanism/probability-of-detection basis or approve a special process from one nominal run |
| IQ/OQ/PQ / process validation | manufacturing validation family | output cannot be fully verified later or process variables materially determine quality | qualify equipment but not the process, validate one narrow “golden run,” or ignore worst cases/change control |
| Factory / Site Acceptance Testing — FAT/SAT | contractual acceptance tests | equipment/system must be tested before shipment and after installation against agreed criteria | FAT substitutes for site integration/commissioning or SAT substitutes for operational validation |
| Integration / system acceptance testing | assurance method | interfaces, controls, utilities, loads, faults, and end-to-end behavior require integrated evidence | components passed individually and integration is assumed |
| Safe launch / heightened launch controls | temporary assurance strategy | early production uncertainty justifies additional containment, inspection, review, and exit criteria | temporary inspection becomes permanent camouflage for incapable process |
| Production readiness review — PRR | decision gate | manufacturing plans, supply, tooling, workforce, quality, rate, configuration, and residual risks support release | schedule or purchase commitments force approval despite missing objective evidence |

FAI, qualification, capability, and process validation support different claims: the first production article matches the design record; the design survives intended conditions; a stable repeated process meets specification; and an inadequately inspectable process remains controlled. Join them with `+` when their claims are material, not `/` as alternatives. A PRR must name entry evidence, open deviations/concessions, residual-risk owners, release scope/rate, independent approver, stop conditions, and exit actions.

There is no single universal FAI package. Use controlled design records, characteristic accountability, qualified measurement, nonconformance closure, and configuration evidence, then apply the sector/customer FAI scheme only when applicable. Do not import AS9102 or PPAP requirements into another sector merely because they are detailed.


## Composition patterns

### Develop a safety-relevant physical product

`intended use/context → stakeholder and system requirements → hazard analysis + human/task analysis → architecture/trade studies → prototype ladder + configuration → simulation V&V + physical tests → PDR/CDR gates → design validation → manufacturing readiness/APQP → qualification + production acceptance → regulatory/independent gate → field monitoring`

### Industrialize a prototype

`frozen-enough design baseline → MRL/gap assessment → process flow + PFMEA → material/special-process controls → tooling/work instructions → MSA → control plan → production-representative pilot build → FAI + qualification + capability/process validation as their claims require → PPAP or sector approval when required → safe launch → PRR → controlled ramp + FRACAS`

Tailor by consequence. A low-volume, low-criticality item may need only controlled baseline, representative build, FAI/functional acceptance, control plan, and authorized release. Repeated or safety-relevant production adds measurement assurance, capability/stability evidence, durability qualification, traceability, independent review, and controlled ramp. Contractual or regulated sectors add their mandated approval package; APQP/PPAP is not a universal default.


## Research anchors and status

Status checked 2026-08-12. Full implementation requires authorized standards and sector/jurisdiction-specific requirements.

- [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) is the current systems-lifecycle edition. NASA and DoD guides remain implementation anchors for reviews and TRL; TRL is not MRL.
- AIAG Core Tools include APQP, Control Plan, PPAP, FMEA, MSA, and SPC; current licensed manuals govern automotive implementation. Do not reproduce or infer requirements from summaries.
- The [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) is a generic statistical anchor for measurement, stability, capability, DOE, and assumptions; capability presupposes a stable process. [SAE AS9102C](https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements) is an aerospace FAI anchor, not a universal production-release standard.
- [JCGM metrology publications](https://www.bipm.org/en/committees/jc/jcgm/publications) are the generic anchors for measurement uncertainty and conformity decisions. At check date, JCGM 100:2008 has Amendment 1:2026; use the applicable GUM-series part and JCGM 106 rather than treating one gauge study as the entire measurement model.
- Route asset management/maintenance to `34`, human factors and medical devices to `35`, and construction/infrastructure/BIM to `36`.
