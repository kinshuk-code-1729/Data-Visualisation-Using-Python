import matplotlib.pyplot as plt
c=[23.4,17.8,25,34,40]
z=['East','West','North','South','Central']
plt.axis("equal")
plt.pie(c,labels=z,explode=[0,0,0.2,0,0],autopct="%1.2f%%")
plt.show()
