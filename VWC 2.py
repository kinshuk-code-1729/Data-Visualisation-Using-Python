import matplotlib.pyplot as plt
import numpy as np
c=[8000,12000,9800,11200,15500,7300]
X=np.arange(6)
plt.title("Volunteering Week Collection")
plt.bar(X,c,color='olive',width=0.25)
plt.xticks(X,['Mon','Tue','Wed','Thu','Fri','Sat'])
plt.xlabel("Days")
plt.ylabel("Collection")
plt.show()
