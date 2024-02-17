import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'java']
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=True, startangle=140)
plt.axis('equal')
plt.show()
