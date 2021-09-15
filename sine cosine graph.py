import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,10,0.1)
a=np.cos(x)
b=np.sin(x)
plt.plot(x,a,linewidth=2)
plt.plot(x,b,linewidth=2)
plt.show()
