import matplotlib.pyplot as plt
city=['Delhi','Mumbai','Bangalore','Hyderabad']
population=[23456123,20083104,18456123,13411093]
plt.barh(city,population,color='m')
plt.xlabel("Cities")
plt.ylabel("Population")
plt.title("Population graph")
plt.show()
