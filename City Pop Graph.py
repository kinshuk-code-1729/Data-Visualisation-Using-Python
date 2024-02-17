import matplotlib.pyplot as plt

city = ['Delhi', 'Mumbai', 'Chennai', 'Hyderabad']
p = [1500, 2000, 1800, 1200]
plt.bar(city, p)
plt.xlabel("City")
plt.ylabel("Population in Lacs ")
plt.title("Population of different cities")
plt.show()
