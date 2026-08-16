# Geospatial data, spatial analysis, and location decisions

Use this catalog when location, distance, network access, spatial dependence, mapped suitability, remote sensing, service areas, or historical spatial conditions determine a decision. Use `16-supply-chain-logistics.md` for supply-network operating models, inventory, logistics, routing operations, reverse flows, and traceability; use `08` for generic optimization/causal inference and `31` for investigation protocol and claim assurance.

## Geospatial data foundations

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Coordinate Reference System governance — ISO 19111 | representation/control discipline; declared CRS, datum, axis order, and transformations | spatial layers from different sources must align or distances/areas matter | coordinates are accepted without CRS, epoch, precision, or transformation provenance |
| Geocoding and entity resolution | data-resolution method; address/place candidates, confidence, and provenance | textual addresses or place descriptions must bind to spatial entities | automatically select a low-confidence match or equate postal centroid with premises-level location |
| ISO 19157-1:2023 geographic data quality | quality framework; completeness, logical consistency, positional, thematic, and temporal quality evidence | determine whether spatial data are fit for a specific use | assign one global “accuracy” score or assume newer data are more accurate |
| Spatial data lineage and temporal validity | provenance artifact | maps from different dates, surveys, sensors, or transformations support historical/current claims | publication date is confused with observation date or later features are projected backward |
| OGC API Features / GeoPackage | interoperability standards | retrieve feature-level data over APIs or exchange portable self-describing spatial packages | treat encoding/interface conformance as proof of data quality or fitness |
| SpatioTemporal Asset Catalog — STAC | catalog specification | search imagery and other assets by footprint, time, collection, and metadata | catalog availability substitutes for cloud/quality screening or analytic validation |

## Spatial analysis and location decisions

| Candidate | Type and output | Use when | Avoid when |
| --- | --- | --- | --- |
| Exploratory Spatial Data Analysis — ESDA | analysis family; distributions, spatial patterns, neighbors, and anomalies | investigate whether place and neighborhood structure alter a phenomenon | exploratory clusters are presented as confirmatory effects |
| Global Moran's I / Geary's C | global spatial-autocorrelation statistics | test whether similar values are spatially patterned under a justified weight matrix | identify where clusters occur or ignore sensitivity to scale and neighborhood definition |
| Local Indicators of Spatial Association — LISA / Getis–Ord Gi* | local cluster/hotspot statistics | locate statistically unusual clusters or local spatial association with multiplicity controls | label hotspots as causes, permanent zones, or operational truth without field validation |
| Kernel density estimation | spatial smoothing technique | point-event intensity and broad concentration patterns need exploration | infer risk from raw event concentration without exposure/population denominator or bandwidth sensitivity |
| Spatial interpolation / kriging | geostatistical prediction family | sampled continuous phenomena exhibit defensible spatial structure and uncertainty | interpolate categorical events, cross barriers, or hide extrapolation beyond support |
| Spatial multicriteria suitability analysis | MCDA + GIS method; exclusion mask, normalized criteria, weights, and suitability surface | candidate locations depend on multiple mapped criteria and constraints | weighted overlay is treated as objective, criteria are double-counted, or weights/scale are not sensitivity-tested |
| Location–allocation | network optimization method | choose facilities and allocate demand to optimize coverage, travel, or impedance under capacity | a suitability heatmap alone is mistaken for economically feasible network design |
| Origin–destination matrix / service areas | network-analysis artifacts | quantify travel impedance, catchments, access, and coverage using the actual network | Euclidean buffers substitute for network travel or time-of-day variation is material but omitted |
| Gravity / Huff-style spatial interaction model | demand-allocation model | choice probability plausibly depends on attraction and distance/impedance | competition, capacity, heterogeneous preferences, or trip chaining dominate and are omitted |
| Spatial econometrics | statistical family; lag/error/Durbin or related models | residual dependence or spillovers violate independent-observation models | choose a spatial model only because Moran's I is significant or interpret association as causation |
| Geographically Weighted Regression — GWR | exploratory local-regression method | nonstationary associations and local model diagnostics are the research question | local coefficients are reported as causal effects or multiple-testing/collinearity/bandwidth issues are ignored |
| Spatial causal inference | causal design family using spatial assignment, boundaries, interference, or exposure | estimate interventions where geography defines treatment, spillovers, or comparison structure | proximity is treated as random assignment or spatial interference and sorting are ignored |
| Remote-sensing classification | measurement pipeline; preprocessing, features, labels, map, and accuracy assessment | land cover, assets, conditions, or phenomena can be observed consistently from sensors | training labels, cloud/shadow, sensor differences, resolution, and domain shift are ignored |
| Time-series change detection | temporal remote-sensing method | persistent or abrupt change must be separated from seasonal/noise variation | compare two unnormalized images and call every difference a real-world change |
| Ground truth / field validation and spatial sampling | assurance method | remotely inferred or mapped conditions support consequential decisions | convenience samples validate only accessible areas or reference data are not temporally aligned |

## Composition patterns

### Choose a facility, depot, or charging site

`decision frame + hard exclusions → demand estimation → geocoding/quality audit → network service areas → spatial suitability/MCDA → location–allocation + capacity model → competitor/cannibalization model → unit economics/scenarios → field validation → permitting/grid/site due diligence → pilot and monitored decision`

Do not optimize coordinates before estimating demand and hard constraints. Do not call a weighted heatmap “econometrics.”

### Reconstruct a historical spatial condition

`atomic claim + target time/location → temporal/source protocol in 31 → CRS/geocoding resolution → multichannel imagery/records → feature/change analysis → source lineage → ground or documentary triangulation → claim–evidence matrix → uncertainty and saturation`

## Research anchors and status

Status checked 2026-08-12.

- [ISO 19157-1:2023](https://www.iso.org/standard/78900.html) defines principles and procedures for geographic-data quality; [ISO 19111:2019](https://www.iso.org/standard/74039.html) defines coordinate referencing concepts.
- [OGC API Features](https://www.ogc.org/standards/ogcapi-features/) defines modular interfaces for feature data; [OGC GeoPackage](https://www.ogc.org/standards/geopackage/) defines a portable SQLite geospatial container. These are representations, not analysis methods.
- Use official transport-network, statistical-agency, cadastral, environmental, and remote-sensing data first. Record observation time, spatial support, resolution, CRS, completeness, and lineage for every decisive layer.
