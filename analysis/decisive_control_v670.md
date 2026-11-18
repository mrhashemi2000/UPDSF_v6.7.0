[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="5915" height="1766" alt="decisive_control_v670" src="https://github.com/user-attachments/assets/4e1e7936-b4a8-418c-b67c-654b397e4a81" />

### Overview
The image displays a three-panel scientific dashboard titled **"UPDSF v6.6.1 — Decisive control sweep (T=90 C, pH=11.0, 240 h, n=20)"**. This dashboard presents the same data as the previous "Decomposed destruction channels" dashboard, but uses line graphs instead of bar charts to more clearly illustrate the trends across the different control scenarios.

The X-axis for all panels is categorical, listing seven different scenarios: **baseline**, **equal_polymer_only_gm**, **equal_free_only_gm**, **equal_degradation_gm**, **equal_degradation_kT**, **equal_pools**, and **no_compartments**.

### Panel Descriptions

**1. CSI decomposition across controls (Left Panel)**
*   **Axes:** Y-axis is "Multiplier" (0.5 to 6.0), X-axis lists the scenarios.
*   **Content:** A line graph showing the breakdown of the Chemical Selection Index.
    *   **CSI (solid dark red line with circle markers):** Starts at ~3.47 (baseline), drops to a local minimum of ~1.8 (equal_degradation_gm), spikes dramatically to ~5.5 at **equal_pools**, and settles at ~4.8 for no_compartments.
    *   **drift (dotted green line with triangle markers):** Follows a similar but more exaggerated path. It peaks significantly at `equal_polymer_only_gm` (~4.7) and `equal_pools` (~6.0). 
    *   **real (dashed blue line with square markers):** Stays near 1.0 (no enrichment line) but shows slight deviations, dipping to ~0.6 at `equal_polymer_only_gm`, rising to ~1.5 at `equal_free_only_gm`, and ending at ~1.3 for `no_compartments`.
*   **Key Takeaway:** The `equal_pools` control is a massive outlier that produces the highest total selection, driven almost entirely by a surge in indirect drift.

**2. Free vs DNA T/(U+T) across controls (Middle Panel)**
*   **Axes:** Y-axis is "T/(U+T)" (0.15 to 0.85+), X-axis lists the scenarios. A grey dotted horizontal line marks the starting influx ratio of 0.2727.
*   **Content:** A line graph comparing the free pool and the DNA polymer.
    *   **free T/(U+T) (solid purple line with circle markers):** The baseline starts high at ~0.62. The `equal_free_only_gm`, `equal_degradation_gm`, and `equal_degradation_kT` controls plunge it down to ~0.19 (near the influx line). It then spikes to ~0.78 at `equal_pools`.
    *   **DNA T/(U+T) (dashed orange line with square markers):** Starts at ~0.55 (baseline). It tracks downward across the degradation controls, bottoming out at ~0.19, before spiking to ~0.72 at `equal_pools` and reaching its maximum of ~0.85 at `no_compartments`.
*   **Key Takeaway:** The T fraction in the DNA polymer is highly sensitive to the controls. The `no_compartments` control achieves the highest T enrichment in the final DNA, even though its free pool ratio is lower than the `equal_pools` scenario.

**3. Yield & survival across controls (Right Panel)**
*   **Axes:** Left Y-axis is "Final total DNA" (purple bars), Right Y-axis is "Final per-polymer survival" (dark red line with circle markers).
*   **Content:** A combined bar and line chart.
    *   **Final total DNA (Bars):** Yield peaks at ~120,000 for `equal_polymer_only_gm` and `equal_degradation_kT`. It is lowest for `no_compartments` at ~72,000.
    *   **Survival (Line):** Survival is highest (~0.95) at `equal_degradation_kT` and `equal_polymer_only_gm`. It drops sharply to ~0.56 in the `no_compartments` scenario.
*   **Key Takeaway:** There appears to be an inverse relationship or trade-off between achieving maximum T enrichment in DNA (seen in `no_compartments`) and maintaining high overall yield and survival. The `no_compartments` scenario produces highly T-rich DNA but destroys a massive portion of the total polymer population in the process.
