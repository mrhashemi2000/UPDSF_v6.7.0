[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Environment: 🐍 Python 3.8+

## Author: Seyed Mohammad Reza Hashemi (Reza Hashemi)

## ORCID: 0009-0002-0645-5180

## Overview
**UPDSF v6.7.0** is a mass-consistent, kinetically-consistent, provenance-tracked simulation framework testing whether **differential hydrolysis stability alone** can chemically filter **thymine (T) over uracil (U)** in dark, alkaline, high-temperature hydrothermal-vent conditions. The underlying v6.5.1 homopolymer engine (VSSUFEngine) is unchanged — all physics, kinetics, parameters, and existing output schemas are bit-identical at equal seeds. An opt-in **copolymer / Darwinian layer** adds sequence resolution and heredity.

# UPDSF v6.7.0 — Copolymer & Darwinian Extension

## Release Summary
**UPDSF v6.7.0** is an opt-in extension to the UPDSF framework. The underlying **v6.5.1 homopolymer engine (VSSUFEngine)** is entirely unchanged: all physics, kinetics, parameters, and existing output schemas remain bit-identical to previous releases (equal seeds reproduce every v6.6.1 number exactly).

The v6.7.0 release adds an **opt-in copolymer / Darwinian layer** that addresses two structural weaknesses of the homopolymer abstraction:
1. **No sequence** — the homopolymer engine tracks nucleotide *counts* (e.g., 30,000 T + 18,000 U), but not their order.
2. **No heredity** — the homopolymer engine tracks the *population* of polymers as a single statistical pool, with no mechanism for a specific polymer's success to depend on its own sequence.

## Architecture & Compatibility
*   **Engine (Unchanged):** `VSSUFEngine` (v6.5.1). Handles all thermodynamic and kinetic calculations (hydrolysis, UV damage, drift, CSI decomposition, etc.).
*   **Layer (New):** `CopolymerLayer` (v6.7.0). Wraps the engine, adding sequence-resolved polymer tracking and selection dynamics.
*   **Schema Guarantee:** All existing `*.csv`, `*.json`, and dashboard plotting routines are unaffected. Legacy runs require no changes.
*   **Opt-In:** The copolymer layer is activated via a single flag: `--enable-copolymer` (default: `false`).

# What the Extension Adds

### 1. Sequence Resolution
The homopolymer abstraction treats all T-molecules as interchangeable and all U-molecules as interchangeable. The copolymer layer assigns each polymer a specific sequence of nucleotides (e.g., `T-U-T-T-U`). This allows the model to track:
*   Local sequence features (e.g., runs of T vs. alternating T/U).
*   Sequence-dependent hydrolysis and damage susceptibility (via a pluggable `SequenceEffect` interface).
*   Sequence fingerprints in the output schemas (e.g., `sequence_string`, `GC_content`, etc.).

### 2. Heredity & Darwinian Selection
The homopolymer engine models population growth as a bulk rate (`net_population_growth`). The copolymer layer introduces **per-sequence differential survival and replication**:
*   Each distinct sequence has its own fitness, derived from its chemical stability (from the engine) and its sequence-dependent growth rate.
*   Successive generations inherit the parent sequence (with a configurable mutation rate, defaulting to 0 for deterministic runs).
*   This creates a Darwinian selection loop: sequences that are more stable or replicate faster will dominate the population over time.

### 3. New Output Schema (Copolymer Mode Only)
When `--enable-copolymer` is set, the following additional outputs are generated:
*   `sequence_table.csv`: Top-N most abundant sequences, their counts, and their derived fitness.
*   `sequence_diversity.png`: A plot tracking sequence diversity over time.
*   `fitness_landscape.png`: A heatmap of sequence fitness (if a sweep is run).
*   `heredity_trace.json`: A detailed log of mutations, replication events, and lineage branching.

## Intended Use Cases
*   **Sequence-Dependent Chemistry:** Studying how the order of T and U affects the stability of the polymer, beyond bulk composition.
*   **Darwinian Evolution of Polymers:** Modeling the emergence of a "fittest" sequence over long horizons (e.g., the 2400h runs), simulating the transition from a chemical pool to a genetic sequence.
*   **Bridging the Gap:** Exploring how the homopolymer metrics (CSI, drift) map onto sequence-level outcomes (e.g., does a high CSI always correlate with a specific winning sequence?).

## Migration Guide from v6.6.1
1.  **No changes required** for homopolymer runs. Simply upgrade the binary/package; all existing scripts and dashboards will function identically.
2.  **To enable the new layer:** Add `--enable-copolymer` to your command-line arguments.
3.  **New dependencies:** The copolymer layer requires `biopython` (for sequence handling) and `seaborn` (for the diversity plots).
4.  **Dashboard compatibility:** The existing dashboards (e.g., *CSI trajectory*, *Decomposed controls*) remain valid. To visualize the new outputs, use the provided `plot_copolymer_dashboard.py` script.

## Key Result
At the model optimum (**90 °C, in-situ pH 11, 240 h, zero photon flux**), differential hydrolysis (k_U/k_T ≈ 357) raises DNA T/(U+T) from **0.67× influx** under a no-selection control to **2.02× influx** in the baseline — a **control-corrected enrichment of ≈3.0×**. This figure is immune to assumed influx stoichiometry and CSI normalization convention, as both arms share every assumption.

## Decisive Controls (7 arms × 20 seeds, pre-registered)
| Control arm | DNA T/(U+T) | CSI |
|---|---|---|
| baseline | 0.551 | 3.465 |
| equal_polymer_only_gm | 0.371 | 2.827 |
| equal_free_only_gm | 0.299 | 2.463 |
| equal_degradation_gm | 0.183 | 1.804 |
| equal_degradation_kT | 0.184 | 1.893 |
| equal_pools | 0.726 | 5.492 |
| no_compartments | 0.853 | 4.853 |

### Verdict: REFUTED for the claim "free-pool hydrolysis drives the enrichment." Chemical filtering acts at **both monomer and polymer levels** (free-monomer channel dominant under assumed free-hydrolysis scale). Suppressing both channels eliminates enrichment (CSI 1.80; DNA T/(U+T) below feedstock).

## Darwinian Layer (v6.7.0, opt-in)
100-residue copolymers, Wright–Fisher reproduction (N=512), template-dependent misincorporation. Replication **amplifies** the chemistry-built T-skew with a control-corrected gain of only **≈1.06×**. Without mutation, the population freezes as a clone (0.39 pop T/(U+T)); without replication, extinction in 10/10 seeds.

## Robustness
- **Ea_T sweep (the "357× question"):** CSI 3.457–3.474 across Ea_T = 28–36 kcal/mol, even though k_U/k_T swings from 1,195× to 107×.
- **Time-horizon sweep:** Enrichment still rising at 240 h (3.46×), 1,000 h (5.10×), 2,400 h (6.49×), 10,000 h (10.16×) as survival decays to 0.32. Horizon-edge optimum reported as lower bound.
- **UV robustness:** No effect up to ~10¹⁵ photons cm⁻² s⁻¹; "UV selection" at extreme fluxes is differential sterilization, not compositional filtering.
- **Influx-stoichiometry sweep:** Absolute CSI scales with feedstock T-fraction; control-corrected metric cancels this dependence.

## Numerical Integrity
All parameters carry explicit provenance (47 literature, 44 assumed, 15 imposed, 3 derived, 1 extrapolated). Mass balance closes to **max relative error 5.7 × 10⁻¹⁵** across a 572-cell sensitivity grid, with **exactly zero** consumed-identity residuals. Deterministic at fixed seeds; bit-identical serial vs. 4-worker parallel execution.

# A Computational Theoretical Refutation of the RNA World Hypothesis

**A brief based on UPDSF v6.7.0 — Chemical Filtering of Thymine over Uracil**

---

## The RNA World Hypothesis (RWH)

The RNA World Hypothesis posits that life began with a self-replicating RNA molecule. Its implicit sequence of events:

1. A prebiotic pool contains activated ribonucleotides (A, **U**, G, C).
2. These monomers polymerize into RNA oligomers.
3. RNA replicates with errors, generating variation.
4. Darwinian selection acts on replicating populations, and order emerges from chemistry.

The RWH treats prebiotic chemistry as a **neutral stage** — a U-rich feedstock that is simply *available* — with selection emerging only at the level of replication.

---

## The v6.7.0 Finding

Under dark, alkaline hydrothermal-vent conditions (90 °C, in-situ pH 11, zero photon flux), **differential hydrolysis stability alone** chemically filters T over U. The result is a control-corrected enrichment of **≈3.0×** — measured against an equal-degradation control that, with no differential chemistry, actively **depletes** T (0.67× influx).

The filtering is **dual-channel**: it operates at both the **free-monomer** level (dominant, ≈68% of the enrichment gap) and the **polymer** level (≈49%), acting in series. The pre-registered single-channel hypothesis was **REFUTED**.

The opt-in Darwinian layer shows replication amplifies this chemistry-built skew by only **≈1.06×** (control-corrected). Without replication, populations go extinct in 10/10 seeds.

---

## The Computational Theoretical Refutation, in Four Points

**1. The RWH's feedstock cannot persist.**
The RWH requires a U-rich pool. Under vent conditions the free pool drifts from 0.273 to **0.620 T/(U+T)** — a 2.27× enrichment of T over U — *before any polymerization occurs*. The environment the RWH depends on is actively destroying the U it needs.

**2. The RWH assumes neutral chemistry. The chemistry is already a filter.**
The RWH treats prebiotic chemistry as a passive backdrop. The v6.7.0 controls show the monomer-level filter dominates, and that polymer-level selection is secondary. Selection begins **before** replication — at the level of the molecule itself.

**3. The RWH's central mechanism is only a marginal amplifier.**
The RWH claims replication and selection **create** order. The data show they **preserve and weakly amplify** an order chemistry has already built (≈1.06×). Replication is necessary for persistence, but it is not the creator of the T-skew.

**4. The RWH's implicit selection model is refuted.**
The RWH implicitly assumes a single-channel, polymer-centric selection (T-DNA is more stable than U-RNA). The pre-registered control sweep **REFUTES** this. Both channels are required; neither alone suffices.

---

## The Counter-Frame: The Matter World Hypothesis (MWH)

The v6.7.0 computational theoretical results are consistent with — and support — the **Matter World Hypothesis**:

- **Selection is a material property.** Differential stability is not a mechanism that *emerges* at the polymer level; it is a fundamental property of the molecules, operating wherever they exist (free pool, clay, lipid, polymer).
- **The environment is the selector.** The vent does not *permit* RNA and then select among variants. It actively filters the monomer pool, enriching T and depleting U, before polymerization.
- **Genetic machinery is a latecomer.** Replication, when it appears, is a marginal amplifier of a chemistry-built skew, not its creator.

> **The RWH assumes chemistry is the stage and selection is the play.**
> **The v6.7.0 framework shows chemistry is the playwright, and selection is a bit player.**

---

## Conclusion

The v6.7.0 framework constitutes a **theoretical refutation of the RNA World Hypothesis**:

- The RWH requires a U-rich feedstock that the MWH-consistent chemistry preferentially destroys.
- The RWH assumes neutral chemistry that is, in fact, already selective.
- The RWH requires Darwinian selection to create order, but the data show it only amplifies a pre-existing chemical order.
- The RWH's implicit single-channel selection model is pre-registered and **REFUTED**.

**Chemistry precedes and constrains the Genetic World.** The path to T-rich DNA does not run through a U-rich RNA world; it runs through a dark, alkaline vent that filters matter before any gene exists.

---

## Citation

Reza Hashemi. (2026). Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0). Zenodo. https://doi.org/10.5281/zenodo.24331292

Reza Hashemi. (2026). mrhashemi2000/UPDSF_v6.7.0: Initial release [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.24328241

Reza Hashemi. (2026). Supplementary Information For: "Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0)". Zenodo. https://doi.org/10.5281/zenodo.24331086
