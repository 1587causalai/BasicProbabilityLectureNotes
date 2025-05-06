import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate x values
x = np.linspace(-5, 5, 500)

# PDF for Standard Normal N(0,1)
pdf_normal = stats.norm.pdf(x, 0, 1)

# PDF for Standard Cauchy C(0,1)
pdf_cauchy = stats.cauchy.pdf(x, 0, 1)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_normal, label='Normal N(0,1)', color='blue')
plt.plot(x, pdf_cauchy, label='Cauchy C(0,1)', color='red')

# Add labels and title (in English for compatibility)
plt.title('PDF Comparison: Normal vs. Cauchy Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0) # Ensure y-axis starts at 0 for density plots

# Save the plot to the specified path
# Make sure the 'docs/07_slide/' directory exists or adjust the path
image_path = "docs/07_slide/pdf_normal_cauchy_comparison.png"
try:
    plt.savefig(image_path)
    print(f"Plot saved to {image_path}")
except FileNotFoundError:
    print(f"Error: The directory for path {image_path} was not found. Please create it or check the path.")
    # As a fallback, save to current directory if the specified one doesn't exist
    fallback_path = "pdf_normal_cauchy_comparison.png"
    plt.savefig(fallback_path)
    print(f"Plot saved to {fallback_path} instead.")

# plt.show() # Uncomment to display the plot directly if running interactively 