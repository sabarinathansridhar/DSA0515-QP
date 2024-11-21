import matplotlib.pyplot as plt
import numpy as np

# Sample data for three groups
np.random.seed(42)  # For reproducibility

# Group 1: Random weights and heights
group1_weights = np.random.normal(60, 5, 30)  # Mean weight: 60 kg, SD: 5
group1_heights = np.random.normal(160, 10, 30)  # Mean height: 160 cm, SD: 10

# Group 2: Random weights and heights
group2_weights = np.random.normal(70, 7, 30)  # Mean weight: 70 kg, SD: 7
group2_heights = np.random.normal(170, 12, 30)  # Mean height: 170 cm, SD: 12

# Group 3: Random weights and heights
group3_weights = np.random.normal(80, 6, 30)  # Mean weight: 80 kg, SD: 6
group3_heights = np.random.normal(180, 8, 30)  # Mean height: 180 cm, SD: 8

# Create scatter plot
plt.figure(figsize=(10, 7))

plt.scatter(group1_weights, group1_heights, color='blue', alpha=0.7, label='Group 1')
plt.scatter(group2_weights, group2_heights, color='green', alpha=0.7, label='Group 2')
plt.scatter(group3_weights, group3_heights, color='red', alpha=0.7, label='Group 3')

# Add labels, title, and legend
nplt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot of Weights vs Heights for Three Groups')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Show plot
plt.tight_layout()
plt.show()
