import numpy as np
import pandas as pd
from scipy import stats

def compute_practical_sig(
    df,
    experiment_id,
    control_label="control",
    metric_type="proportional",     # "proportional" → MetricA / MetricB | "continuous" → direct metric column
    metric=None,                    # required for continuous metrics
    metricA=None,                   # numerator (for proportional)
    metricB=None,                   # denominator (for proportional)
    alpha=0.10,
    lift_threshold=5
):
    """
    Computes practical significance for A/B tests by evaluating confidence intervals
    and comparing lift against a practical threshold.

    Parameters
    ----------
    df : DataFrame
        Input dataset containing experiment records.
    experiment_id : str / int
        Experiment identifier to filter data.
    control_label : str
        Name of the control bucket.
    metric_type : str
        "proportional" → Metric = MetricA / MetricB (e.g., CTR, CVR, Save rate)
        "continuous"   → Metric = direct column (e.g., Time Spent per User)
    metric : str
        Column name of continuous metric (required if metric_type="continuous").
    metricA : str
        Column name of numerator (required if metric_type="proportional").
    metricB : str
        Column name of denominator (required if metric_type="proportional").
    alpha : float
        Confidence level. alpha=0.10 → 90% CI.
    lift_threshold : float
        Minimum % lift required for practical significance.

    Returns
    -------
    DataFrame
        Practical significance summary for each variant vs control.
    """

    df_exp = df[df["experiment_id"] == experiment_id].copy()
    if df_exp.empty:
        raise ValueError("No rows detected for provided experiment_id.")

    # ------------------------------------------------------------------
    # AGGREGATION FOR METRIC VALUE
    # ------------------------------------------------------------------
    if metric_type == "proportional":
        if metricA is None or metricB is None:
            raise ValueError("metricA and metricB are required for proportional metrics.")

        agg = df_exp.groupby("bucket_label").agg({
            metricA: "sum",
            metricB: "sum"
        }).reset_index()

        agg["metric"] = np.where(agg[metricB] > 0, agg[metricA] / agg[metricB], 0)

    elif metric_type == "continuous":
        if metric is None:
            raise ValueError("metric parameter required for continuous metrics.")

        agg = df_exp.groupby("bucket_label").agg({
            metric: "mean",
            "user_id": "count" if "user_id" in df_exp.columns else "size"
        }).reset_index()

        agg = agg.rename(columns={metric: "metric", "user_id": "n"})

    else:
        raise ValueError("metric_type must be 'continuous' or 'proportional'.")

    # Validate control
    if control_label not in agg["bucket_label"].values:
        raise ValueError("Control bucket not found.")

    results = []
    control = agg[agg["bucket_label"] == control_label].iloc[0]
    metric_control = control["metric"]
    n_control = control[metricB] if metric_type == "proportional" else control["n"]

    z = stats.norm.ppf(1 - alpha / 2)

    # ------------------------------------------------------------------
    # PRACTICAL SIGNIFICANCE CALCULATION
    # ------------------------------------------------------------------
    for _, row in agg.iterrows():
        if row["bucket_label"] == control_label:
            continue

        metric_var = row["metric"]
        n_var = row[metricB] if metric_type == "proportional" else row["n"]

        diff = metric_var - metric_control

        # Standard Error (different for proportional vs continuous)
        if metric_type == "proportional":
            p1, p2 = metric_control, metric_var
            se = np.sqrt((p1 * (1 - p1) / n_control) + (p2 * (1 - p2) / n_var))
        else:  # continuous
            se = np.sqrt((np.var(df_exp[df_exp["bucket_label"] == control_label][metric], ddof=1) / n_control) +
                         (np.var(df_exp[df_exp["bucket_label"] == row["bucket_label"]][metric], ddof=1) / n_var))

        ci = (diff - z * se, diff + z * se)
        lift_percent = (diff / metric_control * 100) if metric_control != 0 else 0

        # Practical significance → lower bound of CI > lift threshold
        practical_sig = (ci[0] / metric_control * 100) > lift_threshold

        results.append({
            "Comparison": f"{row['bucket_label']} vs {control_label}",
            "Metric Control": round(metric_control, 4),
            "Metric Variant": round(metric_var, 4),
            "ΔMetric": round(diff, 4),
            f"{int((1-alpha)*100)}% CI ΔMetric": (round(ci[0], 4), round(ci[1], 4)),
            "Lift %": round(lift_percent, 2),
            "Practical Significance": practical_sig
        })

    return pd.DataFrame(results)
