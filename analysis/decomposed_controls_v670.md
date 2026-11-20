[![DOI](https://img.shields.io/badge/DOI-10.26434/chemrxiv.15012436/v1-green)](https://doi.org/10.26434/chemrxiv.15012436/v1) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="4770" height="3236" alt="decomposed_controls_v670" src="https://github.com/user-attachments/assets/c1b3e7ed-f4ca-4b82-9fb2-68fd67937019" />

### Overview
The image displays a 4-panel scientific dashboard titled **"UPDSF v6.6.1 — Decomposed destruction channels (T=90 C, pH=11.0, 240 h, n=20)"**. It provides a detailed breakdown of the simulation by comparing a **baseline** scenario against six different **control scenarios** (where specific mechanisms are equalized or disabled) to determine what drives chemical selection and yield. 

A prominent feature is the **"Decision: REFUTED"** badge in the first panel, indicating that the initial hypothesis (likely regarding the primary driver of selection) has been rejected by the control tests.

The X-axis for all panels lists the same seven scenarios:
*   **baseline**
*   **equal_polymer_only_gm**
*   **equal_free_only_gm**
*   **equal_degradation_gm**
*   **equal_degradation_kT**
*   **equal_pools**
*   **no_compartments**

### Panel Descriptions

**A. CSI across controls (Top Left)**
*   **Axes:** Y-axis is "CSI (mean ± 95% CI)", X-axis is the list of scenarios.
*   **Content:** A bar chart showing the total Chemical Selection Index. The baseline (dark red) is **3.47**, which is well above the grey dashed line representing "no enrichment" (1.0).
*   **Key Findings:**
    *   Disabling differential polymer growth (`equal_polymer_only_gm`) drops CSI to 2.83.
    *   Disabling free-pool differences (`equal_free_only_gm`) drops it further to 2.46.
    *   Equalizing degradation (`equal_degradation_gm`, `equal_degradation_kT`) drops CSI significantly to ~1.8–1.9.
    *   **Shockingly**, forcing completely equal pools (`equal_pools`) results in the *highest* CSI of **5.49**, suggesting the baseline system is actually somewhat constrained by its starting conditions.

**B. Free-pool drift across controls (Top Right)**
*   **Axes:** Y-axis is "Final free T/(U+T)", X-axis is the scenarios.
*   **Content:** A bar chart showing the T fraction in the free nucleotide pool. The dotted grey line indicates the starting influx ratio of 0.2727.
*   **Key Findings:** The baseline ends with a free pool ratio of ~0.62, demonstrating substantial drift from the initial 0.27. The `equal_free_only_gm`, `equal_degradation_gm`, and `equal_degradation_kT` controls completely fail to drift, staying at ~0.2. Interestingly, `equal_pools` (starting at 0.5) drifts all the way up to ~0.79.

**C. DNA composition across controls (Bottom Left)**
*   **Axes:** Y-axis is "Final DNA T/(U+T)", X-axis is the scenarios.
*   **Content:** A bar chart showing the final T fraction incorporated into the DNA polymer. 
*   **Key Findings:** The baseline DNA is **0.55** T. The controls that failed to drift in the free pool (e.g., `equal_free_only_gm`, `equal_degradation_gm`) also produce DNA with low T fractions (~0.17 to 0.30). The `equal_pools` and `no_compartments` scenarios produce highly T-enriched DNA (>0.7).

**D. Yield and survival across controls (Bottom Right)**
*   **Axes:** Left Y-axis is "Final total DNA" (blue bars), Right Y-axis is "Final per-polymer survival" (red line with circle markers).
*   **Content:** A combined bar and line chart.
*   **Key Findings:** The baseline yield is ~101,000 molecules with a survival rate of ~0.80. The `equal_polymer_only_gm` and `no_compartments` controls achieve slightly higher yields. However, the most drastic result is the **`no_compartments` survival rate, which plummets to ~0.56**, indicating that without compartmentalization, the system produces a lot of DNA but a much higher fraction of it is destroyed/degraded by the end of the run.

### Summary Interpretation
The "REFUTED" decision and the control breakdown reveal that Chemical Selection (CSI) is not driven by a single simple mechanism. While degradation differences are crucial (dropping CSI to ~1.8 when equalized), the system actually achieves *maximum* selection when forced into `equal_pools` (CSI 5.49). Furthermore, compartmentalization is critical for survival; removing it (`no_compartments`) maximizes certain yield metrics but causes survival to crash.
