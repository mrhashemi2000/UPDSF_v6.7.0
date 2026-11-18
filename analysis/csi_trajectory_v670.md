[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="4166" height="2954" alt="csi_trajectory_v670" src="https://github.com/user-attachments/assets/aab5d358-e1b0-4ad3-8bd3-c4342505c86b" />

### Overview
The image displays a four-panel scientific dashboard titled **"UPDSF v6.6.1 — CSI trajectory at T=90 C, pH=11.0 (horizon 2400 h, shape=rising)"**. This dashboard shows the detailed time-course behavior of the system under the optimal conditions identified in earlier sweeps (high temperature and high pH) over the extended 2400-hour horizon.

The X-axis for all four panels is **"Time (h)"**, ranging from 0 to 2500. A vertical dashed orange line in the top-left panel marks the end of the simulation at 2400 hours.

### Panel Descriptions

**1. CSI = real x drift (Top Left)**
*   **Axes:** Y-axis is "Multiplier" (0 to 7), X-axis is "Time (h)".
*   **Content:** A line graph showing the trajectory of the Chemical Selection Index.
    *   **CSI (total) (solid red line):** Rises steeply in the first 500 hours, then continues a steady climb, reaching ~6.5 at 2400 hours.
    *   **drift (indirect) (dotted green line):** Rises very rapidly initially, briefly surpassing the total CSI, then stays slightly below it, ending at ~6.1. This confirms that indirect drift is the dominant mechanism driving selection over time.
    *   **real (direct) (dashed blue line):** Dips below 1.0 initially, then stabilizes at approximately 1.05 for the remainder of the simulation.
*   **Key Takeaway:** Selection compounds continuously over the long horizon, driven almost entirely by the "drift" mechanism.

**2. Free vs DNA vs influx T/(U+T) (Top Right)**
*   **Axes:** Y-axis is "T/(U+T)" (0.0 to 1.0), X-axis is "Time (h)".
*   **Content:** A line graph tracking the fraction of Thymine in different pools.
    *   **influx T/(U+T) (dotted grey line):** Remains constant at the starting ratio of 0.2727.
    *   **free T/(U+T) (solid purple line):** Rises sharply from the influx ratio, reaching ~0.8 by 500 hours and asymptotically approaching ~0.95 by 2400 hours.
    *   **DNA T/(U+T) (dashed orange line):** Rises even faster than the free pool initially, closely tracking it until about 500 hours, after which it pulls ahead and approaches nearly 1.0 (pure Thymine DNA).
*   **Key Takeaway:** The chemical filtering process is highly effective, eventually enriching the DNA polymer to be almost entirely composed of Thymine.

**3. Yield (Bottom Left)**
*   **Axes:** Y-axis is "Total DNA molecules" (0 to 700,000+), X-axis is "Time (h)".
*   **Content:** A line graph (solid black line) showing total DNA yield.
*   **Trend:** The yield increases linearly over the entire 2400-hour horizon, starting at 0 and reaching over 700,000 molecules. Unlike the selection metrics, yield does not plateau.
*   **Key Takeaway:** The system continuously produces DNA as long as the simulation runs, with no signs of stalling within this timeframe.

**4. Survival (Bottom Right)**
*   **Axes:** Y-axis is "Survival" (0.55 to 1.0), X-axis is "Time (h)".
*   **Content:** A line graph comparing survival metrics.
    *   **per-polymer (solid dark blue line)** and **residue (dashed green line):** These lines are nearly identical, showing a continuous decline in survival from 1.0 down to roughly 0.56 at 2400 hours.
*   **Key Takeaway:** While yield increases and the DNA becomes nearly pure Thymine, the overall survival rate of the polymers steadily degrades over the extended timeline, consistent with the continuous hydrolysis occurring in the system.
