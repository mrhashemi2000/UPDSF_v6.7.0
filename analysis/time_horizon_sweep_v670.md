EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="7170" height="1631" alt="time_horizon_sweep_v670" src="https://github.com/user-attachments/assets/f710c6b5-7dc1-4b5b-b243-f18877743aea" />


### Overview
The image displays a single-row, four-panel scientific dashboard titled **"UPDSF v6.6.1 — CSI vs time horizon at the optimum"**. Unlike previous dashboards that swept across Temperature and pH, this dashboard isolates the optimal conditions (identified previously as high T and high pH) and plots how key metrics evolve as the simulation **time horizon** is extended. The X-axis on all four panels is **"Horizon (h)"**, plotted on a logarithmic scale ranging from approximately 240 hours to 10,000 hours.

### Panel Descriptions

**1. CSI vs horizon (Far Left)**
*   **Axes:** Y-axis is "CSI" (3.5 to 10.5), X-axis is "Horizon (h)" (log scale).
*   **Content:** A line graph showing the total Chemical Selection Index. The **CSI_end** (solid red line with circle markers) and **peak CSI** (dashed orange line with square markers) are perfectly superimposed.
*   **Trend:** The CSI grows steadily from ~3.5 at 240 hours to just over 10.0 at 10,000 hours. Because the two lines are identical, it indicates that at these optimal conditions, the peak selection is reached exactly at the end of the simulation horizon.

**2. Real vs drift vs horizon (Middle Left)**
*   **Axes:** Y-axis is "Multiplier" (0 to 10+), X-axis is "Horizon (h)" (log scale).
*   **Content:** A line graph breaking down the CSI into its components.
    *   **drift** (dashed green line with square markers): Rises steeply, correlating almost exactly with the total CSI curve (from ~3.9 to ~10.0). This confirms that indirect drift is the primary driver of selection over long horizons.
    *   **real** (solid blue line with circle markers): Remains flat at roughly 1.0 across all horizons.
    *   **free T/(U+T) (norm.)** (dotted grey line with triangle markers): Remains flat at roughly 0.8.

**3. Yield vs horizon (Middle Right)**
*   **Axes:** Y-axis is "Final total DNA" (0 to 1.8e6), X-axis is "Horizon (h)" (log scale).
*   **Content:** A line graph (solid purple line with circle markers) showing total DNA yield.
*   **Trend:** The yield increases exponentially (on this log-linear plot) as the horizon extends, starting at ~0.12e6 at 240 hours and climbing to ~1.7e6 (1.7 million) at 10,000 hours.

**4. Survival vs horizon (Far Right)**
*   **Axes:** Y-axis is "Final per-polymer survival" (0.3 to 0.8+), X-axis is "Horizon (h)" (log scale).
*   **Content:** A line graph (solid dark red line with circle markers) showing survival rates.
*   **Trend:** Survival declines steadily as the horizon increases. It starts near 0.80 at 240 hours and drops to approximately 0.32 at 10,000 hours, indicating that while yield increases, the fraction of surviving polymers decreases due to prolonged degradation/hydrolysis over the extended time.

### Key Takeaways
*   **Unbounded Selection:** Under optimal conditions, Chemical Selection (CSI) continues to compound over time, doubling from ~5 at 1,000 hours to ~10 at 10,000 hours.
*   **Drift Dominates:** The continuous selection over time is driven almost entirely by "drift" (indirect selection), while "real" (direct) selection stays constant at 1.0.
*   **Yield vs. Survival Trade-off:** Extending the time horizon drastically increases total DNA yield (more molecules are produced) but simultaneously decreases per-polymer survival (the existing molecules degrade).
