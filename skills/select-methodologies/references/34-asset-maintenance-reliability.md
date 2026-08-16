# Asset management, maintenance, and operational reliability

Use this catalog when an operated physical asset or fleet must deliver lifecycle value through criticality, maintenance, inspection, monitoring, spares, failure learning, renewal, and obsolescence decisions. Use `14` for product/manufacturing realization and `36` for built-asset delivery/BIM.

## Asset management and maintenance

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| ISO 55000/55001 asset management system | governance/management-system family | organizations must balance performance, risk, and expenditure across asset lifecycles to deliver value | use as a maintenance manual or assume certification optimizes individual assets |
| Asset criticality analysis | prioritization technique | maintenance, spares, monitoring, renewal, and assurance should reflect consequence and dependency | simple replacement cost ignores safety, service, environment, bottlenecks, common cause, and recoverability |
| Life Cycle Costing | economic method | acquisition, operation, maintenance, downtime, renewal, and disposal alternatives need comparison | optimize cost while violating service/safety/environment constraints or hide uncertain failure/usage assumptions |
| Reliability-Centered Maintenance — RCM | maintenance-requirements method | functions, functional failures, failure modes, consequences, and applicable/effective tasks need systematic selection | “RCM-lite” skips functions/consequences or every asset receives the full heavy process |
| Preventive / predictive / condition-based maintenance policy | maintenance strategy family | failure behavior, detectability, consequence, and economics support differentiated tasks | predictive analytics are used where no detectable degradation interval exists |
| Condition monitoring and diagnostics — ISO 17359 family | monitoring methodology | vibration, oil, thermal, electrical, acoustic, or process condition can reveal actionable degradation | collect sensors without baseline, diagnosis, thresholds, work process, and false-alarm controls |
| Risk-Based Inspection — RBI | inspection-planning method | degradation likelihood and consequence can optimize pressure/mechanical integrity inspection | replace design/operating controls, apply outside competence, or let risk ranking defer mandatory inspection |
| FRACAS | closed-loop reliability process | failures must be reported, analyzed, corrected, verified, and trended through configuration | ticket closure, symptom repair, or blame substitutes for corrective effectiveness |
| Reliability/maintenance data governance | data standardization and knowledge discipline | equipment taxonomy, failure modes, maintenance actions, downtime, and context support analysis across assets | dirty CMMS codes and missing exposure hours feed precise models |
| Obsolescence management — IEC 62402 | lifecycle management method | components, software, materials, suppliers, or skills may become unavailable before asset retirement | react only at last-time-buy or stockpile without redesign, counterfeit, shelf-life, and demand analysis |
| Spares optimization | inventory/reliability method | intermittent demand, lead time, criticality, repair, commonality, and downtime cost shape holdings | apply ordinary EOQ alone to rare critical spares |

## Composition pattern

`service/value objectives → asset hierarchy and criticality → lifecycle/risk/cost baseline → RCM/RBI/condition strategy → spares/obsolescence → work execution + data quality → performance/reliability trends → failure learning → renewal decision`

## Research anchors and status

Status checked 2026-08-12.

- [ISO 55000:2024](https://www.iso.org/standard/83053.html) and [ISO 55001:2024](https://www.iso.org/standard/83054.html) are current asset-management editions.
- SAE JA1011/JA1012 are the criteria/guidance anchors for calling a process RCM; API RP 580/581 govern RBI in their applicable process-industry context.
