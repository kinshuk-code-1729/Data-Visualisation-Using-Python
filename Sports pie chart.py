import matplotlib.pyplot as plt

s = ('Football', 'Foosball', 'Cricket', 'Badminton', 'T.T', 'Squash')
p = [10, 8, 13, 7, 9, 3]
c = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'gray', 'cyan']
e = (0, 0.1, 0, 0, 0, 0)
plt.pie(p, explode=e, labels=s, colors=c, autopct="%1.1f%%")
plt.axis('equal')
plt.show()
