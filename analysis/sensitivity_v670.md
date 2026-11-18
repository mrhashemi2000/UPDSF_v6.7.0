[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="7719" height="4424" alt="sensitivity_v670" src="https://github.com/user-attachments/assets/a12a7734-f039-412d-b73d-cb92a5b76491" />


### **Overview**
The image displays a 12-panel parameter sweep dashboard titled **"UPDSF v6.6.1 — Vent Chemical Filtering (T over U)"**. It visualizes simulation outcomes across a 2D parameter space defined by **Temperature (T, °C) on the X-axis (40 to 90 °C)** and **pH on the Y-axis (5 to 11)**. The plots are heatmaps (contour plots) showing how various metrics respond to changes in these two primary variables. The underlying simulation settings are likely the same as the previous dashboards (e.g., dark vent, 240h horizon), but this view shows a broad sweep of conditions.

### **Panel Descriptions (Row by Row)**

**Row 1 (Top)**
1.  **CSI (total env. selection):** A heatmap showing total environmental selection. Values range from ~1.76 (dark purple) to ~3.44 (yellow). The highest selection occurs at high temperatures (>80 °C) and high pH (>9). Lower temperatures and lower pH show minimal selection.
2.  **Real T-pref enrichment (direct):** A heatmap showing direct T-preference. Values range from ~0.81 to ~1.02. The highest enrichment (yellow/green) occurs at lower temperatures (40–60 °C) across most pH levels, while high temperatures (>80 °C) show reduced enrichment (purple).
3.  **Pool-composition drift (indirect):** A heatmap showing indirect drift. Values range from ~1.8 to ~3.9. This metric strongly correlates with the total CSI, being highest (yellow) at high T and high pH.
4.  **Fraction T in DNA:** A heatmap showing the final fraction of T in DNA. Values range from ~0.114 to ~0.222. The highest fraction of T in DNA occurs at high temperatures (>80 °C) and high pH (>9), consistent with the total selection plot.

**Row 2 (Middle)**
5.  **Heuristic contribution (red=helps):** A heatmap with values ranging from ~0.675 to ~1.200. Higher values (red/orange) are seen at high temperatures and high pH, indicating that the heuristic mechanism contributes positively under these conditions.
6.  **CSI — zero-UV control:** A heatmap showing CSI under zero-UV conditions. The pattern is nearly identical to the "CSI (total env. selection)" panel, suggesting UV damage is not a primary driver of the selection pattern in this parameter space.
7.  **CSI — equal-pools control:** A heatmap showing CSI under equal-pools conditions. Values range from ~3.3 to ~5.4. This control shows even higher selection values (up to 5.4) at high T and high pH compared to the baseline scenario.
8.  **Fraction of destruction events from UV:** A uniform light blue heatmap. The color bar scale is extremely small (1e-14), indicating that the fraction of destruction events due to UV is effectively zero across the entire parameter space.

**Row 3 (Bottom)**
9.  **log10 max |consumed identity rel err|:** A uniform orange heatmap. The color bar scale is extremely small (1e-12), indicating that numerical errors (relative error in consumed identity) are negligible and consistent across all conditions.
10. **Residue retention ratio:** A heatmap showing the ratio of residue retention. Values range from ~0.05 to ~0.95. Retention is highest (green/yellow) at low temperatures (40–60 °C) and decreases (orange/red) as temperature increases.
11. **Peak CSI over the run:** A heatmap showing the maximum CSI reached during the simulation. Values range from ~1.75 to ~7.00. The highest peaks (yellow) are observed at high temperatures (>80 °C) and high pH (>9).
12. **Time to peak CSI (h):** A heatmap showing the time required to reach peak CSI. Values range from 0 to 240 hours. Peak CSI is reached quickly (dark purple/blue, <60h) at low temperatures and low pH, but takes the full 240 hours (yellow/orange) at high temperatures and high pH.

### **Key Takeaways**
*   **High T & High pH Drive Selection:** The highest chemical selection for T over U (CSI, drift, Fraction T in DNA) occurs in the upper-right quadrant of the parameter space (T > 80°C, pH > 9).
*   **Direct vs. Indirect:** While direct T-preference enrichment is highest at lower temperatures, the massive *drift* (indirect) effect at high temperatures and pH dominates the overall selection outcome.
*   **UV is Irrelevant:** The UV destruction fraction is zero (1e-14), and the zero-UV control is identical to the baseline, confirming this is a purely chemical/thermal selection process.
*   **Time Dependency:** At the conditions that produce the highest selection (high T/high pH), it takes the entire 240-hour horizon to reach that peak.
