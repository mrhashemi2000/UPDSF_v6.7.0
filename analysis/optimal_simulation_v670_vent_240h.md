<img width="4500" height="3656" alt="optimal_simulation_v670_vent_240h" src="https://github.com/user-attachments/assets/45bfcd98-0763-4fe4-99a1-56064244be13" />

### **Overview**
The image displays a multi-panel scientific dashboard titled **"UPDSF v6.6.1 — Vent Chemical Filtering (T over U)"**. It presents simulation results for a chemical system at **T=90.0°C** and **pH=11.00** over a **240-hour horizon**. The simulation focuses on the chemical selection (vent) of nucleotides, specifically the filtering of Thymine (T) over Uracil (U).

### **Panel Descriptions**

**1. DNA steady state (Top Left)**
*   **Axes:** Y-axis is "DNA molecules" (0 to 30000), X-axis is "Time (h)" (0 to 250).
*   **Content:** A line graph showing the accumulation of different nucleotides in DNA over time. U-DNA (blue line) rises quickly and plateaus around 18,000-19,000 molecules. T-DNA (red line) and A-DNA (orange line) rise steadily, with A exceeding T. G-DNA (purple line) rises the fastest and highest, reaching nearly 30,000 molecules. C-DNA (green line) rises slightly then slowly declines. X-DNA (brown line) remains flat and negligible near zero.

**2. Nucleotide fractions (Top Middle)**
*   **Axes:** Y-axis is "Fraction of total DNA" (0.00 to 0.40), X-axis is "Time (h)" (0 to 250).
*   **Content:** A line graph showing the relative proportions of each nucleotide. U (blue line) starts high (~0.34) and slowly declines to ~0.18. G (purple line) starts low (~0.16) and steadily rises to ~0.29. A (orange line) rises from ~0.16 to ~0.27. T (red line) rises from 0 to ~0.22. C (green line) starts high but quickly drops and continues to decline to ~0.03. X (brown line) remains at zero.

**3. CSI = real x drift [rising] (Top Right)**
*   **Axes:** Y-axis is "Multiplier" (0.0 to 4.0), X-axis is "Time (h)" (0 to 250).
*   **Content:** A line graph showing three multipliers. The "CSI (total)" (solid red line) rises steadily from 0 to ~3.45. The "drift (indirect)" (dotted green line) rises similarly to ~3.88. The "real (direct)" (dashed blue line) dips slightly from 1.0 and stabilizes around 0.89. A horizontal dashed grey line marks "no enrichment" at 1.0. A vertical dashed orange line marks the end of the simulation at 240h.

**4. Survival (net_population_growth) (Bottom Left)**
*   **Axes:** Y-axis is "Survival" (0.0 to 1.0), X-axis is "Time (h)" (0 to 250).
*   **Content:** A line graph showing survival metrics. The "per-polymer" (solid dark blue line) and "residue" (dashed green line) curves are nearly identical, slowly declining from 1.0 to ~0.8 over 240 hours. The "retention" (dotted red line) drops sharply from 0.7 to ~0.1 within the first 50 hours and then plateaus.

**5. Final composition (Bottom Middle)**
*   **Axes:** Y-axis is "Molecules" (0 to 30000), X-axis is "Nucleotide" (U, T, C, A, G, X).
*   **Content:** A bar chart showing the final count of each nucleotide at 240 hours.
    *   **G:** 29,261
    *   **A:** 26,983
    *   **T:** 23,118
    *   **U:** 18,885
    *   **C:** 2,949
    *   **X:** 30

**6. Text Box Summary (Bottom Right)**
*   **Content:** A detailed text log providing the exact parameters and results of the simulation.
    *   **Conditions:** T = 90.0 °C, pH_in_situ = 11.00, photon_flux = 0.00e+00 (VENT (dark)), horizon = 240 h, regime = net_population_growth, CSI shape = rising.
    *   **Two environmental channels:**
        *   CSI_end = 3.453x
        *   peak CSI = 3.452x @ 240 h
        *   real (direct) = 0.889x
        *   drift (indirect) = 3.883x
        *   free T/(U+T) = 0.6191
        *   DNA T/(U+T) = 0.5504
        *   influx T/(U+T) = 0.2727
    *   **Mechanism (extrapolated):**
        *   k_U/K_T = 357.0x [Ea_T assumed; see sweep]
        *   t½(U) hydrolysis = 21.72 h
        *   t½(T) hydrolysis = 7754.90 h
        *   hydrolysis events = 25,493
        *   UV damage events = 0
    *   **Yield / survival:**
        *   total DNA (final) = 101,226
        *   per-polymer = 0.7925
        *   residue survival = 0.7988
    *   **Confidence:**
        *   max mass balance = 5.59e-15
        *   max consumed res = 0.00e+00
    *   **Decisive controls:** Notes about equal_polymer_only and equal_free_only decomposing the hydrolytic contribution, with a reference to see decomposed_controls_v670.png.
