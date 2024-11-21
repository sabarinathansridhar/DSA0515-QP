import matplotlib.pyplot as plt
import numpy as np

# Data
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]
categories = ['A', 'B', 'C', 'D', 'E']

# Bar positions
x = np.arange(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# Men bars
men_bars = ax.bar(x, men_means, yerr=men_std, label='Men', color='skyblue', capsize=5)

# Women bars stacked on men
women_bars = ax.bar(x, women_means, yerr=women_std, label='Women', color='lightcoral', bottom=men_means, capsize=5)

# Labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Scores')
ax.set_title('Stacked Bar Plot with Error Bars')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
