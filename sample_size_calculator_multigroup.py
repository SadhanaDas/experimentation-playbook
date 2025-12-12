import numpy as np
import scipy.stats as stats

def sample_size_calculator_multigroup(
    baseline, 
    desired_lift_percentage, 
    groups=3, 
    two_sided=True, 
    significance_level=0.05, 
    power=0.8, 
    test_type="z"
):
    # Compute the new conversion rate after applying the uplift
    p2 = baseline * (1 + desired_lift_percentage / 100)
    minimum_detectable_effect = p2 - baseline

    print(f"Baseline: {baseline}") 
    print(f"Expected Proportion after {desired_lift_percentage}% uplift: {round(p2, 4)}")
    print(f"MDE: {round(minimum_detectable_effect, 4)}")

    # Calculate Cohen's h (effect size for proportions)
    
    effect_size = (p2 - baseline) / np.sqrt(
        (baseline * (1 - baseline) + p2 * (1 - p2)) / 2
    )

    # Adjust alpha based on the number of groups 
    
    if groups > 2: # Bonferroni Correction
        adjusted_alpha = significance_level / (groups - 1) # Since 1 group is control 
        print(f"Adjusted Alpha (Bonferroni): {round(adjusted_alpha, 5)}")
    else:
        adjusted_alpha = significance_level  # No correction needed for A/B test
  
    # Compute Z-scores or T-scores
    if test_type == "z":
        alpha = stats.norm.ppf(1 - adjusted_alpha / 2) if two_sided else stats.norm.ppf(1 - adjusted_alpha)
        beta = stats.norm.ppf(power)
        print(f"Z-Test: Alpha Z-Score = {round(alpha, 4)}, Beta Z-Score = {round(beta, 4)}")
    elif test_type == "t":
        alpha = stats.t.ppf(1 - adjusted_alpha / 2, df=1e6) if two_sided else stats.t.ppf(1 - adjusted_alpha, df=1e6)
        beta = stats.t.ppf(power, df=1e6)
        print(f"T-Test: Alpha T-Score = {round(alpha, 4)}, Beta T-Score = {round(beta, 4)}")
    else:
        raise ValueError("Invalid test type. Must be either 'z' or 't'.")

    # Calculate the sample size using power analysis
    sample_size_per_group = ((alpha + beta) ** 2) * (2 / (effect_size ** 2))
    
    return round(sample_size_per_group)
