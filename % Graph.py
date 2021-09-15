import matplotlib.pyplot as plt
import numpy as np
label = ['Anil', 'Vikas', 'Dharma','Mahen', 'Manish', 'Rajesh']
per = [94,85,45,25,50,54]
index = np.arange(len(label))
plt.bar(index, per, color='Black')
plt.xlabel('Student Name', fontsize=15)
plt.ylabel('Percentage', fontsize=15)
plt.xticks(index, label, fontsize=10,rotation=20)
plt.title('Percentage of Marks achieved by student of Class XII')
plt.show()
