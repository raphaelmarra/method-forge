# Supply-chain, inventory, logistics, traceability, and reverse-flow methods

Use this catalog when materials, orders, inventory, suppliers, facilities, routes, returns, traceability, or supply-network resilience determine performance. Supply-chain reference models, inventory policies, optimization models, and traceability standards occupy different layers; do not compare them as rival methodologies. For geospatial data, spatial statistics, mapping, remote sensing, service areas, suitability, or location analysis, use `33-geospatial-location-analysis.md`.

## Contents

1. Supply-chain operating models
2. Planning, inventory, logistics, and reverse flows
3. Supply-chain assurance and traceability
4. Composition patterns
5. Research anchors and status

## Supply-chain operating models

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| SCOR Digital Standard — SCOR DS | supply-chain reference model; process hierarchy, practices, performance attributes, and metrics | map and benchmark an end-to-end chain using Orchestrate, Plan, Order, Source, Transform, Fulfill, and Return | treat the reference model as a ready-made organization design or mathematical optimizer |
| Integrated Business Planning / S&OP | cross-functional planning process; reconciled demand, supply, capacity, inventory, and financial plan | medium-term trade-offs cross commercial, operations, procurement, and finance boundaries | use a monthly meeting to override transactional execution or conceal poor data |
| Demand-driven planning | planning family; buffers, replenishment signals, and decoupling choices | lead-time variability and forecast error justify strategically placed buffers | apply branded rules without validating demand shape, service goals, and cost of stockouts |
| Sales–operations execution | near-term exception-management cadence | actual orders, supply changes, and capacity deviations require rapid reconciliation between planning cycles | continually replan noise and destabilize production without frozen zones or decision rights |
| Control tower | operating capability; event visibility, exceptions, decisions, and coordinated response | multi-tier events and dependencies require near-real-time detection and accountable intervention | a dashboard is labeled a control tower without reliable data, decision authority, or response playbooks |
| Supply-chain segmentation | design technique; differentiated policies by demand, margin, criticality, variability, and service | one inventory/service policy performs poorly across heterogeneous products and customers | segments are marketing labels with no corresponding planning or fulfillment policy |

## Planning, inventory, logistics, and reverse flows

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Forecast hierarchy and reconciliation | statistical planning method; coherent forecasts across SKU, region, channel, and time | decisions occur at multiple aggregation levels and totals must reconcile | aggregation is assumed to improve every sparse/intermittent series or judgmental overrides are unlogged |
| Time-series / causal demand forecasting | predictive method family | sufficient historical demand and relevant drivers support out-of-sample validation | unprecedented regime change dominates or prediction is confused with causal impact |
| Intermittent-demand methods | forecasting family, including Croston variants and probabilistic approaches | many periods are zero but nonzero demand sizes and intervals still matter | continuous high-volume demand or obsolete items with no continuing process |
| ABC–XYZ segmentation | prioritization artifact; value/criticality by variability/predictability | planning attention and service policies should differ by economic importance and uncertainty | revenue alone substitutes for criticality, margin, substitutability, or consequence of shortage |
| Economic Order Quantity — EOQ | inventory optimization model | stationary independent demand, known replenishment, and simple holding/order trade-off are a useful baseline | quantity discounts, capacity, perishability, stochastic lead times, or joint replenishment dominate |
| Reorder point + safety stock | inventory-control policy | demand/lead-time uncertainty and a service target can be estimated | arbitrary “months of stock,” nonstationarity, or correlated disruptions invalidate the distributional model |
| Newsvendor / single-period inventory | stochastic decision model | one selling period, uncertain demand, and explicit overage/underage costs define the choice | replenishment, substitution, strategic behavior, or multi-period learning is material |
| Multi-echelon inventory optimization — MEIO | network inventory method | buffers at several tiers interact and service/cost should be optimized end to end | topology, lead times, service definitions, or demand correlation are not trustworthy |
| Material / Distribution Requirements Planning — MRP/DRP | dependent-demand planning logic | bills of material or distribution structures and time-phased requirements are reasonably controlled | inaccurate master data, unstable lead times, or capacity constraints are ignored |
| Network design / facility location | optimization family; selected plants, hubs, depots, assignments, capacities, and flows | strategic footprint and fixed/variable trade-offs matter | use straight-line distances, one-period demand, or average costs when resilience and service tails decide |
| Transportation optimization / Vehicle Routing Problem — VRP | combinatorial optimization family; routes, loads, time windows, and fleet use | repeated pickups/deliveries face capacity, service-time, and routing constraints | road restrictions, uncertain service times, breaks, compatibility, or real dispatch conditions are omitted |
| Last-mile service-area analysis | network-accessibility method | response time, travel time, and catchment coverage matter more than Euclidean radius | road direction, congestion, barriers, or mode restrictions are ignored |
| Warehouse slotting and picking analysis | operations-design technique | travel, handling, affinity, size, velocity, and replenishment affect warehouse cost/service | optimize one historical period and create unsafe, unstable, or replenishment-heavy locations |
| Queueing and discrete-event simulation | analytical/simulation family | congestion, stochastic arrivals, service times, resources, and operating rules drive performance | averages alone hide bursts/tails or the simulation is uncalibrated; see `08-decision-optimization-causality.md` |
| Reverse-logistics network design | network methodology; acquisition, collection, consolidation, inspection, sorting, recovery, and disposition | return quantity/quality/timing and alternative recovery routes shape economics | model reverse flows as predictable forward orders or omit incentives, contamination, ownership, and regulation |
| Closed-loop supply-chain design | integrated forward/reverse method | recovered outputs substitute inputs or products and feedback affects both networks | the recovered material lacks quality, demand, traceability, or viable reprocessing economics |
| Total Cost to Serve / landed cost | cost-to-flow method | customer, channel, SKU, route, duties, inventory, handling, and returns create different economics | average gross margin is treated as service profitability or excluded costs are hidden |

## Supply-chain assurance and traceability

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Supply-chain risk mapping | risk method; nodes, tiers, dependencies, failure scenarios, controls, and recovery options | disruption, concentration, geopolitics, climate, fraud, or quality risk crosses organizations | score suppliers in isolation while ignoring shared upstream dependencies and network propagation |
| Time-to-Recover / Time-to-Survive | resilience metrics and scenario technique | determine whether inventory, alternate capacity, and recovery time can bridge a node disruption | input estimates are treated as stable guarantees or correlated disruptions are ignored |
| Stress testing and digital-twin simulation | assurance technique | plausible disruptions should challenge service, cash, capacity, and recovery policies before events | a visually realistic model is trusted without calibration, uncertainty, or independent scenarios |
| ISO 28000:2022 | security-management-system standard | an organization needs auditable management of security risks relevant to supply chains | optimize ordinary cost/service or assess one shipment without a management-system need |
| Supplier qualification and periodic surveillance | assurance lifecycle | material quality, continuity, compliance, or rights risk requires evidence before and during the relationship | onboarding questionnaires are treated as perpetual proof; see procurement in `12-finance-market-audit-procurement.md` |
| Chain of custody — ISO 22095 models | traceability/accounting framework | claims about origin, characteristics, or certified quantity pass through transformations and organizations | a book-and-claim or mass-balance model is represented as physical segregation |
| Event-level traceability / EPCIS-style event model | representation and interchange pattern; what, when, where, why, and business context | item/batch movements and transformations must be queried across parties | event capture is incomplete, identifiers are unstable, or traceability is claimed without reconciliation |
| Recall and mock-recall exercise | operational assurance test | regulated or safety-relevant products require rapid forward/backward trace and containment | a paper procedure is accepted without timed exercises, mass balance, and unreachable-party handling |

## Composition patterns

### Design an urban collection and reverse-logistics network

`material/source census → geocoded supply with uncertainty in 33 → participation/yield model → candidate depots → location–allocation + VRP across 16/33 → pickup policy → contamination/chain-of-custody controls → TEA/LCA → stress tests → staged pilot → route and recovery metrics`

### Improve an operating supply chain

`SCOR scope and metrics → segmentation → demand/supply diagnostics → constraint/network/inventory model → S&OP decision rights → controlled policy pilot → service/cost/resilience measures → exception response and periodic stress test`

## Research anchors and status

Status checked 2026-08-12.

- [ASCM SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) is the current official SCOR reference; current public training describes seven processes: Orchestrate, Plan, Order, Source, Transform, Fulfill, and Return.
- [ISO 28000:2022](https://www.iso.org/standard/79612.html) is the current supply-chain-relevant security management system standard; do not cite the superseded 2007 edition as current.
- [UNECE integrated track-and-trace and reverse-logistics work](https://unece.org/sites/default/files/2021-03/ECE_TRADE_C_CEFACT_2021_INF4E-Integrated-T-T.pdf) is an official public anchor for traded-product, material, and transport-asset reverse flows.
- Route spatial-data quality, GIS, remote sensing, spatial statistics, service areas, suitability, and location analysis to `33-geospatial-location-analysis.md`.
