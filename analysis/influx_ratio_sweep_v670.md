[![DOI](https://img.shields.io/badge/DOI-10.26434/chemrxiv.15012436/v1-green)](https://doi.org/10.26434/chemrxiv.15012436/v1) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="5369" height="1484" alt="influx_ratio_sweep_v670" src="https://github.com/user-attachments/assets/cc7560f1-3663-43ab-8185-b6447c035bcd" />


### Overview
The image displays a three-panel scientific dashboard titled **"UPDSF v6.6.0 — Sensitivity to assumed influx stoichiometry"**. This dashboard explores how different assumed ratios of Thymine (T) to Uracil (U) entering the system (the "influx") affect selection metrics, yield, and survival. Note that this is version 6.6.0, whereas previous dashboards were 6.6.1.

The X-axis on all three panels is **"Influx T/(U+T)"**, ranging from 0.10 to 0.50. A vertical dashed line at **0.2727** represents the **"default 45:120"** stoichiometry used in the earlier simulations.

### Panel Descriptions

**1. CSI decomposition vs influx T fraction (Left Panel)**
*   **Axes:** Y-axis is "Multiplier" (0 to 7+), X-axis is "Influx T/(U+T)" (0.10 to 0.50).
*   **Content:** A line graph showing the breakdown of Chemical Selection Index (CSI) as the influx ratio changes.
    *   **CSI (solid red line with circle markers):** Rises linearly from ~1.4 at an influx of 0.10 to ~6.6 at an influx of 0.50.
    *   **drift (dotted green line with triangle markers):** Follows a similar upward linear trend, rising from ~1.6 to ~7.1, staying consistently above the total CSI.
    *   **real (dashed blue line with square markers):** Remains nearly flat at roughly 0.9 across the entire range.
*   **Key Takeaway:** Higher initial concentrations of T relative to U (higher influx fraction) lead to significantly higher overall selection, driven almost entirely by an increase in "drift" (indirect selection).

**2. Convention-free metrics vs influx T fraction (Middle Panel)**
*   **Axes:** Y-axis is "Convention-free multiplier" (0.5 to 3.5), X-axis is "Influx T/(U+T)" (0.10 to 0.50).
*   **Content:** A line graph showing normalized metrics to remove baseline convention effects.
    *   **csi_vs_influx (solid purple line with circle markers):** Remains flat at approximately 0.8, slightly below the 1.0 baseline (grey dotted line).
    *   **drift_independent (dashed teal line with square markers):** Declines steadily from ~3.15 at an influx of 0.10 down to ~1.6 at an influx of 0.50.
*   **Key Takeaway:** When the inherent bias of the influx ratio is factored out ("convention-free"), the relative benefit of drift actually decreases as the influx of T increases. The raw numbers (left panel) look better, but the underlying efficiency of the selection process per available T is lower.

**3. Yield vs influx T fraction (Right Panel)**
*   **Axes:** Y-axis is "Yield / survival" (0 to 100,000+), X-axis is "Influx T/(U+T)" (0.10 to 0.50).
*   **Content:** A line graph comparing final yield and survival.
    *   **total DNA (solid purple line with circle markers):** Rises slightly from just under 100,000 at an influx of 0.10 to nearly 110,000 at an influx of 0.50. *(Note: The absolute values here are lower than the ~714k seen in the 2400h optimal run, suggesting different base conditions for this sweep).*
    *   **final survival (dashed teal line with square markers):** Remains essentially flat at 0 across the entire range. *(Note: Given the scale of the Y-axis, a survival rate of ~0.55 would appear near zero here. The metric is effectively unreadable on this scale).*
*   **Key Takeaway:** Increasing the influx of T results in a modest increase in total DNA yield, but does not change overall survival rates.
