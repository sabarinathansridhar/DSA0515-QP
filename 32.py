import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # For reproducibility
x = np.random.randn(100)  # 100 random points for X
y = np.random.randn(100)  # 100 random points for Y

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='k', label='Data points')

# Add labels, title, and legend
plt.xlabel('X-axis (Random Distribution)')
plt.ylabel('Y-axis (Random Distribution)')
plt.title('Scatter Plot of Random Distributions')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
