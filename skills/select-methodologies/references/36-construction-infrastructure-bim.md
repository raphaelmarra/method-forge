# Construction, infrastructure, built assets, and BIM

Use this catalog when project information, constructability, production planning, collaborative contracting, commissioning, or handover determines delivery of a building or infrastructure asset. Use `30` for generic project governance/controls, `14` for physical product/manufacturing realization, and `34` for lifecycle asset maintenance.

## Construction, infrastructure, and BIM

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 19650 information management using BIM | collaborative information-management lifecycle | multiple parties must define requirements, produce, review, authorize, exchange, and operate trusted information models | “BIM” means a 3D authoring tool/CDE folder or replaces design, contract, and technical assurance |
| Project/asset information requirements + BIM Execution Plan | requirements/governance artifacts | owner decisions and asset uses must become testable information deliverables with roles and exchanges | copy a template, ask for “LOD 300,” or accept bidder promises without capability and acceptance rules |
| Level of Information Need — ISO 7817-1 | information-requirements framework | geometry, attributes, and documents must be proportional to purpose, actor, milestone, and object | one LOD number means correctness, design maturity, constructability, or as-built truth |
| IFC + IDS + BCF | open schemas/protocols | model exchange, machine-readable information requirements, validation, and issue coordination need interoperability | schema-valid IFC proves engineering correctness, coordination, safety, or semantic truth |
| Asset Information Model / COBie handover | structured data artifact/process | installed, commissioned asset information must enter EAM/CMMS without rekeying | filled spreadsheet/model is assumed as-built, commissioned, complete, or maintained |
| Last Planner System — LPS | production-planning methodology | site variability, constraints, trade coordination, and reliable short-term commitments need collaborative control | substitute for master schedule, contract, safety planning, or game PPC with easy tasks |
| Takt / location-based planning | production-flow method | repetitive work areas and trade flow can be balanced spatially and temporally | variability, design instability, or nonrepetitive work makes rigid takt unsafe/unreliable |
| Integrated Project Delivery — IPD / alliance pattern | commercial/governance methodology | early integrated parties and shared risk/reward can align design and construction decisions | workshops/BIM are called IPD without changing incentives, authority, contract, and transparency |
| Building commissioning — ISO 24359-1 / ASHRAE interface | lifecycle assurance process | owner requirements, design reviews, installation, functional/integrated tests, training, and first-year performance need closure | visual completion, FAT/SAT, or data handover substitutes for functional performance |
| BIM safety information — ISO 19650-6 | information-management interface | health/safety information must be created, controlled, and shared through BIM lifecycle | hazard icons replace hazard analysis, legal duty holders, safe systems of work, and field assurance |
| Constructability / temporary works review | engineering assurance | means/methods, access, sequence, tolerances, lifting, temporary stability, and interfaces can invalidate design intent | permanent design approval is assumed to cover construction states |
| Infrastructure asset-management plan | lifecycle governance artifact | level of service, condition, risk, deterioration, intervention, funding, and resilience must be optimized over decades | lowest initial CAPEX or annual maintenance backlog substitutes for lifecycle value |

## Composition pattern

`owner/project/asset information requirements → ISO 19650 appointments/BEP → purpose-specific LOIN → coordinated design + constructability → IFC/IDS/BCF exchanges → LPS/IPD only when context supports → installed-state verification → functional commissioning → AIM/COBie reconciliation → asset acceptance and operating feedback`

## Research anchors and status

Status checked 2026-08-12.

- ISO 19650 Parts 1–5 remain published with revisions of some parts under development; ISO 19650-6:2025 is published. [ISO 7817-1:2024](https://www.iso.org/standard/82914.html) is current while later parts remain under development.
- ISO 16739-1:2024 is the current IFC standard; buildingSMART publishes IFC/IDS/BCF implementation material. Interoperability conformance is not technical correctness.
- [ISO 24359-1:2026](https://www.iso.org/standard/78490.html) and ASHRAE Standard 202-2024 are current building-commissioning anchors; do not generalize building commissioning unchanged to every infrastructure sector.
