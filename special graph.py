import matplotlib.pyplot as plt
import numpy as np

a = np.arange(1, 20, 1.25)
b = np.log(a)
c = np.cos(a)
plt.plot(a, b)
plt.plot(a, c, 'bo', linestyle='dashdot')
plt.show()
