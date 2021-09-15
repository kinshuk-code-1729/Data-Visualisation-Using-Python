import matplotlib.pyplot as plt
import numpy as np
d=[[5.,25.,45.,20.],[8.,13.,29.,27.],[9.,29.,27.,39.]]
X=np.arange(4)
plt.title("MultiRange Line Chart")
plt.plot(X,d[0],color='b',label='range1')
plt.plot(X,d[1],color='g',label='range2')
plt.plot(X,d[2],color='r',label='range3')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.show()
