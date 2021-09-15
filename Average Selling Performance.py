import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0.0,20.0,1)
s=[3.8,2.1,3,3,3,2.5,2,2,3.1,3.4,3.8,4,4.3,4.9,5.6,6,6.7,8.28,9.9,12]
s2=[4.7,5.3,6.8,3.7,3.8,4.9,5.6,6.5,6.5,6.5,7.4,8.5,7.6,7.97,8.8,9.2,10,10.5,8.9,7.3]
plt.plot(t,s,label='Fast Moving Items')
plt.plot(t,s2,label='Drinks')
plt.xlabel('Item (s)')
plt.ylabel('Average Score')
plt.title('Average Selling Performance')
plt.grid(True)
plt.show()
