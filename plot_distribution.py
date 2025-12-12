import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def plot_distribution(control_mean, control_se, variant_mean, variant_se, metric_name="Metric", alpha=0.10):
    """
    Plot normal distribution curves for control and variant with CI shading.
    """
    # Generate x range around means
    xmin = min(control_mean - 4*control_se, variant_mean - 4*variant_se)
    xmax = max(control_mean + 4*control_se, variant_mean + 4*variant_se)
    x = np.linspace(xmin, xmax, 500)
    # Normal pdfs
    control_pdf = stats.norm.pdf(x, loc=control_mean, scale=control_se)
    variant_pdf = stats.norm.pdf(x, loc=variant_mean, scale=variant_se)
    # Critical z for CI
    z = stats.norm.ppf(1 - alpha/2)
    control_ci = (control_mean - z*control_se, control_mean + z*control_se)
    variant_ci = (variant_mean - z*variant_se, variant_mean + z*variant_se)
    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(x, control_pdf, label=f"Control mean={control_mean:.2f}", color="blue")
    plt.plot(x, variant_pdf, label=f"Variant mean={variant_mean:.2f}", color="green")
    # Shade CI
    plt.axvspan(control_ci[0], control_ci[1], color="blue", alpha=0.2)
    plt.axvspan(variant_ci[0], variant_ci[1], color="green", alpha=0.2)
    # Vertical lines for means
    plt.axvline(control_mean, color="blue", linestyle="--")
    plt.axvline(variant_mean, color="green", linestyle="--")
    plt.title(f"Normal Approximation of {metric_name}\n90% CI Shaded")
    plt.xlabel(metric_name)
    plt.ylabel("Density")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # === Example: BPU (Control vs Vertical Lightbox) ===
    control_mean = 4.65
    variant_mean = 7.67
    # Approximate SE from CI width (from your earlier 90% CI)
    se_control = (6.69 - control_mean)/stats.norm.ppf(0.95)  # control CI upper bound
    se_variant = (10.28 - variant_mean)/stats.norm.ppf(0.95) # variant CI upper bound
    plot_distribution(control_mean, se_control, variant_mean, se_variant, 
                      metric_name="BPU (Images Saved per Saver)")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def plot_distribution(control_mean, control_se, variant_mean, variant_se, metric_name="Metric", alpha=0.10):
    """
    Plot normal distribution curves for control and variant with CI shading.
    """
    # Generate x range around means
    xmin = min(control_mean - 4*control_se, variant_mean - 4*variant_se)
    xmax = max(control_mean + 4*control_se, variant_mean + 4*variant_se)
    x = np.linspace(xmin, xmax, 500)
    # Normal pdfs
    control_pdf = stats.norm.pdf(x, loc=control_mean, scale=control_se)
    variant_pdf = stats.norm.pdf(x, loc=variant_mean, scale=variant_se)
    # Critical z for CI
    z = stats.norm.ppf(1 - alpha/2)
    control_ci = (control_mean - z*control_se, control_mean + z*control_se)
    variant_ci = (variant_mean - z*variant_se, variant_mean + z*variant_se)
    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(x, control_pdf, label=f"Control mean={control_mean:.2f}", color="blue")
    plt.plot(x, variant_pdf, label=f"Variant mean={variant_mean:.2f}", color="green")
    # Shade CI
    plt.axvspan(control_ci[0], control_ci[1], color="blue", alpha=0.2)
    plt.axvspan(variant_ci[0], variant_ci[1], color="green", alpha=0.2)
    # Vertical lines for means
    plt.axvline(control_mean, color="blue", linestyle="--")
    plt.axvline(variant_mean, color="green", linestyle="--")
    plt.title(f"Normal Approximation of {metric_name}\n90% CI Shaded")
    plt.xlabel(metric_name)
    plt.ylabel("Density")
    plt.legend()
    plt.show()
# === Example: BPU (Control vs Vertical Lightbox) ===
control_mean = 4.65
variant_mean = 7.67
# Approximate SE from CI width (from your earlier 90% CI)
se_control = (6.69 - control_mean)/stats.norm.ppf(0.95)  # control CI upper bound
se_variant = (10.28 - variant_mean)/stats.norm.ppf(0.95) # variant CI upper bound
plot_distribution(control_mean, se_control, variant_mean, se_variant, 
                  metric_name="BPU (Images Saved per Saver)")
