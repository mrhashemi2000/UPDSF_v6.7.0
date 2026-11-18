[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="5368" height="1484" alt="ea_T_sweep_v670" src="https://github.com/user-attachments/assets/8514e99a-1f4a-473f-a3a7-1115f86e9ab9" />

### Overview
The image displays a three-panel scientific dashboard titled **"UPDSF v6.6.1 — Sensitivity to assumed Ea_T (the 357x question)"**. This dashboard investigates how sensitive the simulation results are to the assumed activation energy (Ea) for the hydrolysis of Thymine (T). 

In previous dashboards, the default assumption was a ratio of \(k\_U/k\_T = 357.0\), which was flagged as an assumed value based on Ea_T. This sweep tests how varying Ea_T (which changes the ratio) impacts the system's stability, selection metrics, and yield.

The X-axis on all three panels is **"Ea_T (kcal/mol)"**, ranging from 28 to 36.

### Panel Descriptions

**1. Extrapolated stability ratio (Left Panel)**
*   **Axes:** Y-axis is "k_U / k_T (log scale)" (ranging from \(10^2\) to \(10^3+\)), X-axis is "Ea_T (kcal/mol)" (28 to 36).
*   **Content:** A line graph (solid dark red line with circle markers) showing the stability ratio between Uracil and Thymine.
*   **Trend:** There is a steep, continuous exponential decline (linear on a log scale) in the ratio. At an Ea_T of 28, the ratio is over 1000x. At an Ea_T of 36, it drops to roughly 100x.
*   **Key Takeaway:** A higher activation energy for T implies that T is much more stable, but the *relative* difference in stability (the ratio) shrinks as Ea_T increases.

**2. CSI decomposition vs Ea_T (Middle Panel)**
*   **Axes:** Y-axis is "Multiplier" (1.0 to 4.0+), X-axis is "Ea_T (kcal/mol)" (28 to 36).
*   **Content:** A line graph breaking down the Chemical Selection Index.
    *   **CSI (solid red line with circle markers):** Extremely flat, hovering at roughly 3.47 across the entire range.
    *   **drift (dotted green line with triangle markers):** Also extremely flat, staying consistently at ~3.9.
    *   **real (dashed blue line with square markers):** Flat and low, hovering just below 1.0.
*   **Key Takeaway:** The overall selection metrics (CSI and drift) are completely insensitive to changes in the assumed Ea_T parameter. The ~3.5x selection advantage is robust regardless of this uncertainty.

**3. Yield vs Ea_T (Right Panel)**
*   **Axes:** Y-axis is "Final total DNA" (101,000 to 101,500+), X-axis is "Ea_T (kcal/mol)" (28 to 36).
*   **Content:** A line graph (solid purple line with circle markers) showing final yield.
*   **Trend:** Unlike the selection metrics, the yield shows a non-linear, chaotic response. It peaks sharply at Ea_T = 31, drops dramatically to a local minimum at Ea_T = 33, and then begins to rise again towards 36. 
*   **Key Takeaway:** While the *selection advantage* is robust, the absolute *yield* is highly sensitive to the exact assumed activation energy, though the total variation remains relatively small (fluctuating within a ~500 molecule range out of ~101,500).

### Summary Conclusion
The dashboard answers the "357x question" by demonstrating that the assumed kinetic ratio (driven by Ea_T) has a **negligible impact on the calculated Chemical Selection Index (CSI)**. The mechanism driving drift and selection is robust. However, the absolute yield is highly sensitive and non-linear with respect to this parameter, suggesting that while the "winner" (T) remains the same, the total amount of product produced is dependent on these fine-tuned thermodynamic assumptions.
