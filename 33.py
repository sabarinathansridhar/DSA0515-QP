import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # For reproducibility
x = np.random.randn(100)  # 100 random points for X
y = np.random.randn(100)  # 100 random points for Y

# Create scatter plot with empty circles
plt.figure(figsize=(8, 6))
plt.scatter(x, y, facecolors='none', edgecolors='blue', label='Data points')

# Add labels, title, and legend
plt.xlabel('X-axis (Random Distribution)')
plt.ylabel('Y-axis (Random Distribution)')
plt.title('Scatter Plot with Empty Circles')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
