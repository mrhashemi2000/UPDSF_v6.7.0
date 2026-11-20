[![DOI](https://img.shields.io/badge/DOI-10.26434/chemrxiv.15012436/v1-green)](https://doi.org/10.26434/chemrxiv.15012436/v1) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="5370" height="1484" alt="clay_rate_sweep_v670" src="https://github.com/user-attachments/assets/144d6ea5-2b27-4629-91ab-f6d9f7751c0b" />

### **Overview**
The image displays a three-panel scientific dashboard titled **"UPDSF v6.6.1 — Sensitivity to clay adsorption rate"**. This dashboard explores how varying the rate at which molecules adsorb (stick) to clay surfaces affects selection, compartmentalization, and overall yield.

The X-axis on all three panels is **"CLAY_ADSORPTION_RATE (s^-1)"**, plotted on a logarithmic scale with specific tick marks at 0, \(10^{-4}\), \(10^{-3}\), \(10^{-2}\), and \(10^{-1}\).

### **Panel Descriptions**

**1. CSI decomposition vs clay adsorption (Left Panel)**
*   **Axes:** Y-axis is "Multiplier" (0.5 to 5.0), X-axis is "CLAY_ADSORPTION_RATE".
*   **Content:** A line graph showing the breakdown of the Chemical Selection Index.
    *   **CSI (solid dark red line with circle markers):** Decreases steadily from ~4.8 at a rate of 0 to ~3.25 at a rate of \(10^{-1}\).
    *   **drift (dotted green line with triangle markers):** Remains relatively flat, hovering between 3.5 and 4.1, and actually slightly *increases* at the highest adsorption rates.
    *   **real (dashed blue line with square markers):** Decreases from ~1.35 down to ~0.85 as the adsorption rate increases.
*   **Key Takeaway:** Higher clay adsorption rates decrease overall selection (CSI). This is primarily driven by a reduction in "real" (direct) selection, while "drift" (indirect selection) remains largely robust or even slightly improves.

**2. Compartmentalization vs clay adsorption (Middle Panel)**
*   **Axes:** Y-axis is "Fraction in protected compartment" (0.00 to 0.20+), X-axis is "CLAY_ADSORPTION_RATE".
*   **Content:** A line graph showing the fraction of molecules that end up in the protected clay/lipid compartment.
    *   **T on clay/lipid (solid red line with circle markers):** Rises from 0 to ~0.05 at \(10^{-3}\), then surges to ~0.21 at \(10^{-2}\) before plateauing.
    *   **U on clay/lipid (dashed blue line with square markers):** Rises later and more gradually, staying near zero until \(10^{-3}\), then climbing steeply to match T at \(10^{-1}\) (~0.21).
*   **Key Takeaway:** Adsorption acts as a protective mechanism. At moderate rates (\(10^{-3}\) to \(10^{-2}\)), Thymine (T) is preferentially adsorbed and protected compared to Uracil (U). Only at very high rates (\(10^{-1}\)) do both molecules achieve equal protection.

**3. Yield vs clay adsorption (Right Panel)**
*   **Axes:** Y-axis is "Final total DNA" (0 to 100,000+), X-axis is "CLAY_ADSORPTION_RATE".
*   **Content:** A line graph showing yield metrics.
    *   **total DNA (solid purple line with circle markers):** Increases steadily from ~72,000 at a rate of 0 to over 105,000 at \(10^{-1}\).
    *   **ads events (norm.) (dotted grey line with square markers):** Remains flat at zero across the entire scale (this is likely a normalized metric that is visually indistinguishable at this scale compared to the yield).
*   **Key Takeaway:** Increased clay adsorption leads to a higher total yield of DNA.

### **Summary Interpretation**
The system exhibits a trade-off with respect to clay adsorption. While higher adsorption rates increase the total yield of DNA (likely by protecting molecules from degradation), they actually **reduce the overall chemical selection (CSI)**. The selection process is most efficient at low adsorption rates where direct discrimination favors T. However, moderate adsorption rates are beneficial for selectively protecting T over U in the compartment. At extreme adsorption rates, the protection loses its selectivity, favoring both T and U equally, and the selection advantage diminishes significantly.
