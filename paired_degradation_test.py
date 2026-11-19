from pathlib import Path
import importlib.util
import sys
import math
import time
import traceback

import numpy as np
import pandas as pd


# ============================================================
# 1. LOAD THE MODEL
# ============================================================

MODEL_FILE = Path(__file__).with_name("UPDSF_v6.7.0.py")

if not MODEL_FILE.exists():
    raise FileNotFoundError(
        f"Model file not found: {MODEL_FILE}\n"
        "Place this script beside UPDSF_v6.7.0.py"
    )

spec = importlib.util.spec_from_file_location(
    "updsf_v670", MODEL_FILE
)
UPDSF = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = UPDSF
spec.loader.exec_module(UPDSF)

VSSUFEngine = UPDSF.VSSUFEngine


# ============================================================
# 2. EXPERIMENT SETTINGS
# ============================================================

TEMPERATURE_C = 90.0
PH = 11.0
SIMULATION_HOURS = 240.0

DT_SECONDS = 60.0
RECORD_INTERVAL_SECONDS = 600.0

POLYMER_LENGTH = 100
LIPID_CONC = 0.05
PHOTON_FLUX = 0.0
FREE_HYDRO_SCALE = 1.0

N_REPLICATES = 10
BASE_SEED = 20261119

# Two-sided 95% t critical values, df = n - 1.
# Used for paired-ratio confidence intervals.
T_CRIT_95 = {
    2: 12.706, 3: 4.303, 4: 3.182, 5: 2.776,
    6: 2.571, 7: 2.447, 8: 2.365, 9: 2.306,
    10: 2.262, 11: 2.228, 12: 2.201, 15: 2.145,
    20: 2.093, 25: 2.064, 30: 2.045,
}

if N_REPLICATES not in T_CRIT_95:
    raise ValueError(
        f"N_REPLICATES={N_REPLICATES} has no t-critical entry. "
        f"Add it to T_CRIT_95."
    )

T_CRITICAL = T_CRIT_95[N_REPLICATES]

# Target U/T degradation ratios and corresponding Ea_T.
EA_CASES = [
    (4.7,    46.3332212987),
    (10.0,   43.8339701484),
    (106.6,  36.0),
    (357.0,  32.0),
    (1195.0, 28.0),
]

CONTROL_MODE = "geometric_mean"

OUTPUT_RAW = "paired_dt60_raw.csv"
OUTPUT_SUMMARY = "paired_dt60_summary.csv"
OUTPUT_CONVERGENCE = "paired_dt_convergence.csv"

# Previous run's summary, used for the dt-convergence comparison.
# Set to None to skip the comparison.
PREVIOUS_SUMMARY = "paired_degradation_summary.csv"

# Metrics analysed as paired baseline/control ratios.
PAIRED_METRICS = [
    ("DNA_T_over_influx_T", "raw"),
    ("DNA_T_over_influx_T_per_survival", "persurv"),
]


# ============================================================
# 3. ENGINE CONSTRUCTION
# ============================================================

def create_engine(ea_T, seed):

    return VSSUFEngine(
        temperature_C=TEMPERATURE_C,
        pH_in_situ=PH,
        seed=int(seed),
        max_time_hours=SIMULATION_HOURS,
        verbose=False,

        photon_flux=PHOTON_FLUX,
        polymer_length=POLYMER_LENGTH,
        lipid_conc=LIPID_CONC,

        record_interval_seconds=RECORD_INTERVAL_SECONDS,
        dt=DT_SECONDS,

        free_hydro_scale=FREE_HYDRO_SCALE,
        ea_T_kcal_override=float(ea_T),
    )


# ============================================================
# 4. EXTRACT METRICS
# ============================================================

def extract_metrics(eng):

    survival = float(eng.get_final_survival_fraction())

    dna_feed = float(eng.get_dna_TU_over_influx())

    dna_feed_per_survival = (
        dna_feed / survival if survival > 0 else float("nan")
    )

    return {
        "DNA_T_fraction_TU":
            float(eng.get_dna_TU_fraction()),

        "DNA_T_over_influx_T":
            dna_feed,

        "DNA_T_over_influx_T_per_survival":
            dna_feed_per_survival,

        "CSI":
            float(eng.get_chemical_selection_index()),

        "DNA_TU_over_free_TU":
            float(eng.get_dna_TU_over_free_TU()),

        "free_T_fraction_TU":
            float(eng.get_free_TU_ratio()),

        "pool_drift_factor":
            float(eng.get_pool_drift_factor()),

        "total_DNA":
            int(eng.total_dna()),

        "final_survival":
            survival,

        "mass_balance_rel_error":
            float(eng.max_abs_rel_error()),

        "consumed_identity_residual":
            float(eng.max_abs_consumed_residual()),

        "hydrolysis_events":
            int(eng.hydrolysis_events),

        "free_hydrolysis_events":
            int(eng.free_hydrolysis_events),
    }


# ============================================================
# 5. RUN ONE SIMULATION
# ============================================================

def run_one(ea_T, seed, condition):

    eng = create_engine(ea_T, seed)

    k_u_before = float(eng.k_hydro["U"])
    k_t_before = float(eng.k_hydro["T"])

    ratio_before = (
        k_u_before / k_t_before
        if k_t_before > 0 else float("inf")
    )

    if condition == "equal_control":
        eng._apply_equal_degradation_control(mode=CONTROL_MODE)
    elif condition != "baseline":
        raise ValueError(f"Unknown condition: {condition}")

    k_u_after = float(eng.k_hydro["U"])
    k_t_after = float(eng.k_hydro["T"])

    ratio_after = (
        k_u_after / k_t_after
        if k_t_after > 0 else float("inf")
    )

    eng.run()

    result = extract_metrics(eng)

    result.update({
        "seed": int(seed),
        "condition": condition,
        "Ea_T_kcal": float(ea_T),
        "actual_kU_kT_before_control": ratio_before,
        "actual_kU_kT": ratio_after,
        "dt_seconds": DT_SECONDS,
        "simulation_hours": SIMULATION_HOURS,
    })

    return result


# ============================================================
# 6. PAIRED STATISTICS FOR ONE METRIC
# ============================================================

def paired_stats(base_values, control_values, metric_tag):

    base_values = np.asarray(base_values, dtype=float)
    control_values = np.asarray(control_values, dtype=float)

    differences = base_values - control_values

    ratios = np.divide(
        base_values,
        control_values,
        out=np.full_like(base_values, np.nan),
        where=control_values != 0,
    )

    finite = np.isfinite(ratios)

    if not np.all(finite):
        raise RuntimeError(
            f"Non-finite paired ratio for metric '{metric_tag}': "
            f"{ratios}"
        )

    n = int(finite.sum())
    if n < 2:
        raise RuntimeError(
            f"Need >=2 pairs for metric '{metric_tag}', got {n}"
        )

    mean_ratio = float(np.mean(ratios))
    sd_ratio = float(np.std(ratios, ddof=1))
    se_ratio = sd_ratio / math.sqrt(n)

    mean_diff = float(np.mean(differences))
    sd_diff = float(np.std(differences, ddof=1))
    se_diff = sd_diff / math.sqrt(n)

    return {
        f"paired_ratio_{metric_tag}_mean": mean_ratio,
        f"paired_ratio_{metric_tag}_sd": sd_ratio,
        f"paired_ratio_{metric_tag}_CI95_low":
            mean_ratio - T_CRITICAL * se_ratio,
        f"paired_ratio_{metric_tag}_CI95_high":
            mean_ratio + T_CRITICAL * se_ratio,
        f"paired_diff_{metric_tag}_mean": mean_diff,
        f"paired_diff_{metric_tag}_sd": sd_diff,
        f"paired_diff_{metric_tag}_CI95_low":
            mean_diff - T_CRITICAL * se_diff,
        f"paired_diff_{metric_tag}_CI95_high":
            mean_diff + T_CRITICAL * se_diff,
        f"all_pairs_baseline_greater_{metric_tag}":
            bool(np.all(differences > 0)),
        f"n_pairs_{metric_tag}": n,
    }


# ============================================================
# 7. RUN PAIRED EXPERIMENTS
# ============================================================

def main():

    all_rows = []

    total_runs = len(EA_CASES) * N_REPLICATES * 2

    completed = 0
    start_time = time.time()

    print("=" * 70)
    print("UPDSF v6.7.0 - PAIRED DEGRADATION TEST")
    print("=" * 70)

    print(f"Temperature: {TEMPERATURE_C} C")
    print(f"pH: {PH}")
    print(f"Duration: {SIMULATION_HOURS} hours")
    print(f"Time step: {DT_SECONDS} seconds")
    print(f"Replicates per condition: {N_REPLICATES}")
    print(f"Total simulations: {total_runs}")
    print(f"t critical (95%, df={N_REPLICATES - 1}): {T_CRITICAL}")
    print("=" * 70)

    for nominal_ratio, ea_T in EA_CASES:

        print(
            f"\nTarget U/T ratio = {nominal_ratio:g} "
            f"| Ea_T = {ea_T:.4f} kcal/mol"
        )

        for replicate in range(N_REPLICATES):

            seed = BASE_SEED + replicate
            pair_results = []

            for condition in ("baseline", "equal_control"):

                completed += 1

                print(
                    f"[{completed}/{total_runs}] "
                    f"ratio={nominal_ratio:g}, "
                    f"seed={seed}, "
                    f"condition={condition}",
                    flush=True
                )

                t0 = time.time()
                result = run_one(
                    ea_T=ea_T,
                    seed=seed,
                    condition=condition,
                )
                elapsed_one = time.time() - t0

                result["nominal_target_ratio"] = nominal_ratio

                all_rows.append(result)
                pair_results.append(result)

                # Checkpoint after every simulation.
                pd.DataFrame(all_rows).to_csv(
                    OUTPUT_RAW, index=False
                )

                remaining = total_runs - completed
                eta_min = remaining * elapsed_one / 60.0

                print(
                    "    DNA/feed = "
                    f"{result['DNA_T_over_influx_T']:.5f} | "
                    "DNA T fraction = "
                    f"{result['DNA_T_fraction_TU']:.5f} | "
                    "survival = "
                    f"{result['final_survival']:.5f} | "
                    "mass error = "
                    f"{result['mass_balance_rel_error']:.2e}"
                )
                print(
                    f"    [{elapsed_one:.1f}s, "
                    f"~{eta_min:.1f} min remaining]",
                    flush=True
                )

            # Paired guards.
            assert (
                pair_results[0]["seed"] == pair_results[1]["seed"]
            )

            control_ratio = pair_results[1]["actual_kU_kT"]
            if not math.isclose(
                control_ratio, 1.0,
                rel_tol=1e-9, abs_tol=1e-12
            ):
                raise RuntimeError(
                    "Equal-degradation control failed: "
                    f"kU/kT = {control_ratio}"
                )

    # ========================================================
    # 8. CREATE PAIRED SUMMARY
    # ========================================================

    df = pd.DataFrame(all_rows)
    summary_rows = []

    for nominal_ratio, ea_T in EA_CASES:

        subset = df[
            df["nominal_target_ratio"] == nominal_ratio
        ]

        base = (
            subset[subset["condition"] == "baseline"]
            .sort_values("seed")
            .reset_index(drop=True)
        )
        control = (
            subset[subset["condition"] == "equal_control"]
            .sort_values("seed")
            .reset_index(drop=True)
        )

        if len(base) != N_REPLICATES:
            raise RuntimeError(
                f"Incorrect baseline replicate count "
                f"for ratio {nominal_ratio}: {len(base)}"
            )
        if len(control) != N_REPLICATES:
            raise RuntimeError(
                f"Incorrect control replicate count "
                f"for ratio {nominal_ratio}: {len(control)}"
            )

        if not np.array_equal(
            base["seed"].to_numpy(),
            control["seed"].to_numpy()
        ):
            raise RuntimeError(
                f"Paired seeds do not match for ratio "
                f"{nominal_ratio}"
            )

        row = {
            "nominal_target_ratio": nominal_ratio,
            "Ea_T_kcal": ea_T,

            "baseline_DNA_feed_mean":
                float(base["DNA_T_over_influx_T"].mean()),
            "baseline_DNA_feed_sd":
                float(base["DNA_T_over_influx_T"].std(ddof=1)),
            "control_DNA_feed_mean":
                float(control["DNA_T_over_influx_T"].mean()),
            "control_DNA_feed_sd":
                float(control["DNA_T_over_influx_T"].std(ddof=1)),

            "baseline_DNA_T_fraction_mean":
                float(base["DNA_T_fraction_TU"].mean()),
            "control_DNA_T_fraction_mean":
                float(control["DNA_T_fraction_TU"].mean()),
            "baseline_DNA_free_ratio_mean":
                float(base["DNA_TU_over_free_TU"].mean()),
            "control_DNA_free_ratio_mean":
                float(control["DNA_TU_over_free_TU"].mean()),

            "baseline_survival_mean":
                float(base["final_survival"].mean()),
            "control_survival_mean":
                float(control["final_survival"].mean()),
            "baseline_total_DNA_mean":
                float(base["total_DNA"].mean()),
            "control_total_DNA_mean":
                float(control["total_DNA"].mean()),

            "max_mass_balance_error":
                float(subset["mass_balance_rel_error"].max()),
            "max_consumed_identity_residual":
                float(subset["consumed_identity_residual"].max()),
        }

        for metric, tag in PAIRED_METRICS:
            row.update(
                paired_stats(
                    base[metric].to_numpy(dtype=float),
                    control[metric].to_numpy(dtype=float),
                    metric_tag=tag,
                )
            )

        summary_rows.append(row)

    summary = pd.DataFrame(summary_rows)
    summary.to_csv(OUTPUT_SUMMARY, index=False)

    # ========================================================
    # 9. DT-CONVERGENCE COMPARISON (OPTIONAL)
    # ========================================================

    convergence_written = False

    if PREVIOUS_SUMMARY is not None:

        prev_path = Path(PREVIOUS_SUMMARY)

        if prev_path.exists():

            old = pd.read_csv(prev_path)

            # Previous summary may key on a different column name.
            # Normalize to nominal_target_ratio if possible.
            if (
                "nominal_target_ratio" not in old.columns
                and "target_ratio" in old.columns
            ):
                old = old.rename(
                    columns={"target_ratio": "nominal_target_ratio"}
                )

            if "nominal_target_ratio" not in old.columns:
                print(
                    f"\nWARNING: previous summary {prev_path} "
                    "has no usable ratio column; "
                    "skipping convergence comparison."
                )
            else:
                old_key = old[
                    ["nominal_target_ratio", "condition"]
                ].copy()

                # Only compare baseline rows on the previous run.
                old_base = old[
                    old["condition"] == "baseline"
                ].copy()

                new_base = pd.DataFrame({
                    "nominal_target_ratio":
                        summary["nominal_target_ratio"],
                    "new_baseline_DNA_feed_mean":
                        summary["baseline_DNA_feed_mean"],
                    "new_paired_ratio_raw_mean":
                        summary["paired_ratio_raw_mean"],
                    "new_paired_ratio_raw_CI95_low":
                        summary["paired_ratio_raw_CI95_low"],
                    "new_paired_ratio_raw_CI95_high":
                        summary["paired_ratio_raw_CI95_high"],
                })

                merged = new_base.merge(
                    old_base[[
                        "nominal_target_ratio",
                        "mean_DNA_T_over_influx_T",
                        "mean_survival",
                    ]],
                    on="nominal_target_ratio",
                    how="inner",
                    suffixes=("", "_dt_prev"),
                )

                if len(merged) > 0:
                    merged["delta_baseline_DNA_feed"] = (
                        merged["new_baseline_DNA_feed_mean"]
                        - merged["mean_DNA_T_over_influx_T"]
                    )

                    merged.to_csv(
                        OUTPUT_CONVERGENCE, index=False
                    )
                    convergence_written = True

                    print("\n" + "=" * 70)
                    print("DT-CONVERGENCE COMPARISON")
                    print("=" * 70)
                    print(
                        merged[[
                            "nominal_target_ratio",
                            "mean_DNA_T_over_influx_T",
                            "new_baseline_DNA_feed_mean",
                            "delta_baseline_DNA_feed",
                            "new_paired_ratio_raw_mean",
                            "new_paired_ratio_raw_CI95_low",
                            "new_paired_ratio_raw_CI95_high",
                        ]].to_string(
                            index=False,
                            float_format=lambda x: f"{x:.5f}",
                        )
                    )
                    print(
                        "\nDelta is dt60 baseline mean minus "
                        "dt300 baseline mean. If |delta| is "
                        "within the new paired SD, the dt300 run "
                        "was converged."
                    )
                else:
                    print(
                        "\nWARNING: no overlapping rows between "
                        f"{prev_path} and current summary; "
                        "skipping convergence comparison."
                    )
        else:
            print(
                f"\nNote: previous summary {prev_path} not found; "
                "skipping dt-convergence comparison."
            )

    # ========================================================
    # 10. PRINT FINAL RESULTS
    # ========================================================

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)
    print("FINAL PAIRED RESULTS")
    print("=" * 70)

    columns_to_show = [
        "nominal_target_ratio",
        "baseline_DNA_feed_mean",
        "control_DNA_feed_mean",
        "paired_ratio_raw_mean",
        "paired_ratio_raw_CI95_low",
        "paired_ratio_raw_CI95_high",
        "paired_ratio_persurv_mean",
        "paired_ratio_persurv_CI95_low",
        "paired_ratio_persurv_CI95_high",
        "all_pairs_baseline_greater_raw",
        "all_pairs_baseline_greater_persurv",
    ]

    print(
        summary[columns_to_show].to_string(
            index=False,
            float_format=lambda x: f"{x:.5f}",
        )
    )

    print("\n" + "=" * 70)
    print(f"Completed simulations: {len(df)}")
    print(f"Elapsed time: {elapsed / 60:.1f} minutes")
    print(f"Raw results: {OUTPUT_RAW}")
    print(f"Summary results: {OUTPUT_SUMMARY}")
    if convergence_written:
        print(f"Convergence comparison: {OUTPUT_CONVERGENCE}")
    print("=" * 70)


# ============================================================
# 11. ENTRY POINT
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        print(
            "Completed results remain in the raw CSV checkpoint."
        )

    except Exception:
        print("\nERROR:")
        traceback.print_exc()
        print(
            "\nIf some simulations completed, their results "
            "remain in the raw CSV checkpoint."
        )
