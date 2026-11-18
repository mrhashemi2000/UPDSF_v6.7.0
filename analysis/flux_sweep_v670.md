EXTENSION RELEASE. The v6.5.1 homopolymer engine (VSSUFEngine) is UNCHANGED: physics, kinetics, parameters, and all existing output schemas are identical, and at equal seeds every v6.6.1 number is reproduced bit-identically. v6.7.0 adds an OPT-IN copolymer / Darwinian layer that addresses the two structural weaknesses of the homopolymer abstraction (no sequence, no heredity):

<img width="7171" height="1631" alt="flux_sweep_v670" src="https://github.com/user-attachments/assets/7a0eb929-5d05-4fff-815b-765f5b6ee63f" />

### **Overview**
The image displays a four-panel scientific dashboard titled **"UPDSF v6.6.1 — Robustness to assumed UV scale (surface only)"**. This dashboard analyzes how varying levels of UV radiation (photon flux) affect the chemical selection process and overall system viability.

The X-axis on all four panels is **"photon_flux (photons/cm^2/s)"**, plotted on a logarithmic scale ranging from \(10^8\) to \(10^{18}\). Each panel contains three lines representing different quantum yields (qy) for UV damage: **qy=1e-04 (blue)**, **qy=1e-03 (orange)**, and **qy=1e-02 (green)**.

### **Panel Descriptions**

**1. CSI vs UV (Far Left)**
*   **Axes:** Y-axis is "CSI" (3.0 to 7.0), X-axis is "photon_flux".
*   **Content:** A line graph showing the Chemical Selection Index. 
*   **Trend:** CSI remains completely flat at ~3.45 for low to moderate UV levels (up to \(10^{14}\)). Above \(10^{14}\), CSI begins to climb exponentially. The rate of increase depends heavily on the quantum yield (qy): the highest sensitivity (qy=1e-02, green line) spikes earliest and highest, reaching nearly 7.0 at \(10^{18}\), while the lowest (qy=1e-04, blue line) stays lower, reaching just under 4.0.
*   **Key Takeaway:** High UV flux artificially inflates the CSI metric, especially if the assumed UV damage yield is high.

**2. Real vs UV (Middle Left)**
*   **Axes:** Y-axis is "Real" (0.85 to 1.40), X-axis is "photon_flux".
*   **Content:** A line graph showing the "real" (direct) selection multiplier.
*   **Trend:** Similar to the CSI panel, the "Real" multiplier is flat at ~0.89 below \(10^{14}\). Above this threshold, it rises sharply. The green line (qy=1e-02) reaches ~1.38, the orange line (qy=1e-03) reaches ~1.31, and the blue line (qy=1e-04) barely rises to 1.0.
*   **Key Takeaway:** Extremely high UV flux can force a direct selection effect (Real > 1.0), but only if the UV damage yield is significant.

**3. UV events vs UV (Middle Right)**
*   **Axes:** Y-axis is "UV damage events" (0 to 120,000+), X-axis is "photon_flux".
*   **Content:** A line graph showing the absolute number of damage events.
*   **Trend:** There are zero events below \(10^{14}\). Above this, the number of events skyrockets. The green line (qy=1e-02) generates over 120,000 events at \(10^{18}\), whereas the blue line (qy=1e-04) generates only ~20,000.
*   **Key Takeaway:** This panel confirms the mechanism: at high flux, the absolute number of UV damage events scales dramatically based on the assumed quantum yield.

**4. Yield vs UV (Far Right)**
*   **Axes:** Y-axis is "Final total DNA" (0 to 100,000+), X-axis is "photon_flux".
*   **Content:** A line graph showing total DNA yield.
*   **Trend:** Yield is steady at ~101,000 up to \(10^{14}\). Beyond that, UV radiation becomes lethal to the simulated system. The green line (qy=1e-02) crashes first (starting around \(10^{15}\)) and drops to near zero at \(10^{18}\). The orange line (qy=1e-03) crashes later, and the blue line (qy=1e-04) only drops to ~80,000 at the maximum flux.
*   **Key Takeaway:** High UV flux is destructive. If the UV damage yield is high (green), the system cannot survive high photon flux. If the yield is low (blue), the system is more robust but still suffers a yield penalty at extreme UV levels.

### **Summary Conclusion**
The system is highly **robust** to UV radiation up to a threshold of roughly **\(10^{14}\) photons/cm²/s**. Below this threshold, UV has no measurable impact on selection, composition, or yield. Above this threshold, the system's behavior is entirely dependent on the assumed quantum yield (qy) of UV damage. High UV flux acts to artificially inflate the selection metrics (CSI and Real) while simultaneously destroying the total yield.
