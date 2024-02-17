import matplotlib.pyplot as plt
import numpy as np

c = [8000, 12000, 9800, 11200, 15500, 7300]
X = np.arange(6)
plt.title("Volunteering Week Collection")
plt.bar(X, c, color='r', width=0.25)
plt.show()
