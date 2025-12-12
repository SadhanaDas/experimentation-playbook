import numpy as np
import pandas as pd
from scipy import stats

def perform_ab_test(
    df,
    experiment_id,
    metric, #the primary metric
    metricA=None,
    metricB=None,
    metric_type="continuous",   # continuous → t-test; proportional → z-test
    alpha=0.1,
    lift_threshold=5,
    power_threshold=0.8
):
    """
    Perform A/B tests across buckets for continuous or proportional metrics.

    metric_type:
        - "continuous"   → numeric metric (e.g., Time Spent, IPU, TPU) → Welch's t-test
        - "proportional" → ratio metricA / metricB (e.g., CVR = conversions / UVs) → Two-proportion z-test
    """

    df_exp = df[df["experiment_id"] == experiment_id]
    results = []
    buckets = df_exp["bucket_label"].unique()

    for i in range(len(buckets)):
        for j in range(i + 1, len(buckets)):
            bucket1, bucket2 = buckets[i], buckets[j]

            data1 = df_exp[df_exp["bucket_label"] == bucket1]
            data2 = df_exp[df_exp["bucket_label"] == bucket2]

            # ================================================================
            # CONTINUOUS METRICS → Welch's T-test
            # ================================================================
            if metric_type == "continuous":
                m1 = data1[metric].dropna()
                m2 = data2[metric].dropna()

                mean1, mean2 = m1.mean(), m2.mean()
                std1, std2 = m1.std(ddof=1), m2.std(ddof=1)
                n1, n2 = len(m1), len(m2)

                # Welch's t-test: mean comparison with unequal variances
                t_stat, p_value = stats.ttest_ind(m1, m2, equal_var=False)

                lift = ((mean2 - mean1) / mean1 * 100) if mean1 != 0 else 0

                # Confidence Interval (based on difference in means)
                se = np.sqrt((std1**2 / n1) + (std2**2 / n2))
                t_crit = stats.t.ppf(1 - alpha/2, df=min(n1 - 1, n2 - 1))
                ci_low = (mean2 - mean1) - t_crit * se
                ci_high = (mean2 - mean1) + t_crit * se

                # Cohen's d effect size for power calculation
                pooled_std = np.sqrt(std1**2 + std2**2)
                effect_size = (mean2 - mean1) / pooled_std if pooled_std > 0 else 0

                # Approximate power for t-test
                power = stats.norm.cdf(effect_size - stats.norm.ppf(1 - alpha/2))

                stat_used = "T-Test"

            # ================================================================
            # PROPORTIONAL METRICS → Two-Proportion Z-test
            # ================================================================
            elif metric_type == "proportional":
                A1, B1 = data1[metricA].sum(), data1[metricB].sum()
                A2, B2 = data2[metricA].sum(), data2[metricB].sum()

                rate1 = A1 / B1 if B1 != 0 else 0
                rate2 = A2 / B2 if B2 != 0 else 0

                # Z-statistic for difference in proportions
                pooled_rate = (A1 + A2) / (B1 + B2) if (B1 + B2) != 0 else 0
                se = np.sqrt(pooled_rate * (1 - pooled_rate) * (1/B1 + 1/B2)) if B1 > 0 and B2 > 0 else 0
                z_stat = (rate2 - rate1) / se if se > 0 else 0

                # Convert to p-value
                p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

                lift = ((rate2 - rate1) / rate1 * 100) if rate1 != 0 else 0

                # Confidence Interval for difference in proportions
                z_crit = stats.norm.ppf(1 - alpha/2)
                ci_low = (rate2 - rate1) - z_crit * se
                ci_high = (rate2 - rate1) + z_crit * se

                # Effect size (Cohen's h)
                effect_size = 2 * (np.arcsin(np.sqrt(rate2)) - np.arcsin(np.sqrt(rate1)))

                # Approximate power for z-test
                power = stats.norm.cdf(effect_size - stats.norm.ppf(1 - alpha/2))

                t_stat = z_stat      # keep column name consistent
                stat_used = "Z-Test"

            else:
                raise ValueError("metric_type must be 'continuous' or 'proportional'")

            # ================================================================
            # P-value interpretability
            # ================================================================
            p_strength = (
                "Very Strong" if p_value < 0.001 else
                "Strong"       if p_value < 0.01 else
                "Moderate"     if p_value < 0.05 else
                "Not Significant"
            )
            significant = p_value < alpha

            # ================================================================
            # Decision Logic
            # ================================================================
            if significant and lift > lift_threshold and power > power_threshold:
                decision = "Accept better variant"
            elif not significant:
                decision = "Reject due to non-significance"
            else:
                decision = "No decision"

            results.append({
                "Experiment ID": experiment_id,
                "Comparison": f"{bucket1} vs {bucket2}",
                "Statistic Used": stat_used,
                "Bucket 1": bucket1,
                "Bucket 2": bucket2,
                "Primary Metric": metric,
                "Test Statistic": t_stat,
                "P-value": p_value,
                "Significant": significant,
                "P-value Strength": p_strength,
                "Lift (%)": f"{lift:.2f}%",
                "CI Lower": ci_low,
                "CI Upper": ci_high,
                "Power": f"{power:.2f}",
                "Decision": decision
            })

    return pd.DataFrame(results)
