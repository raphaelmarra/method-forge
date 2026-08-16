# Human factors, ergonomics, health systems, and medical devices

Use this catalog when human–system performance, physical/cognitive ergonomics, use-related risk, clinical evidence, or a regulated medical-device lifecycle determines the method. Clinical, medical-device, and health-system work is jurisdiction- and product-class-specific. Agent research cannot authorize treatment, market entry, human studies, or product release.

## Human factors and ergonomics

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Ergonomic design of work systems — ISO 6385/26800 | human-factors design framework | tasks, organization, tools, environment, physical/cognitive demand, and worker variability must be designed jointly | “train the operator” compensates for a preventable design hazard |
| Human Systems Integration — HSI | program integration framework | manpower, personnel, training, human factors, safety, survivability, habitability, and maintainability interact across acquisition | add a usability review at the end or optimize headcount independently of workload/safety |
| Human-centred design — ISO 9241-210 | iterative design lifecycle specialized for human–system engineering | interactive physical/digital systems require explicit users, context, requirements, design, and evaluation | UI preference testing substitutes for system safety, domain correctness, or accessibility obligations; UX/service execution belongs to `20-design-experience-communication.md` |
| Work / task / cognitive task analysis | analysis family | work-as-done, goals, decisions, information, variability, coordination, and error opportunities must be understood | document only work-as-imagined or decompose adaptive work into misleading linear steps |
| Anthropometric accommodation | physical-design method | reach, clearance, strength, posture, fit, egress, and population coverage determine geometry | design to an “average person,” mix incompatible percentiles, or ignore clothing/PPE/dynamics |
| Human-in-the-loop evaluation | iterative assurance method | representative users must perform representative tasks under realistic conditions before release | experts substitute for target users or scripted happy paths hide workload and recovery |
| NASA-TLX / workload measures | subjective workload measurement technique | compare workload across tasks/designs with a validated protocol and complementary performance evidence | one score diagnoses the causal source or replaces errors, physiology, observation, and context |
| Revised NIOSH Lifting Equation | specialist ergonomic assessment | specified two-handed lifting conditions fit the model's scope | apply outside assumptions, to pushing/pulling/carrying or complex unstable loads as a universal safe limit |
| Human Reliability Analysis — HRA | risk-analysis family | human actions, dependencies, context, recovery, and performance-shaping factors affect safety/reliability | assign generic “human error probabilities,” blame operators, or ignore system design |
| Cognitive Work Analysis — CWA | constraint-based analysis framework | work is complex/adaptive and must remain safe under unanticipated conditions | a stable routine task only needs direct task analysis or analysts lack domain access |

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

## Composition pattern

`jurisdiction/classification/intended use → QMS + design controls → clinical/user needs → ISO 14971 risk → usability/biological/software specialists → traceable design V&V → process validation/transfer → clinical/regulatory evidence → authorized production release → postmarket surveillance/CAPA`

## Research anchors and status

Status checked 2026-08-12.

- ISO 9241-210 remains the human-centred-design anchor; ISO 6385/26800 frame ergonomic work-system design. Check the exact edition and national adoption before conformity claims.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), ISO 14971:2019, IEC 62366-1, ISO 10993-1:2025, ISO 14155:2026, and IEC 62304 are current owner-page anchors subject to regulatory recognition/transition by jurisdiction.
- [FDA Quality Management System Regulation](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr) became effective in 2026; its applicability and enforcement details must be checked live.
