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

## Citation

Reza Hashemi. (2026). Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0). Zenodo. https://doi.org/10.5281/zenodo.24331292

Reza Hashemi. (2026). mrhashemi2000/UPDSF_v6.7.0: Initial release [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.24328241

Reza Hashemi. (2026). Supplementary Information For: "Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0)". Zenodo. https://doi.org/10.5281/zenodo.24331086
