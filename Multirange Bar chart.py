import matplotlib.pyplot as plt
import numpy as np

v = [[5., 25., 45., 20.], [4., 23., 49., 17.], [6., 22., 47., 19.]]
X = np.arange(4)
plt.title("MultiRange Bar Chart")
plt.bar(X + 0.00, v[0], color='purple', width=0.25, label='range1')
plt.bar(X + 0.25, v[1], color='g', width=0.25, label='range2')
plt.bar(X + 0.50, v[2], color='r', width=0.25, label='range3')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.show()
