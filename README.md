
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Environment: 🐍 Python 3.8+

## Author: Seyed Mohammad Reza Hashemi (Reza Hashemi)

## ORCID: 0009-0002-0645-5180

## Overview
**UPDSF v6.7.0** is a mass-consistent, kinetically-consistent, provenance-tracked simulation framework testing whether **differential hydrolysis stability alone** can chemically filter **thymine (T) over uracil (U)** in dark, alkaline, high-temperature hydrothermal-vent conditions. The underlying v6.5.1 homopolymer engine (VSSUFEngine) is unchanged — all physics, kinetics, parameters, and existing output schemas are bit-identical at equal seeds. An opt-in **sequence-resolved copolymer / Darwinian layer** adds sequence resolution and heredity.

---

<br>
<br>

📂 **Critique: Robustness of the CSI to Uncertainty in the Uracil-to-Thymine Hydrolysis Rate Ratio**

The detailed Critique: Robustness of the CSI to Uncertainty in the Uracil-to-Thymine Hydrolysis Rate Ratio can be found in the 📄 [Robustness of the CSI to Uncertainty in the Uracil-to-Thymine Hydrolysis Rate Ratio](analysis/Robustness_of_the_CSI_to\-Uncertainty.md)

<br>
<br>

## Architecture & Compatibility

*   **Engine (Unchanged):** `VSSUFEngine` (v6.5.1, Section 6). Handles all thermodynamic and kinetic calculations: Arrhenius hydrolysis (polymer, clay, lipid channels), free-monomer hydrolysis and deamination, two-state UV lesion model, CSI decomposition.
*   **Layer (New, v6.7.0):** `SequenceEvolutionEngine` (Section 6c). Individuals are 100-residue sequences over {U, T, C, A, G} drawn from the feedstock influx ratios (INFLUX 45 T : 120 U residues/s). Viability uses the **same Arrhenius rates** as the homopolymer engine (k_U = 8.863×10⁻⁶/s, k_T = 2.483×10⁻⁸/s at 90 °C / pH 11, k_U/k_T ≈ 357×); a single residue hit is a chain scission and kills the individual.
*   **Schema Guarantee:** All existing `*.csv`, `*.json`, and plotting routines are unaffected. At equal seeds, every v6.6.1 number is reproduced bit-identically.
*   **Opt-In:** The sequence layer is opt-in by configuration, not a CLI flag: it is driven by `sequence_evolution_sweep()` (Section 6c), called in `main()` after the homopolymer sweeps, with a `config` dict (`generations`, `pop_size`, `seq_length`, `generation_hours`, `mutation_enabled`, `eq_mode`).

## What the Extension Adds

### 1. Sequence Resolution
The homopolymer abstraction treats all T-molecules (and all U-molecules) as interchangeable 100-residue single-base polymers. The sequence layer draws 100-residue copolymer individuals from the influx composition; each generation, every residue is destroyed independently (P(individual survives) = exp(−Σ_b n_b·k_b·τ)), so sequence composition — not order — determines survival, and every individual carries a full base composition.

### 2. Heredity & Darwinian Selection
Each generation (default 1 h, assumed):
1.  **Viability** — per-residue Arrhenius hydrolysis; any chain scission kills the individual.
2.  **Reproduction** — Wright–Fisher sampling of the next generation (default pop size N = 512) uniformly from survivors.
3.  **Mutation** — template-directed copying with per-position misincorporation that depends on the **template** base (T template: 0.01, U template: 0.05 — G–U wobble makes U templates less faithful); errors substitute a uniformly random other base. Default `mutation_enabled=True`; the `no_mutation` sweep variant disables it for deterministic clonal-heredity control.

### 3. New Output Schema (Sequence Layer)
*   `output_data_v670/sequence_evolution_v670_<timestamp>.csv` — per-seed rows: `variant`, `seed`, `pop_TU_frac`, `seq_TU_over_influx`, `mean_copy_fidelity`, `mean_nU`/`mean_nT`, selection differential, `extinct`, `generations_run`, `pop_alive`.
*   Derived metrics in the analysis JSON (under `sequence_evolution`): `darwinian_gain` (population T/(U+T) with replication ÷ chemistry-only survivor pool) and `control_corrected_seq_enrichment`.
*   In-terminal per-variant aggregates (mean ± CI95, copy fidelity, extinction fraction).

### Sweep Variants
`sequence_evolution_sweep()` runs five variants (default 10 seeds each, base seed 20,000):
| Variant | Replication | Mutation | Degradation |
|---|---|---|---|
| `baseline` | yes | yes | k_U/k_T ≈ 357× |
| `equal_degradation` | yes | yes | k_U = k_T |
| `chemistry_only` | no | — | k_U/k_T ≈ 357× |
| `equal_degradation_chemistry_only` | no | — | k_U = k_T |
| `no_mutation` | yes | no | k_U/k_T ≈ 357× |

Four dedicated self-checks run at startup: sequence determinism, clonal heredity with mutation off, exact k_U == k_T under the equal-degradation control, and the filtering direction (baseline > equal_degradation at matched seeds).

## Intended Use Cases
*   **Sequence-Dependent Chemistry:** How sequence composition (U-rich vs T-rich individuals) affects survival beyond bulk pool statistics.
*   **Darwinian Amplification:** Quantifying how much replication adds on top of the chemistry-built T-skew (`darwinian_gain`).
*   **Robustness:** Mapping homopolymer metrics (CSI, drift) onto sequence-level outcomes at matched seeds.

## Dependencies
NumPy, pandas, matplotlib (Agg backend). No other packages required.

---

## Key Result
At the model optimum (**90 °C, in-situ pH 11, 240 h, zero photon flux**), differential hydrolysis (k_U/k_T ≈ 357, extrapolated) raises DNA T/(U+T) from **0.67× influx** under a no-selection control to **2.02× influx** in the baseline — a **control-corrected enrichment of ≈3.0×**. This figure is immune to assumed influx stoichiometry and CSI normalization convention, as both arms share every assumption.

## Decisive Controls (7 arms × 20 seeds)
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
100-residue copolymers, Wright–Fisher reproduction (N = 512, generation time 1 h, assumed), template-dependent misincorporation (0.01 T-template / 0.05 U-template per residue, assumed). Replication **amplifies** the chemistry-built T-skew with a control-corrected gain of only **≈1.06×**. Without mutation the population freezes as a clone; without replication, populations go extinct (extinction fraction reported per variant in the sequence CSV).

## Robustness
- **Ea_T sweep (the "357× question"):** CSI 3.457–3.474 across Ea_T = 28–36 kcal/mol, even though k_U/k_T swings from 1,195× to 107×.
- **Time-horizon sweep:** Enrichment still rising at 240 h (3.46×), 1,000 h (5.10×), 2,400 h (6.49×), 10,000 h (10.16×). `optimum_is_horizon_edge` and `horizon_edge_warning` flag these optima; the horizon-edge optimum is reported as a lower bound.
- **UV robustness:** No effect up to ~10¹⁵ photons cm⁻² s⁻¹; at extreme fluxes "UV selection" is differential sterilization, not compositional filtering (see `flux_sweep`: 6 fluxes × 3 quantum yields).
- **Influx-stoichiometry sweep:** `influx_ratio_sweep` varies influx T (15–120 residues/s, U fixed at 120); absolute CSI scales with feedstock T-fraction, while the control-corrected metric cancels this dependence.

## Numerical Integrity
Every parameter carries an explicit `Source` with `kind` ∈ {literature, assumed, imposed, derived, extrapolated}; the exact counts are printed at runtime (`PROVENANCE COUNTS`; Section 5) and every sweep result is reproducible at fixed seeds. Mass balance closes to machine precision (max relative error reported per run; the consumed-identity residual is asserted < 10⁻⁹ in `_self_check_mass_identity`), and serial vs 4-worker parallel execution is bit-identical by `_self_check_parallel`.


## The v6.7.0 Finding

Under dark, alkaline hydrothermal-vent conditions (90 °C, in-situ pH 11, zero photon flux), **differential hydrolysis stability alone** chemically filters T over U. The result is a control-corrected enrichment of **≈3.0×** — measured against an equal-degradation control that, with no differential chemistry, actively **depletes** T (0.67× influx).

The filtering is **dual-channel**: it operates at both the **free-monomer** level (dominant) and the **polymer** level, acting in series. The single-channel hypothesis was **REFUTED**.

The opt-in Darwinian layer shows replication amplifies this chemistry-built skew by only **≈1.06×** (control-corrected). Without replication, populations go extinct.

---


---

## Citation

Reza Hashemi. (2026). Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0). Zenodo. https://doi.org/10.5281/zenodo.24331292

Reza Hashemi. (2026). mrhashemi2000/UPDSF_v6.7.0: Initial release [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.24328241

Reza Hashemi. (2026). Supplementary Information For: "Chemical Filtering of Thymine over Uracil by Differential Hydrolysis under Dark Alkaline Hydrothermal-Vent Conditions: A Mass-Consistent, Control-Restrained Simulation Framework (UPDSF v6.7.0)". Zenodo. https://doi.org/10.5281/zenodo.24331086
