import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
plt.plot(x, x * 1.5, label='Normal', linewidth=3, linestyle='dashed')
plt.plot(x, x * 3.0, label='Fast', linewidth=3, linestyle='dashdot')
plt.plot(x, x / 3.0, label='Slow', linewidth=3, linestyle='dotted')
plt.legend()
plt.show()
