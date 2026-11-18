[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="2670" height="2366" alt="free_vs_dna_TU_v670" src="https://github.com/user-attachments/assets/d9671147-39bd-458f-8b13-ece7775d76ba" />

### **Overview**
The image displays a single-panel scientific scatter plot titled **"UPDSF v6.6.1 — Free-pool vs polymer-pool T/(U+T) per seed"**. 
The subtitle provides a key for interpretation: **"Off-diagonal = direct discrimination; horizontal shift from influx = pool drift"**. 

The plot evaluates various control scenarios to decompose the mechanisms of chemical selection (favoring Thymine over Uracil). The X-axis is **"Free-pool T/(U+T)"** (the ratio of T to total T+U in the free nucleotide pool) and the Y-axis is **"Polymer-pool T/(U+T)"** (the ratio of T to total T+U incorporated into the resulting DNA polymer). Both axes range from 0.0 to 1.0.

### **Key Reference Lines**
*   **Dashed Grey Line (y = x):** Represents parity. If a scenario falls on this line, the composition of the polymer exactly matches the composition of the free pool (no direct discrimination).
*   **Dotted Grey Vertical Line:** Marks the **"influx T/(U+T) = 0.2727"** (the default 45:120 stoichiometry used in previous simulations).

### **Scenario Analysis (Data Points)**
The plot contains seven distinct colored data points (some overlapping), representing different simulation controls:

1.  **baseline (Red circle at ~0.62, 0.55):** Located to the right of the influx line (indicating positive pool drift) and below the y=x line (indicating the polymer has a *lower* T fraction than the free pool it drew from). This signifies that while drift enriches the pool, direct incorporation actually favors U over T in this specific baseline.
2.  **equal_polymer_only_gm (Orange circle at ~0.62, 0.37):** Shares the same horizontal position (Free-pool ~0.62) as the baseline, but sits much lower on the Y-axis. This shows that removing polymer growth differences severely reduces T incorporation.
3.  **equal_free_only_gm (Blue circle at ~0.19, 0.30):** Located near the influx line but positioned vertically above the y=x line. This shows that when free pool differences are controlled, the polymer actually enriches T relative to the available free pool.
4.  **equal_degradation_gm (Green circle at ~0.19, 0.18):** Sits almost exactly on the y=x line, near the influx line. This indicates that without differential degradation rates, there is almost no discrimination.
5.  **equal_degradation_kT (Teal circle at ~0.19, 0.18):** Overlaps almost perfectly with the green point, showing similar behavior.
6.  **equal_pools (Purple circle at ~0.78, 0.72):** Located to the far right, showing the highest pool drift. It sits below the y=x line, indicating that even when starting with equal pools, the polymer ends up less T-rich than the free pool.
7.  **no_compartments (Grey circle at ~0.62, 0.86):** Located high on the Y-axis. It shares the same free-pool ratio as the baseline but has a much higher polymer T fraction, sitting far above the y=x line, indicating strong direct preference for T in this configuration.

### **Key Takeaways**
*   **Drift is Universal but Varies:** Most scenarios (except the equal_free ones) result in horizontal movement to the right from the influx line (0.2727), confirming that "pool drift" enriches the free pool with T over time. The `equal_pools` scenario shows the most extreme drift.
*   **Direct Discrimination Varies:** The position relative to the y=x line varies wildly. `no_compartments` shows strong direct preference for T, while the `baseline` and `equal_pools` show a direct preference for U (polymer T fraction is lower than free pool T fraction).
*   **Control Impact:** The `equal_polymer_only` control dramatically drops the polymer T fraction, implying that differential growth rates of T-rich vs U-rich polymers are a major factor in achieving high T incorporation.
