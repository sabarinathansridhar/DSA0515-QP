import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)  
x = np.random.rand(100) * 100  
y = np.random.rand(100) * 100  
sizes = np.random.rand(100) * 1000  
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, s=sizes, color='skyblue', alpha=0.7, edgecolor='k', label='Data points')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Balls of Different Sizes')
plt.legend()

plt.tight_layout()
plt.show()
