EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="4540" height="3656" alt="optimal_simulation_v670_vent_2400h" src="https://github.com/user-attachments/assets/ea07bac0-0a59-4903-bcf5-df7f40883e8b" />


### **Overview**
This image displays a multi-panel scientific dashboard titled **"UPDSF v6.6.1 — Vent Chemical Filtering (T over U)"**. It shows simulation results for a chemical system at **T=90.0°C** and **pH=11.00** over an extended **horizon of 2400 hours**. The simulation illustrates chemical selection (vent) favoring Thymine (T) over Uracil (U).

*Note: Compared to the previous 240-hour simulation, this 2400-hour run shows dramatic changes in nucleotide fractions and final composition, where T now dominates.*

### **Panel Descriptions**

**1. DNA steady state (Top Left)**
*   **Axes:** Y-axis is "DNA molecules" (0 to 300000), X-axis is "Time (h)" (0 to 2500).
*   **Content:** A line graph showing the accumulation of different nucleotides over time. After an initial transient period, **T-DNA (red line)** rises sharply and dominates, reaching over 300,000 molecules by 2400 hours. **G-DNA (purple line)** rises steadily to ~210,000, and **A-DNA (orange line)** reaches ~180,000. **U-DNA (blue line)** peaks early (around 200 hours) and then declines to near zero. C-DNA and X-DNA remain negligible.

**2. Nucleotide fractions (Top Middle)**
*   **Axes:** Y-axis is "Fraction of total DNA" (0.0 to 0.4+), X-axis is "Time (h)" (0 to 2500).
*   **Content:** A line graph showing the relative proportions. **U (blue line)** starts high (~0.38) but rapidly drops to near zero by 500 hours. Conversely, **T (red line)** starts at zero and rises to become the dominant fraction (>0.4) by the end of the simulation. **G (purple)** and **A (orange)** rise to around 0.3 and then slowly decline or plateau. **C (green)** drops quickly to near zero. This panel clearly shows the chemical filtering effect over the long term.

**3. CSI = real x drift [rising] (Top Right)**
*   **Axes:** Y-axis is "Multiplier" (0 to 7), X-axis is "Time (h)" (0 to 2500).
*   **Content:** A line graph showing multipliers. The **CSI (total)** (solid red line) and **drift (indirect)** (dotted green line) rise steadily, reaching approximately 6.4 and 6.1 respectively. The **real (direct)** (dashed blue line) drops slightly from 1.0 and stabilizes around 1.06. A horizontal grey dashed line indicates "no enrichment" at 1.0. A vertical orange dashed line marks the 2400h mark.

**4. Survival (net_population_growth) (Bottom Left)**
*   **Axes:** Y-axis is "Survival" (0.0 to 1.0), X-axis is "Time (h)" (0 to 2500).
*   **Content:** A line graph showing survival metrics. **per-polymer** (solid dark blue) and **residue** (dashed green) curves decline steadily from 1.0 to approximately 0.55-0.56 over 2400 hours. **retention** (dotted red) drops sharply in the first 100 hours to ~0.06 and remains flat.

**5. Final composition (Bottom Middle)**
*   **Axes:** Y-axis is "Molecules" (0 to 300000), X-axis is "Nucleotide" (U, T, C, A, G, X).
*   **Content:** A bar chart showing the final counts at 2400 hours. **T dominates** with 306,528 molecules, followed by **G** (216,071) and **A** (186,035). **X** is 3,541, **U** is 2,406, and **C** is 314.

**6. Text Box Summary (Bottom Right)**
*   **Content:** Detailed simulation parameters and results.
    *   **Conditions:** T = 90.0 °C, pH_in_situ = 11.00, photon_flux = 0.00e+00 (VENT (dark)), **horizon = 2400 h**, regime = net_population_growth, CSI shape = rising.
    *   **Two environmental channels:**
        *   CSI_end = 6.482x
        *   peak CSI = 6.482x @ 2400 h
        *   real (direct) = 1.063x
        *   drift (indirect) = 6.097x
        *   free T/(U+T) = 0.9333
        *   DNA T/(U+T) = 0.9922
        *   influx T/(U+T) = 0.2727
    *   **Mechanism (extrapolated):**
        *   k_U/K_T = 357.0x [Ea_T assumed; see sweep]
        *   t½(U) hydrolysis = 21.72 h
        *   t½(T) hydrolysis = 7754.90 h
        *   hydrolysis events = 552,616
        *   UV damage events = 0
    *   **Yield / survival:**
        *   total DNA (final) = 714,895
        *   per-polymer surv = 0.5523
        *   residue survival = 0.5640
    *   **Confidence:**
        *   max |mass balance| = 1.27e-14
        *   max |consumed res| = 0.00e+00
    *   **Decisive controls:** Notes regarding decomposing hydrolytic contributions and a reference to "see decomposed_controls_v670.png".
