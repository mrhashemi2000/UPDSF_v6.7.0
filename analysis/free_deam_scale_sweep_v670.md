[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="5370" height="1485" alt="free_deam_scale_sweep_v670" src="https://github.com/user-attachments/assets/43d2ae7e-9097-4788-a8e6-67fd5c6c92c7" />


### **Overview**
The image displays a three-panel scientific dashboard titled **"UPDSF v6.6.1 — Sensitivity to free-monomer deamination scale"**. This dashboard explores how adjusting a specific parameter—the rate or scale of deamination (a chemical degradation process) occurring in free nucleotides before they are incorporated into a polymer—affects the system's selection metrics, composition, and yield. 

The X-axis on all three panels is **"FREE_MONOMER_DEAM_SCALE"**, ranging from 0 to 10.

### **Panel Descriptions**

**1. CSI decomposition vs free-deam scale (Left Panel)**
*   **Axes:** Y-axis is "Multiplier" (0.5 to 4.5+), X-axis is "FREE_MONOMER_DEAM_SCALE" (0 to 10).
*   **Content:** A line graph breaking down the Chemical Selection Index (CSI).
    *   **CSI (solid red line with circle markers):** Rises very slightly from ~2.95 to ~3.15 as the scale increases.
    *   **drift (dotted green line with triangle markers):** Declines gradually from ~4.6 at scale 0 down to ~4.1 at scale 10.
    *   **real (dashed blue line with square markers):** Remains flat, hovering just above 0.6 across the entire scale.
*   **Key Takeaway:** Increasing the deamination of free monomers slightly increases total selection (CSI), but this is primarily a balancing act: it slightly decreases the indirect "drift" multiplier while slightly increasing the "real" (direct) component.

**2. Free vs DNA T/(U+T) (Middle Panel)**
*   **Axes:** Y-axis is "T/(U+T)" (0.0 to 0.7+), X-axis is "FREE_MONOMER_DEAM_SCALE" (0 to 10).
*   **Content:** A line graph comparing the Thymine fraction in two different pools.
    *   **free T/(U+T) (solid purple line with circle markers):** Starts high at ~0.73 and slowly declines to ~0.64 as the deamination scale increases.
    *   **DNA T/(U+T) (dashed orange line with square markers):** Remains very low and nearly flat, rising only slightly from ~0.19 to ~0.21.
*   **Key Takeaway:** There is a massive disparity between the free pool and the DNA polymer. While the free pool is heavily enriched with T (due to drift), the DNA incorporates a much lower fraction of T. Increasing free-monomer deamination actually *reduces* the T fraction in the free pool but has a negligible, slightly positive effect on the T fraction in the final DNA.

**3. Yield vs free-deam scale (Right Panel)**
*   **Axes:** Y-axis is "Final total DNA" (101,500 to 102,000), X-axis is "FREE_MONOMER_DEAM_SCALE" (0 to 10).
*   **Content:** A line graph showing total yield (solid purple line with circle markers).
*   **Trend:** The yield starts near 102,000, drops sharply at a scale of 1, spikes back up slightly at a scale of 2, and then steadily declines to roughly 101,450 at a scale of 10. 
*   **Key Takeaway:** Altering the free-monomer deamination scale has a non-linear, generally negative impact on the final DNA yield. The variation is relatively small (less than 1% of the total yield) compared to the dramatic shifts seen in composition metrics in other scenarios.
