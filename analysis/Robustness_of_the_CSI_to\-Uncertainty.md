[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24328241-blue)](https://doi.org/10.5281/zenodo.24328241) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331292-blue)](https://doi.org/10.5281/zenodo.24331292) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.24331086-blue)](https://doi.org/10.5281/zenodo.24331086) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
---

# Robustness of the CSI to Uncertainty in the Uracil-to-Thymine Hydrolysis Rate Ratio



## 1. Overview

This README documents a paired simulation analysis examining how the **CSI** responds to uncertainty in the uracil-to-thymine hydrolysis rate ratio, denoted here as `k_U / k_T`.

The analysis compares two simulation conditions at each tested kinetic setting:

- **Baseline:** the nominal, unequal uracil-to-thymine hydrolysis-rate setting.
- **Equal_control:** a control condition in which the rate ratio is set to 1, while the corresponding simulation setting is otherwise retained as defined by the simulation design.

The central question is whether the principal model response is strongly dependent on the precise value assigned to `k_U / k_T`, especially around the nominal value of approximately **357**.

The supplied summary results indicate that:

1. The paired Baseline response is consistently greater than the Equal_control response at all five tested settings.
2. The raw paired response ratio changes only modestly over the upper part of the tested range (106.6 to 1195), suggesting a near-plateau in that metric.
3. The survival-normalized paired ratio continues to increase somewhat over the same range; it should therefore not be described as completely insensitive.
4. The numerical mass-balance and consumed-identity diagnostics are very small.
5. The tested activation energy `Ea_T` changes together with the rate ratio. Consequently, these results do not isolate the independent causal effect of the rate ratio from the effect of `Ea_T` or other linked kinetic changes.

This is a **robustness analysis within the tested simulation design**. It is not, by itself, experimental validation of the kinetic ratio or proof that the model's chemical or biological assumptions are correct.

---

## 2. Scientific question and scope

### 2.1 Primary question

How much does the CSI-related comparison between Baseline and Equal_control change when the nominal uracil-to-thymine hydrolysis-rate ratio is varied across the tested range?

The tested nominal ratios are:

```
4.7, 10, 106.6, 357, 1195
```

The nominal value of particular interest is:

```
k_U / k_T ≈ 357
```

### 2.2 What this analysis can assess

The supplied results can be used to assess:

- consistency of the Baseline-versus-control difference across repeated paired simulations;
- the magnitude and uncertainty of the paired response ratio and paired response difference;
- whether the raw paired ratio appears to approach a plateau at higher tested rate ratios;
- whether survival normalization changes the interpretation;
- numerical consistency, as indicated by the supplied mass-balance and consumed-identity diagnostics.

### 2.3 What this analysis cannot establish on its own

The supplied summary table does not establish:

- that `k_U / k_T = 357` is the experimentally correct value;
- that the kinetic ratio has been measured directly;
- that the model is chemically or biologically validated;
- that the ratio has an independent effect separate from `Ea_T`;
- that the response is insensitive outside the tested range;
- that the same robustness holds for other model outputs, parameter combinations, simulation durations, or model structures.

---

## 3. Conditions and terminology

### 3.1 Baseline

Baseline denotes the unequal-rate simulation condition at each nominal target ratio. The actual ratio reported by the simulation is expected to correspond to the relevant nominal setting, subject to the simulation's implementation and control logic.

### 3.2 Equal_control

Equal_control denotes the control condition in which the uracil-to-thymine hydrolysis-rate ratio is set to 1. The table reports the control DNA-feed means and standard deviations, as well as control outcome summaries.

The interpretation of this condition depends on the implementation: it is a rate-equality control, not necessarily a control in which every other kinetic or model parameter is identical across all five rows.

### 3.3 Nominal target ratio

`nominal_target_ratio` is the target value used to label each tested kinetic setting. The five values are 4.7, 10, 106.6, 357, and 1195.

### 3.4 Activation energy

`Ea_T_kcal` is the reported activation energy for the thymine-associated process, in kcal/mol. Its value changes across the five tested settings:

| Nominal target ratio | Ea_T (kcal/mol) |
| -------------------- | --------------- |
| 4.7                  | 46.33322        |
| 10                   | 43.83397        |
| 106.6                | 36              |
| 357                  | 32              |
| 1195                 | 28              |

This co-variation is important for causal interpretation and is discussed in Section 10.

### 3.5 Paired comparisons

The table reports paired statistics for the Baseline and control simulations. The pairing should be interpreted according to the simulation's pairing protocol (for example, matched seeds or matched replicate identifiers). The supplied summary reports 10 pairs at each setting.

The paired statistics are:

- `paired_ratio_raw_*`: paired Baseline-to-control ratio for the raw response;
- `paired_diff_raw_*`: paired Baseline-minus-control difference for the raw response;
- `paired_ratio_persurv_*`: paired Baseline-to-control ratio for the survival-normalized response;
- `paired_diff_persurv_*`: paired Baseline-minus-control difference for the survival-normalized response.

The exact response field used to construct each paired metric should be confirmed against the analysis script or data dictionary before attempting an independent reimplementation. This README preserves the field names and reported values without assuming an undocumented formula.

---

## 4. Simulation design represented in the summary

The summary contains five kinetic settings. Each setting has 10 paired comparisons, giving 50 pairs in total across the five settings for each paired metric.

| Nominal target ratio | Ea_T (kcal/mol) | Number of raw pairs | Number of survival-normalized pairs |
| -------------------- | --------------- | ------------------- | ----------------------------------- |
| 4.7                  | 46.33322        | 10                  | 10                                  |
| 10                   | 43.83397        | 10                  | 10                                  |
| 106.6                | 36              | 10                  | 10                                  |
| 357                  | 32              | 10                  | 10                                  |
| 1195                 | 28              | 10                  | 10                                  |
| **Total**            | ---             | **50**              | **50**                              |

The raw simulation records described in the preceding analysis used a simulation duration of 240 hours and a time step of 60 seconds. These settings should be treated as metadata from those raw runs, and verified against the exact run configuration if this README is used as a formal reproducibility record.

---

## 5. Summary results

The numeric values below are transcribed from the supplied summary table. In the source table, `/` was used as the decimal separator; this README renders those values with decimal points.

### 5.1 Paired raw-response statistics

| Nominal ratio | Paired ratio mean | SD       | 95% CI lower | 95% CI upper | Paired difference mean | SD       | 95% CI lower | 95% CI upper | All pairs Baseline > control | n  |
| ------------- | ----------------- | -------- | ------------ | ------------ | ---------------------- | -------- | ------------ | ------------ | ---------------------------- | -- |
| 4.7           | 2.866228          | 0.028952 | 2.845518     | 2.886938     | 1.235993               | 0.013572 | 1.226285     | 1.245701     | TRUE                         | 10 |
| 10            | 2.963829          | 0.030931 | 2.941704     | 2.985954     | 1.301262               | 0.013266 | 1.291773     | 1.310752     | TRUE                         | 10 |
| 106.6         | 3.009173          | 0.020808 | 2.994289     | 3.024057     | 1.346915               | 0.007185 | 1.341776     | 1.352054     | TRUE                         | 10 |
| 357           | 3.034625          | 0.026694 | 3.015530     | 3.053720     | 1.356962               | 0.009429 | 1.350217     | 1.363707     | TRUE                         | 10 |
| 1195          | 3.044299          | 0.031803 | 3.021550     | 3.067048     | 1.360284               | 0.012737 | 1.351173     | 1.369395     | TRUE                         | 10 |

### 5.2 Paired survival-normalized statistics

| Nominal ratio | Paired ratio mean | SD       | 95% CI lower | 95% CI upper | Paired difference mean | SD       | 95% CI lower | 95% CI upper | All pairs Baseline > control | n  |
| ------------- | ----------------- | -------- | ------------ | ------------ | ---------------------- | -------- | ------------ | ------------ | ---------------------------- | -- |
| 4.7           | 2.942054          | 0.039022 | 2.914140     | 2.969967     | 1.617856               | 0.024873 | 1.600064     | 1.635648     | TRUE                         | 10 |
| 10            | 3.170329          | 0.037664 | 3.143388     | 3.197271     | 1.707881               | 0.023191 | 1.691292     | 1.724469     | TRUE                         | 10 |
| 106.6         | 3.497430          | 0.029242 | 3.476513     | 3.518348     | 1.804241               | 0.016380 | 1.792524     | 1.815957     | TRUE                         | 10 |
| 357           | 3.594214          | 0.036129 | 3.568371     | 3.620057     | 1.826506               | 0.015593 | 1.815353     | 1.837660     | TRUE                         | 10 |
| 1195          | 3.656072          | 0.046731 | 3.622645     | 3.689500     | 1.846540               | 0.022689 | 1.830310     | 1.862770     | TRUE                         | 10 |

### 5.3 Descriptive outcome and numerical-diagnostic summaries

| Nominal ratio | Baseline DNA feed mean | Baseline DNA feed SD | Control DNA feed mean | Control DNA feed SD | Baseline DNA T fraction mean | Control DNA T fraction mean | Baseline DNA free ratio mean | Control DNA free ratio mean | Baseline survival mean | Control survival mean |
| ------------- | ---------------------- | -------------------- | --------------------- | ------------------- | ---------------------------- | --------------------------- | ---------------------------- | --------------------------- | ---------------------- | --------------------- |
| 4.7           | 1.898336               | 0.011641             | 0.662343              | 0.004221            | 0.517728                     | 0.180639                    | 0.835984                     | 0.943153                    | 0.774540               | 0.795000              |
| 10            | 1.963935               | 0.010603             | 0.662672              | 0.004571            | 0.535619                     | 0.180729                    | 0.864967                     | 0.943672                    | 0.787230               | 0.842050              |
| 106.6         | 2.017333               | 0.005500             | 0.670418              | 0.004090            | 0.550182                     | 0.182841                    | 0.888498                     | 0.954884                    | 0.798430               | 0.927960              |
| 357           | 2.023951               | 0.007142             | 0.666989              | 0.004987            | 0.551987                     | 0.181906                    | 0.891189                     | 0.949787                    | 0.799790               | 0.947260              |
| 1195          | 2.025753               | 0.009848             | 0.665469              | 0.005128            | 0.552478                     | 0.181491                    | 0.891765                     | 0.947513                    | 0.796990               | 0.957120              |

| Nominal ratio | Baseline total DNA mean | Control total DNA mean | Maximum mass-balance error | Maximum consumed-identity residual |
| ------------- | ----------------------- | ---------------------- | -------------------------- | ---------------------------------- |
| 4.7           | 98057.1                 | 100730.8               | 1.03e-14                   | 0                                  |
| 10            | 99739.6                 | 106621.5               | 9.64e-15                   | 0                                  |
| 106.6         | 101195.3                | 117708.9               | 1.04e-14                   | 0                                  |
| 357           | 101145.2                | 120195.7               | 9.59e-15                   | 0                                  |
| 1195          | 101279.5                | 121333.4               | 8.89e-15                   | 0                                  |

**Important:** `DNA_T_fraction_mean`, `DNA_free_ratio_mean`, and the paired-response fields are retained under the names supplied. Their precise operational definitions should be taken from the simulation code or original data dictionary. Do not infer a formula from the column name alone.

---

## 6. Main findings

### 6.1 Baseline exceeds Equal_control in every reported pair

At every tested nominal ratio:

- `all_pairs_baseline_greater_raw` is `TRUE`;
- `all_pairs_baseline_greater_persurv` is `TRUE`;
- each paired analysis has n = 10.

Thus, in the 10 paired replicates at each setting, the Baseline value exceeds the corresponding control value for both the raw and survival-normalized paired outcomes.

This is a strong consistency pattern within the simulated pairs. It should not be described as proof of universal dominance beyond the tested simulation conditions.

### 6.2 The raw paired ratio approaches a plateau

The raw paired ratio means are:

```
2.8662, 2.9638, 3.0092, 3.0346, 3.0443
```

The change between the 106.6 and 1195 settings is:

```
3.044299 - 3.009173 = 0.035126
```

Relative to the value at 106.6, this is approximately a 1.17% increase. Over this interval, the nominal ratio increases by more than eleven-fold, while the raw paired ratio changes only slightly.

This pattern is consistent with a near-plateau in the **raw paired ratio** over the upper tested range. It does not prove that the response is mathematically saturated, nor does it establish the location of a precise saturation threshold.

### 6.3 The survival-normalized paired ratio retains a modest upward trend

The survival-normalized paired ratio means are:

```
2.9421, 3.1703, 3.4974, 3.5942, 3.6561
```

Between 106.6 and 1195, the increase is:

```
3.656072 - 3.497430 = 0.158642
```

or approximately 4.54% relative to the value at 106.6.

The survival-normalized metric therefore appears less flat than the raw paired ratio in the upper range. The appropriate interpretation is **reduced sensitivity with a residual trend**, not complete invariance.

### 6.4 The nominal value 357 is not an isolated discontinuity

At 357, the raw paired ratio mean is 3.034625, compared with 3.009173 at 106.6 and 3.044299 at 1195. The value at 357 lies between its neighboring tested settings and follows the overall gradual trend.

The supplied table therefore gives no indication of a sharp anomaly at 357. However, because only five discrete settings were tested, it cannot rule out local nonlinear behavior between them.

---

## 7. Interpretation of paired confidence intervals

The supplied 95% confidence intervals are narrow relative to the corresponding means.

For the raw paired ratio at the nominal ratio 357:

```
mean(R_raw) = 3.034625
95% CI: [3.015530, 3.053720]
```

For the survival-normalized paired ratio at the same setting:

```
mean(R_persurv) = 3.594214
95% CI: [3.568371, 3.620057]
```

For the raw paired difference at 357:

```
mean(D_raw) = 1.356962
95% CI: [1.350217, 1.363707]
```

For the survival-normalized paired difference:

```
mean(D_persurv) = 1.826506
95% CI: [1.815353, 1.837660]
```

These intervals quantify uncertainty in the reported paired means under the assumptions of the method used to calculate them. The exact confidence-interval procedure (for example, a paired-t interval or a bootstrap interval) is not specified in the supplied summary. The method should be documented in the analysis code or methods section before publication.

A ratio confidence interval should be compared with 1 when evaluating equality of the paired responses. A difference confidence interval should be compared with 0. The intervals shown here are above those respective null values.

---

## 8. Survival and DNA-feed context

The survival summaries show that the two conditions do not have the same survival profile, particularly at the higher nominal ratios.

| Nominal ratio | Baseline survival | Control survival | Control minus Baseline |
| ------------- | ----------------- | ---------------- | ---------------------- |
| 4.7           | 0.774540          | 0.795000         | 0.020460               |
| 10            | 0.787230          | 0.842050         | 0.054820               |
| 106.6         | 0.798430          | 0.927960         | 0.129530               |
| 357           | 0.799790          | 0.947260         | 0.147470               |
| 1195          | 0.796990          | 0.957120         | 0.160130               |

Control survival rises across the tested settings, while Baseline survival remains close to 0.8. This difference matters when interpreting total or raw DNA outcomes.

The paired survival-normalized ratio is higher than the raw paired ratio at every setting. This is consistent with survival normalization materially changing the comparison. It is not appropriate to treat the raw and normalized metrics as interchangeable.

The DNA-feed means also differ between Baseline and control. For example, at the nominal ratio 357, the reported means are 2.023951 for Baseline and 0.666989 for control. The feed conditions are therefore not numerically equal in the supplied summary. Interpretation of the paired outcome must retain the simulation's feed definition and normalization protocol.

---

## 9. Numerical consistency and mass balance

The maximum reported mass-balance errors range from approximately:

```
8.89e-15 to 1.04e-14
```

The maximum consumed-identity residual is zero at every tested setting.

These values indicate very small numerical residuals for the two reported diagnostics. They support the conclusion that the simulation outputs satisfy the implemented numerical accounting identities to high precision.

They do **not** demonstrate that:

- the reaction network is complete;
- the kinetic constants are experimentally correct;
- the model's biological interpretation is valid;
- the simulation is free of structural or conceptual bias.

Numerical verification and scientific validation are distinct tasks and should be reported separately.

---

## 10. Important confounding and design limitation

The activation energy `Ea_T` changes systematically as the nominal rate ratio changes:

| Nominal ratio | Ea_T (kcal/mol) |
| ------------- | --------------- |
| 4.7           | 46.33322        |
| 10            | 43.83397        |
| 106.6         | 36              |
| 357           | 32              |
| 1195          | 28              |

Because the two quantities co-vary, a trend across the five rows cannot be attributed uniquely to `k_U / k_T`.

The Equal_control condition is informative because the ratio is set to 1 within each setting, but the control outcomes themselves also vary across rows. For example, the control survival mean rises from 0.795000 to 0.957120. This indicates that other setting-dependent features remain relevant to the overall outcome.



---

## 11. Conclusions

The supplied paired simulation summary supports four main conclusions:

1. **Persistent contrast:** Baseline exceeds Equal_control in all 10 reported pairs at each of the five tested nominal ratios, for both raw and survival-normalized paired outcomes.
2. **Raw-response robustness at high ratios:** The raw paired ratio changes only slightly between nominal ratios 106.6 and 1195, consistent with a near-plateau in that range.
3. **Residual normalized trend:** The survival-normalized paired ratio continues to increase modestly over the same interval, so complete insensitivity should not be claimed.
4. **Interpretive limitation:** Since `Ea_T` co-varies with the nominal ratio, the present comparison does not isolate the independent effect of `k_U / k_T`.

For the nominal setting `k_U / k_T ≈ 357`, the raw paired ratio is 3.034625 (95% CI 3.015530–3.053720), and the survival-normalized paired ratio is 3.594214 (95% CI 3.568371–3.620057). These estimates are internally consistent across the 10 paired simulations reported for that setting.

**Overall conclusion:** The results support robustness of the raw CSI-related paired comparison to uncertainty in the precise value of the uracil-to-thymine hydrolysis-rate ratio across the upper tested range. They support treating 357 as a non-critical exact value for that particular raw response, while retaining the distinction between robustness to the precise parameter value and the continued importance of the unequal-rate condition itself.

---

