import matplotlib.pyplot as plt

x = [2, 7, 2, 13]
h = ['Dancing', 'Writing', 'Sketching', 'Playing']
c = ['c', 'm', 'r', 'b']
plt.pie(x, labels=h, colors=c, explode=(0, 0.1, 0, 0), autopct="%1.1f%%")
plt.title('Various Hobbies')
plt.show()
