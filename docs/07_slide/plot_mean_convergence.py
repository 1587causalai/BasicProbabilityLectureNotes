import numpy as np
import matplotlib.pyplot as plt

def plot_sample_mean_path(distribution_name, samples, true_mean=None, filename_suffix=''):
    """
    Plots the path of the sample mean and saves the plot.

    Args:
        distribution_name (str): Name of the distribution (e.g., "Normal", "Cauchy").
        samples (np.ndarray): Array of random samples from the distribution.
        true_mean (float, optional): The true mean of the distribution, if it exists. 
                                     If provided, a horizontal line will be drawn at this value.
        filename_suffix (str): Suffix to append to the filename.
    """
    plt.style.use('seaborn-v0_8-whitegrid') # Apply a style

    n_samples = len(samples)
    sample_means = np.cumsum(samples) / np.arange(1, n_samples + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(1, n_samples + 1), sample_means, label=r'Sample Mean $\bar{X}_n$', linewidth=1.5) # Slightly thicker line
    
    if true_mean is not None:
        plt.axhline(true_mean, color='r', linestyle='--', label=fr'True Mean $\mu={true_mean}$', linewidth=1.5)

    plt.xlabel('Number of Samples (n)', fontsize=14)
    plt.ylabel(r'Sample Mean ($\bar{X}_n$)', fontsize=14)
    
    title_fontsize = 16
    if distribution_name == "Normal":
        plt.title(f'Sample Mean Convergence for {distribution_name} Distribution N(0,1)', fontsize=title_fontsize)
        plt.ylim(-1, 1) # Zoom in for Normal to better see convergence
    elif distribution_name == "Cauchy":
         plt.title(f'Sample Mean Path for {distribution_name} Distribution C(0,1)', fontsize=title_fontsize)
    else:
        plt.title(f'Sample Mean Path for {distribution_name} Distribution', fontsize=title_fontsize)

    plt.legend(fontsize=12)
    plt.grid(True)
    # plt.gca().spines['top'].set_visible(False) # Optionally remove top spine
    # plt.gca().spines['right'].set_visible(False) # Optionally remove right spine
    plt.tick_params(axis='both', which='major', labelsize=12)

    filename = f"{distribution_name.lower().replace(' ', '_')}_mean_{filename_suffix}.png"
    plt.savefig(filename, bbox_inches='tight', dpi=300) # Add bbox_inches and dpi
    print(f"Plot saved as {filename}")
    plt.close()

def main():
    # np.random.seed(42) # for reproducibility
    num_points = 20000

    # Normal Distribution N(0,1)
    normal_samples = np.random.normal(loc=0, scale=1, size=num_points)
    plot_sample_mean_path("Normal", normal_samples, true_mean=0, filename_suffix="convergence")

    # Cauchy Distribution C(0,1)
    cauchy_samples = np.random.standard_cauchy(size=num_points)
    # For Cauchy, the mean is undefined, so we don't pass true_mean
    plot_sample_mean_path("Cauchy", cauchy_samples, filename_suffix="no_convergence")

if __name__ == "__main__":
    main() 