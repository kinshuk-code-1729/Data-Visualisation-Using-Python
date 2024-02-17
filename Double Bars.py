import matplotlib.pyplot as plt
import numpy as np

p = np.arange(1, 5, 1)
plt.bar(p, p ** 2, color='r', width=0.3)
plt.bar(p + 0.3, p * 2, color='purple', width=0.3)
plt.show()
